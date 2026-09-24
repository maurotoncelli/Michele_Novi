import "server-only";
import { href, type Locale } from "@/i18n/routing";
import { pick } from "@/i18n";
import { getPaginaCosaCuro, slugPatologia, type Patologia } from "./content";
import { slugify, temi } from "./markdoc";

export type Sintomo = { testo: string; href: string; area: string };

/** Temi della scheda nella lingua richiesta; se il corpo EN manca, quelli IT. */
export async function temiDi(p: Patologia, l: Locale) {
  const en = l === "en" && p.corpoEn ? await temi(p.corpoEn) : [];
  return en.length ? en : temi(p.corpo);
}

export const hrefPatologia = (p: Patologia, l: Locale, ancora?: string) =>
  `${href(l, { kind: "cosaCuro", slug: slugPatologia(p, l) })}${ancora ? `#${ancora}` : ""}`;

/** Le prime `n` frasi alternando le aree (spalla, gomito, sport, spalla…), nell'ordine di Keystatic. */
export function sintomiVari(sintomi: Sintomo[], n: number): Sintomo[] {
  const gruppi = new Map<string, Sintomo[]>();
  for (const x of sintomi) gruppi.set(x.area, [...(gruppi.get(x.area) ?? []), x]);
  const out: Sintomo[] = [];
  for (let giro = 0; out.length < Math.min(n, sintomi.length); giro++) {
    for (const g of gruppi.values()) if (g[giro] && out.length < n) out.push(g[giro]);
  }
  return out;
}

/**
 * Le frasi "Parti da quello che senti" di Keystatic, risolte in link.
 * Il capitolo si indica col titolo IT; in EN si apre il capitolo nella stessa posizione.
 */
export async function getSintomi(patologie: Patologia[], l: Locale): Promise<Sintomo[]> {
  const pagina = await getPaginaCosaCuro();
  const out = await Promise.all(
    pagina.sintomi.map(async (x) => {
      const p = patologie.find((q) => q.slug === x.patologia);
      const testo = pick(x.testo, l);
      if (!p || !testo) return null;
      const i = x.tema ? (await temi(p.corpo)).findIndex((t) => t.id === slugify(x.tema)) : -1;
      const ancora = i >= 0 ? (await temiDi(p, l))[i]?.id : undefined;
      return { testo, href: hrefPatologia(p, l, ancora), area: pick(p.titolo, l) };
    }),
  );
  return out.filter((x): x is Sintomo => !!x);
}
