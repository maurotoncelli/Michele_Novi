import Link from "next/link";
import Image from "next/image";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import type { Home, Nota, Patologia, Profilo, Pubblicazione, Recensione, Sede, Settings } from "@/lib/content";
import { slugPatologia, telHref, waHref } from "@/lib/content";
import { srcMedia } from "@/lib/media";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";
import { Contatore } from "../ui/Contatore";
import { VideoLastra } from "../ui/VideoLastra";
import { PercorsoScorrevole } from "./PercorsoScorrevole";
import { ModuloSede, SchedaMetodo, SchedaNota, SchedaPaper, SchedaPatologia } from "./Schede";
import { Stelle } from "@/components/ui/Stelle";
import { Parole } from "@/components/ui/Parole";
import { Striscia } from "@/components/blocks/Striscia";
import { Sezione } from "./Pagina";

/* ------------------------------------------------------------------ Hero: immagine a tema a tutto schermo (desktop), testo sopra in basso a sinistra.
   Su mobile: immagine sopra, testo sotto. Non è un ritratto: il dottore sta in Chi sono. */
export function Hero({ home, settings, locale }: { home: Home; settings: Settings; locale: Locale }) {
  const m = getMessages(locale);
  const tel = telHref(settings.telefono);
  const wa = waHref(settings.whatsapp, pick(settings.whatsappTesto, locale));
  const immagine = home.ritratto;
  const foto = srcMedia(immagine?.src, "home") ?? "/images/home/hero-sala-placeholder.jpg";

  return (
    <section className="relative left-1/2 w-screen -translate-x-1/2 overflow-hidden bg-campo">
      <div className="hero-griglia">
        {/* Immagine a vivo: sopra su mobile, a tutto schermo da desktop. Il soggetto sta a destra, il testo a sinistra. */}
        <div className="hero-media">
          <Image
            src={foto}
            alt={pick(immagine?.alt, locale) || ""}
            fill
            priority
            quality={92}
            sizes="100vw"
            className="object-cover object-center"
          />
        </div>

        {/* Testo */}
        <div className="hero-testo margine-sx flex flex-col justify-end pb-12 pt-10 lg:pb-20 lg:pt-16 lg:pr-12">
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
            <p className="cifra-m flex items-baseline gap-2">
              {f.prefisso && <span className="text-[0.32em] font-medium tracking-normal text-grafite">{f.prefisso}</span>}
              <Contatore valore={f.valore} />
            </p>
            <p className="mt-4 max-w-[13rem] text-[0.95rem] leading-snug text-grafite">{f.label}</p>
          </Reveal>
        ))}
      </ul>
    </section>
  );
}

/* ------------------------------------------------------------------ 01 Cosa curo: tre colonne, poi il metodo a sé */
export function FasciaPatologie({ patologie, locale }: { patologie: Patologia[]; locale: Locale }) {
  const m = getMessages(locale);
  const metodo = patologie.find((p) => p.area === "metodo");
  const principali = patologie.filter((p) => !p.secondaria && p !== metodo);
  const centro = principali.find((p) => p.principale) ?? principali[0];
  const colonne = centro ? [centro, ...principali.filter((p) => p !== centro)].slice(0, 3) : [];
  const secondarie = patologie.filter((p) => p.secondaria);
  if (!colonne.length) return null;
  return (
    <>
      <Sezione indice="01" eyebrow={m.nav.cosaCuro} titolo={m.home.cosaCuroTitolo} lead={m.home.cosaCuroLead} azione={{ href: href(locale, { kind: "cosaCuro" }), label: m.cta.tutte }} tinta="osso">
        <ul className="binario items-stretch">
          {colonne.map((p, i) => (
            <Reveal key={p.slug} as="li" delay={i * 130} className="h-full min-w-0">
              <SchedaPatologia p={p} locale={locale} index={i} colonna />
            </Reveal>
          ))}
        </ul>
        {secondarie.length > 0 && (
          <Reveal className="mt-14 flex flex-wrap items-center gap-x-3 gap-y-1 border-t border-linea pt-6 text-[0.95rem] text-grafite">
          <span>{m.cosaCuro.secondarie}:</span>
          {secondarie.map((p) => (
            <Link key={p.slug} href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="underline decoration-linea underline-offset-4 hover:text-petrolio hover:decoration-petrolio">
              {pick(p.titolo, locale)}
            </Link>
          ))}
        </Reveal>
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
      <p className="mt-8 text-[0.8rem] text-nebbia">
        <a href="/images/sedi/ATTRIBUZIONI.txt" className="underline decoration-linea underline-offset-4 hover:text-petrolio">
          {m.dove.fotoCitta}
        </a>
      </p>
    </Sezione>
  );
}

/* ------------------------------------------------------------------ 03 Percorso: luoghi e anni, non aggettivi */
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
        const stelle = r.stelle ?? 5;
        return (
          <li key={r.slug} className="min-w-0">
            <figure className="recensione">
              <span aria-hidden="true" className="virgolette">
                “
              </span>
              <p className="eyebrow flex flex-wrap items-center gap-x-3 gap-y-1">
                {r.piattaforma && <span>{r.piattaforma}</span>}
                <Stelle n={stelle} label={m.home.stelleLabel.replace("{n}", String(stelle))} className="text-petrolio" />
              </p>
              {/* Le parole si compongono una dopo l'altra quando la scheda entra in vista. */}
              <Reveal as="blockquote" solo className="recensione-testo mt-4">
                <Parole testo={pick(r.testo, locale)} />
              </Reveal>
              <figcaption className="mt-5 text-[0.92rem] text-grafite">
                <span className="font-medium text-inchiostro">{r.nome}</span>
              </figcaption>
            </figure>
          </li>
        );
      })}
    </Striscia>
  );
}

/* ------------------------------------------------------------------ 05 Approfondimenti: sette schede in rotaia */
type Voce = { tipo: "paper"; item: Pubblicazione } | { tipo: "nota"; item: Nota };

export function FasciaApprofondimenti({ voci, locale }: { voci: Voce[]; locale: Locale }) {
  const m = getMessages(locale);
  if (!voci.length) return null;
  // Le note dal lavoro davanti, poi i paper: sette schede in fila, il resto nell'hub a griglia.
  const fila = [...voci.filter((v) => v.tipo === "nota"), ...voci.filter((v) => v.tipo === "paper")].slice(0, 7);
  return (
    <Striscia
      n={fila.length}
      scheda={20}
      gap={1.5}
      tinta="osso"
      testa={{ indice: "05", eyebrow: m.nav.approfondimenti, titolo: m.home.approfondimentiTitolo, lead: m.home.approfondimentiLead, azione: { href: href(locale, { kind: "approfondimenti" }), label: m.cta.vediGriglia } }}
    >
      {fila.map((v) => (
        <li key={`${v.tipo}-${v.item.slug}`} className="min-w-0">
          {v.tipo === "paper" ? <SchedaPaper p={v.item} locale={locale} /> : <SchedaNota n={v.item} locale={locale} />}
        </li>
      ))}
    </Striscia>
  );
}
