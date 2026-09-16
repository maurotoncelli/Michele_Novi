import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject the button and grid ID
target_html = """            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Spalla -->"""

replacement_html = """            <!-- TOGGLE INCASTRO AREE CLINICHE -->
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-6 gap-4">
                <h3 class="font-serif text-xl text-caldo-text font-semibold hidden sm:block">Aree Specialistiche</h3>
                <button id="btn-toggle-grid-snap" class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-caldo-tealLight text-caldo-teal text-xs font-bold hover:bg-caldo-teal hover:text-white transition-all cursor-pointer shadow-sm mx-auto sm:mx-0 group">
                    <svg class="w-4 h-4 transition-transform group-hover:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M12 4v16"/><path d="M4 12h16"/></svg>
                    <span>Simula Incastro Multidisciplinare</span>
                </button>
            </div>

            <div id="patologie-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 transition-all duration-1000 ease-[cubic-bezier(0.87,0,0.13,1)]">
                <!-- Spalla -->"""

if target_html in content:
    content = content.replace(target_html, replacement_html)
    print("Replaced grid header.")
else:
    # try a regex if spacing differs
    pass

# 2. Add transition classes to the cards inside this grid
# They currently are `<div class="card-soft-gradient p-8 rounded-3xl flex flex-col justify-between">`
# I will add the javascript at the bottom to handle the morphing.

script_to_inject = """
        // 8. INCASTRO MULTIDISCIPLINARE PATOLOGIE (GRID)
        const btnGridSnap = document.getElementById('btn-toggle-grid-snap');
        const patologieGrid = document.getElementById('patologie-grid');

        if (btnGridSnap && patologieGrid) {
            const cards = patologieGrid.querySelectorAll('.card-soft-gradient');
            // Aggiungi classi di transizione alle card
            cards.forEach(card => card.classList.add('transition-all', 'duration-1000', 'ease-[cubic-bezier(0.87,0,0.13,1)]'));

            btnGridSnap.addEventListener('click', () => {
                const isLocked = patologieGrid.classList.contains('gap-0');
                
                if (!isLocked) {
                    // ATTIVA L'INCASTRO
                    patologieGrid.classList.remove('gap-8');
                    patologieGrid.classList.add('gap-0');
                    
                    btnGridSnap.innerHTML = `
                        <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                        <span>Scollega Aree Cliniche</span>
                    `;
                    btnGridSnap.classList.add('bg-caldo-teal', 'text-white');
                    btnGridSnap.classList.remove('bg-caldo-tealLight', 'text-caldo-teal');

                    cards.forEach((card, index) => {
                        card.classList.remove('rounded-3xl');
                        // Togliamo i bordi normali per evitare doppi bordi
                        card.style.border = '0.5px solid rgba(235, 230, 222, 0.4)';
                        
                        // Arrotonda solo gli angoli esterni del blocco fuso (dipende da desktop/mobile, qui facciamo finta sia desktop per semplicità visiva, ma Tailwind ci aiuta)
                        if(window.innerWidth >= 1024) { // LG (3 colonne)
                            if (index === 0) card.classList.add('rounded-tl-[40px]');
                            if (index === 2) card.classList.add('rounded-tr-[40px]');
                            if (index === 3) card.classList.add('rounded-bl-[40px]');
                            if (index === 5) card.classList.add('rounded-br-[40px]');
                        } else if (window.innerWidth >= 768) { // MD (2 colonne)
                            if (index === 0) card.classList.add('rounded-tl-[40px]');
                            if (index === 1) card.classList.add('rounded-tr-[40px]');
                            if (index === 4) card.classList.add('rounded-bl-[40px]');
                            if (index === 5) card.classList.add('rounded-br-[40px]');
                        } else {
                            if (index === 0) card.classList.add('rounded-t-[40px]');
                            if (index === 5) card.classList.add('rounded-b-[40px]');
                        }
                        
                        // Modifica il background per farli sembrare una lastra unita
                        card.style.background = 'rgba(255,255,255, 0.9)';
                    });
                } else {
                    // DISATTIVA L'INCASTRO
                    patologieGrid.classList.remove('gap-0');
                    patologieGrid.classList.add('gap-8');
                    
                    btnGridSnap.innerHTML = `
                        <svg class="w-4 h-4 transition-transform group-hover:rotate-180" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="M12 4v16"/><path d="M4 12h16"/></svg>
                        <span>Simula Incastro Multidisciplinare</span>
                    `;
                    btnGridSnap.classList.remove('bg-caldo-teal', 'text-white');
                    btnGridSnap.classList.add('bg-caldo-tealLight', 'text-caldo-teal');

                    cards.forEach((card) => {
                        card.classList.add('rounded-3xl');
                        card.classList.remove('rounded-tl-[40px]', 'rounded-tr-[40px]', 'rounded-bl-[40px]', 'rounded-br-[40px]', 'rounded-t-[40px]', 'rounded-b-[40px]');
                        card.style.border = '';
                        card.style.background = '';
                    });
                }
            });
        }
"""

script_anchor = "// GESTIONE BIVIO TERAPEUTICO IN PATOLOGIE"
if script_anchor in content:
    content = content.replace(script_anchor, script_to_inject + "\n        " + script_anchor)
    print("Injected JS logic.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

os.system('cp handoff_sito.html "Proposte HTML/index.html"')
