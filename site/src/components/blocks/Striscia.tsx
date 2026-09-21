import type { CSSProperties, ReactNode } from "react";
import { TestaSezione } from "@/components/blocks/Pagina";

/**
 * Striscia: su desktop la sezione si appunta e le schede scorrono in orizzontale mentre la pagina scende
 * (animazione guidata dallo scroll, solo CSS: niente frecce, niente listener). Su telefono, e dove le
 * animazioni da scroll non ci sono, è una colonna normale. `scheda` e `gap` fissano il passo: la sezione
 * si alza di quanto le schede devono correre, così il rapporto scroll/scorrimento resta circa 1:1.
 */
export function Striscia({
  id,
  tinta,
  testa,
  children,
  n,
  scheda,
  gap,
  className = "",
}: {
  id?: string;
  tinta?: "osso";
  testa: Parameters<typeof TestaSezione>[0];
  children: ReactNode;
  n: number;
  /** Larghezza di una scheda sulla striscia (rem). */
  scheda: number;
  /** Spazio tra schede (rem). */
  gap: number;
  className?: string;
}) {
  const style = { "--n": n, "--scheda": `${scheda}rem`, "--gap": `${gap}rem` } as CSSProperties;
  return (
    <section id={id} className={`striscia ${tinta === "osso" ? "bg-osso-3 trama" : ""} ${className}`} style={style}>
      <div className="striscia-fissa">
        <div className="contenitore striscia-scena">
          <TestaSezione {...testa} className="striscia-testa" />
          <ul className="striscia-binario">{children}</ul>
        </div>
      </div>
    </section>
  );
}
