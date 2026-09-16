import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";

type Attiva = "tutto" | "pubblicazioni" | "dalLavoro";

/** Tab a raccordo inverso: la voce attiva si fonde con il pannello sotto. */
export function TabQuaderno({ locale, attiva, feedHref }: { locale: Locale; attiva: Attiva; feedHref: string }) {
  const m = getMessages(locale);
  const tabs: { id: Attiva; label: string; href: string }[] = [
    { id: "tutto", label: m.quaderno.tutto, href: href(locale, { kind: "quaderno" }) },
    { id: "pubblicazioni", label: m.quaderno.pubblicazioni, href: href(locale, { kind: "quadernoPubblicazioni" }) },
    { id: "dalLavoro", label: m.quaderno.dalLavoro, href: href(locale, { kind: "quadernoDalLavoro" }) },
  ];
  return (
    <div className="contenitore">
      <div className="flex items-end justify-between gap-4 border-b border-linea">
        <nav aria-label={m.quaderno.titolo} className="-mb-px flex gap-1 overflow-x-auto">
          {tabs.map((t) => {
            const on = t.id === attiva;
            return (
              <Link
                key={t.id}
                href={t.href}
                aria-current={on ? "page" : undefined}
                className={`relative whitespace-nowrap rounded-t-[1.25rem] px-5 py-3 text-[0.95rem] font-medium transition ${
                  on
                    ? "bg-osso text-petrolio shadow-[inset_0_1px_0_#fff] before:absolute before:-left-3 before:bottom-0 before:h-3 before:w-3 before:rounded-br-full before:shadow-[3px_3px_0_3px_#fff] after:absolute after:-right-3 after:bottom-0 after:h-3 after:w-3 after:rounded-bl-full after:shadow-[-3px_3px_0_3px_#fff]"
                    : "text-grafite hover:text-inchiostro"
                }`}
              >
                {t.label}
              </Link>
            );
          })}
        </nav>
        <a href={feedHref} className="mb-2 hidden shrink-0 text-xs text-nebbia hover:text-petrolio sm:block">
          {m.quaderno.feed}
        </a>
      </div>
    </div>
  );
}
