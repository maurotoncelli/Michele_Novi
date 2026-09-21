"use client";

import Image from "next/image";
import { useEffect, useRef } from "react";

/**
 * Lastra media: un video muto in loop se c'è, altrimenti la foto.
 * Il video parte solo quando è in vista e si ferma quando esce: niente peso a vuoto.
 */
export function VideoLastra({
  video,
  foto,
  alt,
  ratio = "4/5",
  sizes = "(min-width: 1024px) 40vw, 100vw",
  className = "",
}: {
  video?: string | null;
  foto?: string | null;
  alt: string;
  ratio?: "4/5" | "4/3" | "3/2";
  sizes?: string;
  className?: string;
}) {
  const ref = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    const v = ref.current;
    if (!v || typeof IntersectionObserver === "undefined") return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const obs = new IntersectionObserver(
      ([e]) => {
        if (!e) return;
        if (e.isIntersecting) v.play().catch(() => {});
        else v.pause();
      },
      { threshold: 0.25 },
    );
    obs.observe(v);
    return () => obs.disconnect();
  }, [video]);

  const forma = ratio === "4/3" ? "aspect-[4/3]" : ratio === "3/2" ? "aspect-[3/2]" : "aspect-[4/5]";

  return (
    <div className={`relative overflow-hidden bg-osso-2 ${forma} ${className}`}>
      {video ? (
        <video
          ref={ref}
          src={video}
          poster={foto ?? undefined}
          muted
          loop
          playsInline
          preload="none"
          aria-label={alt}
          className="absolute inset-0 h-full w-full object-cover"
        />
      ) : foto ? (
        <Image src={foto} alt={alt} fill sizes={sizes} className="object-cover" />
      ) : null}
    </div>
  );
}
