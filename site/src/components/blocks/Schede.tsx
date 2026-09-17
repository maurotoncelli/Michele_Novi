import Link from "next/link";
import Image from "next/image";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick, formatDate } from "@/i18n";
import { getDisegni, idDisegnoDaTag, slugNota, slugPatologia, srcDisegno, type Nota, type Patologia, type Pubblicazione, type Sede } from "@/lib/content";
import { hrefArticolo, srcMedia, srcPaper } from "@/lib/media";
import { Disegno } from "../ui/Disegno";
import { isSegno, Segno } from "../ui/Segno";

/** Card patologia: immagine + titolo, niente lastra. */
export async function SchedaPatologia({ p, locale, grande = false }: { p: Patologia; locale: Locale; index?: number; grande?: boolean; strato?: boolean }) {
  const m = getMessages(locale);
  const segno = isSegno(p.segno) ? p.segno : "spalla";
  const catalogo = await getDisegni();
  const disegno = p.immagine?.src
    ? { src: p.immagine.src, alt: pick(p.immagine.alt, locale) || pick(p.titolo, locale) }
    : srcDisegno(catalogo, segno, locale);
  return (
    <Link href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })} className="group flex h-full flex-col">
      <div className="relative mb-5 aspect-[5/4] w-full overflow-hidden bg-petrolio-3">
        {disegno ? (
          <Disegno src={disegno.src} alt={disegno.alt} />
        ) : (
          <span className="absolute inset-0 grid place-items-center text-petrolio">
            <Segno nome={segno} size={40} />
          </span>
        )}
      </div>
      <div className="mt-auto">
        <h3 className={`${grande ? "text-[1.7rem]" : "text-[1.28rem]"} leading-tight group-hover:text-petrolio`}>{pick(p.titolo, locale)}</h3>
        <p className={`mt-2 text-grafite ${grande ? "text-[1.02rem]" : "text-[0.92rem]"} line-clamp-3`}>{pick(p.lead, locale)}</p>
        <span className="sr-only">{m.cta.scopri}</span>
      </div>
    </Link>
  );
}

/** Sede in home: città, non modulo tondo. */
export async function ModuloSede({ s, locale }: { s: Sede; locale: Locale }) {
  const m = getMessages(locale);
  const segno = s.tipo === "ospedale" ? "ospedale" : s.tipo === "studio" ? "studio" : "clinica";
  const disegno = srcDisegno(await getDisegni(), segno, locale);
  return (
    <Link href={href(locale, { kind: "dove", slug: s.slug })} className="group flex flex-col gap-4">
      <span className="relative aspect-[4/3] w-full overflow-hidden bg-petrolio-3">
        {disegno ? <Disegno src={disegno.src} alt={disegno.alt} /> : <span className="absolute inset-0 grid place-items-center text-petrolio"><Segno nome={segno} size={28} /></span>}
      </span>
      <span>
        <span className="serif block text-[1.35rem] leading-tight group-hover:text-petrolio">{s.citta}</span>
        <span className="mt-1 block text-[0.85rem] leading-snug text-grafite">{s.nome}</span>
      </span>
      <span className="flex flex-wrap gap-1">
        {s.visite && <span className="tag tag-petrolio">{m.dove.visite}</span>}
        {s.chirurgia && <span className="tag">{m.dove.chirurgia}</span>}
      </span>
    </Link>
  );
}

/** Scheda sede completa (hub Dove). */
export function SchedaSede({ s, locale }: { s: Sede; locale: Locale }) {
  const m = getMessages(locale);
  const foto = s.foto?.[0];
  return (
    <Link href={href(locale, { kind: "dove", slug: s.slug })} className="group block">
      <div className="relative aspect-[16/9] overflow-hidden bg-petrolio-3">
        {foto?.src ? (
          <Image src={foto.src} alt={pick(foto.alt, locale)} fill sizes="(min-width: 1024px) 30vw, 100vw" className="object-cover" />
        ) : (
          <div className="absolute inset-0 grid place-items-center text-nebbia">
            <Segno nome={s.tipo === "ospedale" ? "ospedale" : s.tipo === "studio" ? "studio" : "clinica"} size={40} />
          </div>
        )}
      </div>
      <div className="pt-4">
        <p className="eyebrow">{s.citta}{s.provincia ? ` (${s.provincia})` : ""}</p>
        <h3 className="mt-1 text-[1.35rem] leading-tight group-hover:text-petrolio">{s.nome}</h3>
        <p className="mt-1 text-sm text-grafite">{s.indirizzo}</p>
        <div className="mt-3 flex flex-wrap gap-1.5">
          {s.visite && <span className="tag tag-petrolio">{m.dove.visite}</span>}
          {s.chirurgia && <span className="tag">{m.dove.chirurgia}</span>}
          {s.infiltrazioni && s.visite && <span className="tag">{m.dove.infiltrazioni}</span>}
          {s.ecografo && <span className="tag">{m.dove.ecografo}</span>}
        </div>
      </div>
    </Link>
  );
}

/** Pubblicazione: sempre un’immagine (disegno dal tag). */
export async function SchedaPaper({ p, locale }: { p: Pubblicazione; locale: Locale }) {
  const m = getMessages(locale);
  const titolo = pick(p.titoloBreve, locale) || p.titolo;
  const catalogo = await getDisegni();
  const id = idDisegnoDaTag(p.tag, p.patologie);
  const disegno = srcDisegno(catalogo, id, locale);
  const pdf = srcPaper(p.pdf);
  const articolo = hrefArticolo(p.doi, p.url);
  return (
    <div>
      <Link href={href(locale, { kind: "paper", slug: p.slug })} className="group block">
        <div className="relative aspect-[16/9] overflow-hidden bg-petrolio-3">
          {disegno ? (
            <Disegno src={disegno.src} alt={disegno.alt} />
          ) : (
            <span className="absolute inset-0 grid place-items-center text-petrolio">
              <Segno nome="doc" size={36} />
            </span>
          )}
        </div>
        <div className="pt-5">
          <div className="flex items-center justify-between gap-3">
            <span className="tag tag-petrolio">{m.quaderno.paper}</span>
            <span className="text-sm text-grafite">{p.anno}</span>
          </div>
          <h3 className="mt-3 text-[1.3rem] leading-snug group-hover:text-petrolio">{titolo}</h3>
          {titolo !== p.titolo && <p className="mt-1 line-clamp-2 text-sm italic text-grafite">{p.titolo}</p>}
          <p className="mt-3 text-sm text-grafite">
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
export async function SchedaNota({ n, locale }: { n: Nota; locale: Locale }) {
  const m = getMessages(locale);
  const copertina = srcMedia(n.copertina?.src, "quaderno");
  const alt = pick(n.copertina?.alt, locale) || pick(n.titolo, locale);
  const catalogo = await getDisegni();
  const fallback = srcDisegno(catalogo, idDisegnoDaTag(n.tag), locale);
  return (
    <Link href={href(locale, { kind: "nota", slug: slugNota(n, locale) })} className="group block">
      <div className="relative aspect-[16/9] overflow-hidden bg-petrolio-3">
        {copertina ? (
          <Image src={copertina} alt={alt} fill sizes="(min-width: 768px) 33vw, 100vw" className="object-cover" />
        ) : fallback ? (
          <Disegno src={fallback.src} alt={alt} />
        ) : (
          <Image src="/images/disegni/quaderno.png" alt={alt} fill sizes="(min-width: 768px) 33vw, 100vw" className="object-contain p-8" />
        )}
      </div>
      <div className="pt-5">
        <div className="flex items-center justify-between gap-3">
          <span className="tag tag-rame">{m.quaderno.nota}</span>
          <time dateTime={n.data ?? undefined} className="text-sm text-grafite">
            {formatDate(n.data, locale)}
          </time>
        </div>
        <h3 className="mt-3 text-[1.3rem] leading-snug group-hover:text-petrolio">{pick(n.titolo, locale)}</h3>
        <p className="mt-2 line-clamp-3 text-[0.95rem] text-grafite">{pick(n.lead, locale)}</p>
      </div>
    </Link>
  );
}
