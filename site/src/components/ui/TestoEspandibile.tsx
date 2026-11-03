"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";
import { Segno } from "./Segno";

type Props = {
  children: ReactNode;
  /** Etichetta per aprire (es. "Leggi tutto") */
  more: string;
  /** Etichetta per chiudere (es. "Riduci") */
  less: string;
  /** Modalità: "righe" usa line-clamp su mobile; "blocco" usa max-height con sfumatura sul fondo. */
  modo?: "righe" | "blocco";
  /** Numero di righe visibili su smartphone quando modo="righe" (default 3). */
  righe?: 2 | 3 | 4;
  /** Colore del fondo per la sfumatura in modalità "blocco" ("campo" | "osso" | "bianca"). */
  sfondo?: "campo" | "osso" | "bianca";
  className?: string;
};

/**
 * Rende espandibili i testi lunghi su smartphone (< md).
 * Da tablet/desktop in su (md:) il contenuto resta sempre interamente visibile,
 * e l'intero testo è comunque nel DOM per SEO e accessibilità.
 */
export function TestoEspandibile({
  children,
  more,
  less,
  modo = "righe",
  righe = 3,
  sfondo = "campo",
  className = "",
}: Props) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  // Se l'utente clicca una voce del Sommario (#ancora) che punta dentro questo blocco, apriamo automaticamente.
  useEffect(() => {
    const checkHash = () => {
      const hash = window.location.hash.slice(1);
      if (!hash || !ref.current) return;
      const target = document.getElementById(hash);
      if (target && ref.current.contains(target)) {
        setOpen(true);
      }
    };
    checkHash();
    window.addEventListener("hashchange", checkHash);
    const onClick = (e: MouseEvent) => {
      const a = (e.target as HTMLElement | null)?.closest?.("a[href^='#']") as HTMLAnchorElement | null;
      if (!a || !ref.current) return;
      const id = a.getAttribute("href")?.slice(1);
      if (!id) return;
      const target = document.getElementById(id);
      if (target && ref.current.contains(target)) {
        setOpen(true);
      }
    };
    document.addEventListener("click", onClick);
    return () => {
      window.removeEventListener("hashchange", checkHash);
      document.removeEventListener("click", onClick);
    };
  }, []);

  const clampClass =
    righe === 2
      ? "max-md:[&>*:first-child]:line-clamp-2 max-md:[&>*+*]:hidden"
      : righe === 4
        ? "max-md:[&>*:first-child]:line-clamp-4 max-md:[&>*+*]:hidden"
        : "max-md:[&>*:first-child]:line-clamp-3 max-md:[&>*+*]:hidden";

  const fadeBg =
    sfondo === "bianca" || sfondo === "osso"
      ? "from-osso via-osso/90 to-transparent"
      : "from-campo via-campo/90 to-transparent";

  if (modo === "blocco") {
    return (
      <div ref={ref} className={className}>
        <div
          className={
            open
              ? ""
              : "relative max-md:max-h-[22rem] max-md:overflow-hidden"
          }
        >
          {children}
          {!open && (
            <div
              aria-hidden="true"
              className={`pointer-events-none absolute inset-x-0 bottom-0 hidden h-24 bg-gradient-to-t ${fadeBg} max-md:block`}
            />
          )}
        </div>
        <div className="mt-4 md:hidden">
          <button
            type="button"
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
            className="btn btn-osso !min-h-[2.35rem] !px-4 !py-1.5 text-[0.86rem]"
          >
            <span>{open ? less : more}</span>
            <Segno
              nome="freccia"
              size={15}
              className={`transition-transform duration-300 ${open ? "-rotate-90" : "rotate-90"}`}
            />
          </button>
        </div>
      </div>
    );
  }

  return (
    <div ref={ref} className={className}>
      <div className={open ? "space-y-3.5" : `md:space-y-3.5 ${clampClass}`}>{children}</div>
      <button
        type="button"
        aria-expanded={open}
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          setOpen((v) => !v);
        }}
        className="mt-2 inline-flex items-center gap-1.5 text-[0.86rem] font-semibold text-petrolio hover:text-petrolio-2 md:hidden"
      >
        <span>{open ? less : more}</span>
        <Segno
          nome="freccia"
          size={14}
          className={`transition-transform duration-300 ${open ? "-rotate-90" : "rotate-90"}`}
        />
      </button>
    </div>
  );
}
