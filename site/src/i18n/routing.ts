/**
 * Locali e slug tradotti. Unico posto in cui vivono i percorsi del sito.
 * Le cartelle in app/[locale]/ usano i nomi IT storici; l'URL pubblico può differire.
 */

export const locales = ["it", "en"] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = "it";

export const isLocale = (v: string): v is Locale => (locales as readonly string[]).includes(v);

/** Segmenti di primo livello: chiave interna → slug pubblico per lingua. */
export const segments = {
  chiSono: { it: "chi-sono", en: "about" },
  cosaCuro: { it: "cosa-curo", en: "conditions" },
  dove: { it: "dove", en: "locations" },
  quaderno: { it: "approfondimenti", en: "in-depth" },
  pubblicazioni: { it: "pubblicazioni", en: "publications" },
  dalLavoro: { it: "dal-lavoro", en: "from-the-clinic" },
  tag: { it: "tag", en: "tag" },
  contatti: { it: "contatti", en: "contact" },
  privacy: { it: "privacy", en: "privacy" },
  cookie: { it: "cookie", en: "cookies" },
} as const;

export type SegmentKey = keyof typeof segments;

/** Cartelle reali in app/[locale]/ (IT storico). */
const folders: Record<SegmentKey, string> = {
  chiSono: "chi-sono",
  cosaCuro: "cosa-curo",
  dove: "dove",
  quaderno: "quaderno",
  pubblicazioni: "pubblicazioni",
  dalLavoro: "dal-lavoro",
  tag: "tag",
  contatti: "contatti",
  privacy: "privacy",
  cookie: "cookie",
};

/** Vecchi slug pubblici → stessa chiave. 301 verso lo slug attuale. */
const aliases: Partial<Record<SegmentKey, { it?: string[]; en?: string[] }>> = {
  quaderno: { it: ["quaderno"], en: ["notebook", "insights"] },
};

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

function join(locale: Locale, parts: string[]) {
  return `/${locale}/${parts.filter(Boolean).join("/")}`;
}

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
 * Percorso interno (cartelle app/).
 * Coincide con href solo quando slug pubblico IT = nome cartella.
 */
export function internalPath(locale: Locale, route: Route): string {
  const f = (k: SegmentKey) => folders[k];
  switch (route.kind) {
    case "home":
      return `/${locale}`;
    case "chiSono":
      return join(locale, [f("chiSono")]);
    case "cosaCuro":
      return join(locale, route.slug ? [f("cosaCuro"), route.slug] : [f("cosaCuro")]);
    case "dove":
      return join(locale, route.slug ? [f("dove"), route.slug] : [f("dove")]);
    case "quaderno":
      return join(locale, [f("quaderno")]);
    case "quadernoPubblicazioni":
      return join(locale, [f("quaderno"), f("pubblicazioni")]);
    case "quadernoDalLavoro":
      return join(locale, [f("quaderno"), f("dalLavoro")]);
    case "paper":
      return join(locale, [f("quaderno"), f("pubblicazioni"), route.slug]);
    case "nota":
      return join(locale, [f("quaderno"), route.slug]);
    case "tag":
      return join(locale, [f("quaderno"), f("tag"), route.tag]);
    case "contatti":
      return join(locale, [f("contatti")]);
    case "privacy":
      return join(locale, [f("privacy")]);
    case "cookie":
      return join(locale, [f("cookie")]);
  }
}

function pair(source: string, destination: string, list: { source: string; destination: string }[]) {
  if (source === destination) return;
  list.push({ source, destination });
  list.push({ source: `${source}/:path*`, destination: `${destination}/:path*` });
}

/**
 * Rewrites e redirect per next.config.ts: lo slug pubblico viene riscritto
 * sulla cartella, e la cartella (se raggiunta) fa 301 allo slug pubblico.
 * Gli slug vecchi (quaderno, notebook) fanno 301 al nome attuale.
 */
export function routingRules() {
  const rewrites: { source: string; destination: string }[] = [];
  const redirects: { source: string; destination: string; permanent: boolean }[] = [];
  const nested: [SegmentKey, SegmentKey][] = [
    ["quaderno", "pubblicazioni"],
    ["quaderno", "dalLavoro"],
    ["quaderno", "tag"],
  ];

  for (const locale of locales) {
    for (const [a, b] of nested) {
      const pub = `/${locale}/${segments[a][locale]}/${segments[b][locale]}`;
      const int = `/${locale}/${folders[a]}/${folders[b]}`;
      pair(pub, int, rewrites);
      if (pub !== int) {
        redirects.push({ source: int, destination: pub, permanent: true });
        redirects.push({ source: `${int}/:path*`, destination: `${pub}/:path*`, permanent: true });
      }
    }
    for (const key of Object.keys(segments) as SegmentKey[]) {
      if (key === "pubblicazioni" || key === "dalLavoro" || key === "tag") continue;
      const pub = `/${locale}/${segments[key][locale]}`;
      const int = `/${locale}/${folders[key]}`;
      pair(pub, int, rewrites);
      if (pub !== int) {
        redirects.push({ source: int, destination: pub, permanent: true });
        redirects.push({ source: `${int}/:path*`, destination: `${pub}/:path*`, permanent: true });
      }
    }

    for (const key of Object.keys(aliases) as SegmentKey[]) {
      for (const old of aliases[key]?.[locale] ?? []) {
        const from = `/${locale}/${old}`;
        const to = `/${locale}/${segments[key][locale]}`;
        if (from === to) continue;
        redirects.push({ source: from, destination: to, permanent: true });
        redirects.push({ source: `${from}/:path*`, destination: `${to}/:path*`, permanent: true });
      }
    }
  }
  return { rewrites, redirects };
}
