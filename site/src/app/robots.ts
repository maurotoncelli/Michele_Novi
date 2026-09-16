import type { MetadataRoute } from "next";
import { getSettings } from "@/lib/content";
import { siteUrl } from "@/lib/seo";

/**
 * In produzione: tutto indicizzabile tranne pannello e API.
 * Nei deploy di anteprima (VERCEL_ENV=preview) e finché non c'è il dominio del cliente
 * (settings.dominio vuoto): niente indicizzazione, così *.vercel.app non finisce su Google.
 */
export default async function robots(): Promise<MetadataRoute.Robots> {
  const settings = await getSettings();
  const base = siteUrl(settings);
  const indicizzabile = process.env.VERCEL_ENV !== "preview" && Boolean(settings.dominio || process.env.NEXT_PUBLIC_SITE_URL);
  if (!indicizzabile) {
    return { rules: [{ userAgent: "*", disallow: "/" }] };
  }
  return {
    rules: [{ userAgent: "*", allow: "/", disallow: ["/keystatic", "/api/"] }],
    sitemap: `${base}/sitemap.xml`,
    host: base,
  };
}
