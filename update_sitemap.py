with open("sitemap.xml", "r") as f:
    content = f.read()

new_node = """  <url>
    <loc>https://lgouvea.com/blog/conta-aberta-com-documento-falso/</loc>
    <lastmod>2026-09-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>"""

content = content.replace("</urlset>", new_node)

with open("sitemap.xml", "w") as f:
    f.write(content)
