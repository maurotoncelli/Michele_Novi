import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getProfilo, getPubblicazioni, getSedi, getSettings } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata, physicianJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Cucitura } from "@/components/ui/Cucitura";
import { Briciole, Sezione } from "@/components/blocks/Pagina";
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

      {/* Apertura: lastra con ritratto in finestra */}
      <section className="contenitore pt-6 md:pt-10">
        <Reveal className="osso osso-lg cucitura relative overflow-hidden">
          <div className="pointer-events-none absolute -right-20 -top-20 h-72 w-72 rounded-full bg-menta blur-3xl" aria-hidden="true" />
          <div className="relative grid gap-8 p-7 md:grid-cols-[1fr_1.4fr] md:items-center md:p-12">
            <div className="mx-auto w-full max-w-[20rem] md:max-w-none">
              <div className="incavo relative aspect-[4/5] overflow-hidden" style={{ borderRadius: "48% 52% 46% 54% / 54% 46% 54% 46%" }}>
                {p.ritratto?.src ? (
                  <Image src={p.ritratto.src} alt={pick(p.ritratto.alt, l) || m.a11y.ritrattoDi} fill priority sizes="(min-width: 768px) 30vw, 80vw" className="object-cover" />
                ) : (
                  <div className="absolute inset-0 grid place-items-center text-petrolio/50">
                    <Segno nome="spalla" size={80} strokeWidth={1} />
                  </div>
                )}
              </div>
            </div>
            <div>
              <p className="eyebrow mb-3">{m.chiSono.titolo}</p>
              <h1 className="text-[2.4rem] leading-[1.05] md:text-[3.2rem]">{p.nome}</h1>
              <p className="serif mt-3 text-[1.25rem] text-petrolio">{pick(p.titolo, l)}</p>
              <p className="mt-5 max-w-2xl text-[1.08rem] leading-relaxed text-grafite">{pick(p.apertura, l)}</p>
              {p.lingue && p.lingue.length > 0 && (
                <p className="mt-4 flex flex-wrap items-center gap-1.5 text-sm text-grafite">
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
        <Sezione titolo={m.chiSono.inEvidenza}>
          <ol className="grid gap-4 md:grid-cols-2">
            {p.inEvidenza.map((v, i) => (
              <Reveal key={i} as="li" delay={i * 80} className={`osso p-6 ${i === 0 ? "vetro vetro-menta md:col-span-2" : ""}`}>
                <p className="eyebrow text-rame">{v.anno}</p>
                <h3 className={`mt-2 leading-tight ${i === 0 ? "text-[1.9rem]" : "text-[1.4rem]"}`}>{pick(v.titolo, l)}</h3>
                <p className="mt-2 text-grafite">{pick(v.testo, l)}</p>
              </Reveal>
            ))}
          </ol>
        </Sezione>
      )}

      {/* Percorso: espandibile */}
      {p.timeline && p.timeline.length > 0 && (
        <Sezione>
          <Reveal>
            <details className="osso group open:pb-2">
              <summary className="flex cursor-pointer list-none items-center justify-between gap-4 px-6 py-5 [&::-webkit-details-marker]:hidden">
                <h2 className="text-[1.6rem]">{m.chiSono.percorso}</h2>
                <span className="incavo grid h-10 w-10 shrink-0 place-items-center text-petrolio transition group-open:rotate-45">
                  <Segno nome="piu" size={18} />
                </span>
              </summary>
              <ol className="relative mx-6 mb-4 border-l border-linea pl-6">
                {p.timeline.map((t, i) => (
                  <li key={i} className="relative py-3">
                    <span className="absolute -left-[1.85rem] top-5 h-3 w-3 rounded-full border-2 border-osso bg-petrolio-2" aria-hidden="true" />
                    <p className="text-xs font-semibold tracking-wide text-grafite">{t.periodo}</p>
                    <p className="mt-0.5 font-medium">{pick(t.titolo, l)}</p>
                    {t.luogo && <p className="text-sm text-grafite">{t.luogo}</p>}
                  </li>
                ))}
              </ol>
            </details>
          </Reveal>
        </Sezione>
      )}

      {/* Pubblicazioni principali */}
      {principali.length > 0 && (
        <Sezione eyebrow={m.nav.quaderno} titolo={m.chiSono.pubblicazioni} azione={{ href: href(l, { kind: "quadernoPubblicazioni" }), label: m.chiSono.tuttePubblicazioni }}>
          <ol className="divide-y divide-linea overflow-hidden rounded-[1.75rem] border border-linea bg-osso">
            {principali.map((x) => (
              <li key={x.slug}>
                <Link href={href(l, { kind: "paper", slug: x.slug })} className="group flex items-baseline gap-4 px-6 py-4 hover:bg-osso-2/60">
                  <span className="w-12 shrink-0 text-sm text-grafite">{x.anno}</span>
                  <span className="flex-1">
                    <span className="serif block text-[1.1rem] leading-snug group-hover:text-petrolio">{pick(x.titoloBreve, l) || x.titolo}</span>
                    <span className="block text-sm text-grafite">{x.rivista}</span>
                  </span>
                  <Segno nome="freccia" size={18} className="hidden shrink-0 self-center text-nebbia group-hover:text-petrolio sm:block" />
                </Link>
              </li>
            ))}
          </ol>
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

      <Cucitura tinta="campo" />
      <FasciaContatto locale={l} />
    </>
  );
}
