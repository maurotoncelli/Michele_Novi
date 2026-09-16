import os
import re

file_path = "handoff_sito.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# We need to replace the script block we just added with an improved one.
script_start = "<!-- ========================================== -->\n    <!-- AWWWARDS SCROLL & PARALLAX (Lenis + GSAP)  -->"

if script_start in content:
    content = content.split(script_start)[0]

new_script = """
    <!-- ========================================== -->
    <!-- AWWWARDS SCROLL & PARALLAX (Lenis + GSAP)  -->
    <!-- ========================================== -->
    <link rel="stylesheet" href="https://unpkg.com/lenis@1.1.9/dist/lenis.css">
    <script src="https://unpkg.com/lenis@1.1.9/dist/lenis.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
    <script>
        // 1. Inizializzazione Lenis (Smooth Scrolling fluido)
        const lenis = new Lenis({
            duration: 1.2,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            direction: 'vertical',
            gestureDirection: 'vertical',
            smooth: true,
            mouseMultiplier: 1,
            smoothTouch: false,
            touchMultiplier: 2,
            infinite: false,
        });

        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => { lenis.raf(time * 1000); });
        gsap.ticker.lagSmoothing(0);

        // 2. Setup Animazioni e Parallasse Magnetica
        function setupScrollAnimations() {
            // Elimina vecchi trigger per non sovrapporli
            ScrollTrigger.getAll().forEach(t => t.kill());

            const activeView = document.querySelector('.page-view.active-view');
            if (!activeView) return;

            // Elementi testuali e contenitori (Apparizione Morbida Awwwards)
            // Selezioniamo elementi blocco principali per evitare di spaccare i layout flex/grid
            const revealElements = activeView.querySelectorAll('h1, h2, h3, p, .magnetic-module, .card, form, .bg-white, img');
            
            revealElements.forEach(el => {
                // Ignora elementi nascosti, header, footer o menu, e bottoni piccoli
                if (el.closest('header') || el.closest('footer') || el.closest('#articular-curtain')) return;
                if (el.closest('[style*="display: none"]') || el.closest('[style*="opacity: 0"]')) return;
                
                // Evita glitch su stringhe vuote o elementi piccolissimi
                if (el.tagName.toLowerCase() === 'p' && el.innerText.trim().length === 0) return;
                if (el.classList.contains('text-xs')) return;

                // Animazione di apparizione con leggero parallax intrinseco (y: 60)
                gsap.fromTo(el, 
                    { opacity: 0, y: 60 },
                    {
                        opacity: 1,
                        y: 0,
                        duration: 1.2,
                        ease: "power3.out",
                        scrollTrigger: {
                            trigger: el,
                            start: "top 95%", // Inizia appena entra nello schermo
                            toggleActions: "play none none reverse", // Appare scorrendo in giù, scompare in su
                        }
                    }
                );
            });

            // Aggiungiamo un vero e proprio effetto parallasse alle immagini (scrub)
            const images = activeView.querySelectorAll('img');
            images.forEach(img => {
                if (img.closest('header') || img.closest('footer') || img.closest('#articular-curtain')) return;
                if (img.closest('[style*="display: none"]')) return;

                // Facciamo un wrap virtuale o usiamo il contenitore per mascherare se possibile, 
                // ma dato che non possiamo modificare l'html, applichiamo un leggero y shift.
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

        // 3. Observer per gestire i cambi pagina (SPA)
        document.addEventListener('DOMContentLoaded', () => {
            const observer = new MutationObserver((mutations) => {
                mutations.forEach(mutation => {
                    if (mutation.type === 'attributes' && mutation.attributeName === 'class') {
                        if (mutation.target.classList.contains('active-view')) {
                            // Quando una vista diventa attiva, resetta scroll e animazioni
                            lenis.scrollTo(0, {immediate: true});
                            // Attendi la fine della tendina (400ms)
                            setTimeout(setupScrollAnimations, 450);
                        }
                    }
                });
            });

            document.querySelectorAll('.page-view').forEach(view => {
                observer.observe(view, { attributes: true });
            });

            // Avvio iniziale (con delay per permettere il rendering)
            setTimeout(setupScrollAnimations, 300);
        });
    </script>
</body>
"""

new_content = content + new_script

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated script applied.")
os.system('cp handoff_sito.html "Proposte HTML/index.html"')

