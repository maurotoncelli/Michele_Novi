import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getSedi, getSettings } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Intestazione, Sezione } from "@/components/blocks/Pagina";
import { SchedaSede } from "@/components/blocks/Schede";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/dove">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "dove" }, title: m.nav.dove, description: m.meta.doveDescription });
}

export default async function DovePage({ params }: PageProps<"/[locale]/dove">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, sedi] = await Promise.all([getSettings(), getSedi()]);
  const m = getMessages(l);

  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.nav.dove, path: href(l, { kind: "dove" }) },
        ])}
      />
      <Intestazione
        eyebrow={m.nav.dove}
        titolo={m.dove.titolo}
        lead={m.dove.lead}
        stretta
        percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.nav.dove }]}
      />

      <Sezione stretta>
        <ul className="grid gap-x-12 gap-y-8 pt-4 md:grid-cols-2 md:gap-y-10">
          {sedi.map((x, i) => (
            <Reveal key={x.slug} as="li" delay={i * 70} className="min-w-0">
              <SchedaSede s={x} locale={l} />
            </Reveal>
          ))}
        </ul>
        <p className="mt-10 text-[0.8rem] text-nebbia">
          <a href="/images/sedi/ATTRIBUZIONI.txt" className="underline decoration-linea underline-offset-4 hover:text-petrolio">
            {m.dove.fotoCitta}
          </a>
        </p>
      </Sezione>

      <FasciaContatto locale={l} />
    </>
  );
}
