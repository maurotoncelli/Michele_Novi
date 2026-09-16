import Image from "next/image";

/** Disegno dal catalogo Keystatic (public/images/disegni/). Fallback: nulla. */
export function Disegno({
  src,
  alt,
  className = "",
  contenere = true,
}: {
  src: string;
  alt: string;
  className?: string;
  contenere?: boolean;
}) {
  return (
    <Image
      src={src}
      alt={alt}
      fill
      sizes="(min-width: 1024px) 20vw, (min-width: 640px) 40vw, 90vw"
      className={`${contenere ? "object-contain" : "object-cover"} ${className}`}
    />
  );
}
