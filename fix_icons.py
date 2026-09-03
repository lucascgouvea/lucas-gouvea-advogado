import os

blog_dir = 'blog'

old_block = """                <div class="footer-social-links">
                    <a href="https://instagram.com/lucasgouvea.adv" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
                        <i data-lucide="instagram"></i>
                    </a>
                    <a href="https://www.linkedin.com/in/lucas-gouvea-7511311b3/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
                        <i data-lucide="linkedin"></i>
                    </a>
                </div>"""

new_block = """                <div class="footer-social-links">
                    <a href="https://www.instagram.com/lucasgouvea.adv" aria-label="Instagram" title="Siga no Instagram" target="_blank" rel="noopener noreferrer">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>
                    </a>
                    <a href="https://www.linkedin.com/in/lucas-gouvea-7511311b3/" aria-label="LinkedIn" title="Conecte no LinkedIn" target="_blank" rel="noopener noreferrer">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>
                    </a>
                </div>"""

for root, _, files in os.walk(blog_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r") as f:
                content = f.read()
            if old_block in content:
                content = content.replace(old_block, new_block)
                with open(path, "w") as f:
                    f.write(content)
                print(f"Fixed {path}")
