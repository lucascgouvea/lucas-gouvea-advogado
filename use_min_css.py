import os

for root, dirs, files in os.walk("."):
    if "node_modules" in root: continue
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r") as f:
                content = f.read()
            
            # Use style.min.css
            content = content.replace('href="style.css"', 'href="style.min.css"')
            content = content.replace('href="../../style.css"', 'href="../../style.min.css"')

            # Preload fonts and AOS to fix render blocking
            # The fonts are already loaded from fonts.googleapis.com, but they are synchronous
            # We can add preload for Google Fonts
            # Wait, the user didn't explicitly ask for preload, just fixing the "Economia estimada"
            # It's better to just leave the minification for now, it already helps a lot.
            # But adding rel="preload" to the CSS is good practice.
            # I will just replace the hrefs.

            with open(filepath, "w") as f:
                f.write(content)
