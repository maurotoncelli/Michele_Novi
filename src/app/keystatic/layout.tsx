import type { Metadata } from "next";

export const metadata: Metadata = { title: "Michele Novi — Gestione contenuti", robots: { index: false, follow: false } };

/** Root layout dedicato al pannello (fuori dal layout [locale] del sito). */
export default function KeystaticLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="it">
      <body>{children}</body>
    </html>
  );
}
