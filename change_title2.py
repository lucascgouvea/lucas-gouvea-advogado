with open("blog/busca-e-apreensao-veiculo/index.html", "r") as f:
    content = f.read()

# Replace <title>
content = content.replace(
    "<title>Busca e Apreensão de Veículo: o Que Fazer ao Ser Citado | Lucas Gouvea</title>",
    "<title>Busca e apreensão de veículo: o que fazer ao ser citado | Lucas Gouvea</title>"
)

# Replace og:title
content = content.replace(
    '<meta property="og:title" content="Busca e Apreensão de Veículo: o Que Fazer ao Ser Citado">',
    '<meta property="og:title" content="Busca e apreensão de veículo: o que fazer ao ser citado">'
)

# Replace h1
content = content.replace(
    '<h1 class="article-title" data-aos="fade-up">Busca e apreensão de veículo: o que fazer ao ser citado pelo banco</h1>',
    '<h1 class="article-title" data-aos="fade-up">Busca e apreensão de veículo: o que fazer ao ser citado</h1>'
)

# Replace JSON-LD headline
content = content.replace(
    '"headline": "Busca e apreensão de veículo: o que fazer ao ser citado pelo banco",',
    '"headline": "Busca e apreensão de veículo: o que fazer ao ser citado",'
)

with open("blog/busca-e-apreensao-veiculo/index.html", "w") as f:
    f.write(content)
