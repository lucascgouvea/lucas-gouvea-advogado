with open("direito-bancario-sao-carlos/index.html", "r") as f:
    content = f.read()

target = """                    <div class="faq-question-page">O que fazer se recebi uma ação de busca e apreensão?</div>
                    <div class="faq-answer-page">Aja com urgência. Procure imediatamente um advogado para apresentar defesa nos autos dentro do prazo legal, analisar a regularidade da cobrança e evitar ou reverter a consolidação da propriedade em nome do banco.</div>"""

new_target = """                    <div class="faq-question-page">O que fazer se recebi uma ação de busca e apreensão?</div>
                    <div class="faq-answer-page">Aja com urgência. Procure imediatamente um advogado para apresentar defesa nos autos dentro do prazo legal, analisar a regularidade da cobrança e evitar ou reverter a consolidação da propriedade em nome do banco. <a href="../blog/busca-e-apreensao-veiculo/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Veja o passo a passo completo, incluindo os prazos exatos e a decisão entre purgar a mora e contestar</a>.</div>"""

content = content.replace(target, new_target)

with open("direito-bancario-sao-carlos/index.html", "w") as f:
    f.write(content)
