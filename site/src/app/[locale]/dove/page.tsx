import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { getSedi, getSettings } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Briciole, Intestazione, Sezione } from "@/components/blocks/Pagina";
import { SchedaSede } from "@/components/blocks/Schede";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";

export async function generateMetadata({ params }: PageProps<"/[locale]/dove">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "dove" }, title: m.dove.titolo, description: m.meta.doveDescription });
}

export default async function DovePage({ params }: PageProps<"/[locale]/dove">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, sedi] = await Promise.all([getSettings(), getSedi()]);
  const m = getMessages(l);
  const visito = sedi.filter((x) => x.visite);
  const opero = sedi.filter((x) => x.chirurgia);

  const colonna = (titolo: string, lista: typeof sedi) => (
    <div className="min-w-0">
      <p className="eyebrow mb-6">{titolo}</p>
      <div className="grid gap-8">
        {lista.map((x, i) => (
          <Reveal key={x.slug} delay={i * 70}>
            <SchedaSede s={x} locale={l} />
          </Reveal>
        ))}
      </div>
    </div>
  );

  return (
    <>
      <JsonLd
        data={breadcrumbJsonLd(s, [
          { name: m.meta.siteName, path: href(l, { kind: "home" }) },
          { name: m.dove.titolo, path: href(l, { kind: "dove" }) },
        ])}
      />
      <Briciole items={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.nav.dove }]} />
      <Intestazione eyebrow={m.nav.dove} titolo={m.dove.titolo} lead={m.dove.lead} compatta />

      <Sezione>
        <div className="grid gap-14 lg:grid-cols-2 lg:gap-16 lg:divide-x lg:divide-linea">
          {colonna(m.dove.visito, visito)}
          {opero.length > 0 ? <div className="lg:pl-16">{colonna(m.dove.opero, opero)}</div> : null}
        </div>
      </Sezione>

      <FasciaContatto locale={l} />
    </>
  );
}
