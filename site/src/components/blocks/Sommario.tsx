"use client";

import { useEffect, useState } from "react";

export type VoceSommario = { id: string; label: string };

/**
 * Sommario che segue la lettura: sticky a sinistra, la voce della sezione
 * che sta passando a un terzo dello schermo si accende. Solo ancore: senza JS
 * è una lista di link che funziona lo stesso.
 */
export function Sommario({ voci, eyebrow }: { voci: VoceSommario[]; eyebrow: string }) {
  const [attiva, setAttiva] = useState<string | null>(voci[0]?.id ?? null);

  useEffect(() => {
    // Poche misure per evento (una per voce): gli eventi scroll sono già allineati al frame, niente rAF.
    const soglia = () => window.innerHeight * 0.33;
    const aggiorna = () => {
      let corrente: string | null = voci[0]?.id ?? null;
      for (const v of voci) {
        const el = document.getElementById(v.id);
        if (!el) continue;
        if (el.getBoundingClientRect().top <= soglia()) corrente = v.id;
        else break;
      }
      // In fondo alla pagina l'ultima voce vince, anche se il suo titolo non è arrivato a un terzo.
      if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2) corrente = voci[voci.length - 1]?.id ?? corrente;
      setAttiva(corrente);
    };
    aggiorna();
    window.addEventListener("scroll", aggiorna, { passive: true });
    window.addEventListener("resize", aggiorna);
    return () => {
      window.removeEventListener("scroll", aggiorna);
      window.removeEventListener("resize", aggiorna);
    };
  }, [voci]);

  if (voci.length < 2) return null;

  return (
    <nav aria-label={eyebrow} className="sommario">
      <p className="eyebrow mb-4">{eyebrow}</p>
      <ol>
        {voci.map((v, i) => (
          <li key={v.id}>
            <a href={`#${v.id}`} data-attiva={v.id === attiva || undefined} className="sommario-voce">
              <span className="sommario-indice">{String(i + 1).padStart(2, "0")}</span>
              <span className="sommario-testo">{v.label}</span>
            </a>
          </li>
        ))}
      </ol>
    </nav>
  );
}
