import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update text "Note cliniche" -> "Pubblicazioni & Ricerca" or similar across the whole file
content = content.replace("Note cliniche (Il Quaderno)", "Pubblicazioni & Ricerca")
content = content.replace("Note cliniche", "Pubblicazioni")
content = content.replace("Torna alle Pubblicazioni", "Torna alle Pubblicazioni")

# 2. Add Cover Photo to #view-articoli-remplissage
target_header = """        <!-- ARTICOLO COMPLETO REMPLISSAGE -->
        <section id="view-articoli-remplissage" class="page-view max-w-3xl mx-auto px-6 py-16">
            <a href="#articoli" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-caldo-teal hover:text-caldo-coral mb-8" data-target="articoli">← Torna alle Pubblicazioni</a>
            <div class="flex items-center gap-3 text-xs text-caldo-muted mb-4">
                <span class="bg-caldo-tealLight text-caldo-teal font-semibold px-3 py-1 rounded-full">Studio Clinico 2022</span>
                <span>Rivista Internazionale Osteology · Autori: M. Novi et al.</span>
            </div>
            <h1 class="text-3xl sm:text-5xl font-serif text-caldo-text leading-tight mb-8">
                Il dubbio nel remplissage: quando la stabilità rischia di sacrificare il movimento.
            </h1>"""

new_header = """        <!-- ARTICOLO COMPLETO REMPLISSAGE -->
        <section id="view-articoli-remplissage" class="page-view w-full">
            <!-- COPERTINA ARTICOLO -->
            <div class="relative w-full h-[50vh] sm:h-[60vh] bg-caldo-tealLight overflow-hidden mb-12">
                <img src="https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?q=80&w=2000&auto=format&fit=crop" alt="Copertina Articolo Remplissage" class="absolute inset-0 w-full h-full object-cover parallax-img opacity-90">
                <div class="absolute inset-0 bg-gradient-to-t from-[#FAF8F5] via-transparent to-black/30"></div>
                
                <!-- Contenuto in Sovrimpressione sulla Copertina -->
                <div class="absolute inset-0 flex flex-col justify-end pb-12">
                    <div class="max-w-4xl mx-auto px-6 w-full">
                        <a href="#articoli" class="nav-trigger inline-flex items-center gap-2 text-xs font-semibold text-white/80 hover:text-white mb-6 backdrop-blur-sm bg-black/20 px-4 py-2 rounded-full transition-all" data-target="articoli">← Torna alle Pubblicazioni</a>
                        <div class="flex items-center gap-3 text-xs text-white/90 mb-4">
                            <span class="bg-caldo-teal text-white font-semibold px-3 py-1 rounded-full shadow-sm">Studio Clinico 2022</span>
                            <span class="backdrop-blur-sm bg-black/20 px-3 py-1 rounded-full">Rivista Internazionale Osteology · Autori: M. Novi et al.</span>
                        </div>
                        <h1 class="text-4xl sm:text-6xl font-serif text-caldo-text leading-tight mb-4 drop-shadow-md">
                            Il dubbio nel remplissage: quando la stabilità rischia di sacrificare il movimento.
                        </h1>
                    </div>
                </div>
            </div>

            <!-- CORPO TESTO -->
            <div class="max-w-3xl mx-auto px-6 pb-24">"""

if target_header in content:
    content = content.replace(target_header, new_header)
    print("Added cover photo to article page!")
else:
    print("Could not find article header to replace.")

# We also need to fix the closing tags for the new structure (max-w-3xl wrapper)
# We added <div class="max-w-3xl mx-auto px-6 pb-24"> so we just let the section end naturally, but wait:
# The old section was `<section id="view-articoli-remplissage" class="page-view max-w-3xl mx-auto px-6 py-16">`
# So the inner content was just inside the section. Now there is a wrapper. We need to close it.
closing_target = """                <!-- PONTE BIOMECCANICO AD INCASTRO PAPER OSTEOLOGY 2022 -->"""
new_closing = """                <!-- PONTE BIOMECCANICO AD INCASTRO PAPER OSTEOLOGY 2022 -->"""
# Actually, if we just let the <section> close it, the <div> will be unclosed.
content = content.replace("</section>\n\n        <!-- ========================================================\n             VISTA 6: CONTATTI", "</div>\n        </section>\n\n        <!-- ========================================================\n             VISTA 6: CONTATTI")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

os.system('cp handoff_sito.html "Proposte HTML/index.html"')
