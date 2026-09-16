import type { Metadata } from "next";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getFaq, getSedi, getSettings, telHref, waHref } from "@/lib/content";
import { breadcrumbJsonLd, buildMetadata, faqItems, faqJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Briciole, Intestazione } from "@/components/blocks/Pagina";
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
      <Briciole items={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.contatti.titolo }]} />
      <Intestazione eyebrow={m.nav.contatti} titolo={m.contatti.titolo} lead={m.contatti.lead} compatta />

      <div className="contenitore grid gap-6 pb-12 lg:grid-cols-[1fr_1.3fr]">
        {/* Canali */}
        <div className="space-y-4">
          <Reveal className="osso cucitura relative overflow-hidden p-6 md:p-8">
            <div className="pointer-events-none absolute -right-16 -top-16 h-56 w-56 rounded-full bg-menta blur-3xl" aria-hidden="true" />
            <div className="relative space-y-5">
              <div>
                <p className="eyebrow">{m.contatti.telefono}</p>
                {tel ? (
                  <a href={tel} className="serif mt-1 block text-[2rem] leading-none text-petrolio hover:text-petrolio-2">
                    {s.telefono}
                  </a>
                ) : (
                  <p className="mt-1 text-grafite">{m.contatti.telefonoMancante}</p>
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
              <div className="incavo flex flex-wrap gap-2 p-2">
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
            </div>
          </Reveal>

          <Reveal delay={80} className="incavo p-2">
            <ul className="grid grid-cols-2 gap-2">
              {sedi.map((x) => (
                <li key={x.slug}>
                  <ModuloSede s={x} locale={l} />
                </li>
              ))}
            </ul>
          </Reveal>
        </div>

        {/* Form */}
        <Reveal delay={120} className="osso relative p-6 md:p-8">
          <h2 className="text-[1.6rem]">{m.contatti.formTitolo}</h2>
          <p className="mt-1 mb-6 text-sm text-grafite">{m.contatti.formLead}</p>
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
        <section className="contenitore pb-16">
          <div className="max-w-3xl">
            <Faq titolo={m.contatti.faq} items={domande} />
          </div>
        </section>
      )}
    </>
  );
}
