with open("direito-bancario-sao-carlos/index.html", "r") as f:
    content = f.read()

target = """                    <div class="faq-question-page">Posso revisar um contrato de financiamento?</div>
                    <div class="faq-answer-page">Sim, caso seja identificada alguma abusividade ou ilegalidade no contrato, é possível buscar a revisão pela via administrativa ou judicial, sempre baseada em análise documental prévia.</div>"""

new_target = """                    <div class="faq-question-page">Posso revisar um contrato de financiamento?</div>
                    <div class="faq-answer-page">Sim, caso seja identificada alguma abusividade ou ilegalidade no contrato, é possível buscar a revisão pela via administrativa ou judicial, sempre baseada em análise documental prévia. <a href="../blog/revisional-financiamento-veiculo/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Entenda o que dá para rever no caso de financiamento de veículo</a>.</div>"""

content = content.replace(target, new_target)

with open("direito-bancario-sao-carlos/index.html", "w") as f:
    f.write(content)
