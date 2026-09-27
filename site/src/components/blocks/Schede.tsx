import Link from "next/link";
import Image from "next/image";
import type { CSSProperties, ReactNode } from "react";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick, formatDate } from "@/i18n";
import { getDisegni, getSedi, idDisegnoDaTag, slugNota, slugPatologia, srcDisegno, type Nota, type Patologia, type Sede } from "@/lib/content";
import { srcMedia } from "@/lib/media";
import { Disegno } from "../ui/Disegno";
import { IconaTecnica, isTecnica } from "../ui/IconaTecnica";
import { isSegno, Segno } from "../ui/Segno";

/** Superficie media delle lastre: stesso stampo, hover a crop lento. */
function Lastra({
  ratio = "4/3",
  className = "",
  children,
}: {
  ratio?: "4/3" | "5/4" | "4/5" | "3/2" | "16/9";
  className?: string;
  children: ReactNode;
}) {
  const forma = ratio === "5/4" ? "aspect-[5/4]" : ratio === "4/5" ? "aspect-[4/5]" : ratio === "3/2" ? "aspect-[3/2]" : ratio === "16/9" ? "aspect-[16/9]" : "aspect-[4/3]";
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

/** Riga di credito sotto le card: numero di pubblicazioni e città in cui si tratta. */
function credito(p: Patologia, dove: string[], locale: Locale) {
  const m = getMessages(locale);
  const n = p.pubblicazioni?.length ?? 0;
  const paper = n === 1 ? m.cosaCuro.pubblicazioniUna : n > 1 ? m.cosaCuro.pubblicazioniN.replace("{n}", String(n)) : "";
  return [paper, ...dove].filter(Boolean).join(" · ");
}

/** Punto di fuoco delle foto verticali quando la lastra le taglia in orizzontale. */
const fuoco: Record<string, string> = {
  "spalla-atleta": "object-[center_12%]",
  "gomito-atleta": "object-[center_45%]",
  "ginocchio-atleta": "object-[center_55%]",
  "sport-volo": "object-[center_50%]",
};
function classeFuoco(src: string) {
  const chiave = Object.keys(fuoco).find((k) => src.includes(k));
  return chiave ? fuoco[chiave] : "object-center";
}

/** In home, all'hover la scheda si accende con la tinta della fascia dello sport: il fondo sporge oltre i bordi senza spostare il layout. */
const accesa =
  "relative isolate before:absolute before:-inset-3 before:-z-10 before:bg-petrolio-3/70 before:opacity-0 before:transition-opacity before:duration-500 before:ease-osso hover:before:opacity-100 md:before:-inset-4";

/** Card patologia. Default: 5/4 compatta (correlate). `riga` = in home, accanto alla spalla: foto 5/4 a sinistra, lead intero; con `alta`, da desktop la foto si allunga a tutta l'altezza della riga. `colonna` = in home, le aree dopo la spalla affiancate alla pari (foto sopra). `ampia` = foto a sinistra, larga una colonna della griglia a tre come le schede `colonna`, testo a destra. `apertura` = in home, la spalla grande (foto 3/2, titolo sotto) accanto alle altre aree. `fascia` = in home, un'area a tutta larghezza e bassa: foto 16/9 a sinistra, testo a destra. */
export async function SchedaPatologia({ p, locale, index, riga = false, alta = false, colonna = false, ampia = false, apertura = false, fascia = false }: { p: Patologia; locale: Locale; index?: number; riga?: boolean; alta?: boolean; colonna?: boolean; ampia?: boolean; apertura?: boolean; fascia?: boolean }) {
  const m = getMessages(locale);
  const segno = isSegno(p.segno) ? p.segno : "spalla";
  const catalogo = await getDisegni();
  const foto = srcMedia(p.immagine?.src, "patologie");
  const disegno = foto ? null : srcDisegno(catalogo, segno, locale);
  const alt = pick(p.immagine?.alt, locale) || pick(p.titolo, locale);
  const media = foto ? (
    <Image src={foto} alt={alt} fill quality={92} sizes="(min-width: 1024px) 30vw, (min-width: 640px) 45vw, 92vw" className={`object-cover ${classeFuoco(foto)}`} />
  ) : disegno ? (
    <Disegno src={disegno.src} alt={disegno.alt || alt} />
  ) : (
    <span className="absolute inset-0 grid place-items-center text-petrolio">
      <Segno nome={segno} size={40} />
    </span>
  );

  if (riga) {
    const tutte = await getSedi();
    const dove = (p.sedi ?? []).map((slug) => tutte.find((s) => s.slug === slug)?.citta).filter((c): c is string => !!c);
    return (
      <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className={`group ${accesa} grid grid-cols-[minmax(0,8.5rem)_minmax(0,1fr)] gap-5 sm:grid-cols-[minmax(0,12rem)_minmax(0,1fr)] sm:gap-6 lg:grid-cols-[minmax(0,11rem)_minmax(0,1fr)] xl:grid-cols-[minmax(0,15rem)_minmax(0,1fr)] ${alta ? "lg:flex-1" : ""}`}>
        <Lastra ratio="5/4" className={`self-start ${alta ? "lg:aspect-auto lg:self-stretch" : ""}`}>{media}</Lastra>
        <div className="flex min-w-0 flex-col">
          <h3 className="text-[1.3rem] leading-tight group-hover:text-petrolio md:text-[1.45rem]">{pick(p.titolo, locale)}</h3>
          <p className="mt-2 text-[0.95rem] leading-relaxed text-grafite">{pick(p.lead, locale)}</p>
          {credito(p, dove, locale) && <p className="mt-auto pt-3 text-[0.8rem] text-grafite">{credito(p, dove, locale)}</p>}
          <span className="sr-only">{m.cta.scopri}</span>
        </div>
      </Link>
    );
  }

  if (fascia) {
    const tutte = await getSedi();
    const dove = (p.sedi ?? []).map((slug) => tutte.find((s) => s.slug === slug)?.citta).filter((c): c is string => !!c);
    return (
      <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group grid items-center gap-5 bg-petrolio-3/70 p-4 transition-colors duration-500 ease-osso hover:bg-petrolio-3 sm:grid-cols-[minmax(0,18rem)_minmax(0,1fr)] sm:gap-6 md:p-5 lg:grid-cols-[minmax(0,30rem)_minmax(0,1fr)] lg:gap-10">
        <Lastra ratio="3/2" className="w-full">
          {media}
        </Lastra>
        <div className="min-w-0">
          <h3 className="text-[1.3rem] leading-tight transition-colors duration-500 group-hover:text-petrolio md:text-[1.45rem]">{pick(p.titolo, locale)}</h3>
          <p className="mt-2 max-w-2xl text-[0.95rem] leading-relaxed text-grafite">{pick(p.lead, locale)}</p>
          <div className="mt-3 flex flex-wrap items-center justify-between gap-x-6 gap-y-2">
            {credito(p, dove, locale) ? <p className="text-[0.8rem] text-grafite">{credito(p, dove, locale)}</p> : <span />}
            <span className="inline-flex shrink-0 items-center gap-1.5 text-[0.85rem] font-medium text-petrolio">
              {m.cta.scopri}
              <Segno nome="freccia" size={16} className="transition-transform duration-500 ease-osso group-hover:translate-x-1" />
            </span>
          </div>
        </div>
      </Link>
    );
  }

  if (apertura) {
    const tutte = await getSedi();
    const dove = (p.sedi ?? []).map((slug) => tutte.find((s) => s.slug === slug)?.citta).filter((c): c is string => !!c);
    return (
      <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className={`group ${accesa} flex h-full flex-col lg:row-span-2 lg:grid lg:grid-rows-subgrid`}>
        <Lastra ratio="3/2" className="w-full transition-colors duration-700 ease-osso group-hover:bg-petrolio-3">
          {foto ? (
            <Image src={foto} alt={alt} fill quality={92} sizes="(min-width: 1024px) 40rem, 100vw" className={`object-cover ${classeFuoco(foto)}`} />
          ) : (
            media
          )}
        </Lastra>
        <div className="mt-6 flex min-w-0 flex-wrap items-end justify-between gap-x-8 gap-y-3">
          <div className="min-w-0 max-w-xl">
            <h2 className="display-m transition-colors duration-500 group-hover:text-petrolio">{m.home.cosaCuroTitolo}</h2>
            <p className="mt-3 text-[1.05rem] leading-relaxed text-grafite md:text-[1.12rem]">{pick(p.lead, locale)}</p>
            {dove.length > 0 && <p className="mt-3 text-[0.8rem] text-grafite">{dove.join(" · ")}</p>}
          </div>
          <span className="btn btn-ghost -ml-3 md:-mr-3 md:ml-0">
            {m.cta.scopri}
            <Segno nome="freccia" size={18} />
          </span>
        </div>
      </Link>
    );
  }

  if (ampia) {
    const tutte = await getSedi();
    const dove = (p.sedi ?? []).map((slug) => tutte.find((s) => s.slug === slug)?.citta).filter((c): c is string => !!c);
    return (
      <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group grid items-center gap-6 sm:grid-cols-2 sm:gap-x-8 lg:grid-cols-3">
        <Lastra ratio="5/4" className="w-full transition-colors duration-700 ease-osso group-hover:bg-petrolio-3">
          {media}
        </Lastra>
        <div className="min-w-0 lg:col-span-2">
          <h3 className="sr-only">{pick(p.titolo, locale)}</h3>
          <p className="lead max-w-xl">{pick(p.lead, locale)}</p>
          {credito(p, dove, locale) && <p className="mt-5 text-[0.8rem] text-grafite">{credito(p, dove, locale)}</p>}
          <span className="btn btn-ghost -ml-3 mt-6">
            {m.cta.scopri}
            <Segno nome="freccia" size={18} />
          </span>
        </div>
      </Link>
    );
  }

  if (colonna) {
    // Senza foto il disegno fluttua allo scroll; la freccia arriva all'hover.
    const tutte = await getSedi();
    const dove = (p.sedi ?? []).map((slug) => tutte.find((s) => s.slug === slug)?.citta).filter((c): c is string => !!c);
    const velocita = [["9%", "-9%"], ["5%", "-5%"], ["12%", "-12%"]][(index ?? 0) % 3] as [string, string];
    return (
      <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group flex h-full flex-col">
        <Lastra ratio="5/4" className="w-full transition-colors duration-700 ease-osso group-hover:bg-petrolio-3">
          {foto ? (
            media
          ) : (
            <div className="fluttua absolute inset-0" style={{ "--fluttua-da": velocita[0], "--fluttua-a": velocita[1] } as CSSProperties}>
              {media}
            </div>
          )}
        </Lastra>
        <div className="flex flex-1 flex-col pt-5">
          {index !== undefined && <p className="eyebrow mb-2">{String(index + 1).padStart(2, "0")}</p>}
          <h3 className="text-[1.45rem] leading-tight transition-colors duration-500 group-hover:text-petrolio md:text-[1.6rem]">{pick(p.titolo, locale)}</h3>
          <p className="mt-2.5 text-[0.98rem] leading-relaxed text-grafite">{pick(p.lead, locale)}</p>
          <div className="mt-auto flex items-end justify-between gap-4 pt-5">
            {credito(p, dove, locale) ? <p className="text-[0.8rem] text-grafite">{credito(p, dove, locale)}</p> : <span />}
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

/** Il metodo (Come si opera): non una patologia, uno spazio a sé. Foto a sinistra (se c'è), altrimenti disegno. */
export async function SchedaMetodo({ p, locale }: { p: Patologia; locale: Locale }) {
  const m = getMessages(locale);
  const segno = isSegno(p.segno) ? p.segno : "artroscopia";
  const catalogo = await getDisegni();
  const foto = srcMedia(p.immagine?.src, "patologie");
  const disegno = foto ? null : srcDisegno(catalogo, segno, locale);
  const alt = pick(p.immagine?.alt, locale) || pick(p.titolo, locale);
  return (
    <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group grid items-center gap-10 md:grid-cols-[minmax(0,1fr)_minmax(0,1fr)] md:gap-16 lg:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)] lg:gap-24">
      <Lastra ratio="5/4" className="w-full transition-colors duration-700 ease-osso group-hover:bg-petrolio-3">
        {foto ? (
          <Image src={foto} alt={alt} fill quality={92} sizes="(min-width: 1024px) 42vw, 100vw" className="object-cover object-[50%_22%]" />
        ) : (
          <div className="fluttua absolute inset-0" style={{ "--fluttua-da": "6%", "--fluttua-a": "-6%" } as CSSProperties}>
            {disegno ? (
              <Disegno src={disegno.src} alt={disegno.alt} />
            ) : (
              <span className="absolute inset-0 grid place-items-center text-petrolio">
                <Segno nome={segno} size={56} />
              </span>
            )}
          </div>
        )}
      </Lastra>
      <div className="min-w-0">
        <p className="eyebrow">{m.cosaCuro.metodoEyebrow}</p>
        <h3 className="display-m mt-4 transition-colors duration-500 group-hover:text-petrolio">{pick(p.titolo, locale)}</h3>
        <p className="lead mt-5 max-w-xl">{pick(p.lead, locale)}</p>
        <ul className="mt-7 grid max-w-xl grid-cols-3 gap-x-4 gap-y-5">
          {m.cosaCuro.tecniche.map((t) => (
            <li key={t.icona} className="flex min-w-0 flex-col items-start">
              <span className="grid size-14 place-items-center rounded-full bg-petrolio-3 text-petrolio transition-colors duration-500 group-hover:bg-petrolio group-hover:text-osso">
                {isTecnica(t.icona) && <IconaTecnica nome={t.icona} size={32} />}
              </span>
              <span className="mt-3 text-[1rem] font-medium leading-tight">{t.nome}</span>
              <span className="mt-1 text-[0.82rem] leading-snug text-grafite">{t.nota}</span>
            </li>
          ))}
        </ul>
        <p className="mt-7 max-w-xl text-[0.98rem] leading-relaxed text-grafite">{m.cosaCuro.metodoLead}</p>
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

/** Scheda sede (hub Dove): riga compatta, foto a sinistra, tutto leggibile in una schermata. Visite e chirurgia in etichetta, subito sotto il nome. */
export async function SchedaSede({ s, locale }: { s: Sede; locale: Locale }) {
  const m = getMessages(locale);
  const foto = s.foto?.[0];
  const fotoSrc = srcMedia(foto?.src, "sedi");
  const catalogo = await getDisegni();
  const segno = s.tipo === "ospedale" ? "ospedale" : s.tipo === "studio" ? "studio" : "clinica";
  const disegno = srcDisegno(catalogo, segno, locale);
  const regime = pick(s.regime, locale);
  const servizi = [s.infiltrazioni && m.dove.infiltrazioni, s.ecografo && m.dove.ecografo].filter(Boolean);
  return (
    <Link href={href(locale, { kind: "dove", slug: s.slug })} className="group grid h-full grid-cols-[minmax(0,6.5rem)_minmax(0,1fr)] items-center gap-4 sm:grid-cols-[minmax(0,8.5rem)_minmax(0,1fr)] sm:gap-5 lg:grid-cols-[minmax(0,10rem)_minmax(0,1fr)]">
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
      <div className="flex min-w-0 flex-col gap-0.5">
        <p className="eyebrow">
          {s.citta}
          {s.provincia ? ` (${s.provincia})` : ""}
        </p>
        <h3 className="text-[1.05rem] leading-tight group-hover:text-petrolio md:text-[1.15rem]">{s.nome}</h3>
        <span className="my-1.5 flex flex-wrap gap-1.5">
          {s.visite && <span className="tag tag-petrolio">{m.dove.visite}</span>}
          {s.chirurgia && <span className="tag">{m.dove.chirurgia}</span>}
        </span>
        <p className="text-sm leading-snug text-grafite">
          {s.indirizzo}
          {s.cap ? `, ${s.cap}` : ""}
        </p>
        {regime && <p className="text-sm leading-snug text-grafite">{regime}</p>}
        {servizi.length > 0 && <p className="text-[0.78rem] leading-snug text-nebbia">{servizi.join(" · ")}</p>}
      </div>
    </Link>
  );
}

/**
 * Nota / approfondimento: copertina Keystatic, o disegno.
 * `sopraPiega` = la copertina è tra i primi contenuti visibili della pagina: si carica subito.
 */
export async function SchedaNota({ n, locale, sopraPiega = false }: { n: Nota; locale: Locale; sopraPiega?: boolean }) {
  const m = getMessages(locale);
  const copertina = srcMedia(n.copertina?.src, "approfondimenti");
  const alt = pick(n.copertina?.alt, locale) || pick(n.titolo, locale);
  const catalogo = await getDisegni();
  const fallback = srcDisegno(catalogo, idDisegnoDaTag(n.tag), locale);
  return (
    <Link href={href(locale, { kind: "nota", slug: slugNota(n, locale) })} className="group flex h-full flex-col">
      <Lastra>
        {copertina ? (
          <Image src={copertina} alt={alt} fill quality={92} sizes="(min-width: 768px) 24rem, 80vw" loading={sopraPiega ? "eager" : undefined} className="object-cover" />
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
        <h3 className="mt-3 line-clamp-3 min-h-[3.6em] text-[1.3rem] leading-snug group-hover:text-petrolio">{pick(n.titolo, locale)}</h3>
        <p className="mt-2 line-clamp-3 min-h-[4.4em] text-[0.95rem] text-grafite">{pick(n.lead, locale)}</p>
      </div>
    </Link>
  );
}
