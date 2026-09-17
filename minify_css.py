import re
import os

with open("style.css", "r") as f:
    css = f.read()

# Remove comments
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
# Remove extra whitespace
css = re.sub(r'\s+', ' ', css)
# Remove space around delimiters
css = re.sub(r'\s*([\{\}:;,])\s*', r'\1', css)

with open("style.min.css", "w") as f:
    f.write(css)
print("Minified style.css to style.min.css")
