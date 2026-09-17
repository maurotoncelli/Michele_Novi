import "server-only";
import { cache } from "react";
import { createReader } from "@keystatic/core/reader";
import keystaticConfig from "../../keystatic.config";
import type { Locale } from "@/i18n/routing";

/**
 * Unico punto di accesso ai dati. Nessuna pagina legge content/ direttamente.
 */
const reader = createReader(process.cwd(), keystaticConfig);

type Collections = typeof reader.collections;
type EntryOf<K extends keyof Collections> = NonNullable<Awaited<ReturnType<Collections[K]["read"]>>>;

export type Settings = NonNullable<Awaited<ReturnType<typeof reader.singletons.settings.read>>>;
export type Profilo = NonNullable<Awaited<ReturnType<typeof reader.singletons.profilo.read>>>;
export type Home = NonNullable<Awaited<ReturnType<typeof reader.singletons.home.read>>>;
export type Disegni = NonNullable<Awaited<ReturnType<typeof reader.singletons.disegni.read>>>;
export type CatalogoDisegni = Record<string, { src: string; alt: { it: string; en: string } }>;
export type Patologia = EntryOf<"patologie"> & { slug: string };
export type Sede = EntryOf<"sedi"> & { slug: string };
export type Pubblicazione = EntryOf<"pubblicazioni"> & { slug: string };
export type Nota = EntryOf<"quaderno"> & { slug: string };
export type Faq = EntryOf<"faq"> & { slug: string };
export type Recensione = EntryOf<"recensioni"> & { slug: string };

const peso = (a: { peso: number | null }, b: { peso: number | null }) => (a.peso ?? 99) - (b.peso ?? 99);

export const getSettings = cache(async (): Promise<Settings> => {
  const s = await reader.singletons.settings.read();
  if (!s) throw new Error("content/settings.yaml mancante");
  return s;
});

export const getProfilo = cache(async (): Promise<Profilo> => {
  const p = await reader.singletons.profilo.read();
  if (!p) throw new Error("content/profilo.yaml mancante");
  return p;
});

export const getHome = cache(async (): Promise<Home> => {
  const h = await reader.singletons.home.read();
  if (!h) throw new Error("content/home.yaml mancante");
  return h;
});

function publicDisegno(file: string | null | undefined, id: string) {
  if (file) return file.startsWith("/") ? file : `/images/disegni/${file}`;
  return `/images/disegni/${id}.png`;
}

/** Catalogo disegni da Keystatic. Se manca il file in CMS si usa public/images/disegni/{id}.png */
export const getDisegni = cache(async (): Promise<CatalogoDisegni> => {
  const d = await reader.singletons.disegni.read();
  const map: CatalogoDisegni = {};
  for (const v of d?.voci ?? []) {
    if (!v.id) continue;
    map[v.id] = { src: publicDisegno(v.file, v.id), alt: v.alt ?? { it: v.id, en: v.id } };
  }
  return map;
});

export function srcDisegno(catalogo: CatalogoDisegni, id: string | null | undefined, locale: Locale): { src: string; alt: string } | null {
  if (!id) return null;
  const voce = catalogo[id];
  const src = voce?.src ?? `/images/disegni/${id}.png`;
  return { src, alt: voce ? (locale === "en" ? voce.alt.en || voce.alt.it : voce.alt.it) || id : id };
}

export const getPatologie = cache(async (): Promise<Patologia[]> => {
  const all = await reader.collections.patologie.all();
  return all.map(({ slug, entry }) => ({ ...entry, slug })).sort(peso);
});

/** Risolve per slug IT o, se locale EN, per slugEn. */
export const getPatologia = cache(async (slug: string, locale: Locale): Promise<Patologia | null> => {
  const all = await getPatologie();
  return all.find((p) => (locale === "en" && p.slugEn ? p.slugEn === slug : p.slug === slug)) ?? all.find((p) => p.slug === slug) ?? null;
});

export const slugPatologia = (p: Patologia, locale: Locale) => (locale === "en" && p.slugEn ? p.slugEn : p.slug);

export const getSedi = cache(async (): Promise<Sede[]> => {
  const all = await reader.collections.sedi.all();
  return all.map(({ slug, entry }) => ({ ...entry, slug })).sort(peso);
});

export const getSede = cache(async (slug: string): Promise<Sede | null> => {
  const s = await reader.collections.sedi.read(slug);
  return s ? { ...s, slug } : null;
});

export const getPubblicazioni = cache(async (): Promise<Pubblicazione[]> => {
  const all = await reader.collections.pubblicazioni.all();
  return all
    .map(({ slug, entry }) => ({ ...entry, slug }))
    .filter((p) => p.pubblicato)
    .sort((a, b) => b.anno - a.anno || a.titolo.localeCompare(b.titolo));
});

export const getPubblicazione = cache(async (slug: string): Promise<Pubblicazione | null> => {
  const p = await reader.collections.pubblicazioni.read(slug);
  return p && p.pubblicato ? { ...p, slug } : null;
});

export const getNote = cache(async (): Promise<Nota[]> => {
  const all = await reader.collections.quaderno.all();
  return all
    .map(({ slug, entry }) => ({ ...entry, slug }))
    .filter((n) => n.pubblicato)
    .sort((a, b) => (b.data ?? "").localeCompare(a.data ?? ""));
});

export const getNota = cache(async (slug: string, locale: Locale): Promise<Nota | null> => {
  const all = await getNote();
  return all.find((n) => (locale === "en" && n.slugEn ? n.slugEn === slug : n.slug === slug)) ?? all.find((n) => n.slug === slug) ?? null;
});

export const slugNota = (n: Nota, locale: Locale) => (locale === "en" && n.slugEn ? n.slugEn : n.slug);

/** Tutti i tag usati da note e pubblicazioni, con conteggio. */
export const getTags = cache(async (): Promise<{ tag: string; n: number }[]> => {
  const [note, paper] = await Promise.all([getNote(), getPubblicazioni()]);
  const m = new Map<string, number>();
  for (const x of [...note, ...paper]) for (const t of x.tag ?? []) m.set(t, (m.get(t) ?? 0) + 1);
  return [...m.entries()].map(([tag, n]) => ({ tag, n })).sort((a, b) => b.n - a.n || a.tag.localeCompare(b.tag));
});

export const getFaq = cache(async (contesto?: Faq["contesto"]): Promise<Faq[]> => {
  const all = await reader.collections.faq.all();
  return all
    .map(({ slug, entry }) => ({ ...entry, slug }))
    .filter((f) => !contesto || f.contesto === contesto)
    .sort(peso);
});

export const getRecensioni = cache(async (): Promise<Recensione[]> => {
  const all = await reader.collections.recensioni.all();
  return all
    .map(({ slug, entry }) => ({ ...entry, slug }))
    .filter((r) => r.mostra)
    .sort((a, b) => (a.peso ?? 10) - (b.peso ?? 10) || a.nome.localeCompare(b.nome));
});

export type TipoPercorso = "lavoro" | "fellowship" | "formazione";

export function tipoPercorso(v: { tipo?: string | null } | null | undefined): TipoPercorso {
  return v?.tipo === "lavoro" || v?.tipo === "fellowship" ? v.tipo : "formazione";
}

export function annoPercorso(periodo: string): number {
  const m = periodo.match(/(\d{4})/);
  return m ? Number(m[1]) : 0;
}

/** Voce degli approfondimenti unificata per liste miste. */
export type VoceQuaderno =
  | { tipo: "paper"; data: string; slug: string; item: Pubblicazione }
  | { tipo: "nota"; data: string; slug: string; item: Nota };

export const getQuaderno = cache(async (): Promise<VoceQuaderno[]> => {
  const [note, paper] = await Promise.all([getNote(), getPubblicazioni()]);
  const voci: VoceQuaderno[] = [
    ...note.map((n) => ({ tipo: "nota" as const, data: n.data ?? "", slug: n.slug, item: n })),
    ...paper.map((p) => ({ tipo: "paper" as const, data: `${p.anno}-01-01`, slug: p.slug, item: p })),
  ];
  return voci.sort((a, b) => b.data.localeCompare(a.data));
});

/** Telefono in forma `tel:` (solo cifre e +). */
export const telHref = (tel: string | null | undefined) => (tel ? `tel:${tel.replace(/[^\d+]/g, "")}` : null);

export const waHref = (numero: string | null | undefined, testo: string) =>
  numero ? `https://wa.me/${numero.replace(/\D/g, "")}${testo ? `?text=${encodeURIComponent(testo)}` : ""}` : null;
