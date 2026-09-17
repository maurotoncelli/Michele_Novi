import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { href, isLocale, locales, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getPatologie, getSede, getSedi, getSettings, slugPatologia } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata, sedeJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno, type NomeSegno } from "@/components/ui/Segno";
import { Briciole } from "@/components/blocks/Pagina";
import { ModuloSede, SchedaPatologia } from "@/components/blocks/Schede";
import { MappaSede } from "@/components/blocks/MappaSede";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export const dynamicParams = false;
export async function generateStaticParams() {
  const all = await getSedi();
  return locales.flatMap((locale) => all.map((s) => ({ locale, slug: s.slug })));
}

export async function generateMetadata({ params }: PageProps<"/[locale]/dove/[slug]">): Promise<Metadata> {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, sede] = await Promise.all([getSettings(), getSede(slug)]);
  if (!sede) return {};
  const m = getMessages(l);
  return buildMetadata(s, {
    locale: l,
    route: { kind: "dove", slug: sede.slug },
    title: pick(sede.seo?.title, l) || `${sede.nome}, ${sede.citta} — ${m.dove.titolo}`,
    description: pick(sede.seo?.description, l) || pick(sede.ruolo, l),
    image: sede.seo?.ogImage ?? sede.foto?.[0]?.src,
    noindex: sede.seo?.noindex,
  });
}

function Fatto({ segno, titolo, testo }: { segno: NomeSegno; titolo: string; testo: string }) {
  return (
    <div>
      <span className="grid h-11 w-11 place-items-center bg-petrolio-3 text-petrolio">
        <Segno nome={segno} size={18} />
      </span>
      <h2 className="mt-4 text-[1.05rem] leading-tight">{titolo}</h2>
      <p className="mt-1.5 whitespace-pre-line text-[0.95rem] leading-relaxed text-grafite">{testo}</p>
    </div>
  );
}

export default async function SedePage({ params }: PageProps<"/[locale]/dove/[slug]">) {
  const { locale, slug } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const sede = await getSede(slug);
  if (!sede) notFound();
  const [s, sedi, patologie] = await Promise.all([getSettings(), getSedi(), getPatologie()]);
  const m = getMessages(l);
  const altre = sedi.filter((x) => x.slug !== sede.slug);
  const tipiche = (sede.patologie ?? []).map((sl) => patologie.find((p) => p.slug === sl)).filter(Boolean) as typeof patologie;
  const indirizzo = [sede.indirizzo, [sede.cap, sede.citta, sede.provincia ? `(${sede.provincia})` : ""].filter(Boolean).join(" ")].filter(Boolean).join(", ");
  const query = `${sede.nome} ${indirizzo}`;
  const maps =
    sede.mapsUrl ||
    (sede.coordinate?.lat != null && sede.coordinate?.lng != null
      ? `https://www.google.com/maps/search/?api=1&query=${sede.coordinate.lat},${sede.coordinate.lng}`
      : `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(query)}`);
  const foto = sede.foto ?? [];

  const fatti: { segno: NomeSegno; label: string }[] = [];
  if (sede.visite) fatti.push({ segno: "check", label: m.dove.visite });
  if (sede.chirurgia) fatti.push({ segno: "artroscopia", label: m.dove.chirurgia });
  if (sede.infiltrazioni && sede.visite) fatti.push({ segno: "protesi", label: m.dove.infiltrazioni });
  if (sede.ecografo) fatti.push({ segno: "eco", label: m.dove.ecografo });

  const info: { segno: NomeSegno; titolo: string; testo: string }[] = [
    { segno: "orologio", titolo: m.dove.prenota, testo: `${m.dove.prenotaTesto}${pick(sede.orari, l) ? `\n${pick(sede.orari, l)}` : `\n${m.dove.suAppuntamento}`}` },
  ];
  const arrivare = pick(sede.comeArrivare, l);
  if (arrivare) info.push({ segno: "pin", titolo: m.dove.comeArrivare, testo: arrivare });
  const accessoRaw = pick(sede.accessibilita, l);
  if (accessoRaw) {
    const pezzi = accessoRaw.split(/(?<=\.)\s+/).filter(Boolean);
    const parcheggi = pezzi.filter((x) => /parcheg/i.test(x));
    const resto = pezzi.filter((x) => !/parcheg/i.test(x));
    if (resto.length) info.push({ segno: "access", titolo: m.dove.accessibilita, testo: resto.join(" ") });
    if (parcheggi.length) info.push({ segno: "auto", titolo: m.dove.parcheggio, testo: parcheggi.join(" ") });
    if (!resto.length && !parcheggi.length) info.push({ segno: "access", titolo: m.dove.accessibilita, testo: accessoRaw });
  }

  return (
    <>
      <JsonLd
        data={[
          sedeJsonLd(s, sede, l),
          breadcrumbJsonLd(s, [
            { name: m.meta.siteName, path: href(l, { kind: "home" }) },
            { name: m.dove.titolo, path: href(l, { kind: "dove" }) },
            { name: sede.nome, path: href(l, { kind: "dove", slug: sede.slug }) },
          ]),
        ]}
      />
      <Briciole items={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.nav.dove, href: href(l, { kind: "dove" }) }, { label: sede.citta || sede.nome }]} />

      <header className="contenitore pt-8 md:pt-12">
        <Reveal>
          <p className="eyebrow mb-3">
            {sede.citta}
            {sede.provincia ? ` (${sede.provincia})` : ""}
            {pick(sede.regime, l) ? ` · ${pick(sede.regime, l)}` : ""}
          </p>
          <h1 className="max-w-3xl text-[2.3rem] leading-[1.05] md:text-[3rem]">{sede.nome}</h1>
          <p className="mt-5 flex items-start gap-2 text-grafite">
            <Segno nome="pin" size={18} className="mt-1 shrink-0 text-petrolio" />
            <span>{indirizzo}</span>
          </p>
          <ul className="mt-5 flex flex-wrap gap-2">
            {fatti.map((f) => (
              <li key={f.label} className="tag tag-petrolio">
                <Segno nome={f.segno} size={14} />
                {f.label}
              </li>
            ))}
            {!sede.visite && sede.chirurgia && <li className="tag">{m.dove.soloChirurgia}</li>}
          </ul>
        </Reveal>
      </header>

      <div className="contenitore grid gap-10 py-10 md:grid-cols-[1fr_minmax(0,1.1fr)] md:items-start md:gap-14">
        <Reveal>
          {foto[0]?.src && (
            <div className="relative mb-8 aspect-[16/9] overflow-hidden bg-petrolio-3">
              <Image src={foto[0].src} alt={pick(foto[0].alt, l)} fill sizes="(min-width: 768px) 45vw, 100vw" className="object-cover" />
            </div>
          )}
          <h2 className="text-[1.4rem]">{m.dove.cosaFaccioQui}</h2>
          <p className="mt-3 whitespace-pre-line text-[1.02rem] leading-relaxed text-grafite">{pick(sede.ruolo, l)}</p>
          <div className="mt-10 grid gap-8 sm:grid-cols-2 sm:gap-x-10 sm:gap-y-12">
            {info.map((x) => (
              <Fatto key={x.titolo} segno={x.segno} titolo={x.titolo} testo={x.testo} />
            ))}
          </div>
          <div className="mt-8 flex flex-wrap gap-2">
            <a href={maps} target="_blank" rel="noopener noreferrer" className="btn btn-petrolio">
              <Segno nome="pin" size={18} />
              {m.cta.vediSuMaps}
            </a>
            {sede.gbpUrl && (
              <a href={sede.gbpUrl} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
                {m.cta.schedaGoogle}
                <Segno nome="esterno" size={16} />
              </a>
            )}
            {sede.sitoStruttura && (
              <a href={sede.sitoStruttura} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
                {m.cta.sitoStruttura}
                <Segno nome="esterno" size={16} />
              </a>
            )}
          </div>
        </Reveal>

        <Reveal delay={80} className="md:sticky md:top-[calc(var(--header-h)+1.25rem)]">
          <p className="eyebrow mb-3">{m.dove.mappa}</p>
          <div className="relative aspect-[4/3] overflow-hidden bg-osso-2 md:aspect-[5/4]">
            <MappaSede lat={sede.coordinate?.lat} lng={sede.coordinate?.lng} query={query} nome={sede.nome} lang={l} />
          </div>
        </Reveal>
      </div>

      {tipiche.length > 0 && (
        <section className="bg-osso-3">
          <div className="contenitore py-12">
            <p className="eyebrow mb-6">{m.dove.patologieTipiche}</p>
            <div className="grid gap-8 md:grid-cols-3">
              {tipiche.map((p, i) => (
                <Reveal key={p.slug} delay={i * 70}>
                  <SchedaPatologia p={p} locale={l} index={i} />
                </Reveal>
              ))}
            </div>
          </div>
        </section>
      )}

      {altre.length > 0 && (
        <section className="contenitore py-12">
          <p className="eyebrow mb-6">{m.dove.altreSedi}</p>
          <ul className="grid gap-8 sm:grid-cols-3">
            {altre.map((x) => (
              <li key={x.slug}>
                <ModuloSede s={x} locale={l} />
              </li>
            ))}
          </ul>
        </section>
      )}

      {tipiche.length === 0 && patologie.length > 0 && (
        <p className="contenitore -mt-2 mb-4 text-sm text-grafite">
          <Link href={href(l, { kind: "cosaCuro", slug: slugPatologia(patologie[0], l) })} className="underline underline-offset-4 hover:text-petrolio">
            {pick(patologie[0].titolo, l)}
          </Link>
        </p>
      )}

      <FasciaContatto locale={l} />
    </>
  );
}
