import Link from "next/link";
import type { ReactNode } from "react";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";

/** Intestazione di pagina: eyebrow, H1, lead. Una sola per pagina. */
export function Intestazione({
  eyebrow,
  titolo,
  lead,
  children,
  compatta = false,
  percorso,
}: {
  eyebrow?: string;
  titolo: string;
  lead?: string;
  children?: ReactNode;
  compatta?: boolean;
  percorso?: { label: string; href?: string }[];
}) {
  return (
    <header className="bg-osso-3">
      {percorso && percorso.length > 0 ? <Briciole items={percorso} dentro /> : null}
      <div className={`contenitore ${compatta ? "pb-10 md:pb-14" : "pb-12 md:pb-20"} ${percorso?.length ? "pt-6 md:pt-10" : compatta ? "pt-10 md:pt-14" : "pt-12 md:pt-20"}`}>
        <Reveal immediate className="max-w-4xl">
          {eyebrow && <p className="eyebrow mb-4">{eyebrow}</p>}
          <h1 className="display-l">{titolo}</h1>
          {lead && <p className="lead mt-6 max-w-2xl">{lead}</p>}
          {children}
        </Reveal>
      </div>
    </header>
  );
}

/**
 * Fascia. Tre misure, alternate lungo la pagina:
 * - griglia: titolo display-m, il corpo del sito (schede);
 * - affermazione: una frase in display-l, molto vuoto, un'azione;
 * - varco: come affermazione, ma il contenuto è un solo oggetto grande.
 * `indice` ("01") dà l'ordine di lettura in home.
 */
export function Sezione({
  id,
  eyebrow,
  indice,
  titolo,
  lead,
  children,
  className = "",
  azione,
  tinta,
  misura = "griglia",
}: {
  id?: string;
  eyebrow?: string;
  indice?: string;
  titolo?: string;
  lead?: string;
  children?: ReactNode;
  className?: string;
  azione?: { href: string; label: string };
  tinta?: "campo" | "osso";
  misura?: "griglia" | "affermazione" | "varco";
}) {
  const grande = misura !== "griglia";
  const passo = grande ? "py-20 md:py-32" : "py-16 md:py-24";
  const sotto = children ? (grande ? "mb-14 md:mb-20" : "mb-10 md:mb-14") : "";
  return (
    <section id={id} className={tinta === "osso" ? "bg-osso-3 trama" : undefined}>
      <div className={`contenitore ${passo} ${className}`}>
        {(titolo || eyebrow) && (
          <div className={`${sotto} grid gap-x-10 gap-y-6 ${grande ? "lg:grid-cols-[minmax(0,1fr)_auto] lg:items-end" : "md:grid-cols-[minmax(0,1fr)_auto] md:items-end"}`}>
            <div className={grande ? "max-w-4xl" : "max-w-3xl"}>
              {eyebrow && (
                <Reveal as="p" className="eyebrow mb-4">
                  {indice && <span className="indice">{indice}</span>}
                  {eyebrow}
                </Reveal>
              )}
              {titolo && (
                <Reveal as="h2" maschera className={grande ? "display-l" : "display-m"}>
                  {titolo}
                </Reveal>
              )}
              {lead && (
                <Reveal as="p" delay={120} className={`${grande ? "lead mt-6 max-w-2xl" : "mt-4 max-w-2xl text-[1.05rem] leading-relaxed text-grafite md:text-[1.12rem]"}`}>
                  {lead}
                </Reveal>
              )}
            </div>
            {azione && (
              <Reveal delay={160} className="justify-self-start md:justify-self-end">
                <Link href={azione.href} className="btn btn-ghost -ml-3 md:-mr-3 md:ml-0">
                  {azione.label}
                  <Segno nome="freccia" size={18} />
                </Link>
              </Reveal>
            )}
          </div>
        )}
        {children}
      </div>
    </section>
  );
}

export function Briciole({ items, dentro = false }: { items: { label: string; href?: string }[]; dentro?: boolean }) {
  return (
    <nav aria-label="Percorso" className={`contenitore text-sm text-grafite ${dentro ? "pt-5" : "pt-6"}`}>
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
