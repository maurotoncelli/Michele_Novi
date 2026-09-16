/** Percorso pubblico di un file Keystatic (già assoluto o solo nome). */
export function srcMedia(file: string | null | undefined, dir: string): string | null {
  if (!file) return null;
  if (file.startsWith("/")) return file;
  if (file.startsWith("http://") || file.startsWith("https://")) return file;
  return `/images/${dir}/${file}`;
}

/** ID YouTube da URL o da ID nudo. */
export function idYoutube(input: string | null | undefined): string | null {
  if (!input) return null;
  const s = input.trim();
  if (!s) return null;
  if (/^[\w-]{11}$/.test(s)) return s;
  try {
    const u = new URL(s);
    const host = u.hostname.replace(/^www\./, "");
    if (host === "youtu.be") {
      const id = u.pathname.split("/").filter(Boolean)[0];
      return id && /^[\w-]{11}$/.test(id) ? id : null;
    }
    if (host === "youtube.com" || host === "m.youtube.com" || host === "youtube-nocookie.com") {
      const v = u.searchParams.get("v");
      if (v && /^[\w-]{11}$/.test(v)) return v;
      const m = u.pathname.match(/\/(?:embed|shorts|live)\/([\w-]{11})/);
      return m?.[1] ?? null;
    }
  } catch {
    return null;
  }
  return null;
}
