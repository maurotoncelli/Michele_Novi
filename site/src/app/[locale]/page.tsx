import type { Metadata } from "next";
import { isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getHome, getPatologie, getProfilo, getPubblicazioni, getApprofondimenti, getRecensioni, getSedi, getSettings } from "@/lib/content";
import { buildMetadata, physicianJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";
import { FasciaFatti, FasciaPatologie, FasciaPercorso, FasciaApprofondimenti, FasciaRecensioni, FasciaSedi, Hero } from "@/components/blocks/Home";

export async function generateMetadata({ params }: PageProps<"/[locale]">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, home] = await Promise.all([getSettings(), getHome()]);
  const m = getMessages(l);
  return buildMetadata(s, {
    locale: l,
    route: { kind: "home" },
    title: pick(home.seo?.title, l) || m.meta.homeTitle,
    description: pick(home.seo?.description, l) || m.meta.homeDescription,
    image: home.seo?.ogImage ?? home.ritratto?.src,
  });
}

export default async function HomePage({ params }: PageProps<"/[locale]">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [settings, home, profilo, patologie, sedi, recensioni, approfondimenti, paper] = await Promise.all([
    getSettings(),
    getHome(),
    getProfilo(),
    getPatologie(),
    getSedi(),
    getRecensioni(),
    getApprofondimenti(),
    getPubblicazioni(),
  ]);

  const fasce = (home.fasce ?? []).filter((f) => f.attiva).map((f) => f.tipo);

  return (
    <>
      <JsonLd data={physicianJsonLd(settings, profilo, sedi, l)} />
      <Hero home={home} settings={settings} locale={l} />
      <FasciaFatti sedi={sedi} paper={paper} profilo={profilo} locale={l} />
      {fasce.map((tipo) => {
        switch (tipo) {
          case "patologie":
            return <FasciaPatologie key={tipo} patologie={patologie} locale={l} />;
          case "sedi":
            return <FasciaSedi key={tipo} sedi={sedi} locale={l} />;
          case "fiducia":
            return <FasciaPercorso key={tipo} profilo={profilo} home={home} locale={l} />;
          case "recensioni":
            return <FasciaRecensioni key={tipo} recensioni={recensioni} locale={l} />;
          case "approfondimenti":
            return <FasciaApprofondimenti key={tipo} voci={approfondimenti} locale={l} />;
          case "contatto":
            return <FasciaContatto key={tipo} locale={l} />;
          default:
            return null;
        }
      })}
    </>
  );
}
