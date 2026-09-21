import React from "react";
import Markdoc, { type Config, type Node, type RenderableTreeNode } from "@markdoc/markdoc";
import type { Locale } from "@/i18n/routing";

/** Il reader Keystatic restituisce il corpo come funzione (lazy) o già risolto. */
type Body = (() => Promise<{ node: Node }>) | { node: Node };
const load = async (b: Body) => (typeof b === "function" ? b() : b);

const config: Config = {
  nodes: {
    heading: {
      ...Markdoc.nodes.heading,
      // Il transform di default emette direttamente h{level}: lo sostituiamo per passare dal componente Heading.
      transform(node, cfg) {
        const attributes = node.transformAttributes(cfg);
        const children = node.transformChildren(cfg);
        return new Markdoc.Tag("Heading", { ...attributes, level: node.attributes.level }, children);
      },
    },
  },
  tags: {
    // Numeri di citazione in apice nel testo dei paper: {% sup %}24{% /sup %}
    sup: { render: "sup", inline: true },
  },
};

function slugify(s: string) {
  return s
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/(^-|-$)/g, "");
}

function textOf(children: React.ReactNode): string {
  return React.Children.toArray(children)
    .map((c) => (typeof c === "string" || typeof c === "number" ? String(c) : React.isValidElement<{ children?: React.ReactNode }>(c) ? textOf(c.props.children) : ""))
    .join("");
}

function Heading({ level, children }: { level: number; children: React.ReactNode }) {
  // Nel corpo di una pagina il livello 1 è già usato dal titolo: # e ## diventano H2, ### H3, #### H4.
  const lvl = Math.min(Math.max(Number(level) || 2, 2), 4);
  const Tag = `h${lvl}` as "h2" | "h3" | "h4";
  return <Tag id={slugify(textOf(children))}>{children}</Tag>;
}

const components = { Heading };

/** Sceglie il corpo nella lingua richiesta; se EN manca, ricade sull'IT. */
export async function renderBody(corpoIt: Body, corpoEn: Body | undefined, locale: Locale) {
  let node: Node | null = null;
  let fallback = false;
  if (locale === "en" && corpoEn) {
    const en = await load(corpoEn);
    if (en.node.children.length > 0) node = en.node;
  }
  if (!node) {
    node = (await load(corpoIt)).node;
    fallback = locale === "en";
  }
  const content: RenderableTreeNode = Markdoc.transform(node, config);
  return { element: Markdoc.renderers.react(content, React, { components }), fallbackToIt: fallback };
}

/** Markdown puro (es. il testo integrale di un paper salvato come stringa in Keystatic). */
export function renderMarkdown(testo: string) {
  const node = Markdoc.parse(testo);
  const content: RenderableTreeNode = Markdoc.transform(node, config);
  return Markdoc.renderers.react(content, React, { components });
}

/** H2 di una stringa markdown, per il sommario. */
export function headingsMarkdown(testo: string): { id: string; text: string }[] {
  const out: { id: string; text: string }[] = [];
  for (const child of Markdoc.parse(testo).walk()) {
    if (child.type === "heading" && child.attributes.level <= 2) {
      const text = [...child.walk()].filter((n) => n.type === "text").map((n) => String(n.attributes.content)).join("");
      out.push({ id: slugify(text), text });
    }
  }
  return out;
}

/** Estrae gli H2 del corpo per un indice. */
export async function headings(corpo: Body): Promise<{ id: string; text: string }[]> {
  const { node } = await load(corpo);
  const out: { id: string; text: string }[] = [];
  for (const child of node.walk()) {
    if (child.type === "heading" && child.attributes.level <= 2) {
      const text = [...child.walk()].filter((n) => n.type === "text").map((n) => String(n.attributes.content)).join("");
      out.push({ id: slugify(text), text });
    }
  }
  return out;
}
