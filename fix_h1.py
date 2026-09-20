with open("blog/conta-aberta-com-documento-falso/index.html", "r") as f:
    content = f.read()

target = '<h1 class="article-title" data-aos="fade-up">Busca e apreensão de veículo: o que fazer ao ser citado</h1>'
new_target = '<h1 class="article-title" data-aos="fade-up">Conta bancária aberta com documento falso: como identificar, o que exigir do banco e quando a instituição responde</h1>'

content = content.replace(target, new_target)

# Also let's fix the date if it says 17 de Setembro
content = content.replace('17 de Setembro, 2026', '20 de Setembro, 2026')

with open("blog/conta-aberta-com-documento-falso/index.html", "w") as f:
    f.write(content)
