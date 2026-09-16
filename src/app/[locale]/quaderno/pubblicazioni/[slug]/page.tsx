import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getPatologie, getPubblicazione, getPubblicazioni, getSettings, slugPatologia } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata, paperJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Briciole, Disclaimer } from "@/components/blocks/Pagina";
import { SchedaPatologia, SchedaPaper } from "@/components/blocks/Schede";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export const dynamicParams = false;
export async function generateStaticParams() {
  const all = await getPubblicazioni();
  return locales.flatMap((locale) => all.map((p) => ({ locale, slug: p.slug })));
}

export async function generateMetadata({ params }: PageProps<"/[locale]/quaderno/pubblicazioni/[slug]">): Promise<Metadata> {
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

export default async function PaperPage({ params }: PageProps<"/[locale]/quaderno/pubblicazioni/[slug]">) {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const p = await getPubblicazione(slug);
  if (!p) notFound();
  const [s, patologie, tutte] = await Promise.all([getSettings(), getPatologie(), getPubblicazioni()]);
  const m = getMessages(l);
  const correlate = (p.patologie ?? []).map((sl) => patologie.find((x) => x.slug === sl)).filter(Boolean) as typeof patologie;
  const altre = tutte.filter((x) => x.slug !== p.slug && (x.tag ?? []).some((t) => (p.tag ?? []).includes(t))).slice(0, 3);
  const titoloBreve = pick(p.titoloBreve, l);
  const fonte = p.doi ? `https://doi.org/${p.doi}` : p.url;

  return (
    <>
      <JsonLd
        data={[
          paperJsonLd(s, p, l),
          breadcrumbJsonLd(s, [
            { name: m.meta.siteName, path: href(l, { kind: "home" }) },
            { name: m.quaderno.titolo, path: href(l, { kind: "quaderno" }) },
            { name: m.quaderno.pubblicazioni, path: href(l, { kind: "quadernoPubblicazioni" }) },
            { name: titoloBreve || p.titolo, path: href(l, { kind: "paper", slug: p.slug }) },
          ]),
        ]}
      />
      <Briciole
        items={[
          { label: m.meta.siteName, href: href(l, { kind: "home" }) },
          { label: m.quaderno.titolo, href: href(l, { kind: "quaderno" }) },
          { label: m.quaderno.pubblicazioni, href: href(l, { kind: "quadernoPubblicazioni" }) },
          { label: titoloBreve || p.titolo },
        ]}
      />

      <article className="contenitore pt-8 md:pt-12">
        {/* Impaginato da paper: testata, titolo, autori, rivista, DOI */}
        <Reveal className="osso osso-lg cucitura relative overflow-hidden p-7 md:p-12">
          <div className="pointer-events-none absolute -right-24 -top-24 h-72 w-72 rounded-full bg-menta blur-3xl" aria-hidden="true" />
          <div className="relative max-w-3xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className="tag tag-petrolio">{m.quaderno.paper}</span>
              {p.principale && <span className="tag tag-rame">{m.quaderno.principale}</span>}
              <span className="text-sm text-grafite">{p.anno}</span>
            </div>
            {titoloBreve && <p className="eyebrow mt-6">{titoloBreve}</p>}
            <h1 className="mt-2 text-[1.9rem] leading-[1.15] md:text-[2.6rem]" lang="en">
              {p.titolo}
            </h1>
            <dl className="mt-6 grid gap-x-8 gap-y-3 text-[0.95rem] sm:grid-cols-2">
              {p.autori && (
                <div>
                  <dt className="eyebrow">{m.quaderno.autori}</dt>
                  <dd className="mt-1 text-grafite">{p.autori}</dd>
                </div>
              )}
              {p.rivista && (
                <div>
                  <dt className="eyebrow">{m.quaderno.rivista}</dt>
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
              {fonte && (
                <a href={fonte} target="_blank" rel="noopener noreferrer" className="btn btn-petrolio">
                  {m.cta.fonte}
                  <Segno nome="esterno" size={16} />
                </a>
              )}
              {p.pdf && (
                <a href={p.pdf} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
                  <Segno nome="doc" size={16} />
                  {m.cta.pdf}
                </a>
              )}
            </div>
          </div>
        </Reveal>

        <div className="grid gap-8 py-10 lg:grid-cols-[1fr_18rem] lg:gap-16">
          <div className="max-w-[42rem] space-y-10">
            {pick(p.riassunto, l) && (
              <Reveal className="osso vetro vetro-pesca p-6 md:p-8">
                <h2 className="text-[1.4rem]">{m.quaderno.riassunto}</h2>
                <p className="mt-3 whitespace-pre-line text-[1.02rem] leading-relaxed">{pick(p.riassunto, l)}</p>
              </Reveal>
            )}
            {p.abstract && (
              <Reveal>
                <h2 className="text-[1.4rem]">{m.quaderno.abstract}</h2>
                <p className="abstract mt-3 whitespace-pre-line" lang="en">
                  {p.abstract}
                </p>
              </Reveal>
            )}
            <Disclaimer testo={m.quaderno.disclaimer} />
          </div>
          <aside className="space-y-6 lg:sticky lg:top-24 lg:self-start">
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
              <div className="osso osso-sm p-5">
                <p className="eyebrow mb-3">{m.quaderno.correlate}</p>
                <ul className="space-y-2">
                  {correlate.map((c) => (
                    <li key={c.slug}>
                      <Link href={href(l, { kind: "cosaCuro", slug: slugPatologia(c, l) })} className="serif text-[1.05rem] hover:text-petrolio">
                        {pick(c.titolo, l)}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </aside>
        </div>
      </article>

      {altre.length > 0 && (
        <section className="contenitore pb-6">
          <p className="eyebrow mb-4">{m.quaderno.pubblicazioni}</p>
          <div className="grid gap-4 md:grid-cols-3">
            {altre.map((x, i) => (
              <Reveal key={x.slug} delay={i * 70}>
                <SchedaPaper p={x} locale={l} />
              </Reveal>
            ))}
          </div>
        </section>
      )}
      {correlate.length > 0 && altre.length === 0 && (
        <section className="contenitore pb-6">
          <div className="grid gap-4 md:grid-cols-3">
            {correlate.slice(0, 3).map((c, i) => (
              <Reveal key={c.slug} delay={i * 70}>
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
