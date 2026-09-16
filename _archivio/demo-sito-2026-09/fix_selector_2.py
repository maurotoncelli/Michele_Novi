import re
import os

file_path = "handoff_sito.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific querySelectorAll line
old_selector = "activeView.querySelectorAll('h1, h2, h3, h4, p, .magnetic-module, form, .form-group, ul li, .card-reveal, .bg-caldo-surface');"
new_selector = "activeView.querySelectorAll('h1, h2, h3, h4, p, .magnetic-module, form, .form-group, ul li, .strata-card-soft, .card-soft-gradient');"

content = content.replace(old_selector, new_selector)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

os.system('cp handoff_sito.html "Proposte HTML/index.html"')

