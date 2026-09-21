import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";

type Attiva = "tutto" | "pubblicazioni" | "dalLavoro";

/** Tab a linea: voce attiva = azzurro + tratto sotto. */
export function TabApprofondimenti({ locale, attiva, feedHref }: { locale: Locale; attiva: Attiva; feedHref: string }) {
  const m = getMessages(locale);
  const tabs: { id: Attiva; label: string; href: string }[] = [
    { id: "tutto", label: m.approfondimenti.tutto, href: href(locale, { kind: "approfondimenti" }) },
    { id: "pubblicazioni", label: m.approfondimenti.pubblicazioni, href: href(locale, { kind: "approfondimentiPubblicazioni" }) },
    { id: "dalLavoro", label: m.approfondimenti.dalLavoro, href: href(locale, { kind: "approfondimentiDalLavoro" }) },
  ];
  return (
    <div className="contenitore">
      <div className="flex items-end justify-between gap-4 border-b border-linea">
        <nav aria-label={m.approfondimenti.titolo} className="flex gap-8 overflow-x-auto">
          {tabs.map((t) => {
            const on = t.id === attiva;
            return (
              <Link
                key={t.id}
                href={t.href}
                aria-current={on ? "page" : undefined}
                className={`relative whitespace-nowrap py-3 text-[0.95rem] transition ${
                  on ? "text-petrolio after:absolute after:inset-x-0 after:bottom-0 after:h-px after:bg-petrolio" : "text-grafite hover:text-inchiostro"
                }`}
              >
                {t.label}
              </Link>
            );
          })}
        </nav>
        <a href={feedHref} className="mb-3 hidden shrink-0 text-xs text-nebbia hover:text-petrolio sm:block">
          {m.approfondimenti.feed}
        </a>
      </div>
    </div>
  );
}
