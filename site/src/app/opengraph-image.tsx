import { ImageResponse } from "next/og";
import { getProfilo, getSettings } from "@/lib/content";
import { pick } from "@/i18n";
import { LOGO_MN_PATH } from "@/components/ui/Logo";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

/** Immagine social di default, generata dai dati con il logo ufficiale. */
export default async function OgImage() {
  const [s, p] = await Promise.all([getSettings(), getProfilo()]);
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          background: "#f7f6f3",
          padding: 56,
          fontFamily: "sans-serif",
        }}
      >
        <div
          style={{
            flex: 1,
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            background: "#ffffff",
            border: "1px solid rgba(26, 30, 34, 0.1)",
            padding: 64,
          }}
        >
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
            <div
              style={{
                fontSize: 22,
                fontWeight: 600,
                letterSpacing: 4,
                textTransform: "uppercase",
                color: "#1e6aa8",
              }}
            >
              {pick(s.ruolo, "it")}
            </div>
            <svg width="72" height="89" viewBox="0 0 398 494" fill="none">
              <path fill="#1e6aa8" fillRule="evenodd" clipRule="evenodd" d={LOGO_MN_PATH} />
            </svg>
          </div>
          <div style={{ display: "flex", flexDirection: "column" }}>
            <div style={{ fontSize: 82, fontWeight: 500, lineHeight: 1.02, letterSpacing: -2, color: "#0f3a5a" }}>
              {s.nome}
            </div>
            <div style={{ marginTop: 18, fontSize: 30, lineHeight: 1.35, color: "#5b6470", maxWidth: 880 }}>
              {pick(p.titolo, "it")}
            </div>
          </div>
          <div style={{ height: 4, width: 120, background: "#1e6aa8" }} />
        </div>
      </div>
    ),
    size,
  );
}
