import Link from "next/link";
import { Segno } from "../ui/Segno";
import { ListaEspandibile } from "./ListaEspandibile";

export type VocePubblicazione = {
  href: string;
  anno: number;
  titolo: string;
  rivista: string;
  pdf?: string | null;
  articolo?: string | null;
};

const INIZIALI = 3;

export function ListaPubblicazioni({
  voci,
  more,
  less,
  pdfLabel,
  articoloLabel,
  iniziali = INIZIALI,
}: {
  voci: VocePubblicazione[];
  more: string;
  less: string;
  pdfLabel: string;
  articoloLabel: string;
  iniziali?: number;
}) {
  if (!voci.length) return null;
  const prime = voci.slice(0, iniziali);
  const altre = voci.slice(iniziali);

  const riga = (x: VocePubblicazione) => (
    <li key={x.href} className="flex items-center gap-4 py-4">
      <Link href={x.href} className="group flex min-w-0 flex-1 items-baseline gap-4">
        <span className="w-12 shrink-0 text-sm text-grafite">{x.anno}</span>
        <span className="min-w-0 flex-1">
          <span className="serif block text-[1.1rem] leading-snug group-hover:text-petrolio">{x.titolo}</span>
          <span className="block text-sm text-grafite">{x.rivista}</span>
        </span>
        <Segno nome="freccia" size={18} className="hidden shrink-0 self-center text-nebbia group-hover:text-petrolio sm:block" />
      </Link>
      {x.pdf ? (
        <a href={x.pdf} target="_blank" rel="noopener noreferrer" className="btn btn-osso shrink-0 !px-3">
          <Segno nome="doc" size={16} />
          {pdfLabel}
        </a>
      ) : x.articolo ? (
        <a href={x.articolo} target="_blank" rel="noopener noreferrer" className="btn btn-osso shrink-0 !px-3">
          {articoloLabel}
          <Segno nome="esterno" size={16} />
        </a>
      ) : null}
    </li>
  );

  return (
    <ListaEspandibile more={`${more} (${voci.length})`} less={less}>
      <ol className="divide-y divide-linea border-t border-linea">{prime.map(riga)}</ol>
      {altre.length > 0 ? (
        <ol className="divide-y divide-linea">{altre.map(riga)}</ol>
      ) : null}
    </ListaEspandibile>
  );
}
