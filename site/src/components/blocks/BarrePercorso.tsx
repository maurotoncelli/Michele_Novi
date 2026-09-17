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

/** 0 quando il primo puntino è sotto la linea di lettura, 1 quando l'ultimo la attraversa. */
function progressoDi(el: HTMLElement) {
  const voci = [...el.querySelectorAll<HTMLElement>("[data-voce]")];
  if (!voci.length) return 0;
  const trigger = window.innerHeight * 0.48;
  const primo = voci[0].getBoundingClientRect();
  const ultimo = voci[voci.length - 1].getBoundingClientRect();
  const start = primo.top + primo.height / 2;
  const end = ultimo.top + ultimo.height / 2;
  const span = end - start;
  if (span <= 1) return trigger >= start ? 1 : 0;
  return Math.min(1, Math.max(0, (trigger - start) / span));
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

function snapshot(el: HTMLElement | null) {
  if (!el) return "0|0|0|";
  const voci = [...el.querySelectorAll<HTMLElement>("[data-voce]")];
  if (!voci.length) return "0|0|0|";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const trigger = window.innerHeight * 0.48;
  const on = reduce
    ? "1".repeat(voci.length)
    : voci.map((v) => (v.getBoundingClientRect().top + 20 <= trigger ? "1" : "0")).join("");
  const p = reduce ? 1 : progressoDi(el);
  const primo = voci[0].offsetTop + 20;
  const ultimo = voci[voci.length - 1].offsetTop + 20;
  const span = Math.max(0, ultimo - primo);
  const fill = Math.round(span * p);
  return `${Math.round(p * 100)}|${fill}|${span}|${on}`;
}

function Traccia({ id, titolo, voci }: BarraPercorso) {
  const getEl = useCallback(() => document.getElementById(`barra-${id}`), [id]);
  const snap = useSyncExternalStore(
    subscribeScroll,
    () => snapshot(getEl()),
    () => "0|0|0|",
  );
  const [pctText, fillText, spanText, onBits = ""] = snap.split("|");
  const pct = Number(pctText) || 0;
  const fill = Number(fillText) || 0;
  const span = Number(spanText) || 0;

  return (
    <article className="osso flex h-full flex-col p-6">
      <h2 className="text-[1.35rem] leading-tight">{titolo}</h2>
      <ol id={`barra-${id}`} className="relative mt-5 flex-1 pl-8" aria-label={titolo}>
        <div
          className="pointer-events-none absolute left-[0.69rem] top-5 w-[3px] -translate-x-1/2 overflow-hidden rounded-full bg-osso-3"
          style={{ height: span || undefined }}
          role="progressbar"
          aria-valuemin={0}
          aria-valuemax={100}
          aria-valuenow={pct}
          aria-label={titolo}
        >
          <div className="absolute inset-x-0 top-0 rounded-full bg-petrolio transition-[height] duration-200 ease-osso" style={{ height: fill }} />
        </div>
        {voci.map((t, i) => {
          const on = onBits[i] === "1";
          return (
            <li key={`${t.periodo}-${t.titolo}`} data-voce className="relative py-3 first:pt-0 last:pb-0">
              <span
                className={`absolute left-[0.69rem] top-5 z-[1] h-3.5 w-3.5 -translate-x-1/2 rounded-full border-2 border-osso transition-colors duration-200 ${on ? "bg-petrolio" : "bg-osso-3"}`}
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

/** Tre (o N) barre verticali del curriculum: il tratto riempie i puntini scorrendo. */
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
