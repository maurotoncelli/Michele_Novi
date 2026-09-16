import Link from "next/link";
import type { ReactNode } from "react";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";

/** Intestazione di pagina: eyebrow, H1, lead. Una sola per pagina. */
export function Intestazione({ eyebrow, titolo, lead, children, compatta = false }: { eyebrow?: string; titolo: string; lead?: string; children?: ReactNode; compatta?: boolean }) {
  return (
    <header className={`contenitore ${compatta ? "pt-10 pb-6 md:pt-14" : "pt-12 pb-10 md:pt-20 md:pb-14"}`}>
      <Reveal className="max-w-3xl">
        {eyebrow && <p className="eyebrow mb-3">{eyebrow}</p>}
        <h1 className="text-[2.4rem] leading-[1.05] md:text-[3.4rem]">{titolo}</h1>
        {lead && <p className="mt-5 max-w-2xl text-[1.1rem] leading-relaxed text-grafite md:text-[1.2rem]">{lead}</p>}
        {children}
      </Reveal>
    </header>
  );
}

export function Sezione({ id, eyebrow, titolo, lead, children, className = "", azione }: { id?: string; eyebrow?: string; titolo?: string; lead?: string; children: ReactNode; className?: string; azione?: { href: string; label: string } }) {
  return (
    <section id={id} className={`contenitore py-12 md:py-16 ${className}`}>
      {(titolo || eyebrow) && (
        <Reveal className="mb-8 flex flex-wrap items-end justify-between gap-4 md:mb-10">
          <div className="max-w-2xl">
            {eyebrow && <p className="eyebrow mb-2">{eyebrow}</p>}
            {titolo && <h2 className="text-[1.9rem] leading-tight md:text-[2.4rem]">{titolo}</h2>}
            {lead && <p className="mt-3 text-[1.05rem] text-grafite">{lead}</p>}
          </div>
          {azione && (
            <Link href={azione.href} className="btn btn-ghost -mr-3">
              {azione.label}
              <Segno nome="freccia" size={18} />
            </Link>
          )}
        </Reveal>
      )}
      {children}
    </section>
  );
}

export function Briciole({ items }: { items: { label: string; href?: string }[] }) {
  return (
    <nav aria-label="Percorso" className="contenitore pt-6 text-sm text-grafite">
      <ol className="flex flex-wrap items-center gap-1.5">
        {items.map((it, i) => (
          <li key={i} className="flex items-center gap-1.5">
            {i > 0 && <span aria-hidden="true" className="text-nebbia">/</span>}
            {it.href ? (
              <Link href={it.href} className="hover:text-petrolio">
                {it.label}
              </Link>
            ) : (
              <span aria-current="page" className="text-inchiostro">
                {it.label}
              </span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}

export function Disclaimer({ testo }: { testo: string }) {
  if (!testo) return null;
  return (
    <p className="mt-10 border-l-2 border-rame/60 pl-4 text-sm text-grafite">{testo}</p>
  );
}

/** Nota sulla lingua quando il corpo EN non esiste ancora. */
export function AvvisoLingua({ show, locale }: { show: boolean; locale: string }) {
  if (!show || locale === "it") return null;
  return (
    <p className="mb-6 inline-flex items-center gap-2 rounded-full bg-pesca px-3 py-1.5 text-sm text-[#8d4a30]">
      <Segno nome="globo" size={16} />
      This page is not yet translated. The Italian text follows.
    </p>
  );
}
