"use client";

import { useEffect, useRef, type ReactNode } from "react";

/**
 * Strati: le card entrano impilate e si aprono a ventaglio con lo scroll,
 * come tessuti che si separano. Guidato da una sola variabile CSS (--apertura).
 * Con prefers-reduced-motion il CSS mostra le card già aperte.
 */
export function Strati({ children, className = "" }: { children: ReactNode; className?: string }) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      el.style.setProperty("--apertura", "1");
      return;
    }
    let raf = 0;
    const update = () => {
      raf = 0;
      const r = el.getBoundingClientRect();
      const vh = window.innerHeight;
      // 0 quando il bordo superiore è al fondo del viewport, 1 quando è al 35% dall'alto
      const t = (vh - r.top) / (vh * 0.65);
      const a = Math.min(1, Math.max(0, t));
      el.style.setProperty("--apertura", a.toFixed(3));
    };
    const onScroll = () => {
      if (!raf) raf = requestAnimationFrame(update);
    };
    update();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      if (raf) cancelAnimationFrame(raf);
    };
  }, []);

  return (
    <div ref={ref} className={`strati ${className}`}>
      {children}
    </div>
  );
}
