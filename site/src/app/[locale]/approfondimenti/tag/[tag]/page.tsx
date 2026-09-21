import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getApprofondimenti, getSettings, getTags } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Intestazione } from "@/components/blocks/Pagina";
import { TabApprofondimenti } from "@/components/blocks/TabApprofondimenti";
import { ListaApprofondimenti } from "@/components/blocks/ListaApprofondimenti";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export const dynamicParams = false;
export async function generateStaticParams() {
  const tags = await getTags();
  return locales.flatMap((locale) => tags.map((t) => ({ locale, tag: t.tag })));
}

export async function generateMetadata({ params }: PageProps<"/[locale]/approfondimenti/tag/[tag]">): Promise<Metadata> {
  const { locale, tag } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  const t = decodeURIComponent(tag);
  return buildMetadata(s, { locale: l, route: { kind: "tag", tag: t }, title: `${m.approfondimenti.taggato} “${t}” — ${m.approfondimenti.titolo}`, description: m.meta.approfondimentiDescription });
}

export default async function TagPage({ params }: PageProps<"/[locale]/approfondimenti/tag/[tag]">) {
  const { locale, tag } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const t = decodeURIComponent(tag);
  const [s, voci, tags] = await Promise.all([getSettings(), getApprofondimenti(), getTags()]);
  if (!tags.some((x) => x.tag === t)) notFound();
  const m = getMessages(l);
  const filtrate = voci.filter((v) => (v.item.tag ?? []).includes(t));
  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.approfondimenti.titolo, path: href(l, { kind: "approfondimenti" }) },
          { name: t, path: href(l, { kind: "tag", tag: t }) },
        ])}
      />
      <Intestazione
        eyebrow={m.approfondimenti.taggato}
        titolo={t}
        compatta
        percorso={[
          { label: m.meta.siteName, href: href(l, { kind: "home" }) },
          { label: m.approfondimenti.titolo, href: href(l, { kind: "approfondimenti" }) },
          { label: t },
        ]}
      />
      <TabApprofondimenti locale={l} attiva="tutto" feedHref={`${href(l, { kind: "approfondimenti" })}/feed.xml`} />
      <ListaApprofondimenti voci={filtrate} locale={l} tags={tags.filter((x) => x.tag !== t)} />
      <FasciaContatto locale={l} />
    </>
  );
}
