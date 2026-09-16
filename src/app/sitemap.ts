import type { MetadataRoute } from "next";
import { href, locales, type Route } from "@/i18n/routing";
import { getNote, getPatologie, getPubblicazioni, getSedi, getSettings, getTags, slugNota, slugPatologia } from "@/lib/content";
import { siteUrl } from "@/lib/seo";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [s, patologie, sedi, paper, note, tags] = await Promise.all([getSettings(), getPatologie(), getSedi(), getPubblicazioni(), getNote(), getTags()]);
  const base = siteUrl(s);
  const now = new Date();

  const entry = (routeFor: (l: (typeof locales)[number]) => Route, priority: number, lastModified: Date = now): MetadataRoute.Sitemap[number] => {
    const languages: Record<string, string> = {};
    for (const l of locales) languages[l] = `${base}${href(l, routeFor(l))}`;
    languages["x-default"] = languages.it;
    return { url: languages.it, lastModified, changeFrequency: "monthly", priority, alternates: { languages } };
  };

  return [
    entry(() => ({ kind: "home" }), 1),
    entry(() => ({ kind: "chiSono" }), 0.8),
    entry(() => ({ kind: "cosaCuro" }), 0.9),
    entry(() => ({ kind: "dove" }), 0.9),
    entry(() => ({ kind: "quaderno" }), 0.7),
    entry(() => ({ kind: "quadernoPubblicazioni" }), 0.6),
    entry(() => ({ kind: "quadernoDalLavoro" }), 0.6),
    entry(() => ({ kind: "contatti" }), 0.9),
    ...patologie.map((p) => entry((l) => ({ kind: "cosaCuro", slug: slugPatologia(p, l) }), p.principale ? 0.9 : 0.8)),
    ...sedi.map((x) => entry(() => ({ kind: "dove", slug: x.slug }), 0.8)),
    ...paper.map((p) => entry(() => ({ kind: "paper", slug: p.slug }), 0.5, new Date(`${p.anno}-01-01`))),
    ...note.map((n) => entry((l) => ({ kind: "nota", slug: slugNota(n, l) }), 0.6, new Date(n.aggiornato ?? n.data ?? now))),
    ...tags.map((t) => entry(() => ({ kind: "tag", tag: t.tag }), 0.3)),
  ];
}
