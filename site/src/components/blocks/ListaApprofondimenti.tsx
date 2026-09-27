import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import type { Nota } from "@/lib/content";
import { Reveal } from "../ui/Reveal";
import { SchedaNota } from "./Schede";

/** Approfondimenti in griglia, dal più recente. */
export function ListaApprofondimenti({ note, locale, tags = [], feedHref }: { note: Nota[]; locale: Locale; tags?: { tag: string; n: number }[]; feedHref?: string }) {
  const m = getMessages(locale);

  return (
    <div className="contenitore py-10 md:py-14">
      {(tags.length > 0 || feedHref) && (
        <Reveal className="mb-10 flex flex-wrap items-center justify-between gap-x-8 gap-y-3">
          <div className="flex flex-wrap items-center gap-2">
            {tags.length > 0 && <span className="eyebrow mr-1">{m.approfondimenti.tag}</span>}
            {tags.map((t) => (
              <Link key={t.tag} href={href(locale, { kind: "tag", tag: t.tag })} className="tag hover:bg-petrolio-3 hover:text-petrolio">
                {t.tag} <span className="text-nebbia">{t.n}</span>
              </Link>
            ))}
          </div>
          {feedHref && (
            <a href={feedHref} className="text-xs text-nebbia hover:text-petrolio">
              {m.approfondimenti.feed}
            </a>
          )}
        </Reveal>
      )}
      {note.length === 0 ? (
        <p className="py-16 text-center text-grafite">{m.approfondimenti.vuoto}</p>
      ) : (
        <ul className="grid items-stretch gap-10 md:grid-cols-2 lg:grid-cols-3">
          {note.map((n, i) => (
            <Reveal key={n.slug} as="li" delay={(i % 3) * 70} className="h-full min-w-0">
              <SchedaNota n={n} locale={locale} sopraPiega={i < 3} />
            </Reveal>
          ))}
        </ul>
      )}
    </div>
  );
}
