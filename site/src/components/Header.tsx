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
  const pathname = usePathname();
  const [openPath, setOpenPath] = useState<string | null>(null);
  const open = openPath !== null && openPath === pathname;
  const setOpen = (v: boolean | ((prev: boolean) => boolean)) => {
    const next = typeof v === "function" ? v(open) : v;
    setOpenPath(next ? pathname : null);
  };

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

  const isActive = (href: string) => {
    if (!pathname) return false;
    const hit = pathname === href || pathname.startsWith(`${href}/`);
    if (!hit) return false;
    return !nav.some(
      (n) =>
        n.href !== href &&
        n.href.length > href.length &&
        (pathname === n.href || pathname.startsWith(`${n.href}/`)),
    );
  };

  const voce = (n: NavItem, grande = false) => (
    <Link
      key={n.href}
      href={n.href}
      aria-current={isActive(n.href) ? "page" : undefined}
      className={
        grande
          ? `flex items-center justify-between border-b border-linea py-4 text-[1.45rem] last:border-0 ${isActive(n.href) ? "text-petrolio" : "text-inchiostro"}`
          : `relative whitespace-nowrap py-3.5 text-[0.8rem] tracking-[0.02em] transition xl:text-[0.92rem] ${
              isActive(n.href)
                ? "text-petrolio after:absolute after:inset-x-0 after:bottom-0 after:h-px after:bg-petrolio"
                : "text-inchiostro/70 hover:text-inchiostro"
            }`
      }
    >
      {n.label}
      {grande && <Segno nome="freccia" size={18} className="text-nebbia" />}
    </Link>
  );

  return (
    <>
      <a href="#contenuto" className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[60] focus:rounded-full focus:bg-petrolio focus:px-4 focus:py-2 focus:text-white">
        {a11y.salta}
      </a>
      <header className="header-solido sticky top-0 z-50">
        <div className="contenitore flex min-h-[4.5rem] items-center gap-4 md:min-h-[5.25rem] lg:gap-6 xl:gap-10">
          <Link href={homeHref} className="group flex min-w-0 shrink-0 items-center gap-2.5 xl:gap-3" aria-label={nome}>
            <span className="grid h-9 w-9 shrink-0 place-items-center border border-linea text-petrolio md:h-10 md:w-10">
              <Segno nome="spalla" size={18} />
            </span>
            <span className="min-w-0 leading-tight">
              <span className="serif block truncate text-[1.05rem] text-inchiostro md:text-[1.15rem] xl:text-[1.25rem]">{nome}</span>
              <span className="mt-0.5 hidden truncate text-[0.68rem] font-medium tracking-[0.08em] text-grafite uppercase sm:block lg:hidden">{ruolo}</span>
            </span>
          </Link>

          <nav className="hidden min-w-0 flex-1 items-center justify-center gap-x-3.5 xl:gap-x-7 lg:flex" aria-label="Principale">
            {nav.map((n) => voce(n))}
          </nav>

          <div className="ml-auto flex shrink-0 items-center justify-end gap-2 xl:gap-3 lg:ml-0">
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

        <div id="menu-mobile" hidden={!open} className="lg:hidden">
          <div className="contenitore border-t border-linea pb-8 pt-2">
            <nav className="flex flex-col" aria-label="Principale (mobile)">
              {nav.map((n) => voce(n, true))}
            </nav>
            <div className="mt-6 flex flex-wrap items-center gap-2">
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
      </header>
    </>
  );
}
