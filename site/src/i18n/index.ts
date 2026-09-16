import it from "./messages/it.json";
import en from "./messages/en.json";
import type { Locale } from "./routing";

export type Messages = typeof it;

const dictionaries: Record<Locale, Messages> = { it, en: en as Messages };

export function getMessages(locale: Locale): Messages {
  return dictionaries[locale];
}

/** Sceglie il valore nella lingua richiesta, con fallback all'italiano. */
export function pick(v: { it: string; en: string } | null | undefined, locale: Locale): string {
  if (!v) return "";
  const out = locale === "en" ? v.en || v.it : v.it;
  return out ?? "";
}

export function formatDate(iso: string | null | undefined, locale: Locale): string {
  if (!iso) return "";
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return "";
  return new Intl.DateTimeFormat(getMessages(locale).date.locale, {
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(d);
}
