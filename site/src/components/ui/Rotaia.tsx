"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";
import { Segno } from "@/components/ui/Segno";

/**
 * Rotaia: schede in fila che scorrono in orizzontale, a scatti, a filo del bordo destro della finestra.
 * Sotto, una linea che mostra dove sei e due frecce. Il resto è scroll nativo: trackpad, dito, rotella.
 */
export function Rotaia({ children, indietro, avanti }: { children: ReactNode; indietro: string; avanti: string }) {
  const ref = useRef<HTMLUListElement>(null);
  const [stato, setStato] = useState({ pos: 0, frazione: 1 });

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const aggiorna = () => {
      const max = el.scrollWidth - el.clientWidth;
      setStato({ pos: max > 0 ? el.scrollLeft / max : 0, frazione: el.scrollWidth > 0 ? el.clientWidth / el.scrollWidth : 1 });
    };
    aggiorna();
    el.addEventListener("scroll", aggiorna, { passive: true });
    const ro = new ResizeObserver(aggiorna);
    ro.observe(el);
    return () => {
      el.removeEventListener("scroll", aggiorna);
      ro.disconnect();
    };
  }, []);

  // Meta memorizzata: due clic veloci fanno due passi, non uno e mezzo.
  const meta = useRef<number | null>(null);
  const sposta = (dir: 1 | -1) => {
    const el = ref.current;
    if (!el) return;
    const prima = el.firstElementChild as HTMLElement | null;
    const passo = prima ? prima.offsetWidth + 24 : el.clientWidth * 0.8;
    const max = el.scrollWidth - el.clientWidth;
    const da = meta.current ?? el.scrollLeft;
    const a = Math.max(0, Math.min(max, Math.round(da / passo) * passo + dir * passo));
    meta.current = a;
    el.scrollTo({ left: a, behavior: "smooth" });
    window.setTimeout(() => {
      if (meta.current === a) meta.current = null;
    }, 600);
  };

  const scorre = stato.frazione < 0.999;
  const inizio = stato.pos <= 0.01;
  const fine = stato.pos >= 0.99;

  return (
    <div>
      <ul ref={ref} className="rotaia">
        {children}
      </ul>
      {scorre && (
        <div className="mt-8 flex items-center gap-6 md:mt-10">
          <div className="relative h-px flex-1 bg-linea" aria-hidden="true">
            <span
              className="absolute inset-y-[-1px] bg-petrolio"
              style={{ left: `${stato.pos * (1 - stato.frazione) * 100}%`, width: `${stato.frazione * 100}%` }}
            />
          </div>
          <div className="flex gap-2">
            <button type="button" onClick={() => sposta(-1)} disabled={inizio} aria-label={indietro} className="rotaia-freccia">
              <Segno nome="freccia" size={18} className="rotate-180" />
            </button>
            <button type="button" onClick={() => sposta(1)} disabled={fine} aria-label={avanti} className="rotaia-freccia">
              <Segno nome="freccia" size={18} />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
