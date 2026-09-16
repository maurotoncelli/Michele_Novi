"use client";

import { Children, useState, type ReactNode } from "react";

/** Primo figlio sempre visibile; il secondo si apre al click. */
export function ListaEspandibile({ children, more, less }: { children: ReactNode; more: string; less: string }) {
  const [open, setOpen] = useState(false);
  const [preview, resto] = Children.toArray(children);
  if (!resto) return <>{preview}</>;

  return (
    <div>
      {preview}
      {open ? <div className="mt-4">{resto}</div> : null}
      <div className="mt-6 text-center">
        <button type="button" className="btn btn-osso" aria-expanded={open} onClick={() => setOpen((v) => !v)}>
          {open ? less : more}
        </button>
      </div>
    </div>
  );
}
