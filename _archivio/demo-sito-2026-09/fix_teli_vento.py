import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace the view-articoli section
old_section_regex = r'<section id="view-articoli".*?</section>'
# Wait, regex might fail if it spans multiple lines. Let's use substring replacement.

start_str = '<section id="view-articoli" class="page-view'
end_str = '        <!-- ARTICOLO COMPLETO REMPLISSAGE -->'

if start_str in content and end_str in content:
    pre = content.split(start_str)[0]
    post = end_str + content.split(end_str, 1)[1]
    
    new_section = """<section id="view-articoli" class="page-view w-full">
            <!-- Hero Pubblicazioni -->
            <div class="max-w-6xl mx-auto px-6 pt-16 pb-12">
                <a href="#home" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8 transition-colors" data-target="home">
                    <span>← Torna alla Home</span>
                </a>
                <div class="max-w-3xl space-y-5">
                    <span class="text-xs font-semibold text-caldo-teal bg-caldo-tealLight px-3.5 py-1.5 rounded-full inline-block tracking-wider uppercase">Pubblicazioni & Ricerca</span>
                    <h1 class="text-5xl sm:text-7xl font-serif text-caldo-text leading-[1.1]">Letteratura scientifica in corsia.</h1>
                    <p class="text-lg text-caldo-muted font-light leading-relaxed max-w-2xl">
                        Nessun contenuto acchiappa-click: qui trovi paper scientifici, risultati chirurgici documentati e casi di sala operatoria. Un archivio vivo che si spiega scorrendo, come grandi teli mossi dal vento della ricerca.
                    </p>
                </div>
            </div>

            <!-- Contenitore Teli al Vento (perspective-container) -->
            <div class="px-4 sm:px-6 pb-32 max-w-6xl mx-auto space-y-24" style="perspective: 1500px;">
                
                <!-- Articolo 1 (Remplissage) -->
                <a href="#articoli-remplissage" class="nav-trigger block group telo-vento relative overflow-hidden rounded-[40px] shadow-2xl hover:shadow-caldo-teal/20 transition-shadow duration-700 bg-white" data-target="articoli-remplissage" style="transform-origin: top center;">
                    <div class="grid md:grid-cols-2 min-h-[500px]">
                        <div class="relative h-64 md:h-auto overflow-hidden bg-caldo-tealLight">
                            <img src="https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?q=80&w=1600&auto=format&fit=crop" alt="Chirurgia Spalla" class="absolute inset-0 w-full h-full object-cover parallax-img group-hover:scale-105 transition-transform duration-1000 ease-out">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent md:bg-gradient-to-r md:from-transparent md:to-black/10"></div>
                        </div>
                        <div class="p-10 sm:p-14 flex flex-col justify-center bg-white relative z-10">
                            <div class="flex items-center gap-3 mb-6">
                                <span class="bg-caldo-coralLight text-caldo-coral text-[10px] font-bold uppercase tracking-wider px-3 py-1.5 rounded-full">Paper Osteology 2022</span>
                                <span class="text-[10px] text-caldo-muted tracking-wider uppercase font-semibold">CESAT Fucecchio</span>
                            </div>
                            <h2 class="text-3xl sm:text-4xl font-serif text-caldo-text group-hover:text-caldo-teal transition-colors mb-6 leading-tight">
                                Il dubbio nel remplissage: stabilità vs rotazione nello sportivo.
                            </h2>
                            <p class="text-base text-caldo-muted leading-relaxed mb-10 font-light">
                                Nelle lussazioni recidivanti con difetto osseo della testa omerale (Hill-Sachs), colmare la cavità suturando il tendine infraspinato impedisce nuove fuoriuscite. I risultati a due anni confermano una rotazione preservata e zero recidive.
                            </p>
                            <div class="flex items-center gap-4 border-t border-caldo-borderSoft pt-6 mt-auto">
                                <span class="w-10 h-10 rounded-full bg-caldo-tealLight text-caldo-teal flex items-center justify-center group-hover:bg-caldo-teal group-hover:text-white transition-colors">
                                    <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                                </span>
                                <span class="text-sm font-semibold text-caldo-teal">Leggi l'articolo completo</span>
                            </div>
                        </div>
                    </div>
                </a>

                <!-- Articolo 2 (Nuovo per dare l'effetto di flusso multiplo) -->
                <a href="#articoli" class="nav-trigger block group telo-vento relative overflow-hidden rounded-[40px] shadow-2xl hover:shadow-caldo-teal/20 transition-shadow duration-700 bg-white" data-target="articoli" style="transform-origin: top center;">
                    <div class="grid md:grid-cols-2 min-h-[500px]">
                        <div class="md:order-2 relative h-64 md:h-auto overflow-hidden bg-caldo-salviaLight">
                            <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?q=80&w=1600&auto=format&fit=crop" alt="Ricerca Ortopedica" class="absolute inset-0 w-full h-full object-cover parallax-img group-hover:scale-105 transition-transform duration-1000 ease-out">
                        </div>
                        <div class="md:order-1 p-10 sm:p-14 flex flex-col justify-center bg-white relative z-10">
                            <div class="flex items-center gap-3 mb-6">
                                <span class="bg-caldo-tealLight text-caldo-teal text-[10px] font-bold uppercase tracking-wider px-3 py-1.5 rounded-full">Clinical Review 2023</span>
                                <span class="text-[10px] text-caldo-muted tracking-wider uppercase font-semibold">Tecniche Mininvasive</span>
                            </div>
                            <h2 class="text-3xl sm:text-4xl font-serif text-caldo-text group-hover:text-caldo-teal transition-colors mb-6 leading-tight">
                                Decompressione endoscopica del tunnel carpale: i vantaggi per il polso.
                            </h2>
                            <p class="text-base text-caldo-muted leading-relaxed mb-10 font-light">
                                Un'analisi approfondita sul rilascio del nervo mediano in via endoscopica. Lo studio evidenzia una riduzione dei tempi di recupero lavorativo del 40% rispetto alla chirurgia aperta tradizionale, preservando il palmo della mano.
                            </p>
                            <div class="flex items-center gap-4 border-t border-caldo-borderSoft pt-6 mt-auto">
                                <span class="w-10 h-10 rounded-full bg-caldo-tealLight text-caldo-teal flex items-center justify-center group-hover:bg-caldo-teal group-hover:text-white transition-colors">
                                    <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                                </span>
                                <span class="text-sm font-semibold text-caldo-teal">Esplora la ricerca</span>
                            </div>
                        </div>
                    </div>
                </a>

            </div>
        </section>
"""
    content = pre + new_section + post
    print("Section replaced.")
else:
    print("Failed to replace view-articoli section.")

# 2. Add the GSAP telo-vento logic
gsap_anchor = "ScrollTrigger.refresh();"
gsap_logic = """
            // EFFETTO "TELI AL VENTO" PER GLI ARTICOLI
            const teli = activeView.querySelectorAll('.telo-vento');
            teli.forEach(telo => {
                // Se c'è un'animazione nativa, la spegniamo per i teli
                gsap.fromTo(telo,
                    { 
                        rotationX: 12, 
                        y: 120, 
                        z: -50,
                        opacity: 0,
                        transformPerspective: 1500
                    },
                    {
                        rotationX: 0,
                        y: 0,
                        z: 0,
                        opacity: 1,
                        ease: "power2.out",
                        scrollTrigger: {
                            trigger: telo,
                            start: "top 95%",
                            end: "top 40%",
                            scrub: 1.2 // Rende l'effetto di srotolamento fluido al vento (dipendente dallo scroll)
                        }
                    }
                );
            });

            """

if gsap_anchor in content:
    content = content.replace(gsap_anchor, gsap_logic + gsap_anchor)
    print("Injected GSAP teli al vento logic.")
else:
    print("Failed to inject GSAP logic.")

# We also need to exclude .telo-vento from the standard revealElements so they don't get double animated
# The script currently has:
# if (el.closest('.strata-card-soft')) return false;

exclude_str = "if (el.closest('.strata-card-soft')) return false;"
new_exclude = "if (el.closest('.strata-card-soft') || el.closest('.telo-vento')) return false;"

content = content.replace(exclude_str, new_exclude)

# Lastly, we need to update navigation triggers in the footer and quick nav if they said "Note cliniche"
content = content.replace("Note cliniche (Il Quaderno)", "Pubblicazioni & Ricerca")
content = content.replace("← Torna alle Note cliniche", "← Torna alle Pubblicazioni")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

os.system('cp handoff_sito.html "Proposte HTML/index.html"')

