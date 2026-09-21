import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getQuaderno, getSettings, getTags } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Intestazione } from "@/components/blocks/Pagina";
import { TabQuaderno } from "@/components/blocks/TabQuaderno";
import { ListaQuaderno } from "@/components/blocks/ListaQuaderno";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export const dynamicParams = false;
export async function generateStaticParams() {
  const tags = await getTags();
  return locales.flatMap((locale) => tags.map((t) => ({ locale, tag: t.tag })));
}

export async function generateMetadata({ params }: PageProps<"/[locale]/quaderno/tag/[tag]">): Promise<Metadata> {
  const { locale, tag } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  const t = decodeURIComponent(tag);
  return buildMetadata(s, { locale: l, route: { kind: "tag", tag: t }, title: `${m.quaderno.taggato} “${t}” — ${m.quaderno.titolo}`, description: m.meta.quadernoDescription });
}

export default async function TagPage({ params }: PageProps<"/[locale]/quaderno/tag/[tag]">) {
  const { locale, tag } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const t = decodeURIComponent(tag);
  const [s, voci, tags] = await Promise.all([getSettings(), getQuaderno(), getTags()]);
  if (!tags.some((x) => x.tag === t)) notFound();
  const m = getMessages(l);
  const filtrate = voci.filter((v) => (v.item.tag ?? []).includes(t));
  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.quaderno.titolo, path: href(l, { kind: "quaderno" }) },
          { name: t, path: href(l, { kind: "tag", tag: t }) },
        ])}
      />
      <Intestazione
        eyebrow={m.quaderno.taggato}
        titolo={t}
        compatta
        percorso={[
          { label: m.meta.siteName, href: href(l, { kind: "home" }) },
          { label: m.quaderno.titolo, href: href(l, { kind: "quaderno" }) },
          { label: t },
        ]}
      />
      <TabQuaderno locale={l} attiva="tutto" feedHref={`${href(l, { kind: "quaderno" })}/feed.xml`} />
      <ListaQuaderno voci={filtrate} locale={l} tags={tags.filter((x) => x.tag !== t)} />
      <FasciaContatto locale={l} />
    </>
  );
}
