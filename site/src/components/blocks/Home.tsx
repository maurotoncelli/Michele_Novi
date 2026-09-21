import Link from "next/link";
import Image from "next/image";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import type { Home, Nota, Patologia, Profilo, Pubblicazione, Recensione, Sede, Settings } from "@/lib/content";
import { slugNota, slugPatologia, telHref, waHref } from "@/lib/content";
import { srcMedia } from "@/lib/media";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";
import { ModuloSede, SchedaNota, SchedaPaper, SchedaPatologia } from "./Schede";
import { Sezione } from "./Pagina";

/* ------------------------------------------------------------------ Hero: due colonne, la foto è un ritratto, non uno sfondo */
export function Hero({ home, settings, locale }: { home: Home; settings: Settings; locale: Locale }) {
  const m = getMessages(locale);
  const tel = telHref(settings.telefono);
  const wa = waHref(settings.whatsapp, pick(settings.whatsappTesto, locale));
  const ritratto = home.ritratto;
  const foto = srcMedia(ritratto?.src, "home") ?? "/images/home/ritratto-placeholder.jpg";

  return (
    <section className="relative left-1/2 w-screen -translate-x-1/2 overflow-hidden bg-campo">
      <div className="hero-griglia">
        {/* Ritratto a vivo: primo su mobile, a destra da desktop */}
        <div className="hero-media">
          <Image
            src={foto}
            alt={pick(ritratto?.alt, locale) || m.a11y.ritrattoDi}
            fill
            priority
            sizes="(min-width: 1024px) 53vw, 100vw"
            className="parallasse object-cover object-[50%_20%]"
          />
        </div>

        {/* Testo */}
        <div className="hero-testo margine-sx flex flex-col justify-end pb-12 pt-10 lg:py-16 lg:pr-12">
          <Reveal immediate className="max-w-2xl">
            {pick(home.eyebrow, locale) && <p className="eyebrow mb-5">{pick(home.eyebrow, locale)}</p>}
            <h1 className="display-xl">{pick(home.titolo, locale)}</h1>
            <p className="lead mt-7 max-w-xl">{pick(home.sottotitolo, locale)}</p>
            <div className="mt-10 flex flex-wrap items-center gap-2">
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
    <section className="border-y border-linea" aria-label={m.home.fiduciaEyebrow}>
      <ul className="contenitore grid grid-cols-2 gap-x-8 gap-y-12 py-12 md:py-16 lg:grid-cols-4">
        {fatti.map((f, i) => (
          <Reveal key={f.label} as="li" delay={i * 90} className="min-w-0">
            <p className="cifra flex items-baseline gap-2">
              {f.prefisso && <span className="text-[0.32em] font-medium tracking-normal text-grafite">{f.prefisso}</span>}
              {f.valore}
            </p>
            <p className="mt-4 max-w-[13rem] text-[0.95rem] leading-snug text-grafite">{f.label}</p>
          </Reveal>
        ))}
      </ul>
    </section>
  );
}

/* ------------------------------------------------------------------ 01 Cosa curo: quattro righe dense, tutto a colpo d'occhio */
export function FasciaPatologie({ patologie, locale }: { patologie: Patologia[]; locale: Locale }) {
  const m = getMessages(locale);
  const principali = patologie.filter((p) => !p.secondaria);
  const centro = principali.find((p) => p.principale) ?? principali[0];
  const ordinate = centro ? [centro, ...principali.filter((p) => p !== centro)].slice(0, 4) : [];
  const secondarie = patologie.filter((p) => p.secondaria);
  if (!ordinate.length) return null;
  return (
    <Sezione indice="01" eyebrow={m.nav.cosaCuro} titolo={m.home.cosaCuroTitolo} lead={m.home.cosaCuroLead} azione={{ href: href(locale, { kind: "cosaCuro" }), label: m.cta.tutte }} tinta="osso">
      <ul className="grid items-stretch gap-x-12 gap-y-10 md:grid-cols-2 lg:gap-x-16 lg:gap-y-12">
        {ordinate.map((p, i) => (
          <Reveal key={p.slug} as="li" delay={i * 70} className="h-full min-w-0">
            <SchedaPatologia p={p} locale={locale} riga />
          </Reveal>
        ))}
      </ul>
      {secondarie.length > 0 && (
        <Reveal className="mt-12 flex flex-wrap items-center gap-x-3 gap-y-1 border-t border-linea pt-6 text-[0.95rem] text-grafite">
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

/* ------------------------------------------------------------------ 02 Dove: le città come titolo */
export function FasciaSedi({ sedi, locale }: { sedi: Sede[]; locale: Locale }) {
  const m = getMessages(locale);
  if (!sedi.length) return null;
  return (
    <Sezione indice="02" eyebrow={m.nav.dove} titolo={m.home.doveTitolo} lead={m.home.doveLead} azione={{ href: href(locale, { kind: "dove" }), label: m.cta.tutte }} misura="affermazione">
      <ul className="grid items-stretch gap-x-8 gap-y-12 sm:grid-cols-2 lg:grid-cols-4">
        {sedi.map((s, i) => (
          <Reveal key={s.slug} as="li" delay={i * 80} className="h-full min-w-0">
            <ModuloSede s={s} locale={locale} grande />
          </Reveal>
        ))}
      </ul>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ 03 Percorso: luoghi e anni, non aggettivi */
export function FasciaPercorso({ profilo, locale }: { profilo: Profilo; locale: Locale }) {
  const m = getMessages(locale);
  const tappe = (profilo.inEvidenza ?? []).filter((v) => pick(v.titolo, locale));
  if (!tappe.length) return null;
  const [prima, ...altre] = tappe;
  return (
    <Sezione indice="03" eyebrow={m.home.fiduciaEyebrow} titolo={m.home.fiduciaTitolo} lead={m.home.fiduciaLead} azione={{ href: href(locale, { kind: "chiSono" }), label: m.nav.chiSono }} tinta="osso" misura="varco">
      <div className="grid gap-14 lg:grid-cols-[minmax(0,1.15fr)_minmax(0,1fr)] lg:gap-24">
        <Reveal className="relative">
          <span aria-hidden="true" className="cifra-fondo">
            {prima.anno}
          </span>
          <div className="relative pt-[clamp(4rem,10vw,9rem)]">
            <p className="eyebrow text-rame">{prima.anno}</p>
            <h3 className="display-m mt-4">{pick(prima.titolo, locale)}</h3>
            <p className="lead mt-5 max-w-xl">{pick(prima.testo, locale)}</p>
          </div>
        </Reveal>
        {altre.length > 0 && (
          <ol className="divide-y divide-linea lg:pt-[clamp(4rem,10vw,9rem)]">
            {altre.map((v, i) => (
              <Reveal key={i} as="li" delay={i * 90} className="grid grid-cols-[5.5rem_minmax(0,1fr)] gap-4 py-6 first:pt-0">
                <span className="eyebrow pt-1.5">{v.anno}</span>
                <div className="min-w-0">
                  <h3 className="text-[1.2rem] leading-snug">{pick(v.titolo, locale)}</h3>
                  {pick(v.testo, locale) && <p className="mt-1.5 text-[0.95rem] leading-relaxed text-grafite">{pick(v.testo, locale)}</p>}
                </div>
              </Reveal>
            ))}
          </ol>
        )}
      </div>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ 04 Recensioni: una grande, due a lato */
export function FasciaRecensioni({ recensioni, locale }: { recensioni: Recensione[]; locale: Locale }) {
  const m = getMessages(locale);
  const voci = recensioni.slice(0, 3);
  if (!voci.length) return null;
  const [prima, ...altre] = voci;
  const piattaforme = [...new Set(recensioni.map((r) => r.piattaforma).filter(Boolean))];
  const eyebrow = piattaforme.length ? `${m.home.recensioniEyebrow} · ${piattaforme.join(", ")}` : m.home.recensioniEyebrow;
  return (
    <Sezione indice="04" eyebrow={eyebrow} titolo={m.home.recensioniTitolo} misura="affermazione">
      <div className="grid gap-14 lg:grid-cols-[minmax(0,1.35fr)_minmax(0,1fr)] lg:gap-24">
        <Reveal as="figure" className="relative">
          <span aria-hidden="true" className="absolute -left-2 -top-10 select-none text-[7rem] leading-none text-osso-3 md:-top-14 md:text-[10rem]">
            “
          </span>
          <blockquote className="citazione relative text-inchiostro">{pick(prima.testo, locale)}</blockquote>
          <figcaption className="mt-7 text-[0.95rem] text-grafite">
            <span className="font-semibold text-inchiostro">{prima.nome}</span>
            {prima.piattaforma ? ` · ${prima.piattaforma}` : ""}
          </figcaption>
        </Reveal>
        {altre.length > 0 && (
          <div className="grid content-start gap-10 lg:pt-3">
            {altre.map((r, i) => (
              <Reveal key={r.slug} as="figure" delay={120 + i * 90}>
                <blockquote className="text-[1.08rem] leading-relaxed">“{pick(r.testo, locale)}”</blockquote>
                <figcaption className="mt-3 text-sm text-grafite">
                  <span className="font-semibold text-inchiostro">{r.nome}</span>
                  {r.piattaforma ? ` · ${r.piattaforma}` : ""}
                </figcaption>
              </Reveal>
            ))}
          </div>
        )}
      </div>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ 05 Approfondimenti: un pezzo grande, gli altri in lista */
type Voce = { tipo: "paper"; item: Pubblicazione } | { tipo: "nota"; item: Nota };

function RigaVoce({ v, locale }: { v: Voce; locale: Locale }) {
  const m = getMessages(locale);
  if (v.tipo === "paper") {
    const p = v.item;
    return (
      <Link href={href(locale, { kind: "paper", slug: p.slug })} className="group grid grid-cols-[4rem_minmax(0,1fr)] gap-4 py-6 first:pt-0">
        <span className="pt-1 text-sm text-grafite">{p.anno}</span>
        <span className="min-w-0">
          <span className="tag tag-petrolio">{m.quaderno.paper}</span>
          <span className="mt-3 block text-[1.15rem] leading-snug group-hover:text-petrolio">{pick(p.titoloBreve, locale) || p.titolo}</span>
          <span className="mt-1.5 block truncate text-sm text-grafite">{p.rivista}</span>
        </span>
      </Link>
    );
  }
  const n = v.item;
  return (
    <Link href={href(locale, { kind: "nota", slug: slugNota(n, locale) })} className="group grid grid-cols-[4rem_minmax(0,1fr)] gap-4 py-6 first:pt-0">
      <span className="pt-1 text-sm text-grafite">{n.data ? new Date(n.data).getFullYear() : ""}</span>
      <span className="min-w-0">
        <span className="tag tag-rame">{m.quaderno.nota}</span>
        <span className="mt-3 block text-[1.15rem] leading-snug group-hover:text-petrolio">{pick(n.titolo, locale)}</span>
        {pick(n.lead, locale) && <span className="mt-1.5 line-clamp-2 block text-sm text-grafite">{pick(n.lead, locale)}</span>}
      </span>
    </Link>
  );
}

export function FasciaQuaderno({ voci, locale }: { voci: Voce[]; locale: Locale }) {
  const m = getMessages(locale);
  if (!voci.length) return null;
  const grande = voci.find((v) => v.tipo === "nota") ?? voci[0];
  const resto = voci.filter((v) => v !== grande).slice(0, 4);
  return (
    <Sezione indice="05" eyebrow={m.nav.quaderno} titolo={m.home.quadernoTitolo} lead={m.home.quadernoLead} azione={{ href: href(locale, { kind: "quaderno" }), label: m.cta.tutte }} tinta="osso">
      <div className="grid gap-12 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)] lg:gap-20">
        <Reveal className="min-w-0">
          {grande.tipo === "paper" ? <SchedaPaper p={grande.item} locale={locale} grande /> : <SchedaNota n={grande.item} locale={locale} grande />}
        </Reveal>
        {resto.length > 0 && (
          <Reveal delay={120} className="divide-y divide-linea self-start">
            {resto.map((v) => (
              <RigaVoce key={v.item.slug} v={v} locale={locale} />
            ))}
          </Reveal>
        )}
      </div>
    </Sezione>
  );
}
