import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

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

anchor = "ScrollTrigger.refresh();"
if anchor in content:
    content = content.replace(anchor, gsap_logic + "\n            " + anchor)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected GSAP logic")
    os.system('cp handoff_sito.html "Proposte HTML/index.html"')
