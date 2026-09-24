import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getFaq, getSedi, getSettings, telHref, waHref } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata, faqItems, faqJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Telefono } from "@/components/ui/Telefono";
import { Intestazione } from "@/components/blocks/Pagina";
import { Faq } from "@/components/blocks/Faq";
import { ModuloSede } from "@/components/blocks/Schede";
import { ContactForm } from "@/components/ContactForm";

export async function generateMetadata({ params }: PageProps<"/[locale]/contatti">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "contatti" }, title: m.contatti.titolo, description: m.meta.contattiDescription });
}

export default async function ContattiPage({ params }: PageProps<"/[locale]/contatti">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, sedi, faq] = await Promise.all([getSettings(), getSedi(), getFaq("contatti")]);
  const m = getMessages(l);
  const tel = telHref(s.telefono);
  const wa = waHref(s.whatsapp, pick(s.whatsappTesto, l));
  const orari = pick(s.orari, l);
  const domande = faqItems(faq, l);

  return (
    <>
      <JsonLd
        data={[
          faqJsonLd(domande),
          breadcrumbJsonLd(s, [
            { name: m.meta.siteName, path: href(l, { kind: "home" }) },
            { name: m.contatti.titolo, path: href(l, { kind: "contatti" }) },
          ]),
        ]}
      />
      <Intestazione
        eyebrow={m.nav.contatti}
        titolo={m.contatti.titolo}
        lead={m.contatti.lead}
        compatta
        percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.contatti.titolo }]}
      />

      <div className="contenitore grid gap-12 pb-16 pt-4 md:pt-8 lg:grid-cols-[1fr_1.3fr] lg:gap-20">
        {/* Canali: il numero è la cosa più grande della pagina. */}
        <div className="space-y-10">
          <Reveal className="relative space-y-6">
              <div>
                <p className="eyebrow">{m.contatti.telefono}</p>
                {tel ? (
                  <a href={tel} className="mt-3 block text-[1.6rem] font-medium leading-tight tracking-[-0.02em] text-petrolio hover:text-petrolio-2 md:text-[1.9rem]">
                    <Telefono numero={s.telefono} />
                  </a>
                ) : (
                  <p className="mt-3 max-w-md text-[1.15rem] leading-relaxed text-grafite">{m.contatti.telefonoMancante}</p>
                )}
              </div>
              {orari ? (
                <div>
                  <p className="eyebrow">{m.contatti.orari}</p>
                  <p className="mt-1 whitespace-pre-line text-grafite">{orari}</p>
                </div>
              ) : (
                <p className="text-sm text-nebbia">{m.contatti.orariMancanti}</p>
              )}
              {s.email && (
                <div>
                  <p className="eyebrow">{m.contatti.email}</p>
                  <a href={`mailto:${s.email}`} className="mt-1 block text-petrolio hover:text-petrolio-2">
                    {s.email}
                  </a>
                </div>
              )}
              {(tel || wa || s.email) && (
              <div className="flex flex-wrap gap-2 pt-1">
                {tel && (
                  <a href={tel} className="btn btn-petrolio">
                    <Segno nome="telefono" size={18} />
                    {m.cta.chiama}
                  </a>
                )}
                {wa && (
                  <a href={wa} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
                    <Segno nome="whatsapp" size={18} />
                    {m.cta.whatsapp}
                  </a>
                )}
                {s.email && (
                  <a href={`mailto:${s.email}`} className="btn btn-osso">
                    <Segno nome="mail" size={18} />
                    {m.contatti.email}
                  </a>
                )}
              </div>
              )}
              <p className="text-sm text-grafite">{m.contatti.costo}</p>
          </Reveal>

          <Reveal delay={80}>
            <p className="eyebrow">{m.nav.dove}</p>
            <ul className="mt-2 divide-y divide-linea border-y border-linea">
              {sedi.map((x) => (
                <li key={x.slug} className="min-w-0">
                  <ModuloSede s={x} locale={l} compatto />
                </li>
              ))}
            </ul>
          </Reveal>
        </div>

        {/* Form */}
        <Reveal delay={120} className="relative">
          <h2 className="display-m">{m.contatti.formTitolo}</h2>
          <p className="mt-3 mb-8 text-[0.98rem] text-grafite">{m.contatti.formLead}</p>
          <ContactForm
            locale={l}
            sedi={sedi.map((x) => ({ slug: x.slug, nome: x.nome, citta: x.citta ?? "" }))}
            privacyHref={href(l, { kind: "privacy" })}
            labels={{
              nome: m.contatti.nome,
              recapito: m.contatti.recapito,
              sede: m.contatti.sede,
              sedeQualsiasi: m.contatti.sedeQualsiasi,
              messaggio: m.contatti.messaggio,
              consenso: m.contatti.consenso,
              invia: m.contatti.invia,
              invio: m.contatti.invio,
              grazie: m.contatti.grazie,
              errore: m.contatti.errore,
              obbligatorio: m.contatti.obbligatorio,
              privacy: m.footer.privacy,
            }}
          />
        </Reveal>
      </div>

      {domande.length > 0 && (
        <section className="contenitore pb-24 md:pb-32">
          <div className="max-w-3xl">
            <Faq titolo={m.contatti.faq} items={domande} />
          </div>
        </section>
      )}
    </>
  );
}
