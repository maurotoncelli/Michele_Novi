import Link from "next/link";
import { Segno } from "../ui/Segno";
import { ListaEspandibile } from "./ListaEspandibile";

export type VocePubblicazione = {
  href: string;
  anno: number;
  titolo: string;
  rivista: string;
};

const INIZIALI = 3;

export function ListaPubblicazioni({
  voci,
  more,
  less,
  iniziali = INIZIALI,
}: {
  voci: VocePubblicazione[];
  more: string;
  less: string;
  iniziali?: number;
}) {
  if (!voci.length) return null;
  const prime = voci.slice(0, iniziali);
  const altre = voci.slice(iniziali);

  const riga = (x: VocePubblicazione) => (
    <li key={x.href}>
      <Link href={x.href} className="group flex items-baseline gap-4 px-6 py-4 hover:bg-osso-2/60">
        <span className="w-12 shrink-0 text-sm text-grafite">{x.anno}</span>
        <span className="flex-1">
          <span className="serif block text-[1.1rem] leading-snug group-hover:text-petrolio">{x.titolo}</span>
          <span className="block text-sm text-grafite">{x.rivista}</span>
        </span>
        <Segno nome="freccia" size={18} className="hidden shrink-0 self-center text-nebbia group-hover:text-petrolio sm:block" />
      </Link>
    </li>
  );

  return (
    <ListaEspandibile more={`${more} (${voci.length})`} less={less}>
      <ol className="divide-y divide-linea overflow-hidden rounded-[1.75rem] border border-linea bg-osso">{prime.map(riga)}</ol>
      {altre.length > 0 ? (
        <ol className="divide-y divide-linea overflow-hidden rounded-[1.75rem] border border-linea bg-osso">{altre.map(riga)}</ol>
      ) : null}
    </ListaEspandibile>
  );
}
