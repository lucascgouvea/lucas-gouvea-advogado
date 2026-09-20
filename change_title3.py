with open("blog/conta-aberta-com-documento-falso/index.html", "r") as f:
    content = f.read()

# Replace <title>
content = content.replace(
    "<title>Conta aberta com documento falso no seu nome: o que fazer | Lucas Gouvea</title>",
    "<title>Conta aberta com documento falso: o que exigir do banco | Lucas Gouvea</title>"
)

# Replace og:title
content = content.replace(
    '<meta property="og:title" content="Conta aberta com documento falso no seu nome: o que fazer">',
    '<meta property="og:title" content="Conta aberta com documento falso: o que exigir do banco">'
)

# Replace h1
content = content.replace(
    '<h1 class="article-title" data-aos="fade-up">Conta bancária aberta com documento falso: como identificar, o que exigir do banco e quando a instituição responde</h1>',
    '<h1 class="article-title" data-aos="fade-up">Conta aberta com documento falso: o que exigir do banco</h1>'
)

# Replace JSON-LD headline
content = content.replace(
    '"headline": "Conta aberta com documento falso no seu nome: o que fazer",',
    '"headline": "Conta aberta com documento falso: o que exigir do banco",'
)

with open("blog/conta-aberta-com-documento-falso/index.html", "w") as f:
    f.write(content)
