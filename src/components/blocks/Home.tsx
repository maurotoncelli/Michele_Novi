import Link from "next/link";
import Image from "next/image";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import type { Home, Patologia, Pubblicazione, Nota, Recensione, Sede, Settings } from "@/lib/content";
import { telHref, waHref, slugPatologia } from "@/lib/content";
import { Reveal } from "../ui/Reveal";
import { Strati } from "../ui/Strati";
import { isSegno, Segno } from "../ui/Segno";
import { ModuloSede, SchedaNota, SchedaPaper, SchedaPatologia } from "./Schede";
import { Sezione } from "./Pagina";

/* ------------------------------------------------------------------ Hero */
export function Hero({ home, settings, locale }: { home: Home; settings: Settings; locale: Locale }) {
  const m = getMessages(locale);
  const tel = telHref(settings.telefono);
  const wa = waHref(settings.whatsapp, pick(settings.whatsappTesto, locale));
  const ritratto = home.ritratto;

  return (
    <section className="contenitore pt-8 md:pt-14">
      <Reveal className="osso osso-lg cucitura relative overflow-hidden">
        <div className="pointer-events-none absolute -left-24 -top-24 h-80 w-80 rounded-full bg-menta blur-3xl" aria-hidden="true" />
        <div className="pointer-events-none absolute -right-16 top-1/3 h-72 w-72 rounded-full bg-pesca blur-3xl" aria-hidden="true" />
        <div className="relative grid gap-8 p-7 md:grid-cols-[1.15fr_1fr] md:items-center md:gap-12 md:p-12 lg:p-16">
          <div>
            {pick(home.eyebrow, locale) && <p className="eyebrow mb-4">{pick(home.eyebrow, locale)}</p>}
            <h1 className="text-[2.6rem] leading-[1.02] md:text-[3.6rem] lg:text-[4.2rem]">{pick(home.titolo, locale)}</h1>
            <p className="mt-5 max-w-xl text-[1.1rem] leading-relaxed text-grafite md:text-[1.2rem]">{pick(home.sottotitolo, locale)}</p>
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
              <Link href={href(locale, { kind: "dove" })} className="btn btn-ghost">
                {m.cta.dove}
                <Segno nome="freccia" size={18} />
              </Link>
            </div>
          </div>

          {/* Finestra: il ritratto alloggiato in una cavità scavata nella lastra */}
          <div className="relative mx-auto w-full max-w-[26rem] md:max-w-none">
            <div
              className="incavo relative aspect-[4/5] overflow-hidden"
              style={{ borderRadius: "46% 54% 48% 52% / 52% 44% 56% 48%" }}
            >
              {ritratto?.src ? (
                <Image
                  src={ritratto.src}
                  alt={pick(ritratto.alt, locale) || m.a11y.ritrattoDi}
                  fill
                  priority
                  sizes="(min-width: 768px) 40vw, 90vw"
                  className="object-cover"
                />
              ) : (
                <div className="absolute inset-0 grid place-items-center bg-gradient-to-b from-osso-2 to-osso-3 text-petrolio/50">
                  <Segno nome="spalla" size={96} strokeWidth={1} />
                </div>
              )}
              <div className="pointer-events-none absolute inset-0 shadow-[inset_0_12px_30px_rgba(26,30,34,.14),inset_0_-4px_12px_rgba(255,255,255,.5)]" style={{ borderRadius: "inherit" }} aria-hidden="true" />
            </div>
          </div>
        </div>
      </Reveal>
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
    <Sezione eyebrow={m.nav.cosaCuro} titolo={m.home.cosaCuroTitolo} lead={m.home.cosaCuroLead} azione={{ href: href(locale, { kind: "cosaCuro" }), label: m.cta.tutte }}>
      <Strati className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {principali.map((p, i) => (
          <div
            key={p.slug}
            className="strato"
            style={{ "--strato-y": `${-i * 56}px`, "--strato-rot": `${(i - (principali.length - 1) / 2) * -1.2}deg` } as React.CSSProperties}
          >
            <SchedaPatologia p={p} locale={locale} index={i} strato />
          </div>
        ))}
      </Strati>
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
      <Reveal className="incavo p-2 sm:p-3">
        <ul className="grid gap-2 sm:grid-cols-2 sm:gap-3 lg:grid-cols-4">
          {sedi.map((s, i) => (
            <Reveal key={s.slug} as="li" delay={i * 80}>
              <ModuloSede s={s} locale={locale} />
            </Reveal>
          ))}
        </ul>
      </Reveal>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ Perché fidarsi */
export function FasciaFiducia({ home, locale }: { home: Home; locale: Locale }) {
  const m = getMessages(locale);
  const voci = (home.fiducia ?? []).filter((v) => pick(v.testo, locale));
  if (!voci.length) return null;
  return (
    <Sezione eyebrow={m.nav.chiSono} titolo={m.home.fiduciaTitolo} azione={{ href: href(locale, { kind: "chiSono" }), label: m.nav.chiSono }}>
      <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
        {voci.map((v, i) => (
          <Reveal key={i} as="li" delay={i * 70} className="osso osso-sm flex items-start gap-3 p-4">
            <span className="incavo grid h-9 w-9 shrink-0 place-items-center text-petrolio">
              <Segno nome={isSegno(v.segno) ? v.segno : "check"} size={18} />
            </span>
            <span className="pt-1.5 text-[0.95rem] leading-snug">{pick(v.testo, locale)}</span>
          </Reveal>
        ))}
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
      <ul className="grid gap-4 md:grid-cols-3">
        {voci.map((r, i) => (
          <Reveal key={r.slug} as="li" delay={i * 90} className="osso p-6">
            <blockquote className="serif text-[1.15rem] leading-relaxed">“{pick(r.testo, locale)}”</blockquote>
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
    <Sezione eyebrow={m.nav.quaderno} titolo={m.home.quadernoTitolo} lead={m.home.quadernoLead} azione={{ href: href(locale, { kind: "quaderno" }), label: m.cta.tutte }}>
      <ul className="grid gap-4 md:grid-cols-3">
        {voci.slice(0, 3).map((v, i) => (
          <Reveal key={v.item.slug} as="li" delay={i * 90}>
            {v.tipo === "paper" ? <SchedaPaper p={v.item} locale={locale} /> : <SchedaNota n={v.item} locale={locale} />}
          </Reveal>
        ))}
      </ul>
    </Sezione>
  );
}
