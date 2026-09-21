import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getQuaderno, getSettings, getTags } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Intestazione } from "@/components/blocks/Pagina";
import { TabQuaderno } from "@/components/blocks/TabQuaderno";
import { ListaQuaderno } from "@/components/blocks/ListaQuaderno";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/quaderno">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "quaderno" }, title: m.quaderno.titolo, description: m.meta.quadernoDescription });
}

export default async function QuadernoPage({ params }: PageProps<"/[locale]/quaderno">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, voci, tags] = await Promise.all([getSettings(), getQuaderno(), getTags()]);
  const m = getMessages(l);
  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.quaderno.titolo, path: href(l, { kind: "quaderno" }) },
        ])}
      />
      <Intestazione
        eyebrow={m.nav.quaderno}
        titolo={m.quaderno.titolo}
        lead={m.quaderno.lead}
        compatta
        percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.quaderno.titolo }]}
      />
      <TabQuaderno locale={l} attiva="tutto" feedHref={`${href(l, { kind: "quaderno" })}/feed.xml`} />
      <ListaQuaderno voci={voci} locale={l} tags={tags} />
      <FasciaContatto locale={l} />
    </>
  );
}
