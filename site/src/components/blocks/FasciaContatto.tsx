import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getSettings, telHref, waHref } from "@/lib/content";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";

/** Chiusura contatto: telefono, WhatsApp, form. Mai Doctolib come bottone principale. */
export async function FasciaContatto({ locale, titolo, lead }: { locale: Locale; titolo?: string; lead?: string }) {
  const s = await getSettings();
  const m = getMessages(locale);
  const tel = telHref(s.telefono);
  const wa = waHref(s.whatsapp, pick(s.whatsappTesto, locale));
  const orari = pick(s.orari, locale);

  return (
    <section className="contenitore py-12 md:py-16" aria-labelledby="contatto-titolo">
      <Reveal className="osso osso-lg cucitura relative overflow-hidden p-8 md:p-12">
        <div className="pointer-events-none absolute -right-20 -top-24 h-72 w-72 rounded-full bg-menta/80 blur-3xl" aria-hidden="true" />
        <div className="pointer-events-none absolute -bottom-24 -left-16 h-64 w-64 rounded-full bg-pesca/90 blur-3xl" aria-hidden="true" />
        <div className="relative grid gap-8 md:grid-cols-[1.2fr_1fr] md:items-center">
          <div>
            <h2 id="contatto-titolo" className="text-[2rem] leading-tight md:text-[2.6rem]">
              {titolo ?? m.home.contattoTitolo}
            </h2>
            <p className="mt-3 max-w-lg text-[1.05rem] text-grafite">{lead ?? m.home.contattoLead}</p>
            {orari && (
              <p className="mt-4 inline-flex items-start gap-2 text-sm text-grafite">
                <Segno nome="orologio" size={18} className="mt-0.5 shrink-0 text-nebbia" />
                <span className="whitespace-pre-line">{orari}</span>
              </p>
            )}
          </div>
          <div className="incavo flex flex-wrap items-center gap-2 p-3 md:justify-end">
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
        </div>
      </Reveal>
    </section>
  );
}
