import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import type { Pubblicazione } from "@/lib/content";
import { hrefArticolo, srcPaper } from "@/lib/media";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";
import { ListaEspandibile } from "./ListaEspandibile";

const INIZIALI = 3;

/** "Novi M. et al." dalla riga autori com'è in rivista. */
function primoAutore(autori: string | null | undefined) {
  if (!autori) return "";
  const [primo, ...altri] = autori.split(",");
  return altri.length ? `${primo.trim()} et al.` : primo.trim();
}

/** Elenco bibliografico: anno, titolo, autore e rivista, PDF o link all'articolo. `espandibile` mostra le prime tre e apre le altre. */
export function ListaPubblicazioni({ pubblicazioni, locale, espandibile = false }: { pubblicazioni: Pubblicazione[]; locale: Locale; espandibile?: boolean }) {
  const m = getMessages(locale);
  if (!pubblicazioni.length) return null;

  const riga = (p: Pubblicazione) => {
    const pdf = srcPaper(p.pdf);
    const articolo = hrefArticolo(p.doi, p.url);
    const autore = primoAutore(p.autori);
    return (
      <li key={p.slug} className="flex flex-col gap-3 py-4 sm:flex-row sm:items-center sm:gap-4">
        <Link href={href(locale, { kind: "paper", slug: p.slug })} className="group flex min-w-0 flex-1 items-baseline gap-4">
          <span className="w-12 shrink-0 text-sm tabular-nums text-grafite">{p.anno}</span>
          <span className="min-w-0 flex-1">
            <span className="serif block text-[1.1rem] leading-snug group-hover:text-petrolio">{pick(p.titoloBreve, locale) || p.titolo}</span>
            <span className="mt-0.5 block text-sm text-grafite">
              {autore && `${autore} · `}
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

/** Archivio scientifico: il numero dei lavori a sinistra, l'elenco a destra. `totale` conta anche le voci non mostrate. */
export function ArchivioPubblicazioni({ pubblicazioni, totale, locale }: { pubblicazioni: Pubblicazione[]; totale: number; locale: Locale }) {
  const m = getMessages(locale);
  return (
    <div className="grid gap-8 lg:grid-cols-[minmax(0,13rem)_minmax(0,1fr)] lg:gap-16">
      <Reveal>
        <p className="cifra text-petrolio">{totale}</p>
        <p className="mt-3 max-w-44 text-[0.9rem] leading-relaxed text-grafite">{m.approfondimenti.peerReviewed}</p>
      </Reveal>
      <Reveal delay={90}>
        <ListaPubblicazioni pubblicazioni={pubblicazioni} locale={locale} />
      </Reveal>
    </div>
  );
}
