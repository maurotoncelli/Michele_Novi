import Link from "next/link";
import type { Sintomo } from "@/lib/sintomi";
import { Reveal } from "../ui/Reveal";
import { Segno } from "../ui/Segno";

/**
 * Frasi "come le direbbe un paziente", ognuna verso il capitolo della scheda. La freccia sta sull'area: indica la destinazione, non lega le voci tra loro.
 * `compatto` = righe più basse, dove l'elenco non deve spingere sotto la piega quello che segue.
 */
export function ElencoSintomi({ sintomi, compatto = false }: { sintomi: Sintomo[]; compatto?: boolean }) {
  if (!sintomi.length) return null;
  return (
    <ul className="grid gap-x-10 border-t border-linea sm:grid-cols-2 lg:grid-cols-4">
      {sintomi.map((x, i) => (
        <Reveal key={x.href} as="li" delay={(i % 4) * 60} className="min-w-0 border-b border-linea">
          <Link href={x.href} className={`group block h-full ${compatto ? "py-3" : "py-4"}`}>
            <span className="block text-[1rem] leading-snug group-hover:text-petrolio">{x.testo}</span>
            <span className={`${compatto ? "mt-1" : "mt-1.5"} inline-flex items-center gap-1.5 text-[0.78rem] text-nebbia group-hover:text-petrolio`}>
              {x.area}
              <Segno nome="freccia" size={13} className="transition-transform duration-500 ease-osso group-hover:translate-x-1" />
            </span>
          </Link>
        </Reveal>
      ))}
    </ul>
  );
}
