"use client";

import { useCallback, useSyncExternalStore } from "react";

export type VocePercorso = {
  periodo: string;
  titolo: string;
  luogo?: string | null;
};

export type BarraPercorso = {
  id: string;
  titolo: string;
  voci: VocePercorso[];
};

function progressoDi(el: HTMLElement) {
  const r = el.getBoundingClientRect();
  const vh = window.innerHeight;
  const start = vh * 0.72;
  const end = vh * 0.22;
  const span = r.height + (start - end);
  const scrolled = start - r.top;
  return Math.min(1, Math.max(0, scrolled / Math.max(span, 1)));
}

function subscribeScroll(onChange: () => void) {
  const on = () => onChange();
  window.addEventListener("scroll", on, { passive: true });
  window.addEventListener("resize", on);
  const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
  mq.addEventListener("change", on);
  const raf = requestAnimationFrame(on);
  return () => {
    cancelAnimationFrame(raf);
    window.removeEventListener("scroll", on);
    window.removeEventListener("resize", on);
    mq.removeEventListener("change", on);
  };
}

function pctDi(el: HTMLElement | null) {
  if (!el) return 0;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return 100;
  return Math.round(progressoDi(el) * 100);
}

function Traccia({ id, titolo, voci }: BarraPercorso) {
  const getEl = useCallback(() => document.getElementById(`barra-${id}`), [id]);
  const pct = useSyncExternalStore(
    subscribeScroll,
    () => pctDi(getEl()),
    () => 0,
  );
  const p = pct / 100;
  const attiva = Math.min(voci.length - 1, Math.floor(p * voci.length + 0.001));

  return (
    <article id={`barra-${id}`} className="osso flex h-full flex-col p-6">
      <header className="sticky top-20 z-10 -mx-2 mb-5 bg-osso px-2 pb-3 pt-1">
        <h2 className="text-[1.35rem] leading-tight">{titolo}</h2>
        <div
          className="mt-3 h-1.5 overflow-hidden rounded-full bg-osso-3"
          role="progressbar"
          aria-valuemin={0}
          aria-valuemax={100}
          aria-valuenow={pct}
          aria-label={titolo}
        >
          <div className="h-full rounded-full bg-petrolio transition-[width] duration-200 ease-osso" style={{ width: `${pct}%` }} />
        </div>
      </header>
      <ol className="relative flex-1 border-l border-linea pl-6">
        {voci.map((t, i) => {
          const on = i <= attiva;
          return (
            <li key={`${t.periodo}-${t.titolo}`} className="relative py-3">
              <span
                className={`absolute -left-[1.85rem] top-5 h-3 w-3 rounded-full border-2 border-osso transition-colors ${on ? "bg-petrolio-2" : "bg-osso-3"}`}
                aria-hidden="true"
              />
              <p className="text-xs font-semibold tracking-wide text-grafite">{t.periodo}</p>
              <p className={`mt-0.5 font-medium leading-snug ${on ? "text-inchiostro" : "text-inchiostro/70"}`}>{t.titolo}</p>
              {t.luogo ? <p className="text-sm text-grafite">{t.luogo}</p> : null}
            </li>
          );
        })}
      </ol>
    </article>
  );
}

/** Tre (o N) barre del curriculum: si riempiono scorrendo ciascuna colonna. */
export function BarrePercorso({ barre }: { barre: BarraPercorso[] }) {
  const visibili = barre.filter((b) => b.voci.length > 0);
  if (!visibili.length) return null;
  const cols = visibili.length === 1 ? "lg:grid-cols-1" : visibili.length === 2 ? "lg:grid-cols-2" : "lg:grid-cols-3";
  return (
    <div className={`grid gap-4 ${cols}`}>
      {visibili.map((b) => (
        <Traccia key={b.id} {...b} />
      ))}
    </div>
  );
}
