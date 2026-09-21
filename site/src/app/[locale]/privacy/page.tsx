import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getSettings } from "@/lib/content";
import { buildMetadata } from "@/lib/seo";
import { Intestazione } from "@/components/blocks/Pagina";
import { Legale } from "@/components/blocks/Legale";

export async function generateMetadata({ params }: PageProps<"/[locale]/privacy">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "privacy" }, title: m.legale.privacyTitolo, noindex: true });
}

export default async function PrivacyPage({ params }: PageProps<"/[locale]/privacy">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return (
    <>
      <Intestazione titolo={m.legale.privacyTitolo} compatta percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.legale.privacyTitolo }]} />
      <Legale tipo="privacy" locale={l} settings={s} />
    </>
  );
}
