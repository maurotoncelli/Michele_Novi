"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { locales, segments, type Locale, type SegmentKey } from "@/i18n/routing";

/**
 * Traduce il percorso corrente segmento per segmento.
 * Gli slug dinamici (es. patologie) restano uguali: le pagine EN risolvono
 * anche lo slug IT e il canonical punta allo slug tradotto.
 */
function translatePath(pathname: string, from: Locale, to: Locale): string {
  const parts = pathname.split("/").filter(Boolean);
  if (parts[0] !== from) return `/${to}`;
  const rest = parts.slice(1);
  const out: string[] = [];
  const keys = Object.keys(segments) as SegmentKey[];
  rest.forEach((seg, i) => {
    // Solo i primi due livelli sono segmenti statici traducibili
    if (i < 2) {
      const k = keys.find((key) => segments[key][from] === seg);
      out.push(k ? segments[k][to] : seg);
    } else out.push(seg);
  });
  return `/${to}${out.length ? "/" + out.join("/") : ""}`;
}

export function LanguageSwitcher({ locale, label }: { locale: Locale; label: string }) {
  const pathname = usePathname() ?? `/${locale}`;
  return (
    <nav aria-label={label} className="flex items-center gap-0.5 text-[0.8rem] font-semibold tracking-wide">
      {locales.map((l, i) => (
        <span key={l} className="flex items-center">
          {i > 0 && <span className="mx-1 text-nebbia" aria-hidden="true">·</span>}
          {l === locale ? (
            <span aria-current="true" className="rounded-full bg-petrolio-3 px-2 py-0.5 text-petrolio">
              {l.toUpperCase()}
            </span>
          ) : (
            <Link
              href={translatePath(pathname, locale, l)}
              hrefLang={l}
              lang={l}
              className="rounded-full px-2 py-0.5 text-grafite transition hover:bg-osso-2 hover:text-inchiostro"
            >
              {l.toUpperCase()}
            </Link>
          )}
        </span>
      ))}
    </nav>
  );
}
