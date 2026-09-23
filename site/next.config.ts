import type { NextConfig } from "next";
import { routingRules } from "./src/i18n/routing";

const { rewrites, redirects } = routingRules();

const nextConfig: NextConfig = {
  allowedDevOrigins: ["127.0.0.1"],
  images: {
    formats: ["image/avif", "image/webp"],
    // Senza questo elenco Next ignora quality={92} e ricomprime la hero a 75: diventa morbida.
    qualities: [75, 92],
  },
  async rewrites() {
    // Slug tradotti (EN) → cartelle IT in app/[locale]/
    return { beforeFiles: rewrites, afterFiles: [], fallback: [] };
  },
  async redirects() {
    return [
      // Cartelle IT raggiunte con prefisso EN → slug tradotto (canonical unico)
      ...redirects,
    ];
  },
  async headers() {
    return [
      {
        source: "/(.*)",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
          { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
        ],
      },
    ];
  },
};

export default nextConfig;
