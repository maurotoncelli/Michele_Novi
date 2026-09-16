import { NextResponse, type NextRequest } from "next/server";
import { defaultLocale, isLocale } from "@/i18n/routing";

const COOKIE = "mn_lang";

function preferred(req: NextRequest): string {
  const c = req.cookies.get(COOKIE)?.value;
  if (c && isLocale(c)) return c;
  const al = req.headers.get("accept-language") ?? "";
  for (const part of al.split(",")) {
    const lang = part.trim().split(";")[0].slice(0, 2).toLowerCase();
    if (isLocale(lang)) return lang;
  }
  return defaultLocale;
}

export function proxy(req: NextRequest) {
  const { pathname } = req.nextUrl;
  const first = pathname.split("/")[1] ?? "";

  if (isLocale(first)) {
    // Ricorda la lingua scelta esplicitamente
    const res = NextResponse.next();
    if (req.cookies.get(COOKIE)?.value !== first) {
      res.cookies.set(COOKIE, first, { path: "/", maxAge: 60 * 60 * 24 * 365, sameSite: "lax" });
    }
    return res;
  }

  // Percorso senza lingua → redirect alla lingua preferita
  const locale = preferred(req);
  const url = req.nextUrl.clone();
  url.pathname = `/${locale}${pathname === "/" ? "" : pathname}`;
  return NextResponse.redirect(url, pathname === "/" ? 307 : 308);
}

export const config = {
  matcher: [
    // Tutto tranne asset, API, keystatic e file di metadata
    `/((?!_next|api|keystatic|images|paper|fonts|favicon\\.ico|icon|apple-icon|opengraph-image|robots\\.txt|sitemap\\.xml|manifest\\.webmanifest|llms\\.txt|.*\\..*).*)`,
  ],
};
