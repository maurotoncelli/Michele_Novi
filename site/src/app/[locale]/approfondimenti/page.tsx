import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getApprofondimenti, getSettings, getTags } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Intestazione } from "@/components/blocks/Pagina";
import { TabApprofondimenti } from "@/components/blocks/TabApprofondimenti";
import { ListaApprofondimenti } from "@/components/blocks/ListaApprofondimenti";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/approfondimenti">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "approfondimenti" }, title: m.approfondimenti.titolo, description: m.meta.approfondimentiDescription });
}

export default async function ApprofondimentiPage({ params }: PageProps<"/[locale]/approfondimenti">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, voci, tags] = await Promise.all([getSettings(), getApprofondimenti(), getTags()]);
  const m = getMessages(l);
  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.approfondimenti.titolo, path: href(l, { kind: "approfondimenti" }) },
        ])}
      />
      <Intestazione
        eyebrow={m.nav.approfondimenti}
        titolo={m.approfondimenti.titolo}
        lead={m.approfondimenti.lead}
        compatta
        percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.approfondimenti.titolo }]}
      />
      <TabApprofondimenti locale={l} attiva="tutto" feedHref={`${href(l, { kind: "approfondimenti" })}/feed.xml`} />
      <ListaApprofondimenti voci={voci} locale={l} tags={tags} />
      <FasciaContatto locale={l} />
    </>
  );
}
