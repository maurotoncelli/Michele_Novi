import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = '<h4 class="text-xl font-serif text-caldo-text font-semibold">Tappe Salienti della Formazione</h4>'
end_marker = """                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================"""

new_timeline = """<h4 class="text-xl font-serif text-caldo-text font-semibold mb-8">Tappe Salienti della Formazione</h4>

                        <!-- TIMELINE VERTICALE FLUIDA -->
                        <div class="relative pl-6 sm:pl-8 border-l-2 border-caldo-borderSoft space-y-8 timeline-container">
                            
                            <!-- Tappa 1 -->
                            <div class="relative timeline-item opacity-0 translate-x-[-20px]">
                                <div class="absolute -left-[35px] sm:-left-[43px] top-1 w-6 h-6 rounded-full bg-caldo-surface border-2 border-caldo-teal flex items-center justify-center">
                                    <div class="w-2 h-2 rounded-full bg-caldo-teal"></div>
                                </div>
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-teal block mb-1">Universit&agrave; di Pisa</span>
                                <strong class="text-base font-serif text-caldo-text block">Laurea in Medicina e Chirurgia</strong>
                                <p class="text-xs text-caldo-muted mt-1 font-light">Votazione 108/110. Formazione di base e solida impronta clinica e diagnostica.</p>
                            </div>

                            <!-- Tappa 2 -->
                            <div class="relative timeline-item opacity-0 translate-x-[-20px]">
                                <div class="absolute -left-[35px] sm:-left-[43px] top-1 w-6 h-6 rounded-full bg-caldo-surface border-2 border-caldo-teal flex items-center justify-center">
                                    <div class="w-2 h-2 rounded-full bg-caldo-teal"></div>
                                </div>
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-teal block mb-1">Universit&agrave; di Pisa</span>
                                <strong class="text-base font-serif text-caldo-text block">Specializzazione in Ortopedia e Traumatologia</strong>
                                <p class="text-xs text-caldo-muted mt-1 font-light">Votazione 110/110 e Lode. Tesi su instabilit&agrave; gleno-omerale (Bankart).</p>
                            </div>

                            <!-- Tappa 3 -->
                            <div class="relative timeline-item opacity-0 translate-x-[-20px]">
                                <div class="absolute -left-[35px] sm:-left-[43px] top-1 w-6 h-6 rounded-full bg-caldo-surface border-2 border-caldo-coral flex items-center justify-center">
                                    <div class="w-2 h-2 rounded-full bg-caldo-coral"></div>
                                </div>
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-coral block mb-1">Fellowship Internazionali</span>
                                <strong class="text-base font-serif text-caldo-text block">UK, USA, Germania</strong>
                                <p class="text-xs text-caldo-muted mt-1 font-light">
                                    RNOH Londra (nervo periferico), Harborview Medical Center Seattle (microchirurgia), Charit&eacute; Berlino (spalla/gomito). Esperienze operative globali.
                                </p>
                            </div>

                            <!-- Tappa 4 -->
                            <div class="relative timeline-item opacity-0 translate-x-[-20px]">
                                <div class="absolute -left-[35px] sm:-left-[43px] top-1 w-6 h-6 rounded-full bg-caldo-surface border-2 border-caldo-salvia flex items-center justify-center">
                                    <div class="w-2 h-2 rounded-full bg-caldo-salvia"></div>
                                </div>
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-salvia block mb-1">Certificazione Nazionale SIUMB</span>
                                <strong class="text-base font-serif text-caldo-text block">Diploma in Ecografia Muscoloscheletrica</strong>
                                <p class="text-xs text-caldo-muted mt-1 font-light">Fondamentale per la diagnostica immediata in studio e l'esecuzione di infiltrazioni eco-guidate ultra-precise.</p>
                            </div>

                            <!-- Tappa 5 -->
                            <div class="relative timeline-item opacity-0 translate-x-[-20px]">
                                <div class="absolute -left-[35px] sm:-left-[43px] top-1 w-6 h-6 rounded-full bg-caldo-surface border-2 border-caldo-teal flex items-center justify-center">
                                    <div class="w-2 h-2 rounded-full bg-caldo-teal animate-pulse"></div>
                                </div>
                                <span class="text-[10px] font-bold uppercase tracking-wider text-caldo-teal block mb-1">2020 – Presente</span>
                                <strong class="text-base font-serif text-caldo-text block">Dirigente Medico Ortopedico</strong>
                                <p class="text-xs text-caldo-muted mt-1 font-light">Ospedale CESAT Fucecchio. Centro regionale di eccellenza per la chirurgia artroscopica e le sostituzioni articolari.</p>
                            </div>

                        </div>
"""

if start_marker in content and end_marker in content:
    pre = content.split(start_marker)[0]
    post = end_marker + content.split(end_marker)[1]
    content = pre + new_timeline + post
    print("Timeline replaced!")

# We also need to add GSAP logic for .timeline-item to make them fluid
gsap_anchor = "// EFFETTO \"TELI AL VENTO\" PER GLI ARTICOLI"
gsap_logic = """
            // EFFETTO TIMELINE FLUIDA (CHI SONO)
            const timelineItems = activeView.querySelectorAll('.timeline-item');
            if (timelineItems.length > 0) {
                gsap.fromTo(timelineItems,
                    { opacity: 0, x: -30 },
                    {
                        opacity: 1, 
                        x: 0,
                        duration: 0.8,
                        stagger: 0.2, // Appaiono una dopo l'altra
                        ease: "back.out(1.2)",
                        scrollTrigger: {
                            trigger: ".timeline-container",
                            start: "top 85%",
                            once: true
                        }
                    }
                );
            }

"""
if gsap_anchor in content:
    content = content.replace(gsap_anchor, gsap_logic + gsap_anchor)
    print("GSAP Timeline logic injected!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

os.system('cp handoff_sito.html "Proposte HTML/index.html"')

