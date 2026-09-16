import { href } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getPatologie, getProfilo, getPubblicazioni, getSedi, getSettings } from "@/lib/content";
import { siteUrl } from "@/lib/seo";

export const dynamic = "force-static";

/** Sommario leggibile per motori conversazionali. Generato dai dati, non scritto a mano. */
export async function GET() {
  const [s, p, sedi, patologie, paper] = await Promise.all([getSettings(), getProfilo(), getSedi(), getPatologie(), getPubblicazioni()]);
  const base = siteUrl(s);
  const m = getMessages("it");
  const righe = [
    `# ${s.nome}`,
    "",
    `> ${pick(p.titolo, "it").replace(/\.$/, "")}. ${pick(p.apertura, "it")}`,
    "",
    `Sito: ${base}${href("it", { kind: "home" })} (EN: ${base}${href("en", { kind: "home" })})`,
    s.telefono ? `Segreteria: ${s.telefono}` : "",
    s.email ? `Email: ${s.email}` : "",
    "",
    `## ${m.dove.titolo}`,
    ...sedi.map((x) => `- ${x.nome}, ${x.indirizzo}, ${x.citta}${x.provincia ? ` (${x.provincia})` : ""} — ${[x.visite && m.dove.visite, x.chirurgia && m.dove.chirurgia].filter(Boolean).join(", ")}: ${base}${href("it", { kind: "dove", slug: x.slug })}`),
    "",
    `## ${m.cosaCuro.titolo}`,
    ...patologie.map((x) => `- ${pick(x.titolo, "it")}: ${base}${href("it", { kind: "cosaCuro", slug: x.slug })}`),
    "",
    `## ${m.quaderno.pubblicazioni}`,
    ...paper.map((x) => `- ${x.titolo} (${x.rivista}, ${x.anno})${x.doi ? ` https://doi.org/${x.doi}` : ""}`),
    "",
    `## ${m.chiSono.titolo}`,
    `${base}${href("it", { kind: "chiSono" })}`,
    "",
    pick(s.disclaimer, "it"),
  ].filter((r) => r !== undefined && r !== null);
  return new Response(righe.join("\n"), { headers: { "Content-Type": "text/plain; charset=utf-8" } });
}
