import type { Metadata } from "next";
import type { CSSProperties } from "react";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getSedi, getSettings } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Intestazione, Sezione } from "@/components/blocks/Pagina";
import { SchedaSede } from "@/components/blocks/Schede";
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
  const visito = sedi.filter((x) => x.visite);
  const opero = sedi.filter((x) => x.chirurgia);
  const righe = Math.max(visito.length, opero.length);

  const colonna = (titolo: string, lista: typeof sedi) => (
    <div className="dove-colonna">
      <p className="eyebrow">{titolo}</p>
      {lista.map((x, i) => (
        <Reveal key={x.slug} delay={i * 70} className="h-full min-w-0">
          <SchedaSede s={x} locale={l} />
        </Reveal>
      ))}
    </div>
  );

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

      <Sezione stretta>
        <div className="dove-griglia" style={{ "--righe": righe } as CSSProperties}>
          {colonna(m.dove.visito, visito)}
          {opero.length > 0 ? <div className="dove-divisore" aria-hidden="true" /> : null}
          {opero.length > 0 ? colonna(m.dove.opero, opero) : null}
        </div>
        <p className="mt-10 text-[0.8rem] text-nebbia">
          <a href="/images/sedi/ATTRIBUZIONI.txt" className="underline decoration-linea underline-offset-4 hover:text-petrolio">
            {m.dove.fotoCitta}
          </a>
        </p>
      </Sezione>

      <FasciaContatto locale={l} />
    </>
  );
}
