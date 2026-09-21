import { Segno } from "../ui/Segno";

/** FAQ come details/summary: accessibili, senza JS, con il bordo osseo. */
export function Faq({ items, titolo }: { items: { domanda: string; risposta: string }[]; titolo?: string }) {
  if (!items.length) return null;
  return (
    <div>
      {titolo && <h2 className="mb-6 text-[1.7rem] md:text-[2rem]">{titolo}</h2>}
      <div className="divide-y divide-linea border-y border-linea">
        {items.map((f, i) => (
          <details key={i} className="group">
            <summary className="flex cursor-pointer list-none items-center justify-between gap-4 px-6 py-4 text-[1.02rem] font-medium marker:content-none hover:bg-osso-2/60 [&::-webkit-details-marker]:hidden">
              {f.domanda}
              <span className="incavo grid h-8 w-8 shrink-0 place-items-center text-petrolio transition group-open:rotate-45">
                <Segno nome="piu" size={16} />
              </span>
            </summary>
            <div className="px-6 pb-5 text-[0.98rem] leading-relaxed text-grafite">{f.risposta}</div>
          </details>
        ))}
      </div>
    </div>
  );
}
