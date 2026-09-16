import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getQuaderno, getSettings, slugNota } from "@/lib/content";
import { siteUrl } from "@/lib/seo";

export const dynamic = "force-static";
export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

export async function GET(_req: Request, ctx: RouteContext<"/[locale]/quaderno/feed.xml">) {
  const { locale } = await ctx.params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, voci] = await Promise.all([getSettings(), getQuaderno()]);
  const m = getMessages(l);
  const base = siteUrl(s);

  const items = voci
    .slice(0, 30)
    .map((v) => {
      const isPaper = v.tipo === "paper";
      const title = isPaper ? pick(v.item.titoloBreve, l) || v.item.titolo : pick(v.item.titolo, l);
      const link = isPaper ? `${base}${href(l, { kind: "paper", slug: v.slug })}` : `${base}${href(l, { kind: "nota", slug: slugNota(v.item, l) })}`;
      const desc = isPaper ? pick(v.item.riassunto, l) || v.item.abstract || `${v.item.rivista}, ${v.item.anno}` : pick(v.item.lead, l);
      const date = new Date(v.data).toUTCString();
      return `<item><title>${esc(title)}</title><link>${link}</link><guid>${link}</guid><pubDate>${date}</pubDate><description>${esc(desc ?? "")}</description>${(v.item.tag ?? []).map((t) => `<category>${esc(t)}</category>`).join("")}</item>`;
    })
    .join("");

  const xml = `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>${esc(`${m.quaderno.titolo} — ${s.nome}`)}</title><link>${base}${href(l, { kind: "quaderno" })}</link><description>${esc(m.meta.quadernoDescription)}</description><language>${l}</language><atom:link href="${base}${href(l, { kind: "quaderno" })}/feed.xml" rel="self" type="application/rss+xml"/>${items}</channel></rss>`;

  return new Response(xml, { headers: { "Content-Type": "application/rss+xml; charset=utf-8" } });
}
