/**
 * Locali e slug tradotti. Unico posto in cui vivono i percorsi del sito.
 * Le cartelle in app/[locale]/ usano i nomi IT; l'EN arriva via rewrite (next.config.ts).
 */

export const locales = ["it", "en"] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = "it";

export const isLocale = (v: string): v is Locale => (locales as readonly string[]).includes(v);

/** Segmenti di primo livello: chiave interna → slug per lingua. */
export const segments = {
  chiSono: { it: "chi-sono", en: "about" },
  cosaCuro: { it: "cosa-curo", en: "conditions" },
  dove: { it: "dove", en: "locations" },
  quaderno: { it: "quaderno", en: "notebook" },
  pubblicazioni: { it: "pubblicazioni", en: "publications" },
  dalLavoro: { it: "dal-lavoro", en: "from-the-clinic" },
  tag: { it: "tag", en: "tag" },
  contatti: { it: "contatti", en: "contact" },
  privacy: { it: "privacy", en: "privacy" },
  cookie: { it: "cookie", en: "cookies" },
} as const;

export type SegmentKey = keyof typeof segments;

type Route =
  | { kind: "home" }
  | { kind: "chiSono" }
  | { kind: "cosaCuro"; slug?: string }
  | { kind: "dove"; slug?: string }
  | { kind: "quaderno" }
  | { kind: "quadernoPubblicazioni" }
  | { kind: "quadernoDalLavoro" }
  | { kind: "paper"; slug: string }
  | { kind: "nota"; slug: string }
  | { kind: "tag"; tag: string }
  | { kind: "contatti" }
  | { kind: "privacy" }
  | { kind: "cookie" };

export type { Route };

/** Percorso pubblico (quello che si vede nel browser). */
export function href(locale: Locale, route: Route): string {
  const s = (k: SegmentKey) => segments[k][locale];
  const base = `/${locale}`;
  switch (route.kind) {
    case "home":
      return base;
    case "chiSono":
      return `${base}/${s("chiSono")}`;
    case "cosaCuro":
      return route.slug ? `${base}/${s("cosaCuro")}/${route.slug}` : `${base}/${s("cosaCuro")}`;
    case "dove":
      return route.slug ? `${base}/${s("dove")}/${route.slug}` : `${base}/${s("dove")}`;
    case "quaderno":
      return `${base}/${s("quaderno")}`;
    case "quadernoPubblicazioni":
      return `${base}/${s("quaderno")}/${s("pubblicazioni")}`;
    case "quadernoDalLavoro":
      return `${base}/${s("quaderno")}/${s("dalLavoro")}`;
    case "paper":
      return `${base}/${s("quaderno")}/${s("pubblicazioni")}/${route.slug}`;
    case "nota":
      return `${base}/${s("quaderno")}/${route.slug}`;
    case "tag":
      return `${base}/${s("quaderno")}/${s("tag")}/${route.tag}`;
    case "contatti":
      return `${base}/${s("contatti")}`;
    case "privacy":
      return `${base}/${s("privacy")}`;
    case "cookie":
      return `${base}/${s("cookie")}`;
  }
}

/**
 * Percorso interno (cartelle app/, sempre in IT).
 * Coincide con href("it", …) ma con il prefisso della lingua richiesta.
 */
export function internalPath(locale: Locale, route: Route): string {
  const it = href("it", route);
  return `/${locale}${it.slice(3)}`;
}

/**
 * Rewrites e redirect per next.config.ts: per ogni locale non-IT, lo slug tradotto
 * viene riscritto sulla cartella IT, e la cartella IT (se raggiunta) fa 301 allo slug tradotto.
 */
export function routingRules() {
  const rewrites: { source: string; destination: string }[] = [];
  const redirects: { source: string; destination: string; permanent: boolean }[] = [];
  for (const locale of locales) {
    if (locale === "it") continue;
    // Coppie di secondo livello (quaderno/pubblicazioni, quaderno/dal-lavoro, quaderno/tag)
    const nested: [SegmentKey, SegmentKey][] = [
      ["quaderno", "pubblicazioni"],
      ["quaderno", "dalLavoro"],
      ["quaderno", "tag"],
    ];
    for (const [a, b] of nested) {
      const pub = `/${locale}/${segments[a][locale]}/${segments[b][locale]}`;
      const int = `/${locale}/${segments[a].it}/${segments[b].it}`;
      if (pub !== int) {
        rewrites.push({ source: `${pub}/:path*`, destination: `${int}/:path*` });
        redirects.push({ source: `${int}/:path*`, destination: `${pub}/:path*`, permanent: true });
      }
    }
    for (const key of Object.keys(segments) as SegmentKey[]) {
      if (key === "pubblicazioni" || key === "dalLavoro" || key === "tag") continue;
      const pub = `/${locale}/${segments[key][locale]}`;
      const int = `/${locale}/${segments[key].it}`;
      if (pub === int) continue;
      rewrites.push({ source: `${pub}/:path*`, destination: `${int}/:path*` });
      redirects.push({ source: `${int}/:path*`, destination: `${pub}/:path*`, permanent: true });
    }
  }
  return { rewrites, redirects };
}
