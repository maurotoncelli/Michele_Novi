/**
 * Spezza un testo in parole, ognuna con il proprio indice: il CSS le fa comparire una dopo l'altra
 * quando l'antenato prende `is-in` (Reveal). Per lo screen reader resta una frase sola.
 */
export function Parole({ testo, passo = 26 }: { testo: string; passo?: number }) {
  const parole = testo.trim().split(/\s+/);
  return (
    <>
      {parole.map((p, i) => (
        <span key={i}>
          <span className="parola" style={{ "--ritardo": `${i * passo}ms` } as React.CSSProperties}>
            {p}
          </span>
          {i < parole.length - 1 ? " " : ""}
        </span>
      ))}
    </>
  );
}
