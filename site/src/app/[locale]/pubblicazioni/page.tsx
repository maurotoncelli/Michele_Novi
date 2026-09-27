import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getPubblicazioni, getSettings } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Intestazione } from "@/components/blocks/Pagina";
import { ArchivioPubblicazioni } from "@/components/blocks/ListaPubblicazioni";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/pubblicazioni">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "pubblicazioni" }, title: m.nav.pubblicazioni, description: m.approfondimenti.pubblicazioniLead });
}

export default async function PubblicazioniPage({ params }: PageProps<"/[locale]/pubblicazioni">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, pubblicazioni] = await Promise.all([getSettings(), getPubblicazioni()]);
  const m = getMessages(l);
  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.nav.pubblicazioni, path: href(l, { kind: "pubblicazioni" }) },
        ])}
      />
      <Intestazione
        eyebrow={m.approfondimenti.archivioScientifico}
        titolo={m.nav.pubblicazioni}
        lead={m.approfondimenti.pubblicazioniLead}
        compatta
        percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.nav.pubblicazioni }]}
      />
      <section className="border-b border-linea bg-osso">
        <div className="contenitore py-12 md:py-16">
          <ArchivioPubblicazioni pubblicazioni={pubblicazioni} totale={pubblicazioni.length} locale={l} />
        </div>
      </section>
      <FasciaContatto locale={l} />
    </>
  );
}
