import type { Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import { legale } from "@/i18n/legale";
import type { Settings } from "@/lib/content";
import { siteUrl } from "@/lib/seo";
import { Reveal } from "../ui/Reveal";

export function Legale({ tipo, locale, settings }: { tipo: "privacy" | "cookie"; locale: Locale; settings: Settings }) {
  const m = getMessages(locale);
  const vars: Record<string, string> = {
    titolare: settings.nome,
    piva: settings.piva ?? "—",
    pec: settings.pec ?? "—",
    email: settings.email || "—",
    dominio: siteUrl(settings).replace(/^https?:\/\//, ""),
  };
  const fill = (s: string) => s.replace(/\{(\w+)\}/g, (_, k) => vars[k] ?? "");
  const blocchi = legale[tipo][locale];
  return (
    <div className="contenitore pb-16">
      <Reveal className="osso max-w-3xl p-7 md:p-10">
        <p className="tag tag-rame mb-6">{m.legale.bozza}</p>
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
      </Reveal>
    </div>
  );
}
