import type { SVGProps } from "react";

/**
 * Le tre tecniche di Come si opera. Stesso tratto dei Segni, con una campitura leggera:
 * stanno dentro il paragrafo e si devono leggere al primo sguardo.
 */
export type NomeTecnica = "artroscopia" | "aperta" | "protesi";

const disegni: Record<NomeTecnica, React.ReactNode> = {
  // Ottica con la telecamera fuori e la luce dentro l'articolazione; accanto, il portale dello strumento.
  artroscopia: (
    <>
      <circle cx="20" cy="20" r="7.4" fill="currentColor" fillOpacity={0.14} />
      <path d="M16.2 16.2L24 19.4L19.4 24Z" fill="currentColor" fillOpacity={0.32} stroke="none" />
      <path d="M3.6 6.2L6.2 3.6L10.4 7.8L7.8 10.4Z" fill="currentColor" fillOpacity={0.14} />
      <path d="M9.1 9.1L16.2 16.2" />
      <path d="M27 5.5L23 13.3" />
    </>
  ),
  // Bisturi e linea d'incisione.
  aperta: (
    <>
      <path d="M14.5 17.5L24 8c1.6-1.6 4.1-1.4 4.6.4.5 1.8-.8 3.9-2.6 5.7l-7.4 7.4z" fill="currentColor" fillOpacity={0.14} />
      <path d="M14.5 17.5l4.1 4.1" />
      <path d="M14.5 17.5l-9.3 9.3a2 2 0 0 0 2.9 2.9l9.3-9.3" />
      <path d="M17 28.5h3M23 28.5h3" />
    </>
  ),
  // Coppa, testa e stelo.
  protesi: (
    <g transform="translate(2 0.4)">
      <path d="M13.12 15.92L21.01 28.02A0.9 0.9 0 0 0 22.59 27.18L17 13.86" fill="currentColor" fillOpacity={0.14} />
      <path d="M12.6 17.4L18.5 14.3" />
      <circle cx="13" cy="11" r="4.8" fill="currentColor" fillOpacity={0.14} />
      <path d="M5.5 15.3A8 8 0 0 1 17.2 3.9" />
    </g>
  ),
};

export function IconaTecnica({ nome, size = 32, ...rest }: { nome: NomeTecnica; size?: number } & SVGProps<SVGSVGElement>) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 32 32"
      fill="none"
      stroke="currentColor"
      strokeWidth={1.6}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      focusable="false"
      {...rest}
    >
      {disegni[nome]}
    </svg>
  );
}

export const isTecnica = (v: string | null | undefined): v is NomeTecnica => !!v && v in disegni;
