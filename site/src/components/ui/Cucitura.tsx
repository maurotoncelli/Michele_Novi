/**
 * Cucitura articolare: il bordo condiloideo che separa due sezioni.
 * La sezione sopra "scende" sulla successiva con un'onda morbida e una linea rame.
 */
export function Cucitura({
  className = "",
  tinta = "osso",
  flip = false,
}: {
  className?: string;
  tinta?: "osso" | "menta" | "pesca" | "salvia" | "campo";
  flip?: boolean;
}) {
  const fill = {
    osso: "#ffffff",
    menta: "#e8f3f4",
    pesca: "#fdf2ed",
    salvia: "#edf5f0",
    campo: "#f7f6f3",
  }[tinta];
  return (
    <div className={`relative -mb-px h-14 w-full overflow-hidden md:h-20 ${flip ? "rotate-180" : ""} ${className}`} aria-hidden="true">
      <svg viewBox="0 0 1440 80" preserveAspectRatio="none" className="absolute inset-0 h-full w-full">
        <defs>
          <linearGradient id="cucitura-rame" x1="0" x2="1">
            <stop offset="0" stopColor="#c9785c" stopOpacity="0" />
            <stop offset="0.3" stopColor="#c9785c" stopOpacity="0.9" />
            <stop offset="0.7" stopColor="#c9785c" stopOpacity="0.9" />
            <stop offset="1" stopColor="#c9785c" stopOpacity="0" />
          </linearGradient>
          <filter id="cucitura-glow" x="-5%" y="-200%" width="110%" height="500%">
            <feGaussianBlur stdDeviation="3" />
          </filter>
        </defs>
        <path
          d="M0,0 L1440,0 L1440,28 C1240,64 1040,10 840,34 C640,58 440,20 240,46 C140,58 60,64 0,40 Z"
          fill={fill}
        />
        <path
          d="M0,40 C60,64 140,58 240,46 C440,20 640,58 840,34 C1040,10 1240,64 1440,28"
          fill="none"
          stroke="url(#cucitura-rame)"
          strokeWidth="2.5"
          filter="url(#cucitura-glow)"
          opacity="0.7"
        />
        <path
          d="M0,40 C60,64 140,58 240,46 C440,20 640,58 840,34 C1040,10 1240,64 1440,28"
          fill="none"
          stroke="url(#cucitura-rame)"
          strokeWidth="1"
        />
      </svg>
    </div>
  );
}
