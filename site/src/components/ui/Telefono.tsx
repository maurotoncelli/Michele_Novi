import { telPrefisso } from "@/lib/content";

/** Numero con il prefisso (+39) più chiaro, su una sola riga. */
export function Telefono({ numero }: { numero: string }) {
  const prefisso = telPrefisso(numero);
  return (
    <span className="whitespace-nowrap">
      {prefisso && <span className="text-[0.8em] opacity-60">{prefisso}</span>}
      {prefisso && " "}
      {numero.trim()}
    </span>
  );
}
