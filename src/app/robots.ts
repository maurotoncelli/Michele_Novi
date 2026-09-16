import type { MetadataRoute } from "next";
import { getSettings } from "@/lib/content";
import { siteUrl } from "@/lib/seo";

export default async function robots(): Promise<MetadataRoute.Robots> {
  const base = siteUrl(await getSettings());
  return {
    rules: [{ userAgent: "*", allow: "/", disallow: ["/keystatic", "/api/"] }],
    sitemap: `${base}/sitemap.xml`,
    host: base,
  };
}
