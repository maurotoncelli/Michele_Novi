import { NotFoundView } from "@/components/NotFoundView";
import { getMessages } from "@/i18n";
import { href, locales } from "@/i18n/routing";

/** I params non arrivano nel not-found: si passano i testi di tutte le lingue e il client sceglie dal pathname. */
export default function NotFound() {
  const testi = Object.fromEntries(
    locales.map((l) => {
      const m = getMessages(l);
      return [l, { titolo: m.notFound.titolo, testo: m.notFound.testo, home: m.notFound.home, homeHref: href(l, { kind: "home" }) }];
    }),
  ) as Record<(typeof locales)[number], { titolo: string; testo: string; home: string; homeHref: string }>;
  return <NotFoundView testi={testi} />;
}
