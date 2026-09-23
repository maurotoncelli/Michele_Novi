import type { Metadata } from "next";
import Link from "next/link";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getPatologie, getSettings, slugPatologia } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { isSegno, Segno } from "@/components/ui/Segno";
import { Disclaimer, Intestazione, Sezione } from "@/components/blocks/Pagina";
import { SchedaMetodo, SchedaPatologia } from "@/components/blocks/Schede";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/cosa-curo">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "cosaCuro" }, title: m.cosaCuro.titolo, description: m.meta.cosaCuroDescription });
}

export default async function CosaCuroPage({ params }: PageProps<"/[locale]/cosa-curo">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, patologie] = await Promise.all([getSettings(), getPatologie()]);
  const m = getMessages(l);
  const metodo = patologie.find((p) => p.area === "metodo");
  const spalla = patologie.find((p) => p.area === "spalla");
  const resto = patologie.filter((p) => !p.secondaria && p !== metodo && p !== spalla);
  const secondarie = patologie.filter((p) => p.secondaria);

  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.cosaCuro.titolo, path: href(l, { kind: "cosaCuro" }) },
        ])}
      />
      <Intestazione
        eyebrow={m.nav.cosaCuro}
        titolo={m.cosaCuro.titolo}
        lead={m.cosaCuro.lead}
        compatta
        percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.cosaCuro.titolo }]}
      />

      <Sezione compatta>
        <h2 className="display-m max-w-3xl">{m.home.cosaCuroTitolo}</h2>
        {spalla && (
          <Reveal className="mt-8 md:mt-10">
            <SchedaPatologia p={spalla} locale={l} ampia />
          </Reveal>
        )}
        {resto.length > 0 && (
          <div className="mt-10 border-t border-linea pt-8 md:mt-12 md:pt-10">
            <Reveal>
              <h2 className="max-w-3xl text-[1.65rem] leading-tight md:text-[1.85rem]">{m.home.cosaCuroRestoTitolo}</h2>
              <p className="mt-2 max-w-2xl text-[1.02rem] leading-relaxed text-grafite">{m.home.cosaCuroRestoLead}</p>
            </Reveal>
            <ul className="mt-6 grid items-start gap-x-10 gap-y-8 sm:grid-cols-2">
              {resto.map((p, i) => (
                <Reveal key={p.slug} as="li" delay={i * 80} className="min-w-0">
                  <SchedaPatologia p={p} locale={l} riga />
                </Reveal>
              ))}
            </ul>
            {secondarie.length > 0 && (
              <Reveal className="mt-8">
                <p className="eyebrow mb-3">{m.cosaCuro.secondarie}</p>
                <ul className="flex flex-wrap gap-2">
                  {secondarie.map((p) => (
                    <li key={p.slug}>
                      <Link href={href(l, { kind: "cosaCuro", slug: slugPatologia(p, l) })} className="inline-flex items-center gap-2 py-2 text-[0.95rem] hover:text-petrolio">
                        <Segno nome={isSegno(p.segno) ? p.segno : "anca"} size={18} className="text-petrolio" />
                        {pick(p.titolo, l)}
                      </Link>
                    </li>
                  ))}
                </ul>
              </Reveal>
            )}
          </div>
        )}
      </Sezione>

      {metodo && (
        <section className="border-t border-linea">
          <Reveal className="contenitore py-16 md:py-24">
            <SchedaMetodo p={metodo} locale={l} />
          </Reveal>
        </section>
      )}

      <Sezione tinta="osso" misura="affermazione">
        <Reveal as="p" maschera className="citazione-l max-w-4xl">
          {m.cosaCuro.chiusura}
        </Reveal>
        <Disclaimer testo={m.cosaCuro.disclaimer} />
      </Sezione>

      <FasciaContatto locale={l} />
    </>
  );
}
