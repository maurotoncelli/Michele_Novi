"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";

export type Tappa = { anno: string; titolo: string; testo: string };

/**
 * Percorso a scorrimento: a sinistra l'anno grande e la lastra restano fermi (sticky),
 * a destra scorrono le tappe. Quella al centro dello schermo è accesa, le altre attenuate.
 * Sotto 1024px tutto scorre normalmente, niente attenuazione.
 */
export function PercorsoScorrevole({ tappe, media }: { tappe: Tappa[]; media?: ReactNode }) {
  const [attiva, setAttiva] = useState(0);
  const voci = useRef<(HTMLLIElement | null)[]>([]);

  useEffect(() => {
    if (typeof IntersectionObserver === "undefined") return;
    // Una fascia stretta a metà schermo: la tappa che la attraversa è quella attiva.
    const obs = new IntersectionObserver(
      (entries) => {
        for (const e of entries) {
          if (!e.isIntersecting) continue;
          const i = voci.current.indexOf(e.target as HTMLLIElement);
          if (i >= 0) setAttiva(i);
        }
      },
      { rootMargin: "-42% 0px -48% 0px", threshold: 0 },
    );
    for (const el of voci.current) if (el) obs.observe(el);
    return () => obs.disconnect();
  }, [tappe.length]);

  const corrente = tappe[attiva] ?? tappe[0];

  return (
    <div className="grid gap-12 lg:grid-cols-[minmax(0,0.9fr)_minmax(0,1.1fr)] lg:gap-24">
      <div className="lg:sticky lg:top-[calc(var(--header-h)+5rem)] lg:self-start">
        <p className="cifra hidden text-inchiostro lg:block" aria-hidden="true">
          <span key={corrente?.anno} className="anno-entra inline-block">
            {corrente?.anno}
          </span>
        </p>
        {media && <div className="mx-auto max-w-sm lg:mx-0 lg:mt-10 lg:max-w-none">{media}</div>}
      </div>

      <ol className="divide-y divide-linea">
        {tappe.map((t, i) => (
          <li
            key={i}
            ref={(el) => {
              voci.current[i] = el;
            }}
            data-attiva={i === attiva || undefined}
            className="py-10 first:pt-0 transition-opacity duration-500 ease-osso lg:min-h-[38vh] lg:py-14 lg:opacity-35 lg:data-attiva:opacity-100 motion-reduce:lg:opacity-100"
          >
            <p className="eyebrow text-rame">{t.anno}</p>
            <h3 className="mt-3 text-[1.5rem] leading-tight md:text-[1.9rem]">{t.titolo}</h3>
            {t.testo && <p className="lead mt-4 max-w-xl">{t.testo}</p>}
          </li>
        ))}
      </ol>
    </div>
  );
}
