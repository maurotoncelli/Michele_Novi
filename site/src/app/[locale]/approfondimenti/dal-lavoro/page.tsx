import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getApprofondimenti, getSettings } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Intestazione } from "@/components/blocks/Pagina";
import { TabApprofondimenti } from "@/components/blocks/TabApprofondimenti";
import { ListaApprofondimenti } from "@/components/blocks/ListaApprofondimenti";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/approfondimenti/dal-lavoro">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "approfondimentiDalLavoro" }, title: `${m.approfondimenti.dalLavoro} — ${m.approfondimenti.titolo}`, description: m.approfondimenti.dalLavoroLead });
}

export default async function DalLavoroPage({ params }: PageProps<"/[locale]/approfondimenti/dal-lavoro">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, voci] = await Promise.all([getSettings(), getApprofondimenti()]);
  const m = getMessages(l);
  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.approfondimenti.titolo, path: href(l, { kind: "approfondimenti" }) },
          { name: m.approfondimenti.dalLavoro, path: href(l, { kind: "approfondimentiDalLavoro" }) },
        ])}
      />
      <Intestazione
        eyebrow={m.approfondimenti.titolo}
        titolo={m.approfondimenti.dalLavoro}
        lead={m.approfondimenti.dalLavoroLead}
        compatta
        percorso={[
          { label: m.meta.siteName, href: href(l, { kind: "home" }) },
          { label: m.approfondimenti.titolo, href: href(l, { kind: "approfondimenti" }) },
          { label: m.approfondimenti.dalLavoro },
        ]}
      />
      <TabApprofondimenti locale={l} attiva="dalLavoro" feedHref={`${href(l, { kind: "approfondimenti" })}/feed.xml`} />
      <ListaApprofondimenti voci={voci.filter((v) => v.tipo === "nota")} locale={l} />
      <FasciaContatto locale={l} />
    </>
  );
}
