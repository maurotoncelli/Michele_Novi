import Link from "next/link";
import Image from "next/image";
import type { CSSProperties, ReactNode } from "react";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick, formatDate } from "@/i18n";
import { getDisegni, getSedi, idDisegnoDaTag, slugNota, slugPatologia, srcDisegno, type Nota, type Patologia, type Pubblicazione, type Sede } from "@/lib/content";
import { hrefArticolo, srcMedia, srcPaper } from "@/lib/media";
import { Disegno } from "../ui/Disegno";
import { isSegno, Segno } from "../ui/Segno";

/** Superficie media delle lastre: stesso stampo, hover a crop lento. */
function Lastra({
  ratio = "4/3",
  className = "",
  children,
}: {
  ratio?: "4/3" | "5/4" | "4/5";
  className?: string;
  children: ReactNode;
}) {
  const forma = ratio === "5/4" ? "aspect-[5/4]" : ratio === "4/5" ? "aspect-[4/5]" : "aspect-[4/3]";
  return (
    <div className={`relative overflow-hidden bg-osso-2 ${forma} ${className}`}>
      <div className="absolute inset-0 origin-center transition-transform duration-700 ease-osso group-hover:scale-[1.035] motion-reduce:transform-none motion-reduce:transition-none">
        {children}
      </div>
    </div>
  );
}

function ChipSede({ s, locale }: { s: Sede; locale: Locale }) {
  const m = getMessages(locale);
  return (
    <span className="mt-auto flex min-h-8 flex-wrap content-start gap-1.5 pt-3">
      {s.visite && <span className="tag tag-petrolio">{m.dove.visite}</span>}
      {s.chirurgia && <span className="tag">{m.dove.chirurgia}</span>}
    </span>
  );
}

/** Card patologia. Default: 5/4 compatta (correlate). `riga` = disegno piccolo a sinistra, lead intero. `colonna` = colonna alta con disegno che fluttua. */
export async function SchedaPatologia({ p, locale, index, riga = false, colonna = false }: { p: Patologia; locale: Locale; index?: number; riga?: boolean; colonna?: boolean }) {
  const m = getMessages(locale);
  const segno = isSegno(p.segno) ? p.segno : "spalla";
  const catalogo = await getDisegni();
  const disegno = p.immagine?.src
    ? { src: p.immagine.src, alt: pick(p.immagine.alt, locale) || pick(p.titolo, locale) }
    : srcDisegno(catalogo, segno, locale);
  const media = disegno ? (
    <Disegno src={disegno.src} alt={disegno.alt} />
  ) : (
    <span className="absolute inset-0 grid place-items-center text-petrolio">
      <Segno nome={segno} size={40} />
    </span>
  );

  if (riga) {
    const tutte = await getSedi();
    const dove = (p.sedi ?? []).map((slug) => tutte.find((s) => s.slug === slug)?.citta).filter((c): c is string => !!c);
    return (
      <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group grid h-full grid-cols-[minmax(0,7.5rem)_minmax(0,1fr)] gap-5 sm:grid-cols-[minmax(0,10rem)_minmax(0,1fr)] sm:gap-6 lg:grid-cols-[minmax(0,12rem)_minmax(0,1fr)] lg:gap-7">
        <Lastra ratio="4/3" className="self-start">{media}</Lastra>
        <div className="flex min-w-0 flex-col">
          <h3 className="text-[1.3rem] leading-tight group-hover:text-petrolio md:text-[1.45rem]">{pick(p.titolo, locale)}</h3>
          <p className="mt-2 text-[0.95rem] leading-relaxed text-grafite">{pick(p.lead, locale)}</p>
          {dove.length > 0 && <p className="mt-auto pt-3 text-[0.8rem] text-grafite">{dove.join(" · ")}</p>}
          <span className="sr-only">{m.cta.scopri}</span>
        </div>
      </Link>
    );
  }

  if (colonna) {
    // Tre colonne alte: il disegno fluttua allo scroll, la freccia arriva all'hover.
    const tutte = await getSedi();
    const dove = (p.sedi ?? []).map((slug) => tutte.find((s) => s.slug === slug)?.citta).filter((c): c is string => !!c);
    const velocita = [["9%", "-9%"], ["5%", "-5%"], ["12%", "-12%"]][(index ?? 0) % 3] as [string, string];
    return (
      <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group flex h-full flex-col">
        <Lastra ratio="4/5" className="w-full transition-colors duration-700 ease-osso group-hover:bg-petrolio-3">
          <div className="fluttua absolute inset-0" style={{ "--fluttua-da": velocita[0], "--fluttua-a": velocita[1] } as CSSProperties}>
            {media}
          </div>
        </Lastra>
        <div className="flex flex-1 flex-col pt-6">
          {index !== undefined && <p className="eyebrow">{String(index + 1).padStart(2, "0")}</p>}
          <h3 className="mt-2 text-[1.6rem] leading-tight transition-colors duration-500 group-hover:text-petrolio md:text-[1.9rem]">{pick(p.titolo, locale)}</h3>
          <p className="mt-3 text-[0.98rem] leading-relaxed text-grafite">{pick(p.lead, locale)}</p>
          <div className="mt-auto flex items-end justify-between gap-4 pt-5">
            {dove.length > 0 ? <p className="text-[0.8rem] text-grafite">{dove.join(" · ")}</p> : <span />}
            <span className="inline-flex shrink-0 items-center gap-1.5 text-[0.85rem] font-medium text-petrolio">
              {m.cta.scopri}
              <Segno nome="freccia" size={16} className="transition-transform duration-500 ease-osso group-hover:translate-x-1" />
            </span>
          </div>
        </div>
      </Link>
    );
  }

  return (
    <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group flex h-full flex-col">
      <Lastra ratio="5/4" className="mb-5 w-full">
        {media}
      </Lastra>
      <div className="flex flex-1 flex-col">
        <h3 className="line-clamp-2 min-h-[2.55em] text-[1.28rem] leading-tight group-hover:text-petrolio">{pick(p.titolo, locale)}</h3>
        <p className="mt-2 line-clamp-3 min-h-[4.5em] text-[0.92rem] leading-relaxed text-grafite">{pick(p.lead, locale)}</p>
        <span className="sr-only">{m.cta.scopri}</span>
      </div>
    </Link>
  );
}

/** Il metodo (Come si opera): non una patologia, uno spazio a sé. Disegno largo a sinistra, testo a destra. */
export async function SchedaMetodo({ p, locale }: { p: Patologia; locale: Locale }) {
  const m = getMessages(locale);
  const segno = isSegno(p.segno) ? p.segno : "artroscopia";
  const catalogo = await getDisegni();
  const disegno = p.immagine?.src
    ? { src: p.immagine.src, alt: pick(p.immagine.alt, locale) || pick(p.titolo, locale) }
    : srcDisegno(catalogo, segno, locale);
  return (
    <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group grid items-center gap-10 md:grid-cols-[minmax(0,1fr)_minmax(0,1fr)] md:gap-16 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)] lg:gap-24">
      <Lastra ratio="5/4" className="w-full transition-colors duration-700 ease-osso group-hover:bg-petrolio-3">
        <div className="fluttua absolute inset-0" style={{ "--fluttua-da": "6%", "--fluttua-a": "-6%" } as CSSProperties}>
          {disegno ? (
            <Disegno src={disegno.src} alt={disegno.alt} />
          ) : (
            <span className="absolute inset-0 grid place-items-center text-petrolio">
              <Segno nome={segno} size={56} />
            </span>
          )}
        </div>
      </Lastra>
      <div className="min-w-0">
        <p className="eyebrow">{m.cosaCuro.metodoEyebrow}</p>
        <h3 className="display-m mt-4 transition-colors duration-500 group-hover:text-petrolio">{pick(p.titolo, locale)}</h3>
        <p className="lead mt-5 max-w-xl">{pick(p.lead, locale)}</p>
        <p className="mt-4 max-w-xl text-[0.98rem] leading-relaxed text-grafite">{m.cosaCuro.metodoLead}</p>
        <span className="btn btn-ghost -ml-3 mt-6">
          {m.cta.scopri}
          <Segno nome="freccia" size={18} />
        </span>
      </div>
    </Link>
  );
}

/** Sede in home: città in evidenza, stesso 4/3 delle lastre hub. Foto se c’è, altrimenti disegno. `grande` = città in display; `compatto` = riga con miniatura. */
export async function ModuloSede({ s, locale, grande = false, compatto = false }: { s: Sede; locale: Locale; grande?: boolean; compatto?: boolean }) {
  const m = getMessages(locale);
  const catalogo = await getDisegni();
  const segno = s.tipo === "ospedale" ? "ospedale" : s.tipo === "studio" ? "studio" : "clinica";
  const disegno = srcDisegno(catalogo, segno, locale);
  const foto = s.foto?.[0];
  const fotoSrc = srcMedia(foto?.src, "sedi");
  const media = fotoSrc ? (
    <Image src={fotoSrc} alt={pick(foto?.alt, locale) || s.nome} fill sizes={compatto ? "8rem" : "(min-width: 1024px) 25vw, (min-width: 640px) 50vw, 100vw"} className="object-cover" />
  ) : disegno ? (
    <Disegno src={disegno.src} alt={disegno.alt} />
  ) : (
    <span className="absolute inset-0 grid place-items-center text-petrolio">
      <Segno nome={segno} size={28} />
    </span>
  );

  if (compatto) {
    return (
      <Link href={href(locale, { kind: "dove", slug: s.slug })} className="group grid grid-cols-[5.5rem_minmax(0,1fr)] items-center gap-4 py-3">
        <Lastra className="rounded-sm">{media}</Lastra>
        <span className="min-w-0">
          <span className="block text-[1.05rem] font-medium leading-tight group-hover:text-petrolio">{s.citta}</span>
          <span className="mt-0.5 block truncate text-[0.85rem] text-grafite">{s.nome}</span>
          <span className="mt-1 block text-[0.75rem] text-nebbia">
            {[s.visite && m.dove.visite, s.chirurgia && m.dove.chirurgia].filter(Boolean).join(" · ")}
          </span>
        </span>
      </Link>
    );
  }

  return (
    <Link href={href(locale, { kind: "dove", slug: s.slug })} className="group flex h-full flex-col">
      <Lastra>{media}</Lastra>
      <span className={`flex flex-1 flex-col ${grande ? "mt-5" : "mt-4"}`}>
        <span className={`serif block leading-tight group-hover:text-petrolio ${grande ? "line-clamp-2 text-[1.9rem] md:text-[2.2rem]" : "line-clamp-2 min-h-[2.4em] text-[1.35rem]"}`}>{s.citta}</span>
        <span className={`line-clamp-1 block leading-snug text-grafite ${grande ? "mt-2 text-[0.95rem]" : "mt-1 text-[0.85rem]"}`}>{s.nome}</span>
        <ChipSede s={s} locale={locale} />
      </span>
    </Link>
  );
}

/** Scheda sede (hub Dove): riga compatta, foto a sinistra, tutto leggibile in una schermata. */
export async function SchedaSede({ s, locale }: { s: Sede; locale: Locale }) {
  const m = getMessages(locale);
  const foto = s.foto?.[0];
  const fotoSrc = srcMedia(foto?.src, "sedi");
  const catalogo = await getDisegni();
  const segno = s.tipo === "ospedale" ? "ospedale" : s.tipo === "studio" ? "studio" : "clinica";
  const disegno = srcDisegno(catalogo, segno, locale);
  const regime = pick(s.regime, locale);
  return (
    <Link href={href(locale, { kind: "dove", slug: s.slug })} className="group grid h-full grid-cols-[minmax(0,7.5rem)_minmax(0,1fr)] gap-5 sm:grid-cols-[minmax(0,10rem)_minmax(0,1fr)] sm:gap-6 lg:grid-cols-[minmax(0,12rem)_minmax(0,1fr)] lg:gap-7">
      <Lastra className="self-start">
        {fotoSrc ? (
          <Image src={fotoSrc} alt={pick(foto?.alt, locale) || s.nome} fill sizes="10rem" className="object-cover" />
        ) : disegno ? (
          <Disegno src={disegno.src} alt={disegno.alt} />
        ) : (
          <span className="absolute inset-0 grid place-items-center text-nebbia">
            <Segno nome={segno} size={40} />
          </span>
        )}
      </Lastra>
      <div className="flex min-w-0 flex-col">
        <p className="eyebrow">
          {s.citta}
          {s.provincia ? ` (${s.provincia})` : ""}
        </p>
        <h3 className="mt-1 text-[1.3rem] leading-tight group-hover:text-petrolio md:text-[1.45rem]">{s.nome}</h3>
        <p className="mt-1.5 text-sm text-grafite">
          {s.indirizzo}
          {s.cap ? `, ${s.cap}` : ""}
        </p>
        {regime && <p className="mt-1 text-sm text-grafite">{regime}</p>}
        <p className="mt-auto pt-3 text-[0.78rem] text-nebbia">
          {[s.visite && m.dove.visite, s.chirurgia && m.dove.chirurgia, s.infiltrazioni && m.dove.infiltrazioni, s.ecografo && m.dove.ecografo]
            .filter(Boolean)
            .join(" · ")}
        </p>
      </div>
    </Link>
  );
}

/** Pubblicazione: stesso 4/3, meta su una riga. */
export async function SchedaPaper({ p, locale, grande = false }: { p: Pubblicazione; locale: Locale; grande?: boolean }) {
  const m = getMessages(locale);
  const titolo = pick(p.titoloBreve, locale) || p.titolo;
  const catalogo = await getDisegni();
  const id = idDisegnoDaTag(p.tag, p.patologie);
  const disegno = srcDisegno(catalogo, id, locale);
  const pdf = srcPaper(p.pdf);
  const articolo = hrefArticolo(p.doi, p.url);
  return (
    <div className="flex h-full flex-col">
      <Link href={href(locale, { kind: "paper", slug: p.slug })} className="group flex flex-1 flex-col">
        <Lastra>
          {disegno ? (
            <Disegno src={disegno.src} alt={disegno.alt} />
          ) : (
            <span className="absolute inset-0 grid place-items-center text-petrolio">
              <Segno nome="doc" size={36} />
            </span>
          )}
        </Lastra>
        <div className="flex flex-1 flex-col pt-5">
          <div className="flex items-center justify-between gap-3">
            <span className="tag tag-petrolio">{m.approfondimenti.paper}</span>
            <span className="text-sm text-grafite">{p.anno}</span>
          </div>
          <h3 className={`leading-snug group-hover:text-petrolio ${grande ? "mt-4 text-[1.6rem] leading-tight md:text-[1.95rem]" : "mt-3 line-clamp-3 min-h-[3.6em] text-[1.3rem]"}`}>{titolo}</h3>
          {titolo !== p.titolo && <p className="mt-1 line-clamp-2 text-sm italic text-grafite">{p.titolo}</p>}
          <p className="mt-3 line-clamp-1 text-sm text-grafite">
            {p.rivista}
            {p.autori ? ` · ${p.autori.split(",")[0]} et al.` : ""}
          </p>
        </div>
      </Link>
      {pdf ? (
        <div className="mt-4">
          <a href={pdf} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
            <Segno nome="doc" size={16} />
            {m.cta.pdf}
          </a>
        </div>
      ) : articolo ? (
        <div className="mt-4">
          <a href={articolo} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
            {m.cta.articolo}
            <Segno nome="esterno" size={16} />
          </a>
        </div>
      ) : null}
    </div>
  );
}

/** Nota / approfondimento: copertina Keystatic, o disegno. */
export async function SchedaNota({ n, locale, grande = false }: { n: Nota; locale: Locale; grande?: boolean }) {
  const m = getMessages(locale);
  const copertina = srcMedia(n.copertina?.src, "approfondimenti");
  const alt = pick(n.copertina?.alt, locale) || pick(n.titolo, locale);
  const catalogo = await getDisegni();
  const fallback = srcDisegno(catalogo, idDisegnoDaTag(n.tag), locale);
  return (
    <Link href={href(locale, { kind: "nota", slug: slugNota(n, locale) })} className="group flex h-full flex-col">
      <Lastra>
        {copertina ? (
          <Image src={copertina} alt={alt} fill sizes="(min-width: 768px) 33vw, 100vw" className="object-cover" />
        ) : fallback ? (
          <Disegno src={fallback.src} alt={alt} />
        ) : (
          <Image src="/images/disegni/approfondimenti.png" alt={alt} fill sizes="(min-width: 768px) 33vw, 100vw" className="object-contain p-8" />
        )}
      </Lastra>
      <div className="flex flex-1 flex-col pt-5">
        <div className="flex items-center justify-between gap-3">
          <span className="tag tag-rame">{m.approfondimenti.nota}</span>
          <time dateTime={n.data ?? undefined} className="text-sm text-grafite">
            {formatDate(n.data, locale)}
          </time>
        </div>
        <h3 className={`leading-snug group-hover:text-petrolio ${grande ? "mt-4 text-[1.6rem] leading-tight md:text-[1.95rem]" : "mt-3 line-clamp-3 min-h-[3.6em] text-[1.3rem]"}`}>{pick(n.titolo, locale)}</h3>
        <p className={`text-grafite ${grande ? "mt-3 max-w-xl text-[1.05rem] leading-relaxed" : "mt-2 line-clamp-3 min-h-[4.4em] text-[0.95rem]"}`}>{pick(n.lead, locale)}</p>
      </div>
    </Link>
  );
}
