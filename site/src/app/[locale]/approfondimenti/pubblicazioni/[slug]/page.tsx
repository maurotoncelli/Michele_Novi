import type { Metadata } from "next";
import Link from "next/link";
import localFont from "next/font/local";
import { notFound } from "next/navigation";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getPatologie, getPubblicazione, getPubblicazioni, getSettings, slugPatologia } from "@/lib/content";
import { hrefArticolo, srcPaper } from "@/lib/media";
import { headingsMarkdown, renderMarkdown } from "@/lib/markdoc";
import { breadcrumbJsonLd, buildMetadata, paperJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Briciole, Disclaimer } from "@/components/blocks/Pagina";
import { Sommario } from "@/components/blocks/Sommario";
import { SchedaPatologia, SchedaPaper } from "@/components/blocks/Schede";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

/* Serif accademico solo per la Lettura dei paper: Source Serif 4 (OFL), caricato solo su questa pagina. */
const serifLettura = localFont({
  src: [
    { path: "../../../../fonts/SourceSerif4-Variable.woff2", style: "normal", weight: "200 900" },
    { path: "../../../../fonts/SourceSerif4-VariableItalic.woff2", style: "italic", weight: "200 900" },
  ],
  variable: "--font-lettura",
  display: "swap",
});

export const dynamicParams = false;
export async function generateStaticParams() {
  const all = await getPubblicazioni();
  return locales.flatMap((locale) => all.map((p) => ({ locale, slug: p.slug })));
}

export async function generateMetadata({ params }: PageProps<"/[locale]/approfondimenti/pubblicazioni/[slug]">): Promise<Metadata> {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, p] = await Promise.all([getSettings(), getPubblicazione(slug)]);
  if (!p) return {};
  return buildMetadata(s, {
    locale: l,
    route: { kind: "paper", slug: p.slug },
    title: pick(p.titoloBreve, l) || p.titolo,
    description: pick(p.riassunto, l) || p.abstract?.slice(0, 160) || `${p.rivista}, ${p.anno}`,
    type: "article",
    publishedTime: `${p.anno}-01-01`,
  });
}

export default async function PaperPage({ params }: PageProps<"/[locale]/approfondimenti/pubblicazioni/[slug]">) {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const p = await getPubblicazione(slug);
  if (!p) notFound();
  const [s, patologie, tutte] = await Promise.all([getSettings(), getPatologie(), getPubblicazioni()]);
  const m = getMessages(l);
  const correlate = (p.patologie ?? []).map((sl) => patologie.find((x) => x.slug === sl)).filter(Boolean) as typeof patologie;
  const altre = tutte.filter((x) => x.slug !== p.slug && (x.tag ?? []).some((t) => (p.tag ?? []).includes(t))).slice(0, 3);
  const titoloBreve = pick(p.titoloBreve, l);
  const articolo = hrefArticolo(p.doi, p.url);
  const pdf = srcPaper(p.pdf);
  const testo = p.testoIntegrale?.trim();
  const lettura = testo ? renderMarkdown(testo) : null;
  const sommario = [
    ...(pick(p.riassunto, l) ? [{ id: "in-breve", label: m.approfondimenti.riassunto }] : []),
    ...(testo ? headingsMarkdown(testo).map((h) => ({ id: h.id, label: h.text })) : p.abstract ? [{ id: "abstract", label: m.approfondimenti.abstract }] : []),
  ];

  return (
    <>
      <JsonLd
        data={[
          paperJsonLd(s, p, l),
          breadcrumbJsonLd(s, [
            { name: m.meta.siteName, path: href(l, { kind: "home" }) },
            { name: m.approfondimenti.titolo, path: href(l, { kind: "approfondimenti" }) },
            { name: m.approfondimenti.pubblicazioni, path: href(l, { kind: "approfondimentiPubblicazioni" }) },
            { name: titoloBreve || p.titolo, path: href(l, { kind: "paper", slug: p.slug }) },
          ]),
        ]}
      />
      <Briciole
        items={[
          { label: m.meta.siteName, href: href(l, { kind: "home" }) },
          { label: m.approfondimenti.titolo, href: href(l, { kind: "approfondimenti" }) },
          { label: m.approfondimenti.pubblicazioni, href: href(l, { kind: "approfondimentiPubblicazioni" }) },
          { label: titoloBreve || p.titolo },
        ]}
      />

      <article className="contenitore pt-8 md:pt-12">
        {/* Impaginato da paper: testata, titolo, autori, rivista, DOI */}
        <Reveal immediate className="relative max-w-3xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className="tag tag-petrolio">{m.approfondimenti.paper}</span>
              {p.principale && <span className="tag tag-rame">{m.approfondimenti.principale}</span>}
              <span className="text-sm text-grafite">{p.anno}</span>
            </div>
            {titoloBreve && <p className="eyebrow mt-6">{titoloBreve}</p>}
            <h1 className="display-m mt-2" lang="en">
              {p.titolo}
            </h1>
            <dl className="mt-6 grid gap-x-8 gap-y-3 text-[0.95rem] sm:grid-cols-2">
              {p.autori && (
                <div>
                  <dt className="eyebrow">{m.approfondimenti.autori}</dt>
                  <dd className="mt-1 text-grafite">{p.autori}</dd>
                </div>
              )}
              {p.rivista && (
                <div>
                  <dt className="eyebrow">{m.approfondimenti.rivista}</dt>
                  <dd className="mt-1 text-grafite">
                    <span className="italic">{p.rivista}</span>
                    {p.volume ? `, ${p.volume}` : ""} ({p.anno})
                  </dd>
                </div>
              )}
              {p.doi && (
                <div>
                  <dt className="eyebrow">DOI</dt>
                  <dd className="mt-1">
                    <a href={`https://doi.org/${p.doi}`} target="_blank" rel="noopener noreferrer" className="break-all text-petrolio underline underline-offset-2">
                      {p.doi}
                    </a>
                  </dd>
                </div>
              )}
              {p.pubmedId && (
                <div>
                  <dt className="eyebrow">PubMed</dt>
                  <dd className="mt-1">
                    <a href={`https://pubmed.ncbi.nlm.nih.gov/${p.pubmedId}/`} target="_blank" rel="noopener noreferrer" className="text-petrolio underline underline-offset-2">
                      {p.pubmedId}
                    </a>
                  </dd>
                </div>
              )}
            </dl>
            <div className="mt-6 flex flex-wrap gap-2">
              {pdf ? (
                <>
                  <a href={pdf} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
                    <Segno nome="doc" size={16} />
                    {m.cta.pdf}
                  </a>
                  {articolo && (
                    <a href={articolo} target="_blank" rel="noopener noreferrer" className="btn btn-petrolio">
                      {m.cta.fonte}
                      <Segno nome="esterno" size={16} />
                    </a>
                  )}
                </>
              ) : (
                articolo && (
                  <a href={articolo} target="_blank" rel="noopener noreferrer" className="btn btn-petrolio">
                    {m.cta.articolo}
                    <Segno nome="esterno" size={16} />
                  </a>
                )
              )}
            </div>
        </Reveal>

        {/* Sommario sticky a sinistra (come la pagina patologia); a destra In breve, poi la Lettura o l'abstract. */}
        <div className="grid gap-12 py-12 md:py-16 lg:grid-cols-[15rem_minmax(0,1fr)] lg:gap-20 xl:grid-cols-[17rem_minmax(0,1fr)]">
          <div className="space-y-10 lg:sticky lg:top-[calc(var(--header-h)+2.5rem)] lg:self-start">
            {/* I paper lunghi hanno venti sezioni: il sommario scorre dentro la sua colonna, senza spingere giù il resto. */}
            <div className="lg:max-h-[calc(100vh-var(--header-h)-9rem)] lg:overflow-y-auto lg:pr-3 scorri-sottile">
              <Sommario voci={sommario} eyebrow={m.approfondimenti.inQuestaPagina} />
            </div>
            {(p.tag ?? []).length > 0 && (
              <div className="flex flex-wrap gap-1.5">
                {p.tag!.map((t) => (
                  <Link key={t} href={href(l, { kind: "tag", tag: t })} className="tag hover:bg-petrolio-3 hover:text-petrolio">
                    {t}
                  </Link>
                ))}
              </div>
            )}
            {correlate.length > 0 && (
              <div>
                <p className="eyebrow mb-3">{m.approfondimenti.correlate}</p>
                <ul className="space-y-2">
                  {correlate.map((c) => (
                    <li key={c.slug}>
                      <Link href={href(l, { kind: "cosaCuro", slug: slugPatologia(c, l) })} className="text-[1.02rem] hover:text-petrolio">
                        {pick(c.titolo, l)}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          <div className="min-w-0">
            {pick(p.riassunto, l) && (
              <Reveal as="section" id="in-breve" className="ancora max-w-[42rem]">
                <h2 className="text-[1.4rem]">{m.approfondimenti.riassunto}</h2>
                <p className="mt-3 whitespace-pre-line text-[1.02rem] leading-relaxed">{pick(p.riassunto, l)}</p>
              </Reveal>
            )}

            {lettura ? (
              <section id="lettura" className={`ancora mt-16 ${serifLettura.variable}`}>
                <div className="max-w-[38rem] border-t border-inchiostro pt-5">
                  <p className="eyebrow">{m.approfondimenti.letturaEyebrow}</p>
                  <p className="mt-2 text-sm text-grafite">{m.approfondimenti.letturaNota}</p>
                </div>
                <div className="lettura mt-10" lang="en">
                  {lettura}
                </div>
                {p.licenza && (
                  <p className="lettura-colophon mt-10 max-w-[38rem] border-t border-linea pt-4">
                    {p.licenza}
                    {p.doi ? (
                      <>
                        {" · "}
                        <a href={`https://doi.org/${p.doi}`} target="_blank" rel="noopener noreferrer" className="text-petrolio underline underline-offset-2">
                          doi.org/{p.doi}
                        </a>
                      </>
                    ) : null}
                  </p>
                )}
              </section>
            ) : (
              p.abstract && (
                <Reveal as="section" id="abstract" className="ancora mt-16 max-w-[42rem]">
                  <h2 className="text-[1.4rem]">{m.approfondimenti.abstract}</h2>
                  <p className="abstract mt-3 whitespace-pre-line" lang="en">
                    {p.abstract}
                  </p>
                  {p.licenza && <p className="mt-5 text-sm text-grafite">{p.licenza}</p>}
                  <p className="mt-1 text-sm text-grafite">{m.approfondimenti.soloAbstractNota}</p>
                </Reveal>
              )
            )}
            <Disclaimer testo={m.approfondimenti.disclaimer} />
          </div>
        </div>
      </article>

      {altre.length > 0 && (
        <section className="contenitore pb-6">
          <p className="eyebrow mb-4">{m.approfondimenti.pubblicazioni}</p>
          <div className="grid items-stretch gap-10 md:grid-cols-3">
            {altre.map((x, i) => (
              <Reveal key={x.slug} delay={i * 70} className="h-full min-w-0">
                <SchedaPaper p={x} locale={l} />
              </Reveal>
            ))}
          </div>
        </section>
      )}
      {correlate.length > 0 && altre.length === 0 && (
        <section className="contenitore pb-6">
          <div className="grid items-stretch gap-10 md:grid-cols-3">
            {correlate.slice(0, 3).map((c, i) => (
              <Reveal key={c.slug} delay={i * 70} className="h-full min-w-0">
                <SchedaPatologia p={c} locale={l} index={i} />
              </Reveal>
            ))}
          </div>
        </section>
      )}

      <FasciaContatto locale={l} />
    </>
  );
}
