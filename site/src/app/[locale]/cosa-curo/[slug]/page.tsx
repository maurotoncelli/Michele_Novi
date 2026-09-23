import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getDisegni, getPatologia, getPatologie, getPubblicazioni, getSedi, getSettings, slugPatologia, srcDisegno } from "@/lib/content";
import { Disegno } from "@/components/ui/Disegno";
import { renderBody, headings } from "@/lib/markdoc";
import { breadcrumbJsonLd, buildMetadata, faqItems, faqJsonLd, medicalWebPageJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { AvvisoLingua, Briciole, Disclaimer } from "@/components/blocks/Pagina";
import { Faq } from "@/components/blocks/Faq";
import { Sommario } from "@/components/blocks/Sommario";
import { srcMedia } from "@/lib/media";
import { ModuloSede, SchedaPatologia } from "@/components/blocks/Schede";
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
    image: p.seo?.ogImage ?? srcMedia(p.immagine?.src, "patologie") ?? undefined,
    noindex: p.seo?.noindex,
  });
}

export default async function PatologiaPage({ params }: PageProps<"/[locale]/cosa-curo/[slug]">) {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const p = await getPatologia(slug, l);
  if (!p) notFound();
  const [s, tutte, sedi, paper, catalogo] = await Promise.all([getSettings(), getPatologie(), getSedi(), getPubblicazioni(), getDisegni()]);
  const foto = srcMedia(p.immagine?.src, "patologie");
  const disegno = foto ? null : srcDisegno(catalogo, p.segno, l);
  const mediaAlt = pick(p.immagine?.alt, l) || pick(p.titolo, l);
  const m = getMessages(l);

  const { element, fallbackToIt } = await renderBody(p.corpo, p.corpoEn, l);
  const indice = await headings(l === "en" && !fallbackToIt ? p.corpoEn : p.corpo);
  const faq = faqItems(p.faq, l);
  const correlate = (p.correlate ?? []).map((sl) => tutte.find((x) => x.slug === sl)).filter(Boolean) as typeof tutte;
  const doveSiTratta = (p.sedi ?? []).map((sl) => sedi.find((x) => x.slug === sl)).filter(Boolean) as typeof sedi;
  const citati = (p.pubblicazioni ?? []).map((sl) => paper.find((x) => x.slug === sl)).filter(Boolean) as typeof paper;
  const pubSlug = slugPatologia(p, l);
  const sommario = [
    ...indice.map((h) => ({ id: h.id, label: h.text })),
    ...(doveSiTratta.length ? [{ id: "dove", label: m.cosaCuro.doveSiTratta }] : []),
    ...(citati.length ? [{ id: "pubblicazioni", label: m.cosaCuro.pubblicazioniCorrelate }] : []),
    ...(faq.length ? [{ id: "faq", label: m.cosaCuro.faq }] : []),
  ];

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
        <Reveal immediate className="osso relative overflow-hidden">
          <div className="relative grid gap-6 md:grid-cols-[1.4fr_1fr] md:items-center">
            <div>
              <h1 className="display-l">{pick(p.titolo, l)}</h1>
              <p className="mt-4 max-w-2xl text-[1.1rem] leading-relaxed text-grafite">{pick(p.lead, l)}</p>
            </div>
            {(foto || disegno) && (
              <div className="relative aspect-[5/4] overflow-hidden bg-osso-2">
                {foto ? (
                  <Image src={foto} alt={mediaAlt} fill quality={92} sizes="(min-width: 768px) 36vw, 100vw" className="object-cover object-[50%_22%]" />
                ) : (
                  disegno && <Disegno src={disegno.src} alt={disegno.alt} />
                )}
              </div>
            )}
          </div>
        </Reveal>
      </header>

      {/* Sommario sticky a sinistra che segue la lettura; a destra il corpo, poi Dove, Ne ho scritto, FAQ: tutto nel flusso, tutto con ancora. */}
      <div className="contenitore grid gap-12 py-12 md:py-16 lg:grid-cols-[15rem_minmax(0,1fr)] lg:gap-20 xl:grid-cols-[17rem_minmax(0,1fr)]">
        <div className="lg:sticky lg:top-[calc(var(--header-h)+2.5rem)] lg:self-start">
          <Sommario voci={sommario} eyebrow={m.cosaCuro.inQuestaPagina} />
        </div>

        <article className="min-w-0">
          <AvvisoLingua show={fallbackToIt} locale={l} />
          <div className={`testo max-w-[44rem]${p.area === "metodo" || p.area === "spalla" || p.area === "arto-superiore" || p.area === "sport" ? " testo-metodo" : ""}`}>{element}</div>

          {doveSiTratta.length > 0 && (
            <section id="dove" className="ancora mt-20 max-w-[44rem]">
              <p className="eyebrow">{m.nav.dove}</p>
              <h2 className="mt-3 text-[1.75rem] leading-tight">{m.cosaCuro.doveSiTratta}</h2>
              <ul className="mt-6 divide-y divide-linea border-y border-linea">
                {doveSiTratta.map((sd) => (
                  <li key={sd.slug} className="min-w-0">
                    <ModuloSede s={sd} locale={l} compatto />
                  </li>
                ))}
              </ul>
            </section>
          )}

          {citati.length > 0 && (
            <section id="pubblicazioni" className="ancora mt-20 max-w-[44rem]">
              <p className="eyebrow">{m.nav.pubblicazioni}</p>
              <h2 className="mt-3 text-[1.75rem] leading-tight">{m.cosaCuro.pubblicazioniCorrelate}</h2>
              <ul className="mt-6 divide-y divide-linea border-y border-linea">
                {citati.map((x) => (
                  <li key={x.slug}>
                    <Link href={href(l, { kind: "paper", slug: x.slug })} className="group grid grid-cols-[3.5rem_minmax(0,1fr)] gap-4 py-4">
                      <span className="pt-0.5 text-sm text-grafite">{x.anno}</span>
                      <span className="min-w-0">
                        <span className="block text-[1.05rem] leading-snug group-hover:text-petrolio">{pick(x.titoloBreve, l) || x.titolo}</span>
                        <span className="mt-1 block text-sm text-grafite">{x.rivista}</span>
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </section>
          )}

          {faq.length > 0 && (
            <section id="faq" className="ancora mt-20 max-w-[44rem]">
              <Faq titolo={m.cosaCuro.faq} items={faq} />
            </section>
          )}
          <Disclaimer testo={m.cosaCuro.disclaimer} />
        </article>
      </div>

      {correlate.length > 0 && (
        <section className="contenitore pb-6">
          <p className="eyebrow mb-4">{m.cosaCuro.correlate}</p>
          <div className="grid gap-8 md:grid-cols-3">
            {correlate.map((c, i) => (
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
