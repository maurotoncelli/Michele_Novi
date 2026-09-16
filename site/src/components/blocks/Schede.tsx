import Link from "next/link";
import Image from "next/image";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick, formatDate } from "@/i18n";
import { slugNota, slugPatologia, type Nota, type Patologia, type Pubblicazione, type Sede } from "@/lib/content";
import { isSegno, Segno } from "../ui/Segno";

const tinte = ["", "vetro-menta", "vetro-pesca", "vetro-salvia"] as const;

/** Card patologia. Le prime quattro in home sono "strati" con tinte diverse. */
export function SchedaPatologia({ p, locale, index = 0, grande = false, strato = false }: { p: Patologia; locale: Locale; index?: number; grande?: boolean; strato?: boolean }) {
  const m = getMessages(locale);
  const segno = isSegno(p.segno) ? p.segno : "spalla";
  const tinta = strato ? tinte[index % tinte.length] : "";
  return (
    <Link
      href={href(locale, { kind: "cosaCuro", slug: slugPatologia(p, locale) })}
      className={`osso osso-vivo group flex h-full flex-col justify-between p-6 ${tinta ? `vetro ${tinta}` : ""} ${grande ? "md:p-8" : ""}`}
    >
      <div className="flex items-start justify-between gap-4">
        <span className="incavo grid h-12 w-12 shrink-0 place-items-center text-petrolio transition group-hover:text-petrolio-2">
          <Segno nome={segno} size={26} />
        </span>
        <Segno nome="freccia" size={20} className="mt-3 text-nebbia transition group-hover:translate-x-1 group-hover:text-petrolio" />
      </div>
      <div className="mt-8">
        <h3 className={`${grande ? "text-[1.9rem]" : "text-[1.35rem]"} leading-tight`}>{pick(p.titolo, locale)}</h3>
        <p className={`mt-2 text-grafite ${grande ? "text-[1.02rem]" : "text-[0.95rem]"} line-clamp-3`}>{pick(p.lead, locale)}</p>
        <span className="sr-only">{m.cta.scopri}</span>
      </div>
    </Link>
  );
}

/** Modulo sede nel "docking": forma tonda che si alloggia nella gola. */
export function ModuloSede({ s, locale }: { s: Sede; locale: Locale }) {
  const m = getMessages(locale);
  const segno = s.tipo === "ospedale" ? "ospedale" : s.tipo === "studio" ? "studio" : "clinica";
  return (
    <Link
      href={href(locale, { kind: "dove", slug: s.slug })}
      className="osso osso-vivo group flex flex-col items-center gap-3 px-5 py-6 text-center"
    >
      <span className="incavo grid h-12 w-12 place-items-center text-petrolio">
        <Segno nome={segno} size={24} />
      </span>
      <span>
        <span className="serif block text-[1.25rem] leading-tight">{s.citta}</span>
        <span className="mt-1 block text-[0.8rem] leading-snug text-grafite">{s.nome}</span>
      </span>
      <span className="mt-1 flex flex-wrap justify-center gap-1">
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
    <Link href={href(locale, { kind: "dove", slug: s.slug })} className="osso osso-vivo group grid overflow-hidden sm:grid-cols-[minmax(0,1fr)_minmax(0,1.3fr)]">
      <div className="relative min-h-44 bg-osso-2 sm:min-h-full">
        {foto?.src ? (
          <Image src={foto.src} alt={pick(foto.alt, locale)} fill sizes="(min-width: 640px) 30vw, 100vw" className="object-cover" />
        ) : (
          <div className="absolute inset-0 grid place-items-center text-nebbia">
            <Segno nome={s.tipo === "ospedale" ? "ospedale" : s.tipo === "studio" ? "studio" : "clinica"} size={48} />
          </div>
        )}
      </div>
      <div className="p-6">
        <p className="eyebrow">{s.citta}{s.provincia ? ` (${s.provincia})` : ""}</p>
        <h3 className="mt-1 text-[1.5rem] leading-tight">{s.nome}</h3>
        <p className="mt-1 text-sm text-grafite">{s.indirizzo}</p>
        <p className="mt-3 line-clamp-3 text-[0.95rem] text-grafite">{pick(s.ruolo, locale)}</p>
        <div className="mt-4 flex flex-wrap gap-1.5">
          {s.visite && <span className="tag tag-petrolio">{m.dove.visite}</span>}
          {s.chirurgia && <span className="tag">{m.dove.chirurgia}</span>}
          {s.infiltrazioni && s.visite && <span className="tag">{m.dove.infiltrazioni}</span>}
          {s.ecografo && <span className="tag">{m.dove.ecografo}</span>}
        </div>
      </div>
    </Link>
  );
}

/** Pubblicazione in lista: impaginata da paper, compatta. */
export function SchedaPaper({ p, locale }: { p: Pubblicazione; locale: Locale }) {
  const m = getMessages(locale);
  const titolo = pick(p.titoloBreve, locale) || p.titolo;
  return (
    <Link href={href(locale, { kind: "paper", slug: p.slug })} className="osso osso-vivo group block p-6">
      <div className="flex items-center justify-between gap-3">
        <span className="tag tag-petrolio">{m.quaderno.paper}</span>
        <span className="text-sm text-grafite">{p.anno}</span>
      </div>
      <h3 className="mt-4 text-[1.3rem] leading-snug">{titolo}</h3>
      {titolo !== p.titolo && <p className="mt-1 line-clamp-2 text-sm italic text-grafite">{p.titolo}</p>}
      <p className="mt-3 text-sm text-grafite">
        {p.rivista}
        {p.autori ? ` · ${p.autori.split(",")[0]} et al.` : ""}
      </p>
    </Link>
  );
}

/** Nota "Dal lavoro" in lista. */
export function SchedaNota({ n, locale }: { n: Nota; locale: Locale }) {
  const m = getMessages(locale);
  return (
    <Link href={href(locale, { kind: "nota", slug: slugNota(n, locale) })} className="osso osso-vivo group block overflow-hidden">
      {n.copertina?.src && (
        <div className="relative aspect-[16/9] bg-osso-2">
          <Image src={n.copertina.src} alt={pick(n.copertina.alt, locale)} fill sizes="(min-width: 768px) 33vw, 100vw" className="object-cover" />
        </div>
      )}
      <div className="p-6">
        <div className="flex items-center justify-between gap-3">
          <span className="tag tag-rame">{m.quaderno.nota}</span>
          <time dateTime={n.data ?? undefined} className="text-sm text-grafite">
            {formatDate(n.data, locale)}
          </time>
        </div>
        <h3 className="mt-4 text-[1.3rem] leading-snug">{pick(n.titolo, locale)}</h3>
        <p className="mt-2 line-clamp-3 text-[0.95rem] text-grafite">{pick(n.lead, locale)}</p>
      </div>
    </Link>
  );
}
