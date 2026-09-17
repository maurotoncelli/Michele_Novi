import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { formatDate, getMessages, pick } from "@/i18n";
import { getNota, getNote, getPatologie, getPubblicazioni, getSettings, slugNota } from "@/lib/content";
import { srcMedia } from "@/lib/media";
import { renderBody } from "@/lib/markdoc";
import { articleJsonLd, breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { AvvisoLingua, Briciole, Disclaimer } from "@/components/blocks/Pagina";
import { SchedaNota, SchedaPatologia } from "@/components/blocks/Schede";
import { VideoApprofondimento } from "@/components/blocks/VideoApprofondimento";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export const dynamicParams = false;
export async function generateStaticParams() {
  const all = await getNote();
  return locales.flatMap((locale) =>
    all.flatMap((n) => {
      const slugs = new Set([n.slug, slugNota(n, locale)]);
      return [...slugs].map((slug) => ({ locale, slug }));
    }),
  );
}

export async function generateMetadata({ params }: PageProps<"/[locale]/quaderno/[slug]">): Promise<Metadata> {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, n] = await Promise.all([getSettings(), getNota(slug, l)]);
  if (!n) return {};
  return buildMetadata(s, {
    locale: l,
    route: { kind: "nota", slug: n.slug },
    routeEn: { kind: "nota", slug: slugNota(n, "en") },
    title: pick(n.seo?.title, l) || pick(n.titolo, l),
    description: pick(n.seo?.description, l) || pick(n.lead, l),
    image: n.seo?.ogImage ?? srcMedia(n.copertina?.src, "quaderno") ?? undefined,
    noindex: n.seo?.noindex,
    type: "article",
    publishedTime: n.data,
    modifiedTime: n.aggiornato ?? n.data,
  });
}

export default async function NotaPage({ params }: PageProps<"/[locale]/quaderno/[slug]">) {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const n = await getNota(slug, l);
  if (!n) notFound();
  const [s, note, patologie, paper] = await Promise.all([getSettings(), getNote(), getPatologie(), getPubblicazioni()]);
  const m = getMessages(l);
  const { element, fallbackToIt } = await renderBody(n.corpo, n.corpoEn, l);
  const correlate = (n.patologie ?? []).map((sl) => patologie.find((x) => x.slug === sl)).filter(Boolean) as typeof patologie;
  const citati = (n.pubblicazioni ?? []).map((sl) => paper.find((x) => x.slug === sl)).filter(Boolean) as typeof paper;
  const altre = note.filter((x) => x.slug !== n.slug).slice(0, 3);
  const pubSlug = slugNota(n, l);
  const copertina = srcMedia(n.copertina?.src, "quaderno");

  return (
    <>
      <JsonLd
        data={[
          articleJsonLd(s, n, l, pubSlug),
          breadcrumbJsonLd(s, [
            { name: m.meta.siteName, path: href(l, { kind: "home" }) },
            { name: m.quaderno.titolo, path: href(l, { kind: "quaderno" }) },
            { name: pick(n.titolo, l), path: href(l, { kind: "nota", slug: pubSlug }) },
          ]),
        ]}
      />
      <Briciole items={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.quaderno.titolo, href: href(l, { kind: "quaderno" }) }, { label: pick(n.titolo, l) }]} />

      <article className="contenitore pt-8 md:pt-12">
        <Reveal className="mx-auto max-w-3xl text-center">
          <div className="flex flex-wrap items-center justify-center gap-2">
            <span className="tag tag-rame">{m.quaderno.nota}</span>
            <time dateTime={n.data ?? undefined} className="text-sm text-grafite">
              {formatDate(n.data, l)}
            </time>
            {n.aggiornato && (
              <span className="text-sm text-nebbia">
                · {m.quaderno.aggiornato} {formatDate(n.aggiornato, l)}
              </span>
            )}
          </div>
          <h1 className="mt-5 text-[2.3rem] leading-[1.08] md:text-[3.2rem]">{pick(n.titolo, l)}</h1>
          {pick(n.lead, l) && <p className="mt-5 text-[1.15rem] leading-relaxed text-grafite">{pick(n.lead, l)}</p>}
          <p className="mt-5 text-sm text-grafite">{s.nome}</p>
        </Reveal>

        {copertina && (
          <Reveal className="relative mx-auto mt-10 aspect-[16/9] max-w-4xl overflow-hidden bg-petrolio-3">
            <Image src={copertina} alt={pick(n.copertina?.alt, l) || pick(n.titolo, l)} fill priority sizes="(min-width: 1024px) 60rem, 100vw" className="object-cover" />
          </Reveal>
        )}

        <div className="mx-auto max-w-[42rem] py-12">
          <AvvisoLingua show={fallbackToIt} locale={l} />
          <div className="testo">{element}</div>
          <VideoApprofondimento file={n.video} youtube={n.youtube} titolo={pick(n.titolo, l)} />
          {citati.length > 0 && (
            <div className="osso osso-sm mt-12 p-5">
              <p className="eyebrow mb-3">{m.quaderno.paperCorrelati}</p>
              <ul className="space-y-3">
                {citati.map((x) => (
                  <li key={x.slug}>
                    <Link href={href(l, { kind: "paper", slug: x.slug })} className="hover:text-petrolio">
                      <span className="serif block leading-snug">{x.titolo}</span>
                      <span className="text-xs text-grafite">
                        {x.rivista}, {x.anno}
                        {x.doi ? ` · DOI ${x.doi}` : ""}
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          )}
          {(n.tag ?? []).length > 0 && (
            <div className="mt-8 flex flex-wrap gap-1.5">
              {n.tag!.map((t) => (
                <Link key={t} href={href(l, { kind: "tag", tag: t })} className="tag hover:bg-petrolio-3 hover:text-petrolio">
                  {t}
                </Link>
              ))}
            </div>
          )}
          <Disclaimer testo={m.quaderno.disclaimer} />
        </div>
      </article>

      {correlate.length > 0 && (
        <section className="contenitore pb-6">
          <p className="eyebrow mb-4">{m.quaderno.correlate}</p>
          <div className="grid gap-4 md:grid-cols-3">
            {correlate.map((c, i) => (
              <Reveal key={c.slug} delay={i * 70}>
                <SchedaPatologia p={c} locale={l} index={i} />
              </Reveal>
            ))}
          </div>
        </section>
      )}
      {altre.length > 0 && (
        <section className="contenitore pb-6">
          <p className="eyebrow mb-4">{m.quaderno.dalLavoro}</p>
          <div className="grid gap-4 md:grid-cols-3">
            {altre.map((x, i) => (
              <Reveal key={x.slug} delay={i * 70}>
                <SchedaNota n={x} locale={l} />
              </Reveal>
            ))}
          </div>
        </section>
      )}
      <FasciaContatto locale={l} />
    </>
  );
}
