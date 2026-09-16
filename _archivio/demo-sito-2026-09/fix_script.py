import os

out_dir = "/Volumes/Programs/Temporary files/Progetti cursor/Michele_Novi_Website/Proposte HTML"

with open("generate_full_spa.py", "r", encoding="utf-8") as f:
    content = f.read()

content = "out_dir = '" + out_dir + "'\n" + content

with open("generate_full_spa.py", "w", encoding="utf-8") as f:
    f.write(content)
