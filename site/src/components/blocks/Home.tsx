import Link from "next/link";
import Image from "next/image";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import type { Home, Nota, Patologia, Profilo, Pubblicazione, Recensione, Sede, Settings } from "@/lib/content";
import { telHref, waHref } from "@/lib/content";
import { srcMedia } from "@/lib/media";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";
import { Contatore } from "../ui/Contatore";
import { TestoEspandibile } from "../ui/TestoEspandibile";
import { VideoLastra } from "../ui/VideoLastra";
import { PercorsoScorrevole } from "./PercorsoScorrevole";
import { MappaToscanaVisite } from "./MappaToscana";
import { SchedaMetodo, SchedaNota, SchedaPatologia, SchedaSede } from "./Schede";
import { Stelle } from "@/components/ui/Stelle";
import { Parole } from "@/components/ui/Parole";
import { Striscia } from "@/components/blocks/Striscia";
import { Sezione } from "./Pagina";
import { ElencoSintomi } from "./Sintomi";
import { sintomiVari, type Sintomo } from "@/lib/sintomi";
import { ArchivioPubblicazioni } from "./ListaPubblicazioni";

/* ------------------------------------------------------------------ Hero: immagine a tema a tutto schermo (verticale su mobile, ampia su desktop),
   testo in bianco in sovraimpressione in basso. */
export function Hero({ home, settings, locale }: { home: Home; settings: Settings; locale: Locale }) {
  const m = getMessages(locale);
  const tel = telHref(settings.telefono);
  const wa = waHref(settings.whatsapp, pick(settings.whatsappTesto, locale));
  const immagine = home.ritratto;
  const foto = srcMedia(immagine?.src, "home") ?? "/images/home/hero-sala-placeholder.jpg";

  return (
    <section className="relative left-1/2 w-screen -translate-x-1/2 overflow-hidden bg-profondo">
      <div className="hero-griglia">
        {/* Immagine a vivo a tutto schermo: centrata sul dottore su mobile e desktop. */}
        <div className="hero-media">
          <Image
            src={foto}
            alt={pick(immagine?.alt, locale) || ""}
            fill
            priority
            unoptimized
            sizes="100vw"
            className="object-cover object-center"
          />
        </div>

        {/* Testo in sovraimpressione */}
        <div className="hero-testo margine-sx flex flex-col justify-end pb-8 pt-10 sm:pb-12 lg:pb-20 lg:pt-16 lg:pr-12">
          <Reveal immediate className="max-w-4xl">
            {pick(home.eyebrow, locale) && (
              <p className="mb-2 text-[clamp(1rem,0.9rem+0.45vw,1.45rem)] font-normal tracking-[0.02em] text-osso/90 sm:mb-3 lg:text-osso">
                {pick(home.eyebrow, locale)}
              </p>
            )}
            <h1 className="text-[clamp(1.95rem,0.7rem+4.2vw,4.35rem)] font-medium leading-[1.03] tracking-[-0.04em] text-osso [text-wrap:initial]">
              {pick(home.titolo, locale)
                .split(/\n+/)
                .map((riga, idx) => (
                  <span key={idx} className="block whitespace-nowrap">
                    {riga.trim()}
                  </span>
                ))}
            </h1>
            <div className="mt-6 flex flex-wrap items-center gap-2 sm:mt-10">
              {tel && (
                <a href={tel} className="btn btn-petrolio">
                  <Segno nome="telefono" size={18} />
                  {m.cta.chiamaSegreteria}
                </a>
              )}
              {wa && (
                <a href={wa} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
                  <Segno nome="whatsapp" size={18} />
                  {m.cta.whatsapp}
                </a>
              )}
              {!tel && (
                <Link href={href(locale, { kind: "contatti" })} className="btn btn-petrolio">
                  <Segno nome="mail" size={18} />
                  {m.cta.scrivi}
                </Link>
              )}
              <Link href={href(locale, { kind: "dove" })} className="btn btn-osso">
                {m.cta.dove}
                <Segno nome="freccia" size={18} />
              </Link>
            </div>
          </Reveal>
        </div>
      </div>
      <a href="#fatti" className="hero-scorri">
        <span className="hero-scorri-leva">
          {m.home.scorri}
          <Segno nome="freccia" size={18} className="rotate-90" />
        </span>
      </a>
    </section>
  );
}

/* ------------------------------------------------------------------ Fascia introduttiva sotto la Hero (al posto dei numeri) */
export function FasciaIntro({ home, locale }: { home: Home; locale: Locale }) {
  const m = getMessages(locale);
  const righe = pick(home.sottotitolo, locale)
    .split(/\n+/)
    .map((s) => s.trim())
    .filter(Boolean);
  const titoloIntro = righe.length > 1 ? righe[0] : null;
  const paragrafi = righe.length > 1 ? righe.slice(1) : righe;
  if (!paragrafi.length) return null;

  return (
    <section id="fatti" className="hero-arrivo border-y border-linea bg-campo" aria-label={m.home.introEyebrow}>
      <div className="contenitore py-12 md:py-16">
        <Reveal className="max-w-3xl">
          <p className="eyebrow mb-3">{m.home.introEyebrow}</p>
          {titoloIntro && (
            <h2 className="display-m">
              {titoloIntro}
            </h2>
          )}
          <TestoEspandibile more={m.cta.leggiTutto} less={m.cta.riduci} righe={3} className="mt-5">
            {paragrafi.map((par, idx) => (
              <p key={idx} className="text-[1.06rem] leading-relaxed text-grafite md:text-[1.12rem]">
                {par}
              </p>
            ))}
          </TestoEspandibile>
        </Reveal>
      </div>
    </section>
  );
}

/* ------------------------------------------------------------------ Riga dei fatti: cifre, non aggettivi */
export function FasciaFatti({ sedi, paper, profilo, locale }: { sedi: Sede[]; paper: Pubblicazione[]; profilo: Profilo; locale: Locale }) {
  const m = getMessages(locale);
  const evidenza = profilo.inEvidenza ?? [];
  const ospedale = evidenza.find((v) => /^dal\s/i.test(v.anno ?? "") || /fucecchio/i.test(pick(v.titolo, locale)));
  const harvard = evidenza.find((v) => /harvard|massachusetts/i.test(pick(v.titolo, locale)));

  const fatti: { prefisso?: string; valore: string; label: string }[] = [];
  if (sedi.length) fatti.push({ valore: String(sedi.length), label: m.home.fattiSedi });
  if (ospedale?.anno) {
    const [, pre, anno] = ospedale.anno.match(/^(\D*)(\d{4})$/) ?? [];
    fatti.push({ prefisso: pre?.trim() || undefined, valore: anno ?? ospedale.anno, label: m.home.fattiOspedale });
  }
  if (harvard?.anno) fatti.push({ valore: harvard.anno, label: m.home.fattiHarvard });
  if (paper.length) fatti.push({ valore: String(paper.length), label: m.home.fattiPaper });
  if (fatti.length < 2) return null;

  return (
    <section id="fatti" className="hero-arrivo border-y border-linea" aria-label={m.home.fiduciaEyebrow}>
      <ul className="contenitore grid grid-cols-2 gap-x-6 gap-y-4 py-5 md:py-6 lg:grid-cols-4">
        {fatti.map((f, i) => (
          <Reveal key={f.label} as="li" delay={i * 90} className="flex min-w-0 flex-col gap-1 sm:flex-row sm:items-center sm:gap-3">
            <p className="cifra-s flex shrink-0 items-baseline gap-1.5">
              {f.prefisso && <span className="text-[0.45em] font-medium tracking-normal text-grafite">{f.prefisso}</span>}
              <Contatore valore={f.valore} />
            </p>
            <p className="max-w-[11rem] text-[0.82rem] leading-snug text-grafite">{f.label}</p>
          </Reveal>
        ))}
      </ul>
    </section>
  );
}

/* ------------------------------------------------------------------ 01 Cosa curo: spalla grande a sinistra, le altre aree alla pari a destra, lo sport in una fascia sotto */
export function FasciaPatologie({ patologie, sintomi = [], settings, locale }: { patologie: Patologia[]; sintomi?: Sintomo[]; settings?: Settings; locale: Locale }) {
  const m = getMessages(locale);
  const tel = telHref(settings?.telefono);
  const metodo = patologie.find((p) => p.area === "metodo");
  const spalla = patologie.find((p) => p.area === "spalla");
  // Lo sport attraversa le altre aree (anche la spalla): sta da solo, in una fascia a tutta larghezza.
  const sport = patologie.find((p) => p.area === "sport");
  // In home anche le secondarie (anca e ginocchio) stanno nella stessa colonna: prima le principali, poi loro.
  const resto = [...patologie.filter((p) => !p.secondaria && p !== metodo && p !== spalla && p !== sport), ...patologie.filter((p) => p.secondaria)];
  if (!spalla && !resto.length && !sport) return null;
  // Con due aree a destra la colonna si divide a metà l'altezza della spalla, e le foto si allungano a riempirla.
  const allineate = !!spalla && resto.length === 2;
  return (
    <>
      <Sezione id="patologie" indice="01" eyebrow={m.home.patologieEyebrow} azione={{ href: href(locale, { kind: "cosaCuro" }), label: m.cta.tutte }} tinta="bianca" compatta className="hero-arrivo">
        <div className="grid gap-10 lg:grid-cols-[minmax(0,1.15fr)_minmax(0,1fr)] lg:grid-rows-[auto_auto] lg:gap-x-12 lg:gap-y-0 xl:gap-x-16">
          {spalla && (
            <Reveal className="lg:row-span-2 lg:grid lg:grid-rows-subgrid">
              <SchedaPatologia p={spalla} locale={locale} apertura />
            </Reveal>
          )}
          {resto.length > 0 && (
            <ul className={`flex flex-col divide-y divide-linea border-t border-linea pt-6 lg:row-span-2 lg:border-t-0 lg:pt-0 ${allineate ? "lg:grid lg:grid-rows-2" : ""}`}>
              {resto.map((p, i) => (
                <Reveal key={p.slug} as="li" delay={i * 80} className={`flex min-w-0 flex-col py-6 first:pt-0 last:pb-0 ${allineate ? "lg:min-h-0" : "flex-1 justify-center first:justify-start last:justify-end"}`}>
                  <SchedaPatologia p={p} locale={locale} riga alta={allineate} />
                </Reveal>
              ))}
            </ul>
          )}
        </div>
        {sport && (
          <Reveal className="mt-10 md:mt-12">
            <SchedaPatologia p={sport} locale={locale} fascia />
          </Reveal>
        )}
        {sintomi.length > 0 && (
          <div className="mt-10 md:mt-12">
            <Reveal className="mb-5 flex flex-wrap items-end justify-between gap-x-8 gap-y-2">
              <div>
                <p className="eyebrow mb-2">{m.cosaCuro.sintomiEyebrow}</p>
                <h3 className="text-[1.4rem] leading-tight md:text-[1.6rem]">{m.cosaCuro.sintomiTitolo}</h3>
              </div>
              {sintomi.length > 4 && (
                <Link href={`${href(locale, { kind: "cosaCuro" })}#sintomi`} className="btn btn-ghost -ml-3 md:-mr-3 md:ml-0">
                  {m.cta.tutte}
                  <Segno nome="freccia" size={18} />
                </Link>
              )}
            </Reveal>
            <ElencoSintomi sintomi={sintomiVari(sintomi, 4)} />
            {tel && (
              <Reveal className="mt-8 flex flex-col items-start justify-between gap-4 bg-petrolio-3/70 p-5 sm:flex-row sm:items-center sm:p-6">
                <p className="max-w-xl text-[0.98rem] font-medium leading-snug text-profondo sm:text-[1.05rem]">
                  {m.cosaCuro.chiusura}
                </p>
                <div className="flex shrink-0 flex-wrap items-center gap-2">
                  <a href={tel} className="btn btn-petrolio">
                    <Segno nome="telefono" size={18} />
                    {m.cta.chiamaSegreteria}
                  </a>
                  <Link href={href(locale, { kind: "contatti" })} className="btn btn-osso bg-osso/80">
                    <Segno nome="mail" size={18} />
                    {m.cta.scrivi}
                  </Link>
                </div>
              </Reveal>
            )}
          </div>
        )}
      </Sezione>

      {metodo && (
        <section className="border-b border-linea">
          <Reveal className="contenitore py-16 md:py-24">
            <SchedaMetodo p={metodo} locale={locale} />
          </Reveal>
        </section>
      )}
    </>
  );
}

/* ------------------------------------------------------------------ 02 Dove: diviso chiaramente in Dove visito (mappa Toscana) e Dove opero (strutture chirurgiche) */
export function FasciaSedi({ sedi, settings, locale }: { sedi: Sede[]; settings?: Settings; locale: Locale }) {
  const m = getMessages(locale);
  const tel = telHref(settings?.telefono);
  if (!sedi.length) return null;
  const sediVisite = sedi
    .filter((x) => x.visite)
    .map((x) => ({
      slug: x.slug,
      citta: x.citta,
      provincia: x.provincia || undefined,
      nome: x.nome,
      indirizzo: x.indirizzo,
      cap: x.cap || undefined,
      regime: pick(x.regime, locale) || undefined,
      servizi: [x.infiltrazioni && m.dove.infiltrazioni, x.ecografo && m.dove.ecografo].filter((v): v is string => Boolean(v)),
    }));
  const sediChirurgia = sedi.filter((x) => x.chirurgia);

  return (
    <Sezione indice="02" eyebrow={m.nav.dove} titolo={m.home.doveTitolo} lead={m.home.doveLead} azione={{ href: href(locale, { kind: "dove" }), label: m.cta.tutte }} misura="affermazione">
      <div>
        <Reveal className="mb-6">
          <p className="eyebrow mb-2">{m.dove.visite}</p>
          <h3 className="display-m">{m.dove.doveVisitoTitolo}</h3>
        </Reveal>
        <Reveal>
          <MappaToscanaVisite sedi={sediVisite} locale={locale} labelScopri={m.cta.scopri} />
        </Reveal>
        {tel && (
          <Reveal className="mt-8 flex flex-col items-start justify-between gap-4 border-t border-linea pt-6 sm:flex-row sm:items-center">
            <p className="max-w-xl text-[0.95rem] leading-snug text-grafite">
              <strong className="font-medium text-inchiostro">{m.dove.prenota}.</strong> {m.dove.prenotaTesto}
            </p>
            <div className="flex shrink-0 flex-wrap items-center gap-2">
              <a href={tel} className="btn btn-petrolio">
                <Segno nome="telefono" size={18} />
                {m.cta.chiamaSegreteria}
              </a>
              <Link href={href(locale, { kind: "contatti" })} className="btn btn-osso">
                <Segno nome="mail" size={18} />
                {m.cta.scrivi}
              </Link>
            </div>
          </Reveal>
        )}
      </div>

      {sediChirurgia.length > 0 && (
        <div className="mt-16 border-t border-linea pt-12 md:mt-20 md:pt-14">
          <Reveal className="mb-8">
            <p className="eyebrow mb-2">{m.dove.chirurgia}</p>
            <h3 className="display-m">{m.dove.doveOperoTitolo}</h3>
            <p className="mt-2 max-w-2xl text-[1.02rem] leading-relaxed text-grafite">{m.dove.doveOperoLead}</p>
          </Reveal>
          <ul className="grid items-stretch gap-x-10 gap-y-8 md:grid-cols-3">
            {sediChirurgia.map((s, i) => (
              <Reveal key={s.slug} as="li" delay={i * 80} className="h-full min-w-0">
                <SchedaSede s={s} locale={locale} />
              </Reveal>
            ))}
          </ul>
        </div>
      )}
    </Sezione>
  );
}

/* ------------------------------------------------------------------ 03 Percorso formativo: luoghi e anni con scorrimento sticky */
export function FasciaPercorso({ profilo, home, locale }: { profilo: Profilo; home?: Home; locale: Locale }) {
  const m = getMessages(locale);
  const tappe = (profilo.inEvidenza ?? [])
    .filter((v) => pick(v.titolo, locale))
    .map((v) => ({ anno: v.anno ?? "", titolo: pick(v.titolo, locale), testo: pick(v.testo, locale) }));
  if (!tappe.length) return null;
  const lavoro = home?.lavoro;
  const foto = srcMedia(lavoro?.foto?.src, "home");
  const video = lavoro?.video ? (lavoro.video.startsWith("/") ? lavoro.video : `/videos/${lavoro.video}`) : null;
  return (
    <Sezione indice="03" eyebrow={m.home.fiduciaEyebrow} titolo={m.home.fiduciaTitolo} lead={m.home.fiduciaLead} azione={{ href: href(locale, { kind: "chiSono" }), label: m.nav.chiSono }} tinta="osso" misura="varco">
      <PercorsoScorrevole
        tappe={tappe}
        media={
          foto || video ? (
            <Reveal>
              <VideoLastra video={video} foto={foto} alt={pick(lavoro?.foto?.alt, locale) || m.a11y.ritrattoDi} ratio="4/5" sizes="(min-width: 1024px) 34vw, 24rem" />
            </Reveal>
          ) : undefined
        }
      />
    </Sezione>
  );
}

/* ------------------------------------------------------------------ 04 Recensioni: citazioni tipografiche, una alla volta in rotaia */
export function FasciaRecensioni({ recensioni, locale }: { recensioni: Recensione[]; locale: Locale }) {
  const m = getMessages(locale);
  const voci = recensioni.slice(0, 6);
  if (!voci.length) return null;
  const piattaforme = [...new Set(recensioni.map((r) => r.piattaforma).filter(Boolean))];
  const eyebrow = piattaforme.length ? `${m.home.recensioniEyebrow} · ${piattaforme.join(", ")}` : m.home.recensioniEyebrow;
  return (
    <Striscia n={voci.length} scheda={24} gap={3} testa={{ indice: "04", eyebrow, titolo: m.home.recensioniTitolo, misura: "affermazione" }}>
      {voci.map((r) => {
        const stelle = r.stelle;
        const firma = pick(r.firma, locale);
        return (
          <li key={r.slug} className="min-w-0">
            <figure className="recensione">
              <span aria-hidden="true" className="virgolette">
                “
              </span>
              <p className="eyebrow flex flex-wrap items-center gap-x-3 gap-y-1">
                {r.piattaforma && <span>{r.piattaforma}</span>}
                {stelle ? <Stelle n={stelle} label={m.home.stelleLabel.replace("{n}", String(stelle))} className="text-petrolio" /> : null}
              </p>
              {/* Le parole si compongono una dopo l'altra quando la scheda entra in vista. */}
              <Reveal as="blockquote" solo className="recensione-testo mt-4">
                <Parole testo={pick(r.testo, locale)} />
              </Reveal>
              <figcaption className="mt-5 text-[0.92rem] text-grafite">
                {r.nome && <span className="font-medium text-inchiostro">{r.nome}</span>}
                {r.nome && firma && <span aria-hidden="true"> · </span>}
                {firma && <span className={r.nome ? undefined : "font-medium text-inchiostro"}>{firma}</span>}
              </figcaption>
            </figure>
          </li>
        );
      })}
    </Striscia>
  );
}

/* ------------------------------------------------------------------ 05 Approfondimenti: gli ultimi tre articoli per pazienti, in griglia */
export function FasciaApprofondimenti({ note, locale }: { note: Nota[]; locale: Locale }) {
  const m = getMessages(locale);
  if (!note.length) return null;
  return (
    <Sezione
      indice="05"
      eyebrow={m.nav.approfondimenti}
      titolo={m.home.approfondimentiTitolo}
      lead={m.home.approfondimentiLead}
      azione={{ href: href(locale, { kind: "approfondimenti" }), label: m.cta.tuttiApprofondimenti }}
      tinta="osso"
    >
      <ul className="grid items-stretch gap-10 md:grid-cols-2 lg:grid-cols-3">
        {note.slice(0, 3).map((n, i) => (
          <Reveal key={n.slug} as="li" delay={i * 80} className="h-full min-w-0">
            <SchedaNota n={n} locale={locale} />
          </Reveal>
        ))}
      </ul>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ 06 Pubblicazioni: archivio scientifico, compatto e bibliografico */
export function FasciaPubblicazioni({ pubblicazioni, locale }: { pubblicazioni: Pubblicazione[]; locale: Locale }) {
  const m = getMessages(locale);
  if (!pubblicazioni.length) return null;
  return (
    <Sezione
      indice="06"
      eyebrow={m.approfondimenti.archivioScientifico}
      titolo={m.home.pubblicazioniTitolo}
      lead={m.home.pubblicazioniLead}
      azione={{ href: href(locale, { kind: "pubblicazioni" }), label: m.cta.tuttePubblicazioni }}
      tinta="bianca"
    >
      <ArchivioPubblicazioni pubblicazioni={pubblicazioni.slice(0, 3)} totale={pubblicazioni.length} locale={locale} />
    </Sezione>
  );
}
