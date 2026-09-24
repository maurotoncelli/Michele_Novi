import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getSedi, getSettings, telHref, waHref } from "@/lib/content";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";
import { Telefono } from "../ui/Telefono";

/**
 * Chiusura: l'unica fascia scura del sito. Telefono in display quando c'è, tre azioni, le città.
 * Mai Doctolib come bottone principale. Niente urgenza.
 */
export async function FasciaContatto({ locale, titolo, lead }: { locale: Locale; titolo?: string; lead?: string }) {
  const [s, sedi] = await Promise.all([getSettings(), getSedi()]);
  const m = getMessages(locale);
  const tel = telHref(s.telefono);
  const wa = waHref(s.whatsapp, pick(s.whatsappTesto, locale));
  const orari = pick(s.orari, locale);
  const citta = [...new Set(sedi.map((x) => x.citta).filter(Boolean))];

  return (
    <section className="fascia-scura" aria-labelledby="contatto-titolo">
      <div className="contenitore py-20 md:py-28 lg:py-32">
        <div className="grid gap-12 lg:grid-cols-[minmax(0,1.25fr)_minmax(0,1fr)] lg:items-end lg:gap-20">
          <div>
            <Reveal as="p" className="eyebrow mb-5">
              {m.nav.contatti}
            </Reveal>
            <Reveal as="h2" maschera id="contatto-titolo" className="display-l">
              {titolo ?? m.home.contattoTitolo}
            </Reveal>
            <Reveal as="p" delay={120} className="lead mt-6 max-w-xl text-osso/70">
              {lead ?? m.home.contattoLead}
            </Reveal>
            {tel && (
              <Reveal delay={200} className="mt-10">
                <a href={tel} className="display-m inline-block text-osso transition-colors hover:text-[var(--color-petrolio-chiaro)]">
                  <Telefono numero={s.telefono ?? ""} />
                </a>
              </Reveal>
            )}
            {orari && (
              <Reveal as="p" delay={240} className="mt-4 inline-flex items-start gap-2 text-sm text-osso/60">
                <Segno nome="orologio" size={18} className="mt-0.5 shrink-0" />
                <span className="whitespace-pre-line">{orari}</span>
              </Reveal>
            )}
          </div>

          <Reveal delay={160} className="flex flex-col gap-8 lg:items-end">
            <div className="flex flex-wrap items-center gap-2 lg:justify-end">
              {tel && (
                <a href={tel} className="btn btn-petrolio">
                  <Segno nome="telefono" size={18} />
                  {m.cta.chiamaSegreteria}
                </a>
              )}
              {wa && (
                <a href={wa} target="_blank" rel="noopener noreferrer" className="btn btn-osso">
                  <Segno nome="whatsapp" size={18} />
                  {m.cta.whatsapp}
                </a>
              )}
              <Link href={href(locale, { kind: "contatti" })} className={`btn ${tel ? "btn-osso" : "btn-petrolio"}`}>
                <Segno nome="mail" size={18} />
                {m.cta.scrivi}
              </Link>
            </div>
            {citta.length > 0 && (
              <p className="flex flex-wrap gap-x-3 gap-y-1 text-[0.95rem] text-osso/55 lg:justify-end">
                {citta.map((c, i) => (
                  <span key={c} className="inline-flex items-center gap-3">
                    {i > 0 && <span aria-hidden="true">·</span>}
                    {c}
                  </span>
                ))}
              </p>
            )}
          </Reveal>
        </div>
      </div>
    </section>
  );
}
