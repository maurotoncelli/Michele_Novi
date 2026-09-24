import type { Metadata } from "next";
import Link from "next/link";
import { href, isLocale, type Locale } from "@/i18n/routing";
import { getMessages, pick } from "@/i18n";
import { getPaginaCosaCuro, getPatologie, getSettings, type Patologia } from "@/lib/content";
import { getSintomi, hrefPatologia, temiDi } from "@/lib/sintomi";
import { breadcrumbJsonLd, buildMetadata, faqItems, faqJsonLd, patologieListJsonLd } from "@/lib/seo";
import { JsonLd } from "@/components/JsonLd";
import { Reveal } from "@/components/ui/Reveal";
import { Segno } from "@/components/ui/Segno";
import { Disclaimer, Intestazione, Sezione } from "@/components/blocks/Pagina";
import { SchedaMetodo, SchedaPatologia, SchedaSecondaria } from "@/components/blocks/Schede";
import { Faq } from "@/components/blocks/Faq";
import { FasciaContatto } from "@/components/blocks/FasciaContatto";
import { ElencoSintomi } from "@/components/blocks/Sintomi";

export async function generateMetadata({ params }: PageProps<"/[locale]/cosa-curo">): Promise<Metadata> {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const s = await getSettings();
  const m = getMessages(l);
  return buildMetadata(s, { locale: l, route: { kind: "cosaCuro" }, title: m.cosaCuro.titolo, description: m.meta.cosaCuroDescription });
}

export default async function CosaCuroPage({ params }: PageProps<"/[locale]/cosa-curo">) {
  const { locale } = await params;
  const l = (isLocale(locale) ? locale : "it") as Locale;
  const [s, patologie, pagina] = await Promise.all([getSettings(), getPatologie(), getPaginaCosaCuro()]);
  const m = getMessages(l);
  const metodo = patologie.find((p) => p.area === "metodo");
  const spalla = patologie.find((p) => p.area === "spalla");
  const resto = patologie.filter((p) => !p.secondaria && p !== metodo && p !== spalla);
  const secondarie = patologie.filter((p) => p.secondaria);
  const principali = [spalla, ...resto].filter((p): p is Patologia => !!p);

  const temiPer = new Map(await Promise.all(principali.map(async (p) => [p.slug, await temiDi(p, l)] as const)));
  const link = (p: Patologia, ancora?: string) => hrefPatologia(p, l, ancora);
  const sintomi = await getSintomi(patologie, l);
  const percorso = pagina.percorso.map((x) => ({ titolo: pick(x.titolo, l), testo: pick(x.testo, l) })).filter((x) => x.titolo);

  // Una domanda per area, la prima di ogni scheda: le altre stanno nelle pagine.
  const faq = [...principali, ...(metodo ? [metodo] : [])].flatMap((p) => faqItems(p.faq, l).slice(0, 1));

  return (
    <>
      <JsonLd
        data={[
          breadcrumbJsonLd(s, [
            { name: m.meta.siteName, path: href(l, { kind: "home" }) },
            { name: m.cosaCuro.titolo, path: href(l, { kind: "cosaCuro" }) },
          ]),
          patologieListJsonLd(
            s,
            [...principali, ...(metodo ? [metodo] : []), ...secondarie].map((p) => ({ name: pick(p.titolo, l), path: link(p), description: pick(p.lead, l) })),
          ),
          faqJsonLd(faq),
        ]}
      />
      <Intestazione
        eyebrow={m.cosaCuro.eyebrow}
        titolo={m.cosaCuro.titolo}
        lead={m.cosaCuro.lead}
        compatta
        percorso={[{ label: m.meta.siteName, href: href(l, { kind: "home" }) }, { label: m.cosaCuro.titolo }]}
      />

      {sintomi.length > 0 && (
        <section id="sintomi" className="ancora border-b border-linea">
          <div className="contenitore py-10 md:py-14">
            <Reveal>
              <p className="eyebrow mb-3">{m.cosaCuro.sintomiEyebrow}</p>
              <h2 className="max-w-3xl text-[1.65rem] leading-tight md:text-[1.85rem]">{m.cosaCuro.sintomiTitolo}</h2>
              <p className="mt-2 max-w-2xl text-[1.02rem] leading-relaxed text-grafite">{m.cosaCuro.sintomiLead}</p>
            </Reveal>
            <div className="mt-6">
              <ElencoSintomi sintomi={sintomi} />
            </div>
          </div>
        </section>
      )}

      <Sezione compatta>
        <h2 className="display-m max-w-3xl">{m.home.cosaCuroTitolo}</h2>
        {spalla && (
          <>
            <Reveal className="mt-8 md:mt-10">
              <SchedaPatologia p={spalla} locale={l} ampia />
            </Reveal>
            {(temiPer.get(spalla.slug)?.length ?? 0) > 0 && (
              <div className="mt-10">
                <p className="eyebrow mb-4">{m.cosaCuro.temiEyebrow}</p>
                <ul className="grid gap-x-8 gap-y-6 border-t border-linea pt-6 sm:grid-cols-2 lg:grid-cols-4">
                  {temiPer.get(spalla.slug)!.map((t, i) => (
                    <Reveal key={t.id} as="li" delay={i * 70} className="min-w-0">
                      <Link href={link(spalla, t.id)} className="group block">
                        <span className="eyebrow block">{String(i + 1).padStart(2, "0")}</span>
                        <span className="mt-2 block text-[1.2rem] leading-tight group-hover:text-petrolio">{t.text}</span>
                        <span className="mt-2 block text-[0.92rem] leading-relaxed text-grafite">{t.frase}</span>
                      </Link>
                    </Reveal>
                  ))}
                </ul>
                <Link href={href(l, { kind: "contatti" })} className="btn btn-ghost -ml-3 mt-6">
                  {m.cosaCuro.prenotaSpalla}
                  <Segno nome="freccia" size={18} />
                </Link>
              </div>
            )}
          </>
        )}
        {resto.length > 0 && (
          <div className="mt-10 border-t border-linea pt-8 md:mt-12 md:pt-10">
            <Reveal>
              <h2 className="max-w-3xl text-[1.65rem] leading-tight md:text-[1.85rem]">{m.home.cosaCuroRestoTitolo}</h2>
              <p className="mt-2 max-w-2xl text-[1.02rem] leading-relaxed text-grafite">{m.home.cosaCuroRestoLead}</p>
            </Reveal>
            <ul className="mt-6 grid items-start gap-x-10 gap-y-10 sm:grid-cols-2">
              {resto.map((p, i) => (
                <Reveal key={p.slug} as="li" delay={i * 80} className="min-w-0">
                  <SchedaPatologia p={p} locale={l} riga />
                  {(temiPer.get(p.slug)?.length ?? 0) > 0 && (
                    <ul className="mt-4 flex flex-wrap gap-x-3 gap-y-1 border-t border-linea pt-3 text-[0.88rem] text-grafite">
                      {temiPer.get(p.slug)!.map((t) => (
                        <li key={t.id}>
                          <Link href={link(p, t.id)} className="underline decoration-linea underline-offset-4 hover:text-petrolio hover:decoration-petrolio">
                            {t.text}
                          </Link>
                        </li>
                      ))}
                    </ul>
                  )}
                </Reveal>
              ))}
            </ul>
            {secondarie.length > 0 && (
              <Reveal className="mt-10">
                <p className="eyebrow mb-3">{m.cosaCuro.secondarie}</p>
                <ul className="flex flex-wrap gap-x-6 gap-y-2">
                  {secondarie.map((p) => (
                    <li key={p.slug}>
                      <SchedaSecondaria p={p} locale={l} />
                    </li>
                  ))}
                </ul>
              </Reveal>
            )}
          </div>
        )}
      </Sezione>

      {metodo && (
        <section className="border-t border-linea">
          <Reveal className="contenitore py-16 md:py-24">
            <SchedaMetodo p={metodo} locale={l} />
          </Reveal>
        </section>
      )}

      <Sezione tinta="osso">
        <p className="eyebrow mb-4">{m.cosaCuro.percorsoEyebrow}</p>
        <Reveal as="h2" maschera className="citazione-l max-w-4xl">
          {m.cosaCuro.chiusura}
        </Reveal>
        {percorso.length > 0 && (
        <ol className="mt-12 grid gap-x-8 gap-y-8 border-t border-linea pt-8 sm:grid-cols-2 lg:grid-cols-4">
          {percorso.map((passo, i) => (
            <Reveal key={passo.titolo} as="li" delay={i * 90} className="min-w-0">
              <span className="eyebrow block">{String(i + 1).padStart(2, "0")}</span>
              <h3 className="mt-2 text-[1.25rem] leading-tight">{passo.titolo}</h3>
              <p className="mt-2 text-[0.95rem] leading-relaxed text-grafite">{passo.testo}</p>
            </Reveal>
          ))}
        </ol>
        )}
        <Disclaimer testo={m.cosaCuro.disclaimer} />
      </Sezione>

      {faq.length > 0 && (
        <Sezione compatta>
          <div className="max-w-[44rem]">
            <Faq titolo={m.cosaCuro.faq} items={faq} />
          </div>
        </Sezione>
      )}

      <FasciaContatto locale={l} />
    </>
  );
}
