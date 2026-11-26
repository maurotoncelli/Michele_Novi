import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getProfilo, type Profilo, type Pubblicazione } from "@/lib/content";
import { elencoAutori, riconosciTitolare } from "@/lib/autori";
import { hrefArticolo, srcPaper } from "@/lib/media";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";
import { ListaEspandibile } from "./ListaEspandibile";

const INIZIALI = 3;

/**
 * Riga autori breve: primo autore + il titolare del sito in evidenza, ovunque sia nell'elenco.
 * "Michele Novi et al." · "Luigi Tarallo, Michele Novi et al." · "Giuseppe Porcellini, … Michele Novi et al."
 */
function AutoriBrevi({ autori, eTitolare }: { autori: string | null | undefined; eTitolare: (autore: string) => boolean }) {
  const nomi = elencoAutori(autori);
  if (!nomi.length) return null;
  const i = nomi.findIndex(eTitolare);
  const titolare = i >= 0 ? <span className="font-medium text-inchiostro">{nomi[i]}</span> : null;
  const coda = nomi.length > Math.max(i, 0) + 1 ? " et al." : "";
  if (i <= 0) {
    return (
      <>
        {titolare ?? nomi[0]}
        {coda}
      </>
    );
  }
  return (
    <>
      {nomi[0]}
      {i === 1 ? ", " : ", … "}
      {titolare}
      {coda}
    </>
  );
}

/** Elenco bibliografico: anno, titolo, autore e rivista, PDF o link all'articolo. `espandibile` mostra le prime tre e apre le altre. */
export async function ListaPubblicazioni({ pubblicazioni, locale, espandibile = false }: { pubblicazioni: Pubblicazione[]; locale: Locale; espandibile?: boolean }) {
  const m = getMessages(locale);
  if (!pubblicazioni.length) return null;
  const eTitolare = riconosciTitolare((await getProfilo()).nome);

  const riga = (p: Pubblicazione) => {
    const pdf = srcPaper(p.pdf);
    const articolo = hrefArticolo(p.doi, p.url);
    return (
      <li key={p.slug} className="flex flex-col gap-3 py-4 sm:flex-row sm:items-center sm:gap-4">
        <Link href={href(locale, { kind: "paper", slug: p.slug })} className="group flex min-w-0 flex-1 items-baseline gap-4">
          <span className="w-12 shrink-0 text-sm tabular-nums text-grafite">{p.anno}</span>
          <span className="min-w-0 flex-1">
            <span className="serif block text-[1.1rem] leading-snug group-hover:text-petrolio">{pick(p.titoloBreve, locale) || p.titolo}</span>
            <span className="mt-0.5 block text-sm text-grafite">
              {p.autori && (
                <>
                  <AutoriBrevi autori={p.autori} eTitolare={eTitolare} />
                  {" · "}
                </>
              )}
              <span className="italic">{p.rivista}</span>
            </span>
          </span>
          <Segno nome="freccia" size={18} className="hidden shrink-0 self-center text-nebbia group-hover:text-petrolio sm:block" />
        </Link>
        {/* Da sm colonna a larghezza fissa, così le frecce restano in fila qualunque sia il bottone; su telefono il bottone va sotto, allineato al titolo. */}
        <div className="flex shrink-0 pl-16 max-sm:empty:hidden sm:w-32 sm:justify-end sm:pl-0">
          {pdf ? (
            <a href={pdf} target="_blank" rel="noopener noreferrer" className="btn btn-osso !px-3">
              <Segno nome="doc" size={16} />
              {m.cta.pdf}
            </a>
          ) : articolo ? (
            <a href={articolo} target="_blank" rel="noopener noreferrer" className="btn btn-osso !px-3">
              {m.cta.articolo}
              <Segno nome="esterno" size={16} />
            </a>
          ) : null}
        </div>
      </li>
    );
  };

  if (!espandibile) {
    return <ol className="divide-y divide-linea border-y border-linea">{pubblicazioni.map(riga)}</ol>;
  }

  const altre = pubblicazioni.slice(INIZIALI);
  return (
    <ListaEspandibile more={`${m.cta.mostraTutte} (${pubblicazioni.length})`} less={m.cta.mostraMeno}>
      <ol className="divide-y divide-linea border-t border-linea">{pubblicazioni.slice(0, INIZIALI).map(riga)}</ol>
      {altre.length > 0 ? <ol className="divide-y divide-linea">{altre.map(riga)}</ol> : null}
    </ListaEspandibile>
  );
}

/** Archivio scientifico: i dati Scopus/ORCID a sinistra, l'elenco bibliografico a destra. */
export function ArchivioPubblicazioni({
  pubblicazioni,
  totale,
  metriche,
  mostraNotaSelezione = false,
  locale,
}: {
  pubblicazioni: Pubblicazione[];
  totale: number;
  metriche?: Profilo["attivitaScientifica"];
  mostraNotaSelezione?: boolean;
  locale: Locale;
}) {
  const m = getMessages(locale);
  const scopusUrl = metriche?.scopusId ? `https://www.scopus.com/authid/detail.uri?authorId=${metriche.scopusId}` : null;
  const orcidUrl = metriche?.orcid ? `https://orcid.org/${metriche.orcid}` : null;
  const haMetriche = Boolean(metriche?.citazioni || metriche?.hIndex || metriche?.scopusId || metriche?.orcid);
  const notaSelezione =
    mostraNotaSelezione && totale > pubblicazioni.length
      ? m.approfondimenti.selezioneArchivio
          .replace("{n}", String(pubblicazioni.length))
          .replace("{totale}", String(totale))
      : mostraNotaSelezione && pubblicazioni.length > totale
        ? m.approfondimenti.archivioCompleto
            .replace("{n}", String(pubblicazioni.length))
            .replace("{totale}", String(totale))
        : null;

  return (
    <div className="grid gap-8 lg:grid-cols-[minmax(0,15rem)_minmax(0,1fr)] lg:gap-16">
      <Reveal>
        <p className="cifra text-petrolio">{totale}</p>
        <p className="mt-3 max-w-52 text-[0.9rem] leading-relaxed text-grafite">{m.approfondimenti.peerReviewed}</p>
        {haMetriche && (
          <dl className="mt-6 space-y-3 border-t border-linea pt-5 text-[0.88rem]">
            {(metriche?.citazioni || metriche?.hIndex) && (
              <div className="flex flex-wrap gap-x-6 gap-y-2">
                {metriche.citazioni != null && (
                  <div>
                    <dt className="text-[0.75rem] uppercase tracking-[0.06em] text-nebbia">{m.approfondimenti.citazioni}</dt>
                    <dd className="mt-0.5 text-[1.25rem] font-medium tabular-nums leading-none text-inchiostro">{metriche.citazioni}</dd>
                  </div>
                )}
                {metriche.hIndex != null && (
                  <div>
                    <dt className="text-[0.75rem] uppercase tracking-[0.06em] text-nebbia">{m.approfondimenti.hIndex}</dt>
                    <dd className="mt-0.5 text-[1.25rem] font-medium tabular-nums leading-none text-inchiostro">{metriche.hIndex}</dd>
                  </div>
                )}
              </div>
            )}
            {scopusUrl && metriche?.scopusId && (
              <div className="pt-1">
                <dt className="text-[0.75rem] uppercase tracking-[0.06em] text-nebbia">{m.approfondimenti.scopusId}</dt>
                <dd className="mt-0.5">
                  <a
                    href={scopusUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1 font-medium tabular-nums max-md:py-2 text-petrolio underline decoration-petrolio/35 underline-offset-4 hover:decoration-petrolio"
                  >
                    {metriche.scopusId}
                    <Segno nome="esterno" size={14} />
                  </a>
                </dd>
              </div>
            )}
            {orcidUrl && metriche?.orcid && (
              <div>
                <dt className="text-[0.75rem] uppercase tracking-[0.06em] text-nebbia">{m.approfondimenti.orcid}</dt>
                <dd className="mt-0.5">
                  <a
                    href={orcidUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-1 tabular-nums max-md:py-2 text-grafite underline decoration-linea underline-offset-4 hover:text-petrolio hover:decoration-petrolio"
                  >
                    {metriche.orcid}
                    <Segno nome="esterno" size={14} />
                  </a>
                </dd>
              </div>
            )}
          </dl>
        )}
      </Reveal>
      <Reveal delay={90}>
        <ListaPubblicazioni pubblicazioni={pubblicazioni} locale={locale} />
        {notaSelezione && (
          <p className="mt-5 text-[0.88rem] leading-relaxed text-grafite">
            {notaSelezione}
          </p>
        )}
      </Reveal>
    </div>
  );
}
