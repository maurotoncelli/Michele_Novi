import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific querySelectorAll line
old_selector = "activeView.querySelectorAll('h1, h2, h3, p, .magnetic-module, .card, form, .bg-white, img');"
new_selector = "activeView.querySelectorAll('h1, h2, h3, h4, p, .magnetic-module, .card, form, ul li');"

content = content.replace(old_selector, new_selector)

# Update the images parallax script to be slightly less invasive if needed
# We already selected img for appearance in the previous line but wait:
# I had a separate loop for img in parallax. Let's make sure img is not double-animated.

# Let's fix the entire setupScrollAnimations function to be safer.
script_start = "// 2. Setup Animazioni e Parallasse Magnetica"
script_end = "// 3. Observer per gestire i cambi pagina (SPA)"

if script_start in content and script_end in content:
    pre = content.split(script_start)[0]
    post = content.split(script_end)[1]
    
    new_setup = """// 2. Setup Animazioni e Parallasse Magnetica
        function setupScrollAnimations() {
            // Elimina vecchi trigger per non sovrapporli
            ScrollTrigger.getAll().forEach(t => t.kill());

            const activeView = document.querySelector('.page-view.active-view');
            if (!activeView) return;

            // Elementi testuali e piccoli contenitori (Apparizione Morbida Awwwards)
            // NON includere contenitori strutturali come .bg-white o intere sezioni per evitare distacchi dai divisori SVG
            const revealElements = activeView.querySelectorAll('h1, h2, h3, h4, p, .magnetic-module, form, .form-group, ul li, .card-reveal, .bg-caldo-surface');
            
            revealElements.forEach(el => {
                // Ignora elementi in header, footer o menu, e bottoni
                if (el.closest('header') || el.closest('footer') || el.closest('#articular-curtain')) return;
                if (el.closest('[style*="display: none"]') || el.closest('[style*="opacity: 0"]')) return;
                
                // Evita glitch su stringhe vuote
                if (el.tagName.toLowerCase() === 'p' && el.innerText.trim().length === 0) return;
                if (el.classList.contains('text-xs') && el.tagName.toLowerCase() !== 'p') return;

                gsap.fromTo(el, 
                    { opacity: 0, y: 50 },
                    {
                        opacity: 1,
                        y: 0,
                        duration: 1.2,
                        ease: "power3.out",
                        scrollTrigger: {
                            trigger: el,
                            start: "top 95%", 
                            toggleActions: "play none none reverse", 
                        }
                    }
                );
            });

            // Parallasse sulle immagini principali (non loghi o icone)
            const images = activeView.querySelectorAll('img:not(.no-parallax)');
            images.forEach(img => {
                if (img.closest('header') || img.closest('footer') || img.closest('#articular-curtain')) return;
                if (img.closest('[style*="display: none"]')) return;
                
                // Evita badge, bottoni ecc
                if (img.width < 100 && img.height < 100 && img.tagName.toLowerCase() !== 'img') return;

                gsap.fromTo(img,
                    { y: -15 },
                    {
                        y: 15,
                        ease: "none",
                        scrollTrigger: {
                            trigger: img,
                            start: "top bottom",
                            end: "bottom top",
                            scrub: 1
                        }
                    }
                );
            });

            ScrollTrigger.refresh();
        }

        """
    
    content = pre + new_setup + "// 3. Observer per gestire i cambi pagina (SPA)" + post

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated selector fixed.")
os.system('cp handoff_sito.html "Proposte HTML/index.html"')

