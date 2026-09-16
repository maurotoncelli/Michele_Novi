import type { Metadata, Viewport } from "next";
import { Geist } from "next/font/google";
import { notFound } from "next/navigation";
import "../globals.css";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getSettings, telHref } from "@/lib/content";
import { siteUrl } from "@/lib/seo";
import { Header } from "@/components/Header";
import { Footer } from "@/components/Footer";
import { CookieBanner } from "@/components/CookieBanner";

const geist = Geist({
  subsets: ["latin"],
  variable: "--font-geist",
  display: "swap",
});

export const dynamicParams = false;
export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

export async function generateMetadata({ params }: LayoutProps<"/[locale]">): Promise<Metadata> {
  const { locale } = await params;
  if (!isLocale(locale)) return {};
  const s = await getSettings();
  const m = getMessages(locale);
  return {
    metadataBase: new URL(siteUrl(s)),
    title: { default: m.meta.homeTitle, template: `%s — ${m.meta.siteName}` },
    description: m.meta.homeDescription,
    applicationName: m.meta.siteName,
    alternates: {
      types: { "application/rss+xml": `${href(locale, { kind: "quaderno" })}/feed.xml` },
    },
  };
}

export const viewport: Viewport = {
  themeColor: "#f7f6f3",
  width: "device-width",
  initialScale: 1,
};

export default async function LocaleLayout({ children, params }: LayoutProps<"/[locale]">) {
  const { locale } = await params;
  if (!isLocale(locale)) notFound();
  const l = locale as Locale;
  const [s] = await Promise.all([getSettings()]);
  const m = getMessages(l);
  const tel = telHref(s.telefono);
  const gaId = process.env.NEXT_PUBLIC_GA_ID;

  return (
    <html lang={l} className={`${geist.variable} h-full`}>
      <body className="aloni flex min-h-full flex-col">
        <Header
          locale={l}
          homeHref={href(l, { kind: "home" })}
          nome={s.nome}
          ruolo={pick(s.ruolo, l)}
          nav={[
            { label: m.nav.chiSono, href: href(l, { kind: "chiSono" }) },
            { label: m.nav.cosaCuro, href: href(l, { kind: "cosaCuro" }) },
            { label: m.nav.dove, href: href(l, { kind: "dove" }) },
            { label: m.nav.quaderno, href: href(l, { kind: "quaderno" }) },
            { label: m.nav.contatti, href: href(l, { kind: "contatti" }) },
          ]}
          tel={tel ? { href: tel, label: m.cta.chiama } : null}
          scrivi={{ href: href(l, { kind: "contatti" }), label: m.cta.scrivi }}
          a11y={{ apriMenu: m.a11y.apriMenu, chiudiMenu: m.a11y.chiudiMenu, cambiaLingua: m.a11y.cambiaLingua, salta: m.nav.salta }}
        />
        <main id="contenuto" className="flex-1">
          {children}
        </main>
        <Footer locale={l} />
        {gaId && (
          <CookieBanner
            gaId={gaId}
            testo={m.cookie.testo}
            accetta={m.cookie.accetta}
            rifiuta={m.cookie.rifiuta}
            cookieHref={href(l, { kind: "cookie" })}
            cookieLabel={m.cookie.info}
          />
        )}
      </body>
    </html>
  );
}
