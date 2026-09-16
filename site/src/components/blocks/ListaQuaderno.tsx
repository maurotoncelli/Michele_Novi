import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { getMessages } from "@/i18n";
import type { VoceQuaderno } from "@/lib/content";
import { Reveal } from "../ui/Reveal";
import { SchedaNota, SchedaPaper } from "./Schede";
import { ListaEspandibile } from "./ListaEspandibile";

const LIMITE_PAPER = 3;

export function ListaQuaderno({
  voci,
  locale,
  tags,
  limitePaper = LIMITE_PAPER,
}: {
  voci: VoceQuaderno[];
  locale: Locale;
  tags?: { tag: string; n: number }[];
  limitePaper?: number;
}) {
  const m = getMessages(locale);
  let visti = 0;
  const preview: VoceQuaderno[] = [];
  const resto: VoceQuaderno[] = [];
  for (const v of voci) {
    if (v.tipo === "paper") {
      visti += 1;
      if (visti > limitePaper) {
        resto.push(v);
        continue;
      }
    }
    preview.push(v);
  }

  const card = (v: VoceQuaderno, i: number) => (
    <Reveal key={`${v.tipo}-${v.slug}`} as="li" delay={(i % 3) * 70}>
      {v.tipo === "paper" ? <SchedaPaper p={v.item} locale={locale} /> : <SchedaNota n={v.item} locale={locale} />}
    </Reveal>
  );

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
        <ListaEspandibile more={`${m.cta.mostraTutte} (${voci.filter((v) => v.tipo === "paper").length})`} less={m.cta.mostraMeno}>
          <ul className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">{preview.map(card)}</ul>
          {resto.length > 0 ? <ul className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">{resto.map((v, i) => card(v, i + preview.length))}</ul> : null}
        </ListaEspandibile>
      )}
    </div>
  );
}
