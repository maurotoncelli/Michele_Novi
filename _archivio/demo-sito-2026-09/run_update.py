import re
import os

file_path = "handoff_sito.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Make sure we don't duplicate
if "Lenis" in content and "gsap" in content:
    print("Animations already injected.")
else:
    animation_script = """
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

            // Elementi testuali e contenitori (Apparizione Morbida)
            const revealElements = activeView.querySelectorAll('h1, h2, h3, h4, p, li, .magnetic-module, .card, form, .form-group');
            revealElements.forEach(el => {
                // Ignora elementi nascosti, header, footer o menu
                if (el.closest('header') || el.closest('footer') || el.closest('#articular-curtain')) return;
                if (el.closest('[style*="display: none"]') || el.closest('[style*="opacity: 0"]')) return;
                
                // Evita glitch su stringhe vuote
                if (el.tagName.toLowerCase() === 'p' && el.innerText.trim().length === 0) return;

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
                            toggleActions: "play none none reverse",
                        }
                    }
                );
            });

            // Elementi grafici, sfondi e immagini (Parallasse Incastro)
            const parallaxElements = activeView.querySelectorAll('img, .bg-caldo-tealLight, .bg-caldo-coralLight, .bg-caldo-salviaLight, .bg-caldo-goldLight, .rounded-full');
            parallaxElements.forEach(el => {
                if (el.closest('header') || el.closest('footer') || el.closest('#articular-curtain')) return;
                if (el.closest('[style*="display: none"]')) return;
                
                // Ignora bottoni arrotondati o piccole icone per non rompere la UI
                if (el.tagName.toLowerCase() === 'button' || el.classList.contains('w-6') || el.classList.contains('h-6')) return;

                // Calcola un leggero offset basato sull'altezza (parallasse awwwards)
                gsap.fromTo(el,
                    { y: -25 },
                    {
                        y: 25,
                        ease: "none",
                        scrollTrigger: {
                            trigger: el,
                            start: "top bottom",
                            end: "bottom top",
                            scrub: 1.5
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
</body>"""

    # Inject right before </body>
    new_content = content.replace("</body>", animation_script)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("Successfully injected Lenis and GSAP Scroll animations.")

    # Copiamo in Proposte HTML
    os.system('cp handoff_sito.html "Proposte HTML/index.html"')
    print("Copied to Proposte HTML/index.html")

