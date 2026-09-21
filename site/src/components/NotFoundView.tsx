"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { isLocale, type Locale } from "@/i18n/routing";
import { Segno } from "./ui/Segno";

type Testo = { titolo: string; testo: string; home: string; homeHref: string };

export function NotFoundView({ testi }: { testi: Record<Locale, Testo> }) {
  const seg = (usePathname() ?? "").split("/")[1] ?? "";
  const t = testi[isLocale(seg) ? seg : "it"];
  return (
    <div className="contenitore py-24 text-center">
      <span className="incavo mx-auto grid h-16 w-16 place-items-center text-petrolio">
        <Segno nome="frattura" size={30} />
      </span>
      <h1 className="display-l mt-6">{t.titolo}</h1>
      <p className="mt-3 text-grafite">{t.testo}</p>
      <Link href={t.homeHref} className="btn btn-petrolio mt-8">
        <Segno nome="freccia-sx" size={18} />
        {t.home}
      </Link>
    </div>
  );
}
