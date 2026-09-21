import type { Metadata } from "next";
import { href, locales, type Locale, type Route } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import type { Settings, Profilo, Sede, Pubblicazione, Nota, Patologia, Faq } from "./content";
import { srcMedia } from "./media";

/**
 * URL pubblico del sito, in ordine: dominio in Keystatic → env esplicita →
 * URL di produzione Vercel → URL del deploy (preview) → localhost.
 * Quando il cliente compra il dominio basta scriverlo in settings.dominio.
 */
export function siteUrl(settings: Settings): string {
  const vercel = process.env.VERCEL_PROJECT_PRODUCTION_URL || process.env.VERCEL_URL;
  const base = settings.dominio || process.env.NEXT_PUBLIC_SITE_URL || (vercel ? `https://${vercel}` : "") || "http://localhost:3000";
  return base.replace(/\/$/, "");
}

type MetaInput = {
  locale: Locale;
  route: Route;
  /** Rotta EN se diversa da quella IT (slug tradotti). Vuoto = stessa rotta. */
  routeEn?: Route;
  title: string;
  description?: string | null;
  image?: string | null;
  noindex?: boolean | null;
  type?: "website" | "article";
  publishedTime?: string | null;
  modifiedTime?: string | null;
};

/** Metadata completi: title, description, canonical, hreflang, Open Graph. */
export function buildMetadata(settings: Settings, input: MetaInput): Metadata {
  const base = siteUrl(settings);
  const m = getMessages(input.locale);
  const routeFor = (l: Locale) => (l === "en" && input.routeEn ? input.routeEn : input.route);
  const canonical = `${base}${href(input.locale, routeFor(input.locale))}`;
  const languages: Record<string, string> = {};
  for (const l of locales) languages[l] = `${base}${href(l, routeFor(l))}`;
  languages["x-default"] = `${base}${href("it", routeFor("it"))}`;

  const title = input.title;
  const description = input.description?.trim() || m.meta.homeDescription;
  const image = input.image ? `${base}${input.image}` : `${base}/opengraph-image`;

  // Se il titolo SEO scritto a mano contiene già il nome del sito, non applichiamo il template del layout.
  const includesName = title.includes(settings.nome) || title.includes(m.meta.siteName);

  return {
    metadataBase: new URL(base),
    title: includesName ? { absolute: title } : title,
    description,
    alternates: { canonical, languages },
    robots: input.noindex ? { index: false, follow: false } : undefined,
    openGraph: {
      title,
      description,
      url: canonical,
      siteName: m.meta.siteName,
      locale: input.locale === "it" ? "it_IT" : "en_GB",
      type: input.type ?? "website",
      images: [{ url: image }],
      publishedTime: input.publishedTime ?? undefined,
      modifiedTime: input.modifiedTime ?? undefined,
    },
    twitter: { card: "summary_large_image", title, description, images: [image] },
  };
}

/* ------------------------------------------------------------------ JSON-LD */

const sameAs = (s: Settings) => [s.instagram, s.linkedin, s.youtube].filter(Boolean) as string[];

export function physicianId(settings: Settings) {
  return `${siteUrl(settings)}/#physician`;
}

export function physicianJsonLd(settings: Settings, profilo: Profilo, sedi: Sede[], locale: Locale) {
  const base = siteUrl(settings);
  return {
    "@context": "https://schema.org",
    "@type": "Physician",
    "@id": physicianId(settings),
    name: profilo.nome,
    honorificPrefix: locale === "it" ? "Dott." : "Dr",
    jobTitle: pick(profilo.titolo, locale),
    description: pick(profilo.apertura, locale),
    url: `${base}${href(locale, { kind: "home" })}`,
    image: profilo.ritratto?.src ? `${base}${profilo.ritratto.src}` : undefined,
    medicalSpecialty: "Orthopedic",
    telephone: settings.telefono || undefined,
    email: settings.email || undefined,
    sameAs: sameAs(settings),
    knowsLanguage: profilo.lingue ?? undefined,
    workLocation: sedi.map((s) => ({
      "@type": s.tipo === "ospedale" ? "Hospital" : "MedicalClinic",
      name: s.nome,
      address: sedeAddress(s),
      url: `${base}${href(locale, { kind: "dove", slug: s.slug })}`,
    })),
  };
}

function sedeAddress(s: Sede) {
  return {
    "@type": "PostalAddress",
    streetAddress: s.indirizzo || undefined,
    addressLocality: s.citta || undefined,
    addressRegion: s.provincia || undefined,
    postalCode: s.cap || undefined,
    addressCountry: "IT",
  };
}

/** Per la scheda sede: LocalBusiness solo se propria, altrimenti luogo di lavoro. */
export function sedeJsonLd(settings: Settings, sede: Sede, locale: Locale) {
  const base = siteUrl(settings);
  const url = `${base}${href(locale, { kind: "dove", slug: sede.slug })}`;
  const geo =
    sede.coordinate?.lat != null && sede.coordinate?.lng != null
      ? { "@type": "GeoCoordinates", latitude: sede.coordinate.lat, longitude: sede.coordinate.lng }
      : undefined;
  if (sede.propria) {
    return {
      "@context": "https://schema.org",
      "@type": "MedicalClinic",
      "@id": `${url}#clinic`,
      name: sede.nome,
      url,
      address: sedeAddress(sede),
      geo,
      telephone: settings.telefono || undefined,
      medicalSpecialty: "Orthopedic",
      employee: { "@id": physicianId(settings) },
      hasMap: sede.mapsUrl || undefined,
      image: sede.foto?.[0]?.src ? `${base}${sede.foto[0].src}` : undefined,
    };
  }
  return {
    "@context": "https://schema.org",
    "@type": sede.tipo === "ospedale" ? "Hospital" : "MedicalClinic",
    name: sede.nome,
    address: sedeAddress(sede),
    geo,
    url: sede.sitoStruttura || url,
    hasMap: sede.mapsUrl || undefined,
    description: pick(sede.ruolo, locale) || undefined,
  };
}

export function breadcrumbJsonLd(settings: Settings, items: { name: string; path: string }[]) {
  const base = siteUrl(settings);
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((it, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: it.name,
      item: `${base}${it.path}`,
    })),
  };
}

export function paperJsonLd(settings: Settings, p: Pubblicazione, locale: Locale) {
  const base = siteUrl(settings);
  return {
    "@context": "https://schema.org",
    "@type": "ScholarlyArticle",
    headline: p.titolo,
    name: p.titolo,
    author: p.autori ? p.autori.split(/,\s*/).map((n) => ({ "@type": "Person", name: n })) : { "@id": physicianId(settings) },
    contributor: { "@id": physicianId(settings) },
    datePublished: String(p.anno),
    isPartOf: p.rivista ? { "@type": "Periodical", name: p.rivista } : undefined,
    sameAs: p.doi ? `https://doi.org/${p.doi}` : p.url || undefined,
    identifier: p.doi ? { "@type": "PropertyValue", propertyID: "DOI", value: p.doi } : undefined,
    abstract: p.abstract || undefined,
    url: `${base}${href(locale, { kind: "paper", slug: p.slug })}`,
    inLanguage: "en",
    keywords: p.tag?.join(", ") || undefined,
  };
}

export function articleJsonLd(settings: Settings, n: Nota, locale: Locale, slug: string) {
  const base = siteUrl(settings);
  return {
    "@context": "https://schema.org",
    "@type": "MedicalWebPage",
    mainEntity: {
      "@type": "Article",
      headline: pick(n.titolo, locale),
      description: pick(n.lead, locale) || undefined,
      datePublished: n.data,
      dateModified: n.aggiornato || n.data,
      author: { "@id": physicianId(settings) },
      image: srcMedia(n.copertina?.src, "approfondimenti") ? `${base}${srcMedia(n.copertina?.src, "approfondimenti")}` : undefined,
      inLanguage: locale,
      keywords: n.tag?.join(", ") || undefined,
    },
    url: `${base}${href(locale, { kind: "nota", slug })}`,
    lastReviewed: n.aggiornato || n.data,
    reviewedBy: { "@id": physicianId(settings) },
  };
}

export function medicalWebPageJsonLd(settings: Settings, p: Patologia, locale: Locale, slug: string) {
  const base = siteUrl(settings);
  return {
    "@context": "https://schema.org",
    "@type": "MedicalWebPage",
    name: pick(p.titolo, locale),
    description: pick(p.lead, locale) || undefined,
    url: `${base}${href(locale, { kind: "cosaCuro", slug })}`,
    inLanguage: locale,
    about: { "@type": "MedicalSpecialty", name: "Orthopedic" },
    reviewedBy: { "@id": physicianId(settings) },
    audience: { "@type": "MedicalAudience", audienceType: "Patient" },
  };
}

export function faqJsonLd(items: { domanda: string; risposta: string }[]) {
  if (!items.length) return null;
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: items.map((f) => ({
      "@type": "Question",
      name: f.domanda,
      acceptedAnswer: { "@type": "Answer", text: f.risposta },
    })),
  };
}

export const faqItems = (faq: Pick<Faq, "domanda" | "risposta">[] | Patologia["faq"], locale: Locale) =>
  (faq ?? []).map((f) => ({ domanda: pick(f.domanda, locale), risposta: pick(f.risposta, locale) })).filter((f) => f.domanda && f.risposta);
