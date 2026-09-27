import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getNote, getSettings, slugNota } from "@/lib/content";
import { siteUrl } from "@/lib/seo";

export const dynamic = "force-static";
export function generateStaticParams() {
  return locales.map((locale) => ({ locale }));
}

const esc = (s: string) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

export async function GET(_req: Request, ctx: RouteContext<"/[locale]/approfondimenti/feed.xml">) {
  const { locale } = await ctx.params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, note] = await Promise.all([getSettings(), getNote()]);
  const m = getMessages(l);
  const base = siteUrl(s);

  const items = note
    .slice(0, 30)
    .map((item) => {
      const title = pick(item.titolo, l);
      const link = `${base}${href(l, { kind: "nota", slug: slugNota(item, l) })}`;
      const date = new Date(item.data ?? item.aggiornato ?? "1970-01-01").toUTCString();
      return `<item><title>${esc(title)}</title><link>${link}</link><guid>${link}</guid><pubDate>${date}</pubDate><description>${esc(pick(item.lead, l))}</description>${(item.tag ?? []).map((t) => `<category>${esc(t)}</category>`).join("")}</item>`;
    })
    .join("");

  const xml = `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>${esc(`${m.approfondimenti.titolo} — ${s.nome}`)}</title><link>${base}${href(l, { kind: "approfondimenti" })}</link><description>${esc(m.meta.approfondimentiDescription)}</description><language>${l}</language><atom:link href="${base}${href(l, { kind: "approfondimenti" })}/feed.xml" rel="self" type="application/rss+xml"/>${items}</channel></rss>`;

  return new Response(xml, { headers: { "Content-Type": "application/rss+xml; charset=utf-8" } });
}
