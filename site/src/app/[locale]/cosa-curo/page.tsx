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
import { SchedaPatologia } from "@/components/blocks/Schede";
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
  const principali = patologie.filter((p) => !p.secondaria);
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

      <Sezione>
        <div className="grid items-stretch gap-x-12 gap-y-10 md:grid-cols-2 lg:gap-x-16 lg:gap-y-12">
          {principali.map((p, i) => (
            <Reveal key={p.slug} delay={i * 70} className="h-full min-w-0">
              <SchedaPatologia p={p} locale={l} index={i} riga />
            </Reveal>
          ))}
        </div>
        {secondarie.length > 0 && (
          <Reveal className="mt-12 border-t border-linea pt-6">
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
      </Sezione>

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
