import Link from "next/link";
import Image from "next/image";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import type { Home, Patologia, Pubblicazione, Nota, Recensione, Sede, Settings } from "@/lib/content";
import { getDisegni, slugPatologia, srcDisegno, telHref, waHref } from "@/lib/content";
import { Disegno } from "../ui/Disegno";
import { Reveal } from "../ui/Reveal";
import { isSegno, Segno } from "../ui/Segno";
import { ModuloSede, SchedaNota, SchedaPaper, SchedaPatologia } from "./Schede";
import { Sezione } from "./Pagina";

/* ------------------------------------------------------------------ Hero: foto a tutto schermo, niente buco osseo */
export function Hero({ home, settings, locale }: { home: Home; settings: Settings; locale: Locale }) {
  const m = getMessages(locale);
  const tel = telHref(settings.telefono);
  const wa = waHref(settings.whatsapp, pick(settings.whatsappTesto, locale));
  const ritratto = home.ritratto;
  const foto = ritratto?.src
    ? ritratto.src.startsWith("/")
      ? ritratto.src
      : `/images/home/${ritratto.src}`
    : "/images/home/ritratto-placeholder.jpg";

  return (
    <section className="relative left-1/2 w-screen min-h-[calc(100svh-var(--header-h))] -translate-x-1/2">
      <Image
        src={foto}
        alt={pick(ritratto?.alt, locale) || m.a11y.ritrattoDi}
        fill
        priority
        sizes="100vw"
        className="object-cover object-[center_18%]"
      />
      <div className="absolute inset-0 bg-gradient-to-t from-inchiostro/75 via-inchiostro/25 to-inchiostro/30" aria-hidden="true" />
      <div className="contenitore relative flex min-h-[calc(100svh-var(--header-h))] flex-col justify-end pb-12 pt-16 md:pb-16">
        <Reveal className="max-w-2xl text-osso">
          {pick(home.eyebrow, locale) && <p className="eyebrow mb-4 text-osso/70">{pick(home.eyebrow, locale)}</p>}
          <h1 className="text-[2.7rem] leading-[1.02] text-osso md:text-[4rem] lg:text-[4.6rem]">{pick(home.titolo, locale)}</h1>
          <p className="mt-5 max-w-xl text-[1.1rem] leading-relaxed text-osso/85 md:text-[1.22rem]">{pick(home.sottotitolo, locale)}</p>
          <div className="mt-8 flex flex-wrap items-center gap-2">
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
    </section>
  );
}

/* ------------------------------------------------------------------ Cosa curo */
export function FasciaPatologie({ patologie, locale }: { patologie: Patologia[]; locale: Locale }) {
  const m = getMessages(locale);
  const principali = patologie.filter((p) => !p.secondaria).slice(0, 4);
  const secondarie = patologie.filter((p) => p.secondaria);
  if (!principali.length) return null;
  return (
    <Sezione eyebrow={m.nav.cosaCuro} titolo={m.home.cosaCuroTitolo} lead={m.home.cosaCuroLead} azione={{ href: href(locale, { kind: "cosaCuro" }), label: m.cta.tutte }} tinta="osso">
      <ul className="grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
        {principali.map((p) => (
          <li key={p.slug}>
            <SchedaPatologia p={p} locale={locale} />
          </li>
        ))}
      </ul>
      {secondarie.length > 0 && (
        <Reveal className="mt-5 flex flex-wrap items-center gap-x-3 gap-y-1 text-[0.95rem] text-grafite">
          <span>{m.cosaCuro.secondarie}:</span>
          {secondarie.map((p) => (
            <Link key={p.slug} href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="underline decoration-linea underline-offset-4 hover:text-petrolio hover:decoration-petrolio">
              {pick(p.titolo, locale)}
            </Link>
          ))}
        </Reveal>
      )}
    </Sezione>
  );
}

/* ------------------------------------------------------------------ Dove: docking */
export function FasciaSedi({ sedi, locale }: { sedi: Sede[]; locale: Locale }) {
  const m = getMessages(locale);
  if (!sedi.length) return null;
  return (
    <Sezione eyebrow={m.nav.dove} titolo={m.home.doveTitolo} lead={m.home.doveLead} azione={{ href: href(locale, { kind: "dove" }), label: m.cta.tutte }}>
      <ul className="grid gap-10 sm:grid-cols-2 lg:grid-cols-4">
        {sedi.map((s, i) => (
          <Reveal key={s.slug} as="li" delay={i * 80}>
            <ModuloSede s={s} locale={locale} />
          </Reveal>
        ))}
      </ul>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ Perché fidarsi */
export async function FasciaFiducia({ home, locale }: { home: Home; locale: Locale }) {
  const m = getMessages(locale);
  const voci = (home.fiducia ?? []).filter((v) => pick(v.testo, locale));
  if (!voci.length) return null;
  const catalogo = await getDisegni();
  return (
    <Sezione eyebrow={m.nav.chiSono} titolo={m.home.fiduciaTitolo} azione={{ href: href(locale, { kind: "chiSono" }), label: m.nav.chiSono }} tinta="osso">
      <ul className="grid gap-10 sm:grid-cols-2 lg:grid-cols-5">
        {voci.map((v, i) => {
          const disegno = srcDisegno(catalogo, v.segno, locale);
          return (
          <Reveal key={i} as="li" delay={i * 70} className="flex flex-col gap-4">
            <span className="relative aspect-[5/3] w-full overflow-hidden bg-petrolio-3">
              {disegno ? (
                <Disegno src={disegno.src} alt={disegno.alt} />
              ) : (
                <span className="absolute inset-0 grid place-items-center text-petrolio">
                  <Segno nome={isSegno(v.segno) ? v.segno : "check"} size={22} />
                </span>
              )}
            </span>
            <span className="text-[0.95rem] leading-snug">{pick(v.testo, locale)}</span>
          </Reveal>
          );
        })}
      </ul>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ Recensioni (solo se ci sono) */
export function FasciaRecensioni({ recensioni, locale }: { recensioni: Recensione[]; locale: Locale }) {
  const m = getMessages(locale);
  const voci = recensioni.slice(0, 3);
  if (!voci.length) return null;
  return (
    <Sezione titolo={m.home.recensioniTitolo}>
      <ul className="grid gap-10 md:grid-cols-3">
        {voci.map((r, i) => (
          <Reveal key={r.slug} as="li" delay={i * 90}>
            <blockquote className="text-[1.15rem] leading-relaxed">“{pick(r.testo, locale)}”</blockquote>
            <footer className="mt-4 text-sm text-grafite">
              <span className="font-semibold text-inchiostro">{r.nome}</span>
              {r.piattaforma ? ` · ${r.piattaforma}` : ""}
            </footer>
          </Reveal>
        ))}
      </ul>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ Quaderno (ultimi 3, misti) */
export function FasciaQuaderno({ voci, locale }: { voci: ({ tipo: "paper"; item: Pubblicazione } | { tipo: "nota"; item: Nota })[]; locale: Locale }) {
  const m = getMessages(locale);
  if (!voci.length) return null;
  return (
    <Sezione eyebrow={m.nav.quaderno} titolo={m.home.quadernoTitolo} lead={m.home.quadernoLead} azione={{ href: href(locale, { kind: "quaderno" }), label: m.cta.tutte }} tinta="osso">
      <ul className="grid gap-10 md:grid-cols-3">
        {voci.slice(0, 3).map((v, i) => (
          <Reveal key={v.item.slug} as="li" delay={i * 90}>
            {v.tipo === "paper" ? <SchedaPaper p={v.item} locale={locale} /> : <SchedaNota n={v.item} locale={locale} />}
          </Reveal>
        ))}
      </ul>
    </Sezione>
  );
}
