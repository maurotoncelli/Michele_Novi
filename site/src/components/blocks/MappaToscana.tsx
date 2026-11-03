"use client";

import { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { href, type Locale } from "@/i18n/routing";
import { Segno } from "../ui/Segno";

export type SedeVisitaMappa = {
  slug: string;
  citta: string;
  provincia?: string;
  nome: string;
  indirizzo: string;
  cap?: string;
  regime?: string;
  servizi?: string[];
};

type PinId = "pisa" | "fucecchio" | "peccioli";

/**
 * Coordinate esatte nel sistema di coordinate del tracciato ad alto dettaglio
 * della Toscana (viewBox 0 0 520 510, con transform translate(102, 74) scale(0.71)
 * per lasciare ampio margine di mare blu tutto intorno al profilo).
 */
const PIN_COORDS: Record<PinId, { cx: number; cy: number }> = {
  pisa: { cx: 175.8, cy: 191.2 },
  fucecchio: { cx: 227.7, cy: 190.4 },
  peccioli: { cx: 217, cy: 218.8 },
};

const CITTA_RIF = [
  { nome: "Viareggio", cx: 161.6, cy: 168.4, dx: -7, dy: 3, anchor: "end" as const },
  { nome: "Lucca", cx: 191.5, cy: 172, dx: 6, dy: 3, anchor: "start" as const },
  { nome: "Livorno", cx: 168, cy: 218.8, dx: -7, dy: 3.5, anchor: "end" as const },
  { nome: "Firenze", cx: 280.2, cy: 184, dx: 7, dy: 3.5, anchor: "start" as const },
  { nome: "Siena", cx: 288.7, cy: 255.8, dx: 7, dy: 3.5, anchor: "start" as const },
  { nome: "Arezzo", cx: 354, cy: 232.3, dx: 7, dy: 3.5, anchor: "start" as const },
  { nome: "Grosseto", cx: 263.2, cy: 343.8, dx: 7, dy: 3.5, anchor: "start" as const },
];

/* Tracciati geografici reali ad alto dettaglio della Toscana e dell'Arcipelago Toscano */
const TOSCANA_MAIN_PATH =
  "M52.03,97.64l-4.84-1.35s-1.16-.97,2.42-4.26,4.93-3.87,6.09-6-.19-4.64-1.93-6.38-1.93-5.61-5.22-2.51-1.74,7.54-3.48,6.58-2.32-3.49-2.32-7.74.77-8.7-2.13-9.09-8.9,1.16-9.29,0-.19-2.32,1.55-4.06,2.18-5.61-1.71-4.64-8.92,4.64-7.96,1.93.97-13.15-1.55-16.25-14.31-5.42-18.18-14.9-4.06-9.67,0-9.67,4.84.77,5.42-2.32S17.98,3.04,19.53,1.69s18.76-1.35,20.31-.97,4.06,1.93,4.84,3.29,1.55,1.35,2.51,2.13,1.93,6.38.19,7.93,1.16,4.64,3.1,5.61,9.67,8.51,12.57,8.32,6.96-1.93,8.32-.77,1.74,4.26,3.68,5.42,9.09,6.96,10.45,9.48,2.71,5.8,4.06,5.03,2.71-4.84,7.93-3.29,4.64,2.13,8.9,3.68,5.03,8.12,8.9,7.93,10.45,0,13.54,7.74,14.51,18.57,17.22,16.25.58-3.1,5.03-5.8,11.8-1.74,15.67-1.74,4.84,2.9,9.48,6.19,15.28,6.77,16.64,10.83,0,4.84,5.42.97,8.9-14.31,11.41-14.12.97,4.45,3.68,6.96,8.4,6.38,13.29,3.1,13.02-.39,17.85-1.74,10.06-.39,6-5.03-10.05-8.12,1.46-8.51c11.5-.39,11.7-9.87,15.37-10.25s5.42,2.13,6.38-2.71,3.68-4.26,6-2.71,3.29,4.26,5.8,8.9,10.06,8.71,13.15,7.54,1.93-3.48,4.45-2.32,4.26.77,6,1.55,3.48.58,1.35,2.13-7.74,6.19-2.9,6.96,5.61,5.8,7.74,5.22,4.64-4.06,8.9-5.03,10.83-2.13,10.64-.39-4.84,11.61-7.74,14.9-11.8,13.93-8.32,16.06,4.06,4.64,6,9.87,5.22,10.06,5.03,12.19,11.22,8.9,13.54,11.03,1.35,5.03,4.84,5.22,13.54,1.55,16.06,4.45,3.1,8.9,7.54,7.93,6.58-3.66,11.8.1c0,0,2.77,3.52,6.88,2.15s11.73-2.5,13.49.32,6.06.47,11.14-1.68,8.6-1.28,13.29,2.98,4.69,6.99,0,8.95-2.15-.2-8.8,5.28-12.51,5.67-10.75,9.38,4.1,4.1.98,8.01-7.62,13.68-11.53,15.05-9.97,5.08-7.04,7.43,12.9,6.25,7.43,7.04-3.71-1.95-5.86,2.74-3.52,5.86-6.06,5.28-10.36,5.29-6.84,6.46,5.28-2.35,6.84.97-.78,8.01,2.15,7.43,4.1-.98,5.86,2.35,2.35,7.23,1.17,10.36,6.45,8.6,7.82,5.08,3.71-7.62,5.47-4.89,3.32,4.1-.59,6.84-9.77,6.84-15.25,8.41-5.86,3.91-8.41,1.76-5.47-4.52-6.45.87,1.17,9.69-2.74,10.47-2.93-.78-6.65,2.15-11.73,7.82-9.19,14.86-.59,8.8,2.74,9.77,4.1-1.95,5.28,1.17,3.13,5.67.98,9.77-5.86,18.18-5.67,20.52,1.56,5.08,3.32,7.62,7.62,1.56-1.17,5.67-8.41,4.89-14.46,7.62-5.08-.59-8.41,3.32,1.76,7.43-3.32,3.91-6.65-7.82-7.62-2.35-2.15,7.43,1.37,10.36,12.9,7.82,8.01,10.95-8.6,2.93-7.04,6.06,11.34,3.32,6.65,7.62-4.3,4.1-7.62,4.69.78-1.37-4.1,2.35-10.75,9.58-13.88,10.56-3.52,4.3-5.08,2.15-.39-3.66-3.52-.85,1.37,1.64-1.37,3.79-4.1,7.23-1.56,8.6,7.23,4.89,6.84,7.04,1.95,3.13-.78,5.28,1.95,4.69-5.28,3.71-9.38-2.54-12.9-.78-1.76,3.13-5.28,6.65-5.08,7.04-5.47,6.06-12.12-7.62-17.4-7.62-4.89-.59-6.06-1.17-4.5-3.13-8.99-1.37-4.5,3.13-6.06,5.86-1.95,8.99-5.47,7.43-11.14-7.23-11.53-7.82-3.91-5.47-.98-7.43-.59.2,4.5-1.17,7.43,3.52,8.99-4.3-.78-18.37-4.5-22.09-1.17,2.93-5.67-.98-5.28-8.21-8.6-12.71,4.89-1.56-5.08-6.45-3.32,2.54-11.92-9.58-11.53-16.03-20.33-17.4-8.01,1.37-13.1-2.35-9.97-4.1-5.67-6.25,5.67-1.56,5.47-6.45-.39-6.84.2-8.8,4.69-9.19-9.97-12.71-19.94-4.89-21.7-3.13-3.52,2.74-5.28,4.69-2.15,7.23-6.84.39-6.84-7.82-3.52-11.92,3.32-4.1,4.5-6.45,9.19-21.31,4.1-46.72-10.36-19.74-11.92-22.48.2-1.37-1.76-6.84-14.27-18.96-18.18-26.97-5.28-15.25-6.06-20.13-3.52-8.99-3.52-15.83-3.91-47.69-7.23-57.27-18.18-23.85-22.48-29.12-6.63-4.94-6.54-5.69Z";

const ARCIPELAGO_PATHS = [
  "M111.21,364.18c-1.18-3.15,3.74-6.5-1.18-3.15s-4.33,3.54-5.71,6.5,2.17,3.15-2.56,5.31-3.94,4.13-4.72,2.17,2.17-3.74-2.17-4.72-1.18-3.74-4.33-.98-6.3,6.15-6.89,6.52-4.33,1.01-4.33,0,.98-2.78-1.77-3.57-14.37-1.77-15.75,2.76-.2,6.1.2,10.24.2,4.13,4.53,3.35,3.94-2.17,10.04-.59,1.57-6.3,7.48-4.33,7.09,8.46,7.87,3.74.59-7.87,1.77-4.33.59,5.9,2.17,2.56.79-10.43,3.35-5.51,6.5,13.19,6.5,13.19c0,0,2.17-.2,4.53.79s5.51-1.18,3.35-3.94-5.12-4.53-4.92-6.89,7.87-3.71,6.5-6.28-2.36-.8-1.97-5.53.59-6.1.59-6.1l-2.56-1.18Z",
  "M195.19,469.3c-.51-1.02-6.15-8.71-6.92-5.38s-4.87,5.84-2.56,7.92,2.82,1.82,6.4,5.66,8.2,4.1,6.92,1.28-3.84-9.48-3.84-9.48Z",
  "M15.63,319.97c-.59-3.07-4.61-6.4-6.66,0s-1.54,8.96,1.79,7.43,5.89-2.05,4.87-7.43Z",
  "M59.18,421.92s-1.79-12.04-4.61-7.17-3.84,5.64-3.84,8.2,3.59,5.89,5.89,3.33,2.56-4.35,2.56-4.35Z",
  "M96.32,471.88c-1.76-1.58-5.38-.27-5.38,3.31s-2.31,4.87,2.69,3.59,4.99-4.83,2.69-6.9Z",
  "M228.21,493.47c.22-2.39-5.81-.47-5.34,2.2s4.87,2.83,5.34-2.2Z",
];

function getPinId(s: SedeVisitaMappa): PinId {
  const c = s.citta.toLowerCase();
  if (c.includes("pisa")) return "pisa";
  if (c.includes("peccioli")) return "peccioli";
  return "fucecchio";
}

/** Riquadro logo uniforme (stesse dimensioni, stesso fondo e bordo per tutte e 3 le sedi) così i testi partono tutti sulla stessa colonna. */
function LogoSedeVisita({ id, nome }: { id: PinId; nome: string }) {
  const src =
    id === "pisa"
      ? "/images/sedi/logo-san-rossore.png"
      : id === "peccioli"
        ? "/images/sedi/logo-san-verano.png"
        : "/images/sedi/logo-san-pietro.png";
  return (
    <div className="flex h-16 w-24 shrink-0 items-center justify-center rounded-sm border border-linea/70 bg-osso-2/60 p-2 sm:h-[4.25rem] sm:w-28">
      <Image
        src={src}
        alt={nome}
        width={104}
        height={54}
        className="max-h-11 w-auto max-w-full object-contain"
      />
    </div>
  );
}

export function MappaToscanaVisite({
  sedi,
  locale,
  labelScopri,
}: {
  sedi: SedeVisitaMappa[];
  locale: Locale;
  labelScopri: string;
}) {
  const [attiva, setAttiva] = useState<PinId | null>(null);

  return (
    <div className="grid items-center gap-8 lg:grid-cols-[minmax(0,1.08fr)_minmax(0,1fr)] lg:gap-12 xl:gap-16">
      {/* Mappa ad alto dettaglio della Toscana nella palette del sito */}
      <div className="relative aspect-[520/510] w-full overflow-hidden border border-linea bg-[#0f3a5a]">
        <svg
          viewBox="0 0 520 510"
          className="h-full w-full select-none"
          role="img"
          aria-label={
            locale === "en"
              ? "Map of outpatient locations in Tuscany: Pisa, Fucecchio and Peccioli"
              : "Mappa delle sedi ambulatoriali in Toscana: Pisa, Fucecchio e Peccioli"
          }
        >
          <defs>
            <linearGradient id="mare-toscana" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stopColor="#13456b" />
              <stop offset="100%" stopColor="#0c2f4a" />
            </linearGradient>
            <linearGradient id="terra-toscana" x1="0" y1="0" x2="0.8" y2="1">
              <stop offset="0%" stopColor="#f7f6f3" />
              <stop offset="100%" stopColor="#e7e2d7" />
            </linearGradient>
            <filter id="ombra-regione" x="-8%" y="-8%" width="116%" height="116%">
              <feDropShadow dx="0" dy="6" stdDeviation="10" floodColor="#071e30" floodOpacity="0.32" />
            </filter>
            <filter id="ombra-card" x="-10%" y="-10%" width="120%" height="125%">
              <feDropShadow dx="0" dy="4" stdDeviation="6" floodColor="#071e30" floodOpacity="0.22" />
            </filter>
          </defs>

          {/* Mare Tirreno */}
          <rect width="520" height="510" fill="url(#mare-toscana)" />

          {/* Reticolo cartografico sottile */}
          <g stroke="rgba(255,255,255,0.06)" strokeWidth="1">
            <line x1="0" y1="127" x2="520" y2="127" />
            <line x1="0" y1="255" x2="520" y2="255" />
            <line x1="0" y1="382" x2="520" y2="382" />
            <line x1="130" y1="0" x2="130" y2="510" />
            <line x1="260" y1="0" x2="260" y2="510" />
            <line x1="390" y1="0" x2="390" y2="510" />
          </g>

          {/* Tracciato reale ad alto dettaglio della Toscana e dell'Arcipelago (scalato a 0.71 e centrato per ampio margine blu) */}
          <g transform="translate(102, 74) scale(0.71)" filter="url(#ombra-regione)">
            <path
              d={TOSCANA_MAIN_PATH}
              fill="url(#terra-toscana)"
              stroke="#c4bcad"
              strokeWidth="1.9"
              strokeLinejoin="round"
            />
            {ARCIPELAGO_PATHS.map((d, idx) => (
              <path
                key={idx}
                d={d}
                fill="url(#terra-toscana)"
                stroke="#c4bcad"
                strokeWidth="1.6"
                strokeLinejoin="round"
              />
            ))}
          </g>

          {/* Città di riferimento */}
          {CITTA_RIF.map((c) => (
            <g key={c.nome} opacity="0.72">
              <circle cx={c.cx} cy={c.cy} r="2.3" fill="#5b6470" />
              <text
                x={c.cx + c.dx}
                y={c.cy + c.dy}
                textAnchor={c.anchor}
                fill="#5b6470"
                className="fill-[#5b6470] text-[8.8px] font-medium tracking-[0.02em]"
              >
                {c.nome}
              </text>
            </g>
          ))}

          {/* Callout sulla mappa per le 3 sedi di visita */}
          {/* 1. Fucecchio callout box (in alto a destra) */}
          <g
            filter="url(#ombra-card)"
            className={`cursor-pointer transition-opacity duration-200 ${attiva && attiva !== "fucecchio" ? "pointer-events-none" : ""}`}
            opacity={attiva && attiva !== "fucecchio" ? 0 : 1}
            onMouseEnter={() => setAttiva("fucecchio")}
            onMouseLeave={() => setAttiva(null)}
          >
            <line x1="227.7" y1="190.4" x2="264" y2="112" stroke="#1e6aa8" strokeWidth="1.4" />
            <rect x="212" y="58" width="212" height="54" rx="5" fill="#ffffff" stroke="#1e6aa8" strokeWidth={attiva === "fucecchio" ? "2" : "1"} />
            <text x="224" y="78" fill="#0f3a5a" className="fill-[#0f3a5a] text-[11px] font-semibold">
              Fucecchio (FI)
            </text>
            <text x="224" y="93" fill="#1e6aa8" className="fill-[#1e6aa8] text-[10.5px] font-medium">
              Studi Medici San Pietro
            </text>
            <text x="224" y="105" fill="#5b6470" className="fill-[#5b6470] text-[9.2px]">
              Piazza Toscanini, 3
            </text>
          </g>

          {/* 2. Pisa callout box (a sinistra) */}
          <g
            filter="url(#ombra-card)"
            className={`cursor-pointer transition-opacity duration-200 ${attiva && attiva !== "pisa" ? "pointer-events-none" : ""}`}
            opacity={attiva && attiva !== "pisa" ? 0 : 1}
            onMouseEnter={() => setAttiva("pisa")}
            onMouseLeave={() => setAttiva(null)}
          >
            <line x1="175.8" y1="191.2" x2="128" y2="238" stroke="#1e6aa8" strokeWidth="1.4" />
            <rect x="30" y="238" width="184" height="54" rx="5" fill="#ffffff" stroke="#1e6aa8" strokeWidth={attiva === "pisa" ? "2" : "1"} />
            <text x="42" y="258" fill="#0f3a5a" className="fill-[#0f3a5a] text-[11px] font-semibold">
              Pisa (PI)
            </text>
            <text x="42" y="273" fill="#1e6aa8" className="fill-[#1e6aa8] text-[10.5px] font-medium">
              Casa di Cura San Rossore
            </text>
            <text x="42" y="285" fill="#5b6470" className="fill-[#5b6470] text-[9.2px]">
              Viale delle Cascine, 152/F
            </text>
          </g>

          {/* 3. Peccioli callout box (in basso a destra) */}
          <g
            filter="url(#ombra-card)"
            className={`cursor-pointer transition-opacity duration-200 ${attiva && attiva !== "peccioli" ? "pointer-events-none" : ""}`}
            opacity={attiva && attiva !== "peccioli" ? 0 : 1}
            onMouseEnter={() => setAttiva("peccioli")}
            onMouseLeave={() => setAttiva(null)}
          >
            <line x1="217" y1="218.8" x2="258" y2="302" stroke="#1e6aa8" strokeWidth="1.4" />
            <rect x="206" y="302" width="208" height="54" rx="5" fill="#ffffff" stroke="#1e6aa8" strokeWidth={attiva === "peccioli" ? "2" : "1"} />
            <text x="218" y="322" fill="#0f3a5a" className="fill-[#0f3a5a] text-[11px] font-semibold">
              Peccioli (PI)
            </text>
            <text x="218" y="337" fill="#1e6aa8" className="fill-[#1e6aa8] text-[10.5px] font-medium">
              Centro Medico San Verano
            </text>
            <text x="218" y="349" fill="#5b6470" className="fill-[#5b6470] text-[9.2px]">
              Viale Cavour, 13
            </text>
          </g>

          {/* I 3 Pin sulla mappa */}
          {(Object.entries(PIN_COORDS) as [PinId, (typeof PIN_COORDS)[PinId]][]).map(([id, p]) => {
            const isActive = attiva === id;
            return (
              <g
                key={id}
                className="cursor-pointer"
                onMouseEnter={() => setAttiva(id)}
                onMouseLeave={() => setAttiva(null)}
              >
                <circle
                  cx={p.cx}
                  cy={p.cy}
                  r={isActive ? "12" : "8.5"}
                  fill="#1e6aa8"
                  fillOpacity={isActive ? "0.28" : "0.18"}
                />
                <path
                  d={`M ${p.cx} ${p.cy} C ${p.cx - 6.8} ${p.cy - 7.8}, ${p.cx - 8.2} ${p.cy - 17}, ${p.cx} ${p.cy - 17} C ${p.cx + 8.2} ${p.cy - 17}, ${p.cx + 6.8} ${p.cy - 7.8}, ${p.cx} ${p.cy} Z`}
                  fill={isActive ? "#0f3a5a" : "#1e6aa8"}
                  stroke="#ffffff"
                  strokeWidth="1.5"
                />
                <circle cx={p.cx} cy={p.cy - 11} r="2.5" fill="#ffffff" />
              </g>
            );
          })}

          {/* Intestazione discreta in alto a destra sul mare/margine */}
          <text
            x="494"
            y="30"
            textAnchor="end"
            fill="#ffffff"
            fillOpacity="0.85"
            className="fill-white text-[9.5px] font-semibold tracking-[0.2em] uppercase"
          >
            {locale === "en" ? "Tuscany · Outpatient clinics" : "Toscana · Sedi di visita"}
          </text>
        </svg>
      </div>

      {/* Elenco interattivo delle 3 sedi di visita con riquadri logo uniformi e testo allineato */}
      <ul className="flex flex-col divide-y divide-linea border-y border-linea bg-osso">
        {sedi.map((s) => {
          const pinId = getPinId(s);
          const isActive = attiva === pinId;
          return (
            <li key={s.slug} className="min-w-0">
              <Link
                href={href(locale, { kind: "dove", slug: s.slug })}
                onMouseEnter={() => setAttiva(pinId)}
                onMouseLeave={() => setAttiva(null)}
                className={`group grid grid-cols-[6rem_minmax(0,1fr)] items-center gap-4 p-5 transition-colors duration-300 sm:grid-cols-[7rem_minmax(0,1fr)_auto] sm:gap-5 md:p-6 ${
                  isActive ? "bg-petrolio-3/60" : "hover:bg-petrolio-3/40"
                }`}
              >
                <LogoSedeVisita id={pinId} nome={s.nome} />
                <div className="min-w-0">
                  <p className="eyebrow">
                    {s.citta}
                    {s.provincia ? ` (${s.provincia})` : ""}
                  </p>
                  <h3 className="mt-1 text-[1.2rem] font-medium leading-snug text-inchiostro group-hover:text-petrolio md:text-[1.3rem]">
                    {s.nome}
                  </h3>
                  <p className="mt-1 flex items-center gap-1.5 text-[0.92rem] text-grafite">
                    <Segno nome="pin" size={14} className="shrink-0 text-petrolio" />
                    <span>
                      {s.indirizzo}
                      {s.cap ? `, ${s.cap}` : ""}
                    </span>
                  </p>
                  {s.servizi && s.servizi.length > 0 && (
                    <p className="mt-1.5 text-[0.78rem] text-nebbia">{s.servizi.join(" · ")}</p>
                  )}
                </div>
                <span className="col-start-2 inline-flex shrink-0 items-center gap-1.5 text-[0.85rem] font-medium text-petrolio sm:col-start-3">
                  {labelScopri}
                  <Segno nome="freccia" size={16} className="transition-transform duration-300 group-hover:translate-x-1" />
                </span>
              </Link>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
