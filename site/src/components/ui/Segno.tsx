import type { SVGProps } from "react";

/**
 * Catalogo di segni a tratto singolo. Una sola famiglia, stesso spessore.
 * Schematici e riconoscibili: "artroscopia" deve capirsi dal disegno.
 */
export type NomeSegno =
  | "spalla"
  | "gomito"
  | "mano"
  | "sport"
  | "artroscopia"
  | "anca"
  | "ginocchio"
  | "eco"
  | "ospedale"
  | "studio"
  | "clinica"
  | "protesi"
  | "frattura"
  | "esercizio"
  | "telefono"
  | "whatsapp"
  | "mail"
  | "pin"
  | "orologio"
  | "freccia"
  | "freccia-sx"
  | "menu"
  | "x"
  | "esterno"
  | "rss"
  | "instagram"
  | "linkedin"
  | "youtube"
  | "check"
  | "doc"
  | "quaderno"
  | "piu"
  | "meno"
  | "globo";

const paths: Record<NomeSegno, React.ReactNode> = {
  // Testa omerale nella glena: un cerchio che si appoggia in una cavità
  spalla: (
    <>
      <path d="M4 12c0-3.5 2.5-6 6-6" />
      <circle cx="13" cy="10" r="4" />
      <path d="M9.5 13.5C7 15 5 17 4 20" />
      <path d="M17 12.5c1.5 2 2.5 4.5 3 7.5" />
    </>
  ),
  gomito: (
    <>
      <path d="M4 5l7 7" />
      <circle cx="12.5" cy="13.5" r="2.5" />
      <path d="M14.5 15.5L20 20" />
      <path d="M12 4l-1 3.5" />
    </>
  ),
  mano: (
    <>
      <path d="M8 13V6.5a1.5 1.5 0 0 1 3 0V12" />
      <path d="M11 11.5V5a1.5 1.5 0 0 1 3 0v7" />
      <path d="M14 11.5V6.5a1.5 1.5 0 0 1 3 0V13" />
      <path d="M17 12.5a1.5 1.5 0 0 1 3 0V15a6 6 0 0 1-6 6h-2.5a6 6 0 0 1-5-2.7L4 14.5a1.5 1.5 0 0 1 2.5-1.7L8 14.5" />
    </>
  ),
  sport: (
    <>
      <circle cx="15" cy="5" r="2" />
      <path d="M4 20l4-6 3 2 3-5 3 1" />
      <path d="M9 14l-1 6" />
    </>
  ),
  // Due portali che convergono sull'articolazione, con l'ottica angolata
  artroscopia: (
    <>
      <circle cx="12" cy="14" r="5" />
      <path d="M4 4l5 6" />
      <path d="M20 4l-5 6" />
      <path d="M3 4h2M19 4h2" />
      <path d="M12 12v2.5" />
    </>
  ),
  anca: (
    <>
      <path d="M5 5c2 0 4 1.5 5 4" />
      <circle cx="13" cy="12" r="3.5" />
      <path d="M12 15.5L10 21" />
      <path d="M18 8c1 3 1 6-1 9" />
    </>
  ),
  ginocchio: (
    <>
      <path d="M9 3v6" />
      <path d="M15 3v6" />
      <path d="M8 10a4 4 0 0 0 8 0" />
      <path d="M9 15v6" />
      <path d="M15 15v6" />
      <path d="M8 14a4 4 0 0 1 8 0" />
    </>
  ),
  eco: (
    <>
      <path d="M6 4h6l-1 5H7z" />
      <path d="M9 9c0 5 3 7 8 9" />
      <path d="M4 15c3 0 4 3 7 3" />
      <path d="M4 19c4 0 6 2 10 2" />
    </>
  ),
  ospedale: (
    <>
      <rect x="4" y="6" width="16" height="14" rx="1.5" />
      <path d="M12 10v6M9 13h6" />
      <path d="M9 6V4h6v2" />
    </>
  ),
  studio: (
    <>
      <path d="M4 11l8-6 8 6" />
      <path d="M6 10v10h12V10" />
      <path d="M10 20v-5h4v5" />
    </>
  ),
  clinica: (
    <>
      <path d="M5 20V8l7-4 7 4v12" />
      <path d="M9 20v-4h6v4" />
      <path d="M12 9v4M10 11h4" />
    </>
  ),
  protesi: (
    <>
      <path d="M8 21V11l4-3 4 3v10" />
      <circle cx="12" cy="6" r="2.5" />
      <path d="M8 15h8" />
    </>
  ),
  frattura: (
    <>
      <path d="M7 4c-2 0-3 1.5-2 3l3 4-2 3 3 4c1 1.5 3 1.5 4 0" />
      <path d="M17 20c2 0 3-1.5 2-3l-3-4 2-3-3-4c-1-1.5-3-1.5-4 0" />
    </>
  ),
  esercizio: (
    <>
      <circle cx="12" cy="4.5" r="1.8" />
      <path d="M12 7v6" />
      <path d="M5 9l7 1 7-1" />
      <path d="M12 13l-3 7M12 13l3 7" />
    </>
  ),
  telefono: (
    <path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2z" />
  ),
  whatsapp: (
    <>
      <path d="M4 20l1.3-4A8 8 0 1 1 8 18.7z" />
      <path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.5-2-1-1 .8a4 4 0 0 1-2-2l.8-1-1-2z" />
    </>
  ),
  mail: (
    <>
      <rect x="3" y="6" width="18" height="12" rx="2" />
      <path d="M3 8l9 6 9-6" />
    </>
  ),
  pin: (
    <>
      <path d="M12 21s-6-6-6-11a6 6 0 0 1 12 0c0 5-6 11-6 11z" />
      <circle cx="12" cy="10" r="2" />
    </>
  ),
  orologio: (
    <>
      <circle cx="12" cy="12" r="8" />
      <path d="M12 8v4l3 2" />
    </>
  ),
  freccia: <path d="M5 12h14M13 6l6 6-6 6" />,
  "freccia-sx": <path d="M19 12H5M11 6l-6 6 6 6" />,
  menu: <path d="M4 7h16M4 12h16M4 17h16" />,
  x: <path d="M6 6l12 12M18 6L6 18" />,
  esterno: (
    <>
      <path d="M14 4h6v6" />
      <path d="M20 4l-9 9" />
      <path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5" />
    </>
  ),
  rss: (
    <>
      <path d="M5 19a1 1 0 1 0 0-.01" />
      <path d="M4 11a9 9 0 0 1 9 9" />
      <path d="M4 5a15 15 0 0 1 15 15" />
    </>
  ),
  instagram: (
    <>
      <rect x="4" y="4" width="16" height="16" rx="4" />
      <circle cx="12" cy="12" r="3.5" />
      <path d="M16.5 7.5h.01" />
    </>
  ),
  linkedin: (
    <>
      <rect x="4" y="4" width="16" height="16" rx="2" />
      <path d="M8 10v7M8 7v.01M12 17v-4a2 2 0 0 1 4 0v4M12 10v7" />
    </>
  ),
  youtube: (
    <>
      <rect x="3" y="6" width="18" height="12" rx="3" />
      <path d="M10 9.5v5l4.5-2.5z" />
    </>
  ),
  check: <path d="M5 12l4 4L19 6" />,
  doc: (
    <>
      <path d="M7 3h7l5 5v13H7z" />
      <path d="M14 3v5h5" />
      <path d="M10 13h6M10 17h6" />
    </>
  ),
  quaderno: (
    <>
      <path d="M6 3h11a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H6z" />
      <path d="M6 3v18" />
      <path d="M9 8h6M9 12h6" />
    </>
  ),
  piu: <path d="M12 5v14M5 12h14" />,
  meno: <path d="M5 12h14" />,
  globo: (
    <>
      <circle cx="12" cy="12" r="8" />
      <path d="M4 12h16M12 4c3 3 3 13 0 16M12 4c-3 3-3 13 0 16" />
    </>
  ),
};

export function Segno({ nome, size = 24, ...rest }: { nome: NomeSegno; size?: number } & SVGProps<SVGSVGElement>) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={1.5}
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
      focusable="false"
      {...rest}
    >
      {paths[nome] ?? paths.doc}
    </svg>
  );
}

export const isSegno = (v: string | null | undefined): v is NomeSegno => !!v && v in paths;
