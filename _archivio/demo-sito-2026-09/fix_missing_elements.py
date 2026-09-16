import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# We need to completely rewrite the GSAP setupScrollAnimations function to be bulletproof.

start_marker = "// 2. Setup Animazioni e Parallasse Magnetica"
end_marker = "// 3. Observer per gestire i cambi pagina (SPA)"

new_func = """// 2. Setup Animazioni e Parallasse Magnetica
        function setupScrollAnimations() {
            // Elimina vecchi trigger per non sovrapporli
            ScrollTrigger.getAll().forEach(t => t.kill());

            const activeView = document.querySelector('.page-view.active-view');
            if (!activeView) return;

            // Elementi testuali e piccoli contenitori (Apparizione Morbida Awwwards)
            // Selezioniamo tutti i potenziali elementi
            const rawElements = Array.from(activeView.querySelectorAll('h1, h2, h3, h4, p, .magnetic-module, form, ul li, .card-soft-gradient'));
            
            // FILTRIAMO per evitare animazioni annidate (che causano conflitti) e sticky (che rompono ScrollTrigger)
            const revealElements = rawElements.filter(el => {
                if (el.closest('header') || el.closest('footer') || el.closest('#articular-curtain')) return false;
                if (el.closest('.strata-card-soft')) return false;
                
                // Se l'elemento è dentro una card-soft-gradient, animiamo solo la card e NON i suoi figli, 
                // per evitare che si sovrappongano transizioni (il form o l'h3 sparirebbero mentre la card appare)
                if (el.closest('.card-soft-gradient') && el !== el.closest('.card-soft-gradient')) return false;

                // Evita glitch su stringhe vuote
                if (el.tagName.toLowerCase() === 'p' && el.innerText.trim().length === 0) return false;
                return true;
            });

            revealElements.forEach(el => {
                gsap.fromTo(el, 
                    { opacity: 0, y: 40 },
                    {
                        opacity: 1,
                        y: 0,
                        duration: 1,
                        ease: "power3.out",
                        scrollTrigger: {
                            trigger: el,
                            start: "top 95%", 
                            // IMPORTANTE: usiamo once: true in modo che, una volta apparsi, non scompaiano mai più!
                            // Questo previene i conflitti quando si scrolla velocemente in cima (SPA bug)
                            once: true
                        }
                    }
                );
            });

            // Parallasse sulle immagini
            const images = activeView.querySelectorAll('img:not(.no-parallax)');
            images.forEach(img => {
                if (img.closest('header') || img.closest('footer') || img.closest('#articular-curtain')) return;
                if (img.width < 100 && img.height < 100) return;

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

if start_marker in content and end_marker in content:
    pre = content.split(start_marker)[0]
    post = content.split(end_marker)[1]
    
    content = pre + new_func + end_marker + post
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed missing elements script!")

os.system('cp handoff_sito.html "Proposte HTML/index.html"')

