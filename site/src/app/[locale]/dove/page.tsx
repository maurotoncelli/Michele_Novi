import type { Metadata } from "next";
import Link from "next/link";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getSedi, getSettings, telHref } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Intestazione, Sezione } from "@/components/blocks/Pagina";
import { SchedaSede } from "@/components/blocks/Schede";
import { MappaToscanaVisite } from "@/components/blocks/MappaToscana";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/dove">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "dove" }, title: m.nav.dove, description: m.meta.doveDescription });
}

export default async function DovePage({ params }: PageProps<"/[locale]/dove">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, sedi] = await Promise.all([getSettings(), getSedi()]);
  const m = getMessages(l);
  const tel = telHref(s.telefono);

  const sediVisite = sedi
    .filter((x) => x.visite)
    .map((x) => ({
      slug: x.slug,
      citta: x.citta,
      provincia: x.provincia || undefined,
      nome: x.nome,
      indirizzo: x.indirizzo,
      cap: x.cap || undefined,
      regime: pick(x.regime, l) || undefined,
      servizi: [x.infiltrazioni && m.dove.infiltrazioni, x.ecografo && m.dove.ecografo].filter((v): v is string => Boolean(v)),
    }));

  const sediChirurgia = sedi.filter((x) => x.chirurgia);

  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.nav.dove, path: href(l, { kind: "dove" }) },
        ])}
      />
      <Intestazione
        eyebrow={m.nav.dove}
        titolo={m.dove.titolo}
        lead={m.dove.lead}
        stretta
        percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.nav.dove }]}
      />

      {/* 1. DOVE VISITO: Mappa della Toscana con pin e loghi degli studi */}
      <Sezione eyebrow={m.dove.visite} titolo={m.dove.doveVisitoTitolo} lead={m.dove.doveVisitoLead} compatta>
        <Reveal>
          <MappaToscanaVisite sedi={sediVisite} locale={l} labelScopri={m.cta.scopri} />
        </Reveal>
        {tel && (
          <Reveal className="mt-8 flex flex-col items-start justify-between gap-4 border-t border-linea pt-6 sm:flex-row sm:items-center">
            <p className="max-w-xl text-[0.95rem] leading-snug text-grafite">
              <strong className="font-medium text-inchiostro">{m.dove.prenota}.</strong> {m.dove.prenotaTesto}
            </p>
            <div className="flex shrink-0 flex-wrap items-center gap-2">
              <a href={tel} className="btn btn-petrolio">
                <Segno nome="telefono" size={18} />
                {m.cta.chiamaSegreteria}
              </a>
              <Link href={href(l, { kind: "contatti" })} className="btn btn-osso">
                <Segno nome="mail" size={18} />
                {m.cta.scrivi}
              </Link>
            </div>
          </Reveal>
        )}
      </Sezione>

      {/* 2. DOVE OPERO: Le strutture chirurgiche con le foto reali */}
      <Sezione eyebrow={m.dove.chirurgia} titolo={m.dove.doveOperoTitolo} lead={m.dove.doveOperoLead} tinta="osso" compatta>
        <ul className="grid gap-x-10 gap-y-8 md:grid-cols-3">
          {sediChirurgia.map((x, i) => (
            <Reveal key={x.slug} as="li" delay={i * 70} className="min-w-0">
              <SchedaSede s={x} locale={l} />
            </Reveal>
          ))}
        </ul>
      </Sezione>

      <FasciaContatto locale={l} />
    </>
  );
}
