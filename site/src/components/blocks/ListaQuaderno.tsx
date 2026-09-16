import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import type { VoceQuaderno } from "@/lib/content";
import { Reveal } from "../ui/Reveal";
import { SchedaNota, SchedaPaper } from "./Schede";

export function ListaQuaderno({ voci, locale, tags }: { voci: VoceQuaderno[]; locale: Locale; tags?: { tag: string; n: number }[] }) {
  const m = getMessages(locale);
  return (
    <div className="contenitore py-10">
      {tags && tags.length > 0 && (
        <Reveal className="mb-8 flex flex-wrap items-center gap-2">
          <span className="eyebrow mr-1">{m.quaderno.tag}</span>
          {tags.map((t) => (
            <Link key={t.tag} href={href(locale, { kind: "tag", tag: t.tag })} className="tag hover:bg-petrolio-3 hover:text-petrolio">
              {t.tag} <span className="text-nebbia">{t.n}</span>
            </Link>
          ))}
        </Reveal>
      )}
      {voci.length === 0 ? (
        <p className="py-16 text-center text-grafite">{m.quaderno.vuoto}</p>
      ) : (
        <ul className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {voci.map((v, i) => (
            <Reveal key={`${v.tipo}-${v.slug}`} as="li" delay={(i % 3) * 70}>
              {v.tipo === "paper" ? <SchedaPaper p={v.item} locale={locale} /> : <SchedaNota n={v.item} locale={locale} />}
            </Reveal>
          ))}
        </ul>
      )}
    </div>
  );
}
