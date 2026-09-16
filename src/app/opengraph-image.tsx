import { ImageResponse } from "next/og";
import { getProfilo, getSettings } from "@/lib/content";
import { pick } from "@/i18n";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

/** Immagine social di default, generata dai dati. */
export default async function OgImage() {
  const [s, p] = await Promise.all([getSettings(), getProfilo()]);
  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          background: "linear-gradient(135deg, #e8f3f4 0%, #f7f6f3 50%, #fdf2ed 100%)",
          padding: 64,
          fontFamily: "Georgia, serif",
        }}
      >
        <div
          style={{
            flex: 1,
            display: "flex",
            flexDirection: "column",
            justifyContent: "space-between",
            background: "linear-gradient(165deg, #ffffff, #f3f1ec)",
            borderRadius: "72px 96px 72px 104px",
            border: "1px solid rgba(26,30,34,0.06)",
            boxShadow: "0 30px 80px -30px rgba(26,30,34,0.25)",
            padding: 64,
          }}
        >
          <div style={{ fontSize: 24, letterSpacing: 4, textTransform: "uppercase", color: "#5b6470", fontFamily: "sans-serif" }}>{pick(s.ruolo, "it")}</div>
          <div style={{ display: "flex", flexDirection: "column" }}>
            <div style={{ fontSize: 92, lineHeight: 1, color: "#1a1e22" }}>{s.nome}</div>
            <div style={{ marginTop: 20, fontSize: 32, color: "#0c535c", fontStyle: "italic" }}>{pick(p.titolo, "it")}</div>
          </div>
          <div style={{ height: 3, width: 400, background: "linear-gradient(90deg, transparent, #c9785c, transparent)" }} />
        </div>
      </div>
    ),
    size,
  );
}
