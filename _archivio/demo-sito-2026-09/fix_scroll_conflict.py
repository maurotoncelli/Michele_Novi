import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix window.scrollTo conflict
if "window.scrollTo({ top: 0, behavior: 'instant' });" in content:
    content = content.replace(
        "window.scrollTo({ top: 0, behavior: 'instant' });",
        "if (typeof lenis !== 'undefined') { lenis.scrollTo(0, {immediate: true}); } else { window.scrollTo({ top: 0, behavior: 'instant' }); }"
    )
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed scroll conflict")

os.system('cp handoff_sito.html "Proposte HTML/index.html"')

