import type { Metadata } from "next";
import Image from "next/image";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { annoPercorso, getProfilo, getPubblicazioni, getSedi, getSettings, tipoPercorso } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata, physicianJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Briciole, Sezione } from "@/components/blocks/Pagina";
import { BarrePercorso } from "@/components/blocks/BarrePercorso";
import { ListaPubblicazioni } from "@/components/blocks/ListaPubblicazioni";
import { hrefArticolo, srcPaper } from "@/lib/media";
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
    image: p.seo?.ogImage ?? p.ritratto?.src,
    noindex: p.seo?.noindex,
  });
}

export default async function ChiSonoPage({ params }: PageProps<"/[locale]/chi-sono">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, p, paper, sedi] = await Promise.all([getSettings(), getProfilo(), getPubblicazioni(), getSedi()]);
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

      {/* Apertura: ritratto + testo allineati in alto, un solo blocco. */}
      <section className="contenitore pt-6 md:pt-10">
        <Reveal>
          <div className="grid max-w-5xl gap-8 md:grid-cols-[16.5rem_minmax(0,1fr)] md:items-start md:gap-14">
            <div className="relative mx-auto aspect-[4/5] w-full max-w-[16.5rem] overflow-hidden bg-petrolio-3 md:mx-0 md:max-w-none">
              {p.ritratto?.src ? (
                <Image src={p.ritratto.src} alt={pick(p.ritratto.alt, l) || m.a11y.ritrattoDi} fill priority sizes="(min-width: 768px) 18rem, 80vw" className="object-cover" />
              ) : (
                <div className="absolute inset-0 grid place-items-center text-petrolio/50">
                  <Segno nome="spalla" size={80} strokeWidth={1} />
                </div>
              )}
            </div>
            <div>
              <p className="eyebrow mb-3">{m.chiSono.titolo}</p>
              <h1 className="text-[2.4rem] leading-[1.05] md:text-[3.2rem]">{p.nome}</h1>
              {pick(p.titolo, l) && (
                <p className="mt-3 max-w-md text-[1.05rem] leading-snug text-grafite">{pick(p.titolo, l)}</p>
              )}
              <p className="mt-6 max-w-xl text-[1.12rem] leading-relaxed text-inchiostro">{pick(p.apertura, l)}</p>
              {p.lingue && p.lingue.length > 0 && (
                <p className="mt-6 flex flex-wrap items-center gap-1.5 text-sm text-grafite">
                  <Segno nome="globo" size={16} className="text-nebbia" />
                  {p.lingue.join(" · ")}
                </p>
              )}
            </div>
          </div>
        </Reveal>
      </section>

      {/* In evidenza */}
      {p.inEvidenza && p.inEvidenza.length > 0 && (
        <Sezione titolo={m.chiSono.inEvidenza} tinta="osso">
          <ol className="grid gap-10 md:grid-cols-2">
            {p.inEvidenza.map((v, i) => (
              <Reveal key={i} as="li" delay={i * 80} className={i === 0 ? "md:col-span-2" : undefined}>
                <p className="eyebrow text-rame">{v.anno}</p>
                <h3 className={`mt-2 leading-tight ${i === 0 ? "text-[1.9rem]" : "text-[1.4rem]"}`}>{pick(v.titolo, l)}</h3>
                <p className="mt-2 text-grafite">{pick(v.testo, l)}</p>
              </Reveal>
            ))}
          </ol>
        </Sezione>
      )}

      {barre.some((b) => b.voci.length > 0) && (
        <Sezione titolo={m.chiSono.percorso}>
          <BarrePercorso barre={barre} />
        </Sezione>
      )}

      {listaPaper.length > 0 && (
        <Sezione eyebrow={m.nav.quaderno} titolo={m.chiSono.pubblicazioni} azione={{ href: href(l, { kind: "quadernoPubblicazioni" }), label: m.chiSono.tuttePubblicazioni }} tinta="osso">
          <ListaPubblicazioni voci={listaPaper} more={m.cta.mostraTutte} less={m.cta.mostraMeno} pdfLabel={m.cta.pdf} articoloLabel={m.cta.articolo} />
        </Sezione>
      )}

      {/* Docenza, come valuto, territorio */}
      <Sezione>
        <div className="grid gap-4 md:grid-cols-3">
          {p.docenza && p.docenza.length > 0 && (
            <Reveal className="osso p-6">
              <h2 className="text-[1.35rem]">{m.chiSono.docenza}</h2>
              <ul className="mt-4 space-y-2 text-[0.95rem]">
                {p.docenza.map((d, i) => (
                  <li key={i}>
                    <span className="text-xs font-semibold text-grafite">{d.periodo}</span>
                    <span className="block">{pick(d.testo, l)}</span>
                  </li>
                ))}
              </ul>
              {p.societa && p.societa.length > 0 && <p className="mt-4 text-sm text-grafite">{p.societa.join(" · ")}</p>}
            </Reveal>
          )}
          {pick(p.comeValuto, l) && (
            <Reveal delay={80} className="osso vetro vetro-pesca p-6">
              <h2 className="text-[1.35rem]">{m.chiSono.comeValuto}</h2>
              <p className="mt-3 text-[0.98rem] leading-relaxed text-grafite">{pick(p.comeValuto, l)}</p>
            </Reveal>
          )}
          {pick(p.territorio, l) && (
            <Reveal delay={160} className="osso p-6">
              <h2 className="text-[1.35rem]">{m.chiSono.territorio}</h2>
              <p className="mt-3 text-[0.98rem] leading-relaxed text-grafite">{pick(p.territorio, l)}</p>
            </Reveal>
          )}
        </div>
      </Sezione>

      <FasciaContatto locale={l} />
    </>
  );
}
