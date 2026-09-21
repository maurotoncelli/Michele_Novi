"use client";

import { useEffect, useRef } from "react";

/**
 * Cifra che si conta quando entra in vista. Il server rende già il valore finale:
 * senza JS, o con reduced-motion, non cambia nulla.
 */
export function Contatore({ valore, className }: { valore: string; className?: string }) {
  const ref = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    const el = ref.current;
    const fine = Number.parseInt(valore, 10);
    if (!el || !Number.isFinite(fine)) return;
    if (typeof IntersectionObserver === "undefined") return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    // Gli anni partono da poco prima, i numeri piccoli da zero.
    const inizio = fine > 100 ? fine - 24 : 0;
    const durata = 1100;
    let raf = 0;

    const obs = new IntersectionObserver(
      ([e]) => {
        if (!e?.isIntersecting) return;
        obs.disconnect();
        const t0 = performance.now();
        const passo = (t: number) => {
          const p = Math.min(1, (t - t0) / durata);
          const k = 1 - Math.pow(1 - p, 3);
          el.textContent = String(Math.round(inizio + (fine - inizio) * k));
          if (p < 1) raf = requestAnimationFrame(passo);
        };
        raf = requestAnimationFrame(passo);
      },
      { threshold: 0.4 },
    );
    obs.observe(el);
    return () => {
      obs.disconnect();
      cancelAnimationFrame(raf);
    };
  }, [valore]);

  return (
    <span ref={ref} className={className}>
      {valore}
    </span>
  );
}
