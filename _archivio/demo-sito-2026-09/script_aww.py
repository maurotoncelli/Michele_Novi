import os

html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dott. Michele Novi | Ortopedico</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Darker+Grotesque:wght@300;400;500;600;700;800;900&family=Newsreader:ital,opsz,wght@0,6..72,200;0,6..72,300;0,6..72,400;0,6..72,500;1,6..72,200;1,6..72,300;1,6..72,400&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        medical: {
                            bg: '#F3F4F3',          /* Off-white molto materico, stile carta cotone */
                            surface: '#EAEBEA',
                            border: '#D0D1D0',
                            text: '#090A09',        /* Nero off-black profondo */
                            muted: '#6B7280',
                            accent: '#004c57',      /* Ottanio scurissimo scuro, chic */
                            accentHover: '#002930',
                        }
                    },
                    fontFamily: {
                        serif: ['Newsreader', 'serif'],
                        sans: ['Darker Grotesque', 'sans-serif'],
                        mono: ['Courier New', 'monospace']
                    }
                }
            }
        }
    </script>
    
    <style>
        :root {
            --ease-awwwards: cubic-bezier(0.7, 0, 0.3, 1);
            --ease-out: cubic-bezier(0.215, 0.61, 0.355, 1);
        }

        body {
            background-color: var(--medical-bg);
            color: #090A09;
            font-family: 'Darker Grotesque', sans-serif;
            overflow-x: hidden;
            scroll-behavior: smooth;
            -webkit-font-smoothing: antialiased;
        }

        /* Tipografia Awwwards: Enorme, tight tracking */
        .text-huge {
            font-size: clamp(4rem, 12vw, 12rem);
            line-height: 0.85;
            letter-spacing: -0.04em;
            text-transform: uppercase;
            font-weight: 800;
        }
        .text-huge-serif {
            font-family: 'Newsreader', serif;
            font-size: clamp(4rem, 12vw, 13rem);
            line-height: 0.85;
            letter-spacing: -0.05em;
            font-weight: 400;
            text-transform: none;
        }

        /* Grid Architetturale (Awwwards staple) */
        .grid-lines {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            pointer-events: none; z-index: -1; display: flex; justify-content: center;
        }
        .grid-lines-inner {
            width: 100%; height: 100%; display: grid; grid-template-columns: repeat(4, 1fr);
            border-left: 1px solid #D0D1D0; border-right: 1px solid #D0D1D0; opacity: 0.3;
        }
        .grid-lines-inner div { border-right: 1px solid #D0D1D0; }
        .grid-lines-inner div:last-child { border-right: none; }

        /* Linee Awwwards (Thin borders) */
        .aww-border-b { border-bottom: 1px solid #D0D1D0; }
        .aww-border-t { border-top: 1px solid #D0D1D0; }

        /* Reveal text on scroll */
        .reveal-mask { overflow: hidden; display: block; }
        .reveal-inner { 
            display: inline-block; 
            transform: translateY(110%); 
            transition: transform 1.2s var(--ease-awwwards); 
            will-change: transform; 
        }
        .is-visible .reveal-inner { transform: translateY(0); }

        /* Magnetic button estremo */
        .btn-awwwards {
            position: relative; overflow: hidden;
            border-radius: 999px;
            border: 1px solid #090A09;
            color: #090A09; background: transparent;
            transition: color 0.5s var(--ease-awwwards);
            display: inline-flex; align-items: center; justify-content: center;
        }
        .btn-awwwards::after {
            content: ''; position: absolute; bottom: 0; left: 0; width: 100%; height: 0%;
            background: #090A09; z-index: -1; border-radius: 50% 50% 0 0;
            transition: height 0.5s var(--ease-awwwards), border-radius 0.5s var(--ease-awwwards);
        }
        .btn-awwwards:hover { color: #F3F4F3; }
        .btn-awwwards:hover::after { height: 100%; border-radius: 0; }

        /* Hover lists (sostituisce il row-quaderno) */
        .list-row {
            transition: color 0.4s var(--ease-awwwards), padding-left 0.4s var(--ease-awwwards);
            cursor: pointer;
        }
        .list-row:hover {
            color: var(--medical-accent);
            padding-left: 2rem;
        }
        
        .list-row-img {
            position: absolute; right: 2rem; top: 50%; transform: translateY(-50%) scale(0.8) rotate(5deg);
            opacity: 0; pointer-events: none;
            transition: opacity 0.4s var(--ease-awwwards), transform 0.4s var(--ease-awwwards);
            width: 300px; height: 200px; object-fit: cover; z-index: 10;
        }
        .list-row:hover .list-row-img {
            opacity: 1; transform: translateY(-50%) scale(1) rotate(0deg);
        }

        /* Immagini Brutaliste */
        .img-brutalist {
            filter: grayscale(100%);
            transition: filter 1s var(--ease-awwwards);
        }
        .img-brutalist:hover { filter: grayscale(0%); }

        /* SPA Logic */
        .page-view { display: none; opacity: 0; }
        .page-view.active-view { 
            display: block; 
            animation: viewEnter 1s var(--ease-awwwards) forwards; 
        }
        @keyframes viewEnter { 
            0% { opacity: 0; transform: translateY(40px); clip-path: inset(10% 0 0 0); } 
            100% { opacity: 1; transform: translateY(0); clip-path: inset(0% 0 0 0); } 
        }
    </style>
</head>
<body class="selection:bg-medical-text selection:text-medical-bg bg-[#F3F4F3]">

    <div class="grid-lines hidden md:flex"><div class="grid-lines-inner"><div></div><div></div><div></div><div></div></div></div>

    <!-- Header Awwwards: minimale, blend-mode -->
    <header class="fixed top-0 w-full z-50 mix-blend-difference text-white transition-transform duration-500 p-6" id="main-header">
        <div class="flex justify-between items-start">
            <a href="#home" class="nav-target text-2xl font-bold tracking-tighter uppercase leading-none" data-target="home">
                Michele<br>Novi<span class="text-[0.4em] align-top">®</span>
            </a>
            <nav class="hidden lg:flex flex-col text-right text-sm font-semibold tracking-wide uppercase">
                <a href="#chi-sono" class="nav-target hover:opacity-50 transition-opacity" data-target="chi-sono">Chi Sono</a>
                <a href="#patologie" class="nav-target hover:opacity-50 transition-opacity" data-target="patologie">Patologie</a>
                <a href="#sedi" class="nav-target hover:opacity-50 transition-opacity" data-target="sedi">Sedi</a>
                <a href="#articoli" class="nav-target hover:opacity-50 transition-opacity" data-target="articoli">Articoli</a>
            </nav>
            <a href="#contatti" class="nav-target text-sm font-semibold tracking-wide uppercase hover:opacity-50 transition-opacity" data-target="contatti">Contatti / Prenota</a>
        </div>
    </header>

    <main id="app-root">

        <!-- ================= HOME ================= -->
        <section id="view-home" class="page-view active-view">
            <div class="min-h-screen flex flex-col justify-end px-6 pb-12 pt-32">
                <div class="mb-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                    <div class="text-xl md:text-3xl font-medium leading-tight max-w-xl">
                        Ortopedico chirurgo specializzato nell'arto superiore. Ripristinare il movimento, con rigore e precisione estrema.
                    </div>
                    <div class="justify-self-end">
                        <img src="https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&q=80&w=800" alt="Dott. Novi" class="w-[300px] h-[400px] object-cover img-brutalist">
                    </div>
                </div>
                
                <h1 class="text-huge observer-trigger mt-20">
                    <span class="reveal-mask"><span class="reveal-inner">Chirurgia</span></span><br>
                    <span class="reveal-mask"><span class="reveal-inner text-huge-serif italic text-medical-accent">Avanzata</span></span><br>
                    <span class="reveal-mask"><span class="reveal-inner">Della Spalla.</span></span>
                </h1>
            </div>
        </section>

        <!-- ================= CHI SONO ================= -->
        <section id="view-chi-sono" class="page-view min-h-screen pt-32 px-6 pb-20">
            <h1 class="text-huge-serif italic observer-trigger mb-24">Chi Sono.</h1>
            <div class="grid grid-cols-1 md:grid-cols-12 gap-12 text-2xl md:text-4xl font-medium leading-tight max-w-7xl">
                <div class="md:col-span-8 observer-trigger">
                    Esperienza in traumatologia complessa e microchirurgia (Harborview, USA). Attualmente chirurgo ortopedico in Toscana, focalizzato su spalla, gomito e mano. La mia filosofia unisce il massimo rigore scientifico all'accuratezza tecnica in sala operatoria.
                </div>
            </div>
        </section>

        <!-- ================= PATOLOGIE (INDEX) ================= -->
        <section id="view-patologie" class="page-view min-h-screen pt-32 px-6 pb-20">
            <div class="flex justify-between items-end mb-12 aww-border-b pb-8">
                <h1 class="text-huge observer-trigger">Patologie</h1>
                <p class="text-xl max-w-xs font-semibold uppercase">Aree di intervento chirurgico e conservativo.</p>
            </div>
            
            <div class="flex flex-col text-4xl md:text-7xl font-bold uppercase tracking-tighter">
                <a href="#patologie-spalla" class="nav-target list-row aww-border-b py-8 relative flex items-center justify-between group" data-target="patologie-spalla">
                    <span>Spalla</span>
                    <span class="text-lg font-serif italic font-normal opacity-0 group-hover:opacity-100 transition-opacity">Esplora</span>
                    <img src="https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&q=80&w=600" class="list-row-img hidden md:block">
                </a>
                <a href="#patologie-gomito" class="nav-target list-row aww-border-b py-8 relative flex items-center justify-between group" data-target="patologie-gomito">
                    <span>Gomito</span>
                    <span class="text-lg font-serif italic font-normal opacity-0 group-hover:opacity-100 transition-opacity">Esplora</span>
                </a>
                <a href="#patologie-mano" class="nav-target list-row aww-border-b py-8 relative flex items-center justify-between group" data-target="patologie-mano">
                    <span>Mano e Polso</span>
                    <span class="text-lg font-serif italic font-normal opacity-0 group-hover:opacity-100 transition-opacity">Esplora</span>
                </a>
                <a href="#patologie-traumatologia-sportiva" class="nav-target list-row aww-border-b py-8 relative flex items-center justify-between group" data-target="patologie-traumatologia-sportiva">
                    <span>Traumatologia Sportiva</span>
                    <span class="text-lg font-serif italic font-normal opacity-0 group-hover:opacity-100 transition-opacity">Esplora</span>
                </a>
                <a href="#patologie-artroscopia" class="nav-target list-row aww-border-b py-8 relative flex items-center justify-between group" data-target="patologie-artroscopia">
                    <span>Chirurgia Artroscopica</span>
                    <span class="text-lg font-serif italic font-normal opacity-0 group-hover:opacity-100 transition-opacity">Esplora</span>
                </a>
                <a href="#patologie-ecografia-muscoloscheletrica" class="nav-target list-row aww-border-b py-8 relative flex items-center justify-between group" data-target="patologie-ecografia-muscoloscheletrica">
                    <span>Ecografia M.S.</span>
                    <span class="text-lg font-serif italic font-normal opacity-0 group-hover:opacity-100 transition-opacity">Esplora</span>
                </a>
            </div>
        </section>

        <!-- (Singole Patologie Placeholder) -->
        <section id="view-patologie-spalla" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#patologie" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="patologie">← Indietro</a>
            <h1 class="text-huge-serif italic observer-trigger mt-12">Spalla.</h1>
            <p class="text-3xl max-w-4xl mt-12 font-medium">Trattamento della patologia degenerativa e traumatica della spalla: lesioni della cuffia dei rotatori, instabilità, artrosi e necessità di impianto protesico.</p>
        </section>
        <section id="view-patologie-gomito" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#patologie" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="patologie">← Indietro</a>
            <h1 class="text-huge-serif italic observer-trigger mt-12">Gomito.</h1>
        </section>
        <section id="view-patologie-mano" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#patologie" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="patologie">← Indietro</a>
            <h1 class="text-huge-serif italic observer-trigger mt-12">Mano e Polso.</h1>
        </section>
        <section id="view-patologie-traumatologia-sportiva" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#patologie" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="patologie">← Indietro</a>
            <h1 class="text-huge-serif italic observer-trigger mt-12">Sportiva.</h1>
        </section>
        <section id="view-patologie-artroscopia" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#patologie" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="patologie">← Indietro</a>
            <h1 class="text-huge-serif italic observer-trigger mt-12">Artroscopia.</h1>
        </section>
        <section id="view-patologie-ecografia-muscoloscheletrica" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#patologie" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="patologie">← Indietro</a>
            <h1 class="text-huge-serif italic observer-trigger mt-12">Ecografia.</h1>
        </section>

        <!-- ================= SEDI (INDEX) ================= -->
        <section id="view-sedi" class="page-view min-h-screen pt-32 px-6 pb-20">
            <h1 class="text-huge observer-trigger aww-border-b pb-8 mb-12">Sedi</h1>
            
            <div class="grid md:grid-cols-2 gap-x-12 gap-y-16">
                <!-- Sede 1 -->
                <div class="group cursor-pointer">
                    <a href="#sedi-fucecchio" class="nav-target" data-target="sedi-fucecchio">
                        <div class="overflow-hidden mb-6">
                            <img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&q=80&w=800" class="w-full h-[400px] object-cover img-brutalist scale-100 group-hover:scale-105 transition-transform duration-700">
                        </div>
                        <h3 class="text-3xl font-bold uppercase tracking-tight mb-2">Studi Medici San Pietro</h3>
                        <p class="text-xl font-serif italic text-medical-muted">Fucecchio (FI)</p>
                    </a>
                </div>
                <!-- Sede 2 -->
                <div class="group cursor-pointer">
                    <a href="#sedi-cesat" class="nav-target" data-target="sedi-cesat">
                        <div class="overflow-hidden mb-6">
                            <img src="https://images.unsplash.com/photo-1538108149393-fbbd81895907?auto=format&fit=crop&q=80&w=800" class="w-full h-[400px] object-cover img-brutalist scale-100 group-hover:scale-105 transition-transform duration-700">
                        </div>
                        <h3 class="text-3xl font-bold uppercase tracking-tight mb-2">CESAT Ospedale San Pietro Igneo</h3>
                        <p class="text-xl font-serif italic text-medical-muted">Fucecchio (FI) - Ricoveri e Chirurgia</p>
                    </a>
                </div>
            </div>
        </section>
        
        <!-- Singole Sedi Placeholder -->
        <section id="view-sedi-fucecchio" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#sedi" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="sedi">← Tutte le sedi</a>
            <h1 class="text-huge observer-trigger mt-12">San Pietro</h1>
        </section>
        <section id="view-sedi-cesat" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#sedi" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="sedi">← Tutte le sedi</a>
            <h1 class="text-huge observer-trigger mt-12">CESAT</h1>
        </section>

        <!-- ================= ARTICOLI ================= -->
        <section id="view-articoli" class="page-view min-h-screen pt-32 px-6 pb-20">
            <h1 class="text-huge observer-trigger aww-border-b pb-8 mb-12">Articoli.</h1>
            <a href="#articoli-remplissage" class="nav-target block py-12 aww-border-b group" data-target="articoli-remplissage">
                <div class="flex justify-between items-center">
                    <h2 class="text-4xl md:text-6xl font-medium tracking-tight group-hover:text-medical-accent transition-colors">Il dubbio nel remplissage</h2>
                    <span class="text-sm uppercase font-bold px-4 py-2 border border-medical-text rounded-full">Spalla</span>
                </div>
            </a>
        </section>
        
        <section id="view-articoli-remplissage" class="page-view min-h-screen pt-32 px-6 pb-20">
            <a href="#articoli" class="nav-target uppercase font-semibold text-sm hover:opacity-50" data-target="articoli">← Articoli</a>
            <h1 class="text-huge-serif italic observer-trigger mt-12">Il dubbio nel remplissage.</h1>
        </section>

        <!-- ================= CONTATTI ================= -->
        <section id="view-contatti" class="page-view min-h-screen pt-32 px-6 pb-20 flex flex-col justify-center">
            <div class="text-center">
                <h1 class="text-huge observer-trigger mb-12">Contatti</h1>
                <p class="text-2xl font-serif mb-12">Per prenotare una visita o richiedere informazioni.</p>
                <a href="tel:+393484331733" class="btn-awwwards px-12 py-6 text-2xl font-bold uppercase tracking-widest">Chiama il 348 4331733</a>
            </div>
        </section>

    </main>

    <!-- Script per Animazioni (Scroll Observer) e SPA Router -->
    <script>
        // Router SPA Minimale
        document.querySelectorAll('.nav-target').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('data-target');
                document.querySelectorAll('.page-view').forEach(view => {
                    view.classList.remove('active-view');
                });
                const targetView = document.getElementById('view-' + targetId);
                if(targetView) {
                    targetView.classList.add('active-view');
                    window.scrollTo({top: 0, behavior: 'instant'});
                    setTimeout(initObserver, 100);
                }
            });
        });

        // Intersection Observer per animazioni Awwwards
        let observer;
        function initObserver() {
            if(observer) observer.disconnect();
            const elements = document.querySelectorAll('.active-view .observer-trigger');
            observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                    }
                });
            }, { threshold: 0.1 });
            elements.forEach(el => observer.observe(el));
        }
        document.addEventListener('DOMContentLoaded', initObserver);
    </script>
</body>
</html>
"""

with open("/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/handoff_sito.html", "w", encoding="utf-8") as f:
    f.write(html_content)
