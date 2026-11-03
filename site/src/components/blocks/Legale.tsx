import type { Locale } from "@/i18n/routing";
import { legale } from "@/i18n/legale";
import type { Settings } from "@/lib/content";
import { siteUrl } from "@/lib/seo";
import { BottonePreferenzeCookie } from "../CookieBanner";
import { Reveal } from "../ui/Reveal";

export function Legale({ tipo, locale, settings }: { tipo: "privacy" | "cookie"; locale: Locale; settings: Settings }) {
  const vars: Record<string, string> = {
    titolare: settings.nome,
    piva: settings.piva || "02296540509",
    albo: settings.albo || "OMCeO Pisa n. 5749",
    pec: settings.pec || "michele.novi.w5is@pi.omceo.it",
    email: settings.email || settings.pec || "michele.novi.w5is@pi.omceo.it",
    dominio: siteUrl(settings).replace(/^https?:\/\//, ""),
  };
  const fill = (s: string) => s.replace(/\{(\w+)\}/g, (_, k) => vars[k] ?? "");
  const blocchi = legale[tipo][locale];
  return (
    <div className="contenitore pb-16 pt-4 md:pb-24">
      <Reveal className="max-w-3xl">
        <div className="testo">
          {blocchi.map((b, i) => (
            <section key={i}>
              {b.h && <h2>{b.h}</h2>}
              {b.p.map((p, j) => (
                <p key={j}>{fill(p)}</p>
              ))}
            </section>
          ))}
        </div>
        {tipo === "cookie" && (
          <BottonePreferenzeCookie
            label={locale === "en" ? "Review cookie preferences" : "Rivedi preferenze cookie"}
          />
        )}
      </Reveal>
    </div>
  );
}
