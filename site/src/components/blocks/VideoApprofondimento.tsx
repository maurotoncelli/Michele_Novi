import { idYoutube } from "@/lib/media";

export function VideoApprofondimento({
  file,
  youtube,
  titolo,
}: {
  file?: string | null;
  youtube?: string | null;
  titolo: string;
}) {
  const src = file ? (file.startsWith("/") ? file : `/video/quaderno/${file}`) : null;
  const yt = idYoutube(youtube);
  if (!src && !yt) return null;

  return (
    <div className="incavo mt-10 overflow-hidden rounded-[1.75rem]">
      {src ? (
        <video className="aspect-video w-full bg-inchiostro" controls playsInline preload="metadata" title={titolo}>
          <source src={src} />
        </video>
      ) : (
        <iframe
          title={titolo}
          src={`https://www.youtube-nocookie.com/embed/${yt}`}
          className="aspect-video h-full w-full border-0"
          loading="lazy"
          allow="accelerometer; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        />
      )}
    </div>
  );
}
