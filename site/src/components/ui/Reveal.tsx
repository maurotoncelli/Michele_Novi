"use client";

import { useEffect, useRef, type ReactNode, type CSSProperties } from "react";

/**
 * Apparizione graduale. Un solo IntersectionObserver per pagina, condiviso.
 * Rispetta prefers-reduced-motion (il CSS annulla la transizione).
 */
let observer: IntersectionObserver | null = null;
function getObserver() {
  if (observer) return observer;
  observer = new IntersectionObserver(
    (entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          e.target.classList.add("is-in");
          observer?.unobserve(e.target);
        }
      }
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.08 },
  );
  return observer;
}

export function Reveal({
  children,
  as: Tag = "div",
  className = "",
  delay = 0,
  immediate = false,
  maschera = false,
  solo = false,
  style,
  ...rest
}: {
  children: ReactNode;
  as?: keyof React.JSX.IntrinsicElements;
  className?: string;
  delay?: number;
  /** Above-the-fold: visibile al paint, niente fade. */
  immediate?: boolean;
  /** Titoli display: maschera di riga invece del fade. */
  maschera?: boolean;
  /** Nessun effetto proprio: mette solo `is-in`, e sono i figli (es. .parola) ad animarsi. */
  solo?: boolean;
  style?: CSSProperties;
} & Record<string, unknown>) {
  const ref = useRef<HTMLElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el || immediate) return;
    if (typeof IntersectionObserver === "undefined") {
      el.classList.add("is-in");
      return;
    }
    const obs = getObserver();
    obs.observe(el);
    return () => obs.unobserve(el);
  }, [immediate]);
  const Comp = Tag as React.ElementType;
  return (
    <Comp
      ref={ref}
      className={immediate ? className : `${maschera ? "reveal-maschera" : solo ? "reveal-solo" : "reveal"} ${className}`}
      style={immediate ? style : ({ ...style, "--reveal-delay": `${delay}ms` } as CSSProperties)}
      {...rest}
    >
      {/* La maschera sta su un figlio: Chrome tiene conto del clip-path del target nell'IntersectionObserver. */}
      {maschera && !immediate ? <span className="maschera-interno">{children}</span> : children}
    </Comp>
  );
}
