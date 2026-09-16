import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I will replace the script part that defines revealElements and the exclusions.

script_start = "const revealElements = activeView.querySelectorAll('h1, h2, h3, h4, p, .magnetic-module, form, .form-group, ul li, .strata-card-soft, .card-soft-gradient');"

new_script = """const revealElements = activeView.querySelectorAll('h1, h2, h3, h4, p, .magnetic-module, form, .form-group, ul li, .card-soft-gradient');
            
            revealElements.forEach(el => {
                // Ignora elementi in header, footer o menu, e bottoni
                if (el.closest('header') || el.closest('footer') || el.closest('#articular-curtain')) return;
                if (el.closest('[style*="display: none"]') || el.closest('[style*="opacity: 0"]')) return;
                
                // CRITICAL FIX: DO NOT animate elements inside position: sticky containers! 
                // It breaks ScrollTrigger because their visual position doesn't match their native position.
                if (el.closest('.strata-card-soft')) return;
                
                // Evita glitch su stringhe vuote
                if (el.tagName.toLowerCase() === 'p' && el.innerText.trim().length === 0) return;
                if (el.classList.contains('text-xs') && el.tagName.toLowerCase() !== 'p') return;"""

# Replace the chunk
# We will use regex or string replace. Let's just find the start and replace the block.
# Actually I'll use a precise replacement.

old_chunk = """const revealElements = activeView.querySelectorAll('h1, h2, h3, h4, p, .magnetic-module, form, .form-group, ul li, .strata-card-soft, .card-soft-gradient');
            
            revealElements.forEach(el => {
                // Ignora elementi in header, footer o menu, e bottoni
                if (el.closest('header') || el.closest('footer') || el.closest('#articular-curtain')) return;
                if (el.closest('[style*="display: none"]') || el.closest('[style*="opacity: 0"]')) return;
                
                // Evita glitch su stringhe vuote
                if (el.tagName.toLowerCase() === 'p' && el.innerText.trim().length === 0) return;
                if (el.classList.contains('text-xs') && el.tagName.toLowerCase() !== 'p') return;"""

if old_chunk in content:
    content = content.replace(old_chunk, new_script)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed sticky text issue!")
else:
    print("Chunk not found. Let me try regex.")

os.system('cp handoff_sito.html "Proposte HTML/index.html"')

