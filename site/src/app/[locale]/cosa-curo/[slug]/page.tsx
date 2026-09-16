import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import { notFound } from "next/navigation";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getPatologia, getPatologie, getPubblicazioni, getSedi, getSettings, slugPatologia } from "@/lib/content";
import { renderBody, headings } from "@/lib/markdoc";
import { breadcrumbJsonLd, buildMetadata, faqItems, faqJsonLd, medicalWebPageJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { isSegno, Segno } from "@/components/ui/Segno";
import { AvvisoLingua, Briciole, Disclaimer } from "@/components/blocks/Pagina";
import { Faq } from "@/components/blocks/Faq";
import { SchedaPatologia } from "@/components/blocks/Schede";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export const dynamicParams = false;
export async function generateStaticParams() {
  const all = await getPatologie();
  // In EN si generano sia lo slug tradotto (canonical) sia quello IT (fallback dal cambio lingua)
  return locales.flatMap((locale) =>
    all.flatMap((p) => {
      const slugs = new Set([p.slug, slugPatologia(p, locale)]);
      return [...slugs].map((slug) => ({ locale, slug }));
    }),
  );
}

export async function generateMetadata({ params }: PageProps<"/[locale]/cosa-curo/[slug]">): Promise<Metadata> {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, p] = await Promise.all([getSettings(), getPatologia(slug, l)]);
  if (!p) return {};
  return buildMetadata(s, {
    locale: l,
    route: { kind: "cosaCuro", slug: p.slug },
    routeEn: { kind: "cosaCuro", slug: slugPatologia(p, "en") },
    title: pick(p.seo?.title, l) || pick(p.titolo, l),
    description: pick(p.seo?.description, l) || pick(p.lead, l),
    image: p.seo?.ogImage ?? p.immagine?.src,
    noindex: p.seo?.noindex,
  });
}

export default async function PatologiaPage({ params }: PageProps<"/[locale]/cosa-curo/[slug]">) {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const p = await getPatologia(slug, l);
  if (!p) notFound();
  const [s, tutte, sedi, paper] = await Promise.all([getSettings(), getPatologie(), getSedi(), getPubblicazioni()]);
  const m = getMessages(l);

  const { element, fallbackToIt } = await renderBody(p.corpo, p.corpoEn, l);
  const indice = await headings(l === "en" && !fallbackToIt ? p.corpoEn : p.corpo);
  const faq = faqItems(p.faq, l);
  const correlate = (p.correlate ?? []).map((sl) => tutte.find((x) => x.slug === sl)).filter(Boolean) as typeof tutte;
  const doveSiTratta = (p.sedi ?? []).map((sl) => sedi.find((x) => x.slug === sl)).filter(Boolean) as typeof sedi;
  const citati = (p.pubblicazioni ?? []).map((sl) => paper.find((x) => x.slug === sl)).filter(Boolean) as typeof paper;
  const pubSlug = slugPatologia(p, l);

  return (
    <>
      <JsonLd
        data={[
          medicalWebPageJsonLd(s, p, l, pubSlug),
          faqJsonLd(faq),
          breadcrumbJsonLd(s, [
            { name: m.meta.siteName, path: href(l, { kind: "home" }) },
            { name: m.cosaCuro.titolo, path: href(l, { kind: "cosaCuro" }) },
            { name: pick(p.titolo, l), path: href(l, { kind: "cosaCuro", slug: pubSlug }) },
          ]),
        ]}
      />
      <Briciole items={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.cosaCuro.titolo, href: href(l, { kind: "cosaCuro" }) }, { label: pick(p.titolo, l) }]} />

      <header className="contenitore pt-8 md:pt-12">
        <Reveal className="osso osso-lg cucitura relative overflow-hidden">
          <div className="pointer-events-none absolute -left-20 -top-20 h-64 w-64 rounded-full bg-menta blur-3xl" aria-hidden="true" />
          <div className="relative grid gap-6 p-7 md:grid-cols-[1.4fr_1fr] md:items-center md:p-12">
            <div>
              <span className="incavo mb-6 grid h-14 w-14 place-items-center text-petrolio">
                <Segno nome={isSegno(p.segno) ? p.segno : "spalla"} size={30} />
              </span>
              <h1 className="text-[2.4rem] leading-[1.05] md:text-[3.2rem]">{pick(p.titolo, l)}</h1>
              <p className="mt-4 max-w-2xl text-[1.1rem] leading-relaxed text-grafite">{pick(p.lead, l)}</p>
            </div>
            {p.immagine?.src && (
              <div className="incavo relative aspect-[5/4] overflow-hidden" style={{ borderRadius: "52% 48% 50% 50% / 46% 54% 46% 54%" }}>
                <Image src={p.immagine.src} alt={pick(p.immagine.alt, l)} fill sizes="(min-width: 768px) 35vw, 90vw" className="object-cover" />
              </div>
            )}
          </div>
        </Reveal>
      </header>

      <div className="contenitore grid gap-10 py-12 lg:grid-cols-[1fr_18rem] lg:gap-16">
        <article>
          <AvvisoLingua show={fallbackToIt} locale={l} />
          <div className="testo max-w-[42rem]">{element}</div>
          {faq.length > 0 && (
            <div className="mt-14 max-w-[42rem]">
              <Faq titolo={m.cosaCuro.faq} items={faq} />
            </div>
          )}
          <Disclaimer testo={m.cosaCuro.disclaimer} />
        </article>

        <aside className="space-y-6 lg:sticky lg:top-24 lg:self-start">
          {indice.length > 1 && (
            <nav aria-label="Indice" className="osso osso-sm p-5">
              <ul className="space-y-2 text-sm">
                {indice.map((h) => (
                  <li key={h.id}>
                    <a href={`#${h.id}`} className="text-grafite hover:text-petrolio">
                      {h.text}
                    </a>
                  </li>
                ))}
              </ul>
            </nav>
          )}
          {doveSiTratta.length > 0 && (
            <div className="osso osso-sm p-5">
              <p className="eyebrow mb-3">{m.cosaCuro.doveSiTratta}</p>
              <ul className="space-y-2 text-[0.95rem]">
                {doveSiTratta.map((sd) => (
                  <li key={sd.slug}>
                    <Link href={href(l, { kind: "dove", slug: sd.slug })} className="group flex items-start gap-2 hover:text-petrolio">
                      <Segno nome="pin" size={16} className="mt-1 shrink-0 text-nebbia group-hover:text-petrolio" />
                      <span>
                        <span className="font-medium">{sd.citta}</span>
                        <span className="block text-sm text-grafite">{sd.nome}</span>
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          )}
          {citati.length > 0 && (
            <div className="osso osso-sm p-5">
              <p className="eyebrow mb-3">{m.cosaCuro.pubblicazioniCorrelate}</p>
              <ul className="space-y-3 text-[0.95rem]">
                {citati.map((x) => (
                  <li key={x.slug}>
                    <Link href={href(l, { kind: "paper", slug: x.slug })} className="hover:text-petrolio">
                      <span className="serif block leading-snug">{pick(x.titoloBreve, l) || x.titolo}</span>
                      <span className="text-xs text-grafite">
                        {x.rivista}, {x.anno}
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </aside>
      </div>

      {correlate.length > 0 && (
        <section className="contenitore pb-6">
          <p className="eyebrow mb-4">{m.cosaCuro.correlate}</p>
          <div className="grid gap-4 md:grid-cols-3">
            {correlate.map((c, i) => (
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
