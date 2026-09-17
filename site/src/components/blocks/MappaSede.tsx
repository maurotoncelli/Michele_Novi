import { mapsEmbedSrc } from "@/lib/media";

export function MappaSede({
  lat,
  lng,
  query,
  nome,
  lang = "it",
}: {
  lat?: number | null;
  lng?: number | null;
  query?: string | null;
  nome: string;
  lang?: string;
}) {
  const src = mapsEmbedSrc({ lat, lng, query, lang });
  if (!src) return null;
  return (
    <iframe
      title={`Google Maps: ${nome}`}
      src={src}
      className="absolute inset-0 h-full w-full border-0"
      loading="lazy"
      referrerPolicy="no-referrer-when-downgrade"
      allowFullScreen
    />
  );
}
