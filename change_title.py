with open("blog/revisional-financiamento-veiculo/index.html", "r") as f:
    content = f.read()

# Replace <title>
content = content.replace(
    "<title>Revisional de financiamento de veículo: o que dá para rever | Lucas Gouvea</title>",
    "<title>Juros De Financiamento De Veículo: O Que Pode Ser Revisto? | Lucas Gouvea</title>"
)

# Replace og:title
content = content.replace(
    '<meta property="og:title" content="Revisional de financiamento de veículo: o que dá para rever">',
    '<meta property="og:title" content="Juros De Financiamento De Veículo: O Que Pode Ser Revisto?">'
)

# Replace h1
content = content.replace(
    '<h1 class="article-title" data-aos="fade-up">Revisional de financiamento de veículo: o que pode ser revisto no contrato</h1>',
    '<h1 class="article-title" data-aos="fade-up">Juros De Financiamento De Veículo: O Que Pode Ser Revisto?</h1>'
)

# Replace JSON-LD headline
content = content.replace(
    '"headline": "Revisional de financiamento de veículo: o que pode ser revisto no contrato",',
    '"headline": "Juros De Financiamento De Veículo: O Que Pode Ser Revisto?",'
)

with open("blog/revisional-financiamento-veiculo/index.html", "w") as f:
    f.write(content)
