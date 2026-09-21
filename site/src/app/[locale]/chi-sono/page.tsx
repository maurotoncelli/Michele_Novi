import type { Metadata } from "next";
import type { CSSProperties } from "react";
import Image from "next/image";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { annoPercorso, getHome, getProfilo, getPubblicazioni, getSedi, getSettings, tipoPercorso } from "@/lib/content";
import { VideoLastra } from "@/components/ui/VideoLastra";
import { breadcrumbJsonLd, buildMetadata, physicianJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Briciole, Sezione } from "@/components/blocks/Pagina";
import { BarrePercorso } from "@/components/blocks/BarrePercorso";
import { ListaPubblicazioni } from "@/components/blocks/ListaPubblicazioni";
import { hrefArticolo, srcMedia, srcPaper } from "@/lib/media";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/chi-sono">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, p] = await Promise.all([getSettings(), getProfilo()]);
  const m = getMessages(l);
  return buildMetadata(s, {
    locale: l,
    route: { kind: "chiSono" },
    title: pick(p.seo?.title, l) || `${m.chiSono.titolo} — ${p.nome}`,
    description: pick(p.seo?.description, l) || pick(p.apertura, l),
    image: p.seo?.ogImage ?? srcMedia(p.ritratto?.src, "profilo") ?? undefined,
    noindex: p.seo?.noindex,
  });
}

/** Prima frase come titolo, il resto come lead. */
function spezza(testo: string): { titolo: string; resto: string } {
  const i = testo.search(/[.!?]\s/);
  if (i < 0) return { titolo: testo, resto: "" };
  return { titolo: testo.slice(0, i + 1).trim(), resto: testo.slice(i + 1).trim() };
}

export default async function ChiSonoPage({ params }: PageProps<"/[locale]/chi-sono">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, p, paper, sedi, home] = await Promise.all([getSettings(), getProfilo(), getPubblicazioni(), getSedi(), getHome()]);
  const m = getMessages(l);
  const principali = paper.filter((x) => x.principale);
  const listaPaper = (principali.length ? principali : paper).map((x) => ({
    href: href(l, { kind: "paper", slug: x.slug }),
    anno: x.anno,
    titolo: pick(x.titoloBreve, l) || x.titolo,
    rivista: x.rivista,
    pdf: srcPaper(x.pdf),
    articolo: hrefArticolo(x.doi, x.url),
  }));
  const barre = (
    [
      { id: "lavoro" as const, titolo: m.chiSono.esperienze },
      { id: "fellowship" as const, titolo: m.chiSono.fellowship },
      { id: "formazione" as const, titolo: m.chiSono.formazione },
    ]
  ).map((b) => ({
    ...b,
    voci: (p.timeline ?? [])
      .filter((t) => tipoPercorso(t) === b.id)
      .slice()
      .sort((a, b2) => annoPercorso(a.periodo) - annoPercorso(b2.periodo))
      .map((t) => ({ periodo: t.periodo, titolo: pick(t.titolo, l), luogo: t.luogo })),
  }));

  const ritratto = srcMedia(p.ritratto?.src, "profilo");
  const manifesto = pick(p.comeValuto, l) ? spezza(pick(p.comeValuto, l)) : null;
  const passi = (p.comeValutoPassi ?? []).filter((v) => pick(v.titolo, l));
  const lavoroFoto = srcMedia(home.lavoro?.foto?.src, "home");
  const lavoroVideo = home.lavoro?.video ? (home.lavoro.video.startsWith("/") ? home.lavoro.video : `/videos/${home.lavoro.video}`) : null;
  // In grande va l'incarico di oggi (flag in Keystatic; in mancanza, l'anno che inizia con "dal", poi l'ultima).
  // Le altre restano nell'ordine del contenuto, cioè cronologico.
  const tappe = (p.inEvidenza ?? []).filter((v) => pick(v.titolo, l));
  const oggi = tappe.find((v) => v.attuale) ?? tappe.find((v) => /^(dal|since)\s/i.test(v.anno ?? "")) ?? tappe.at(-1);
  const altre = tappe.filter((v) => v !== oggi);
  const oggiAnno = oggi?.anno?.match(/\d{4}/)?.[0] ?? oggi?.anno ?? "";

  // Riga dei fatti sotto l'apertura: cose verificabili, non aggettivi.
  const lavoroAttuale = (p.timeline ?? [])
    .filter((t) => tipoPercorso(t) === "lavoro" && /^dal\s/i.test(t.periodo ?? ""))
    .sort((a, b) => annoPercorso(b.periodo) - annoPercorso(a.periodo))[0];
  const fatti = [
    s.albo,
    lavoroAttuale ? `${pick(lavoroAttuale.titolo, l)} · ${lavoroAttuale.periodo}` : null,
    p.lingue?.length ? p.lingue.join(" · ") : null,
  ].filter(Boolean) as string[];

  return (
    <>
      <JsonLd
        data={[
          physicianJsonLd(s, p, sedi, l),
          breadcrumbJsonLd(s, [
            { name: m.meta.siteName, path: href(l, { kind: "home" }) },
            { name: m.chiSono.titolo, path: href(l, { kind: "chiSono" }) },
          ]),
        ]}
      />
      <Briciole items={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.chiSono.titolo }]} />

      {/* 1. Apertura: il ritratto a sinistra prende tutta l'altezza del testo; i fatti chiudono in basso, allineati al bordo della foto. */}
      <section className="contenitore pb-16 pt-8 md:pb-24 md:pt-12">
        <Reveal immediate>
          <div className="grid gap-10 md:grid-cols-[minmax(0,19rem)_minmax(0,1fr)] md:items-stretch md:gap-14 lg:grid-cols-[minmax(0,23rem)_minmax(0,1fr)] lg:gap-20">
            <div className="relative aspect-[4/5] w-full overflow-hidden bg-osso-2 md:aspect-auto md:h-full md:min-h-[28rem]">
              {ritratto ? (
                <Image src={ritratto} alt={pick(p.ritratto?.alt, l) || m.a11y.ritrattoDi} fill priority sizes="(min-width: 1024px) 23rem, (min-width: 768px) 19rem, 100vw" className="object-cover object-top" />
              ) : (
                <div className="absolute inset-0 grid place-items-center text-petrolio/50">
                  <Segno nome="spalla" size={80} strokeWidth={1} />
                </div>
              )}
            </div>
            <div className="flex min-w-0 flex-col">
              <p className="eyebrow mb-5">{m.chiSono.titolo}</p>
              <h1 className="display-l">{p.nome}</h1>
              {pick(p.titolo, l) && <p className="mt-5 max-w-lg text-[1.15rem] leading-snug text-grafite md:text-[1.25rem]">{pick(p.titolo, l)}</p>}
              <p className="lead mt-8 max-w-2xl text-inchiostro">{pick(p.apertura, l)}</p>
              {fatti.length > 0 && (
                <ul className="mt-auto flex flex-wrap gap-x-6 gap-y-2 border-t border-linea pt-6 text-sm text-grafite max-md:mt-10 md:pt-6">
                  {fatti.map((f) => (
                    <li key={f}>{f}</li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </Reveal>
      </section>

      {/* 2. Come valuto: la frase forte come titolo; sotto, la lastra del lavoro e i tre passi della visita. */}
      {manifesto && (
        <Sezione eyebrow={m.chiSono.comeValuto} titolo={manifesto.titolo} lead={(passi.length && manifesto.resto ? spezza(manifesto.resto).titolo : manifesto.resto) || undefined} tinta="osso" misura="varco">
          {(passi.length > 0 || lavoroFoto) && (
            <div className="grid gap-12 lg:grid-cols-[minmax(0,0.85fr)_minmax(0,1.15fr)] lg:gap-24">
              {lavoroFoto && (
                <Reveal className="self-start">
                  <div className="fluttua" style={{ "--fluttua-da": "5%", "--fluttua-a": "-5%", "--fluttua-scala": "1" } as CSSProperties}>
                    <VideoLastra video={lavoroVideo} foto={lavoroFoto} alt={pick(home.lavoro?.foto?.alt, l) || m.chiSono.comeValuto} ratio="4/5" sizes="(min-width: 1024px) 34vw, 100vw" />
                  </div>
                </Reveal>
              )}
              {passi.length > 0 && (
                <ol className="divide-y divide-linea self-start">
                  {passi.map((v, i) => (
                    <Reveal key={i} as="li" delay={i * 130} className="grid grid-cols-[4rem_minmax(0,1fr)] gap-6 py-9 first:pt-0 last:pb-0 md:grid-cols-[5.5rem_minmax(0,1fr)] md:py-11">
                      <span className="cifra-m pt-1 text-rame" aria-hidden="true">
                        {String(i + 1).padStart(2, "0")}
                      </span>
                      <div className="min-w-0">
                        <h3 className="text-[1.5rem] leading-tight md:text-[1.9rem]">{pick(v.titolo, l)}</h3>
                        {pick(v.testo, l) && <p className="lead mt-4 max-w-xl">{pick(v.testo, l)}</p>}
                      </div>
                    </Reveal>
                  ))}
                </ol>
              )}
            </div>
          )}
        </Sezione>
      )}

      {/* 3. Oggi in grande (dove opera), le tappe di formazione in colonna, in ordine cronologico. */}
      {oggi && (
        <Sezione eyebrow={m.chiSono.inEvidenzaEyebrow} titolo={m.chiSono.inEvidenza} misura="varco">
          <div className="grid gap-14 lg:grid-cols-[minmax(0,1.15fr)_minmax(0,1fr)] lg:gap-24">
            <Reveal className="relative">
              <span aria-hidden="true" className="cifra-fondo">
                {oggiAnno}
              </span>
              <div className="relative pt-[clamp(4rem,10vw,9rem)]">
                <p className="eyebrow text-rame">
                  {m.chiSono.inEvidenzaOggi} · {oggi.anno}
                </p>
                <h3 className="display-m mt-4">{pick(oggi.titolo, l)}</h3>
                <p className="lead mt-5 max-w-xl">{pick(oggi.testo, l)}</p>
              </div>
            </Reveal>
            {altre.length > 0 && (
              <div className="lg:pt-[clamp(4rem,10vw,9rem)]">
                <p className="eyebrow mb-5">{m.chiSono.inEvidenzaTappe}</p>
                <ol className="divide-y divide-linea border-t border-linea">
                  {altre.map((v, i) => (
                    <Reveal key={i} as="li" delay={i * 90} className="grid grid-cols-[5.5rem_minmax(0,1fr)] gap-4 py-6">
                      <span className="eyebrow pt-1.5 text-rame">{v.anno}</span>
                      <div className="min-w-0">
                        <h3 className="text-[1.2rem] leading-snug">{pick(v.titolo, l)}</h3>
                        {pick(v.testo, l) && <p className="mt-1.5 text-[0.95rem] leading-relaxed text-grafite">{pick(v.testo, l)}</p>}
                      </div>
                    </Reveal>
                  ))}
                </ol>
              </div>
            )}
          </div>
        </Sezione>
      )}

      {/* 4. Il percorso, anno per anno: le tre barre. */}
      {barre.some((b) => b.voci.length > 0) && (
        <Sezione eyebrow={m.chiSono.percorsoEyebrow} titolo={m.chiSono.percorso} tinta="osso">
          <BarrePercorso barre={barre} />
        </Sezione>
      )}

      {/* 5. Pubblicazioni principali. */}
      {listaPaper.length > 0 && (
        <Sezione eyebrow={m.nav.pubblicazioni} titolo={m.chiSono.pubblicazioni} azione={{ href: href(l, { kind: "approfondimentiPubblicazioni" }), label: m.chiSono.tuttePubblicazioni }}>
          <ListaPubblicazioni voci={listaPaper} more={m.cta.mostraTutte} less={m.cta.mostraMeno} pdfLabel={m.cta.pdf} articoloLabel={m.cta.articolo} />
        </Sezione>
      )}

      {/* 6. Insegno · Territorio · Società: testo, non scatole. */}
      {((p.docenza && p.docenza.length > 0) || pick(p.territorio, l)) && (
        <Sezione tinta="osso">
          <div className="grid gap-12 md:grid-cols-2 lg:grid-cols-[minmax(0,1fr)_minmax(0,1fr)_minmax(0,0.7fr)] lg:gap-16">
            {p.docenza && p.docenza.length > 0 && (
              <Reveal>
                <p className="eyebrow">{m.chiSono.docenza}</p>
                <ul className="mt-5 space-y-4">
                  {p.docenza.map((d, i) => (
                    <li key={i} className="text-[1.05rem] leading-relaxed">
                      {d.periodo && <span className="block text-sm text-grafite">{d.periodo}</span>}
                      {pick(d.testo, l)}
                    </li>
                  ))}
                </ul>
              </Reveal>
            )}
            {pick(p.territorio, l) && (
              <Reveal delay={90}>
                <p className="eyebrow">{m.chiSono.territorio}</p>
                <p className="mt-5 text-[1.05rem] leading-relaxed">{pick(p.territorio, l)}</p>
              </Reveal>
            )}
            {p.societa && p.societa.length > 0 && (
              <Reveal delay={180}>
                <p className="eyebrow">{m.chiSono.societa}</p>
                <ul className="mt-5 space-y-1.5 text-[1.05rem]">
                  {p.societa.map((x) => (
                    <li key={x}>{x}</li>
                  ))}
                </ul>
              </Reveal>
            )}
          </div>
        </Sezione>
      )}

      <FasciaContatto locale={l} />
    </>
  );
}
