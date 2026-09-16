import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getQuaderno, getSettings } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Briciole, Intestazione } from "@/components/blocks/Pagina";
import { TabQuaderno } from "@/components/blocks/TabQuaderno";
import { ListaQuaderno } from "@/components/blocks/ListaQuaderno";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/quaderno/dal-lavoro">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "quadernoDalLavoro" }, title: `${m.quaderno.dalLavoro} — ${m.quaderno.titolo}`, description: m.quaderno.dalLavoroLead });
}

export default async function DalLavoroPage({ params }: PageProps<"/[locale]/quaderno/dal-lavoro">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, voci] = await Promise.all([getSettings(), getQuaderno()]);
  const m = getMessages(l);
  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.quaderno.titolo, path: href(l, { kind: "quaderno" }) },
          { name: m.quaderno.dalLavoro, path: href(l, { kind: "quadernoDalLavoro" }) },
        ])}
      />
      <Briciole items={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.quaderno.titolo, href: href(l, { kind: "quaderno" }) }, { label: m.quaderno.dalLavoro }]} />
      <Intestazione eyebrow={m.quaderno.titolo} titolo={m.quaderno.dalLavoro} lead={m.quaderno.dalLavoroLead} compatta />
      <TabQuaderno locale={l} attiva="dalLavoro" feedHref={`${href(l, { kind: "quaderno" })}/feed.xml`} />
      <ListaQuaderno voci={voci.filter((v) => v.tipo === "nota")} locale={l} />
      <FasciaContatto locale={l} />
    </>
  );
}
