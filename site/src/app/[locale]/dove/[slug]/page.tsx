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
import { Segno } from "@/components/ui/Segno";
import { Briciole } from "@/components/blocks/Pagina";
import { ModuloSede, SchedaPatologia } from "@/components/blocks/Schede";
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
  const maps =
    sede.mapsUrl ||
    (sede.coordinate?.lat != null && sede.coordinate?.lng != null
      ? `https://www.google.com/maps/search/?api=1&query=${sede.coordinate.lat},${sede.coordinate.lng}`
      : `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(`${sede.nome} ${indirizzo}`)}`);
  const embed =
    sede.coordinate?.lat != null && sede.coordinate?.lng != null
      ? `https://www.openstreetmap.org/export/embed.html?bbox=${sede.coordinate.lng - 0.01},${sede.coordinate.lat - 0.006},${sede.coordinate.lng + 0.01},${sede.coordinate.lat + 0.006}&layer=mapnik&marker=${sede.coordinate.lat},${sede.coordinate.lng}`
      : null;
  const foto = sede.foto ?? [];

  const fatti: { segno: "check" | "artroscopia" | "eco" | "protesi"; label: string }[] = [];
  if (sede.visite) fatti.push({ segno: "check", label: m.dove.visite });
  if (sede.chirurgia) fatti.push({ segno: "artroscopia", label: m.dove.chirurgia });
  if (sede.infiltrazioni && sede.visite) fatti.push({ segno: "protesi", label: m.dove.infiltrazioni });
  if (sede.ecografo) fatti.push({ segno: "eco", label: m.dove.ecografo });

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
        <Reveal className="osso osso-lg cucitura relative overflow-hidden">
          <div className="pointer-events-none absolute -right-20 -top-20 h-72 w-72 rounded-full bg-pesca blur-3xl" aria-hidden="true" />
          <div className="relative grid gap-6 p-7 md:grid-cols-[1.3fr_1fr] md:p-12">
            <div>
              <p className="eyebrow mb-3">
                {sede.citta}
                {sede.provincia ? ` (${sede.provincia})` : ""}
                {pick(sede.regime, l) ? ` · ${pick(sede.regime, l)}` : ""}
              </p>
              <h1 className="text-[2.3rem] leading-[1.05] md:text-[3rem]">{sede.nome}</h1>
              <p className="mt-3 flex items-start gap-2 text-grafite">
                <Segno nome="pin" size={18} className="mt-1 shrink-0 text-nebbia" />
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
              <div className="mt-6 flex flex-wrap gap-2">
                <a href={maps} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
                  <Segno nome="pin" size={18} />
                  {m.cta.vediSuMaps}
                </a>
                {sede.gbpUrl && (
                  <a href={sede.gbpUrl} target="_blank" rel="noopener noreferrer" className="btn btn-ghost">
                    {m.cta.schedaGoogle}
                    <Segno nome="esterno" size={16} />
                  </a>
                )}
                {sede.sitoStruttura && (
                  <a href={sede.sitoStruttura} target="_blank" rel="noopener noreferrer" className="btn btn-ghost">
                    {m.cta.sitoStruttura}
                    <Segno nome="esterno" size={16} />
                  </a>
                )}
              </div>
            </div>
            <div className="incavo relative min-h-56 overflow-hidden md:min-h-full" style={{ borderRadius: "48% 52% 44% 56% / 56% 44% 56% 44%" }}>
              {foto[0]?.src ? (
                <Image src={foto[0].src} alt={pick(foto[0].alt, l)} fill priority sizes="(min-width: 768px) 35vw, 90vw" className="object-cover" />
              ) : embed ? (
                <iframe title={`${m.dove.indirizzo}: ${sede.nome}`} src={embed} className="absolute inset-0 h-full w-full border-0 grayscale-[30%]" loading="lazy" />
              ) : (
                <div className="absolute inset-0 grid place-items-center text-petrolio/40">
                  <Segno nome="pin" size={64} strokeWidth={1} />
                </div>
              )}
            </div>
          </div>
        </Reveal>
      </header>

      <div className="contenitore grid gap-4 py-12 md:grid-cols-3">
        <Reveal className="osso p-6 md:col-span-2">
          <h2 className="text-[1.5rem]">{m.dove.cosaFaccioQui}</h2>
          <p className="mt-3 whitespace-pre-line text-[1.02rem] leading-relaxed text-grafite">{pick(sede.ruolo, l)}</p>
        </Reveal>
        <Reveal delay={80} className="osso vetro vetro-menta p-6">
          <h2 className="text-[1.3rem]">{m.dove.prenota}</h2>
          <p className="mt-2 text-[0.98rem] text-grafite">{m.dove.prenotaTesto}</p>
          <p className="mt-4 flex items-start gap-2 text-[0.95rem]">
            <Segno nome="orologio" size={18} className="mt-0.5 shrink-0 text-nebbia" />
            <span>{pick(sede.orari, l) || m.dove.suAppuntamento}</span>
          </p>
        </Reveal>
        {pick(sede.comeArrivare, l) && (
          <Reveal delay={120} className="osso p-6">
            <h2 className="text-[1.3rem]">{m.dove.comeArrivare}</h2>
            <p className="mt-2 whitespace-pre-line text-[0.98rem] text-grafite">{pick(sede.comeArrivare, l)}</p>
          </Reveal>
        )}
        {pick(sede.accessibilita, l) && (
          <Reveal delay={160} className="osso p-6">
            <h2 className="text-[1.3rem]">{m.dove.accessibilita}</h2>
            <p className="mt-2 whitespace-pre-line text-[0.98rem] text-grafite">{pick(sede.accessibilita, l)}</p>
          </Reveal>
        )}
        {embed && foto[0]?.src && (
          <Reveal delay={200} className="incavo relative min-h-56 overflow-hidden rounded-[1.75rem]">
            <iframe title={`${m.dove.indirizzo}: ${sede.nome}`} src={embed} className="absolute inset-0 h-full w-full border-0 grayscale-[30%]" loading="lazy" />
          </Reveal>
        )}
      </div>

      {tipiche.length > 0 && (
        <section className="contenitore pb-6">
          <p className="eyebrow mb-4">{m.dove.patologieTipiche}</p>
          <div className="grid gap-4 md:grid-cols-3">
            {tipiche.map((p, i) => (
              <Reveal key={p.slug} delay={i * 70}>
                <SchedaPatologia p={p} locale={l} index={i} />
              </Reveal>
            ))}
          </div>
        </section>
      )}

      {altre.length > 0 && (
        <section className="contenitore py-8">
          <p className="eyebrow mb-4">{m.dove.altreSedi}</p>
          <div className="incavo p-2 sm:p-3">
            <ul className="grid gap-2 sm:grid-cols-3 sm:gap-3">
              {altre.map((x) => (
                <li key={x.slug}>
                  <ModuloSede s={x} locale={l} />
                </li>
              ))}
            </ul>
          </div>
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
