"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { usePathname } from "next/navigation";
import type { Locale } from "@/i18n/routing";
import { Segno } from "./ui/Segno";
import { LanguageSwitcher } from "./LanguageSwitcher";

export type NavItem = { label: string; href: string };

export type HeaderProps = {
  locale: Locale;
  homeHref: string;
  nome: string;
  ruolo: string;
  nav: NavItem[];
  tel: { href: string; label: string } | null;
  scrivi: { href: string; label: string };
  a11y: { apriMenu: string; chiudiMenu: string; cambiaLingua: string; salta: string };
};

export function Header({ locale, homeHref, nome, ruolo, nav, tel, scrivi, a11y }: HeaderProps) {
  const [scrolled, setScrolled] = useState(false);
  const pathname = usePathname();
  // Il menu è "aperto per un percorso": cambiando pagina si chiude da solo.
  const [openPath, setOpenPath] = useState<string | null>(null);
  const open = openPath !== null && openPath === pathname;
  const setOpen = (v: boolean | ((prev: boolean) => boolean)) => {
    const next = typeof v === "function" ? v(open) : v;
    setOpenPath(next ? pathname : null);
  };

  useEffect(() => {
    const on = () => setScrolled(window.scrollY > 8);
    on();
    window.addEventListener("scroll", on, { passive: true });
    return () => window.removeEventListener("scroll", on);
  }, []);

  useEffect(() => {
    if (!open) return;
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpenPath(null);
    document.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = "";
    };
  }, [open]);

  const isActive = (href: string) => pathname === href || pathname?.startsWith(href + "/");

  return (
    <>
      <a href="#contenuto" className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[60] focus:rounded-full focus:bg-petrolio focus:px-4 focus:py-2 focus:text-white">
        {a11y.salta}
      </a>
      <header className={`header-vetro sticky top-0 z-50 transition-shadow duration-500 ${scrolled ? "is-scrolled" : ""}`}>
        <div className="contenitore flex h-16 items-center justify-between gap-4 md:h-[4.5rem]">
          <Link href={homeHref} className="group flex min-w-0 items-center gap-3" aria-label={nome}>
            <span className="incavo grid h-10 w-10 shrink-0 place-items-center text-petrolio transition group-hover:text-petrolio-2">
              <Segno nome="spalla" size={22} />
            </span>
            <span className="min-w-0 leading-tight">
              <span className="serif block truncate text-[1.05rem] text-inchiostro">{nome}</span>
              <span className="hidden truncate text-[0.72rem] font-medium tracking-wide text-grafite sm:block">{ruolo}</span>
            </span>
          </Link>

          <nav className="hidden items-center gap-1 lg:flex" aria-label="Principale">
            {nav.map((n) => (
              <Link
                key={n.href}
                href={n.href}
                aria-current={isActive(n.href) ? "page" : undefined}
                className={`rounded-full px-3.5 py-2 text-[0.9rem] font-medium transition ${
                  isActive(n.href) ? "bg-osso text-petrolio shadow-[inset_0_1px_0_#fff,0_1px_2px_rgba(26,30,34,.06)]" : "text-inchiostro/80 hover:bg-osso/70 hover:text-inchiostro"
                }`}
              >
                {n.label}
              </Link>
            ))}
          </nav>

          <div className="flex items-center gap-2">
            <div className="hidden md:block">
              <LanguageSwitcher locale={locale} label={a11y.cambiaLingua} />
            </div>
            {tel && (
              <a href={tel.href} className="btn btn-petrolio hidden sm:inline-flex">
                <Segno nome="telefono" size={18} />
                {tel.label}
              </a>
            )}
            <Link href={scrivi.href} className={`btn ${tel ? "btn-osso" : "btn-petrolio"} hidden sm:inline-flex`}>
              <Segno nome="mail" size={18} />
              {scrivi.label}
            </Link>
            <button
              type="button"
              className="btn btn-osso !px-3 lg:hidden"
              aria-expanded={open}
              aria-controls="menu-mobile"
              aria-label={open ? a11y.chiudiMenu : a11y.apriMenu}
              onClick={() => setOpen((v) => !v)}
            >
              <Segno nome={open ? "x" : "menu"} size={20} />
            </button>
          </div>
        </div>

        {/* Menu mobile: lastra ossea che scende */}
        <div
          id="menu-mobile"
          hidden={!open}
          className="lg:hidden"
        >
          <div className="contenitore pb-5">
            <div className="osso osso-lg p-5">
              <nav className="flex flex-col" aria-label="Principale (mobile)">
                {nav.map((n) => (
                  <Link
                    key={n.href}
                    href={n.href}
                    aria-current={isActive(n.href) ? "page" : undefined}
                    className={`serif flex items-center justify-between border-b border-linea py-3.5 text-[1.35rem] last:border-0 ${isActive(n.href) ? "text-petrolio" : "text-inchiostro"}`}
                  >
                    {n.label}
                    <Segno nome="freccia" size={18} className="text-nebbia" />
                  </Link>
                ))}
              </nav>
              <div className="mt-5 flex flex-wrap items-center gap-2">
                {tel && (
                  <a href={tel.href} className="btn btn-petrolio">
                    <Segno nome="telefono" size={18} />
                    {tel.label}
                  </a>
                )}
                <Link href={scrivi.href} className={`btn ${tel ? "btn-osso" : "btn-petrolio"}`}>
                  <Segno nome="mail" size={18} />
                  {scrivi.label}
                </Link>
                <div className="ml-auto">
                  <LanguageSwitcher locale={locale} label={a11y.cambiaLingua} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
    </>
  );
}
