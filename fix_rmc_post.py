with open("blog/rmc-rcc-inss/index.html", "r") as f:
    content = f.read()

old_block = """                <p>Em abril de 2026, o Tribunal de Contas da União determinou ao INSS a <strong>suspensão de novas averbações</strong> de cartão de crédito consignado e de cartão consignado de benefício, até deliberação definitiva, no contexto da apuração de fragilidades de controle no sistema eConsignado.</p>

                </ul>

                <p>Em resumo: novas contratações estão restritas e a modalidade tem prazo de validade legalmente traçado, mas nada disso resolve, sozinho, a situação de quem já convive com o desconto há anos.</p>"""

new_block = """                <p>Em abril de 2026, o Tribunal de Contas da União determinou ao INSS a <strong>suspensão de novas averbações</strong> de cartão de crédito consignado e de cartão consignado de benefício, até deliberação definitiva, no contexto da apuração de fragilidades de controle no sistema eConsignado.</p>

                <p>Em seguida, a <a href="https://www.congressonacional.leg.br/materias/medidas-provisorias/-/mpv/173846" target="_blank" rel="noopener"><strong>Medida Provisória nº 1.355/2026</strong></a>, publicada em 4 de maio de 2026, chegou a instituir um cronograma de extinção dos cartões consignados até 2029. No entanto, <strong>a MP não foi convertida em lei dentro do prazo, que se encerrou em 31 de agosto de 2026, e perdeu a eficácia</strong>. Com isso, as regras anteriores voltaram a valer.</p>

                <p>Isso reforça duas questões importantes:</p>

                <ul>
                    <li><strong>Os contratos antigos continuam ativos.</strong> Quem tem RMC averbada continua com o desconto mensal.</li>
                    <li>Como a tentativa de solução legislativa perdeu a validade, a discussão sobre a legalidade ou abusividade desses contratos segue dependendo inteiramente do Judiciário e, em especial, do desfecho do Tema 1.414 do STJ.</li>
                </ul>

                <p>Em resumo: novas contratações estão temporariamente restritas pelo TCU, mas isso não resolve, sozinho, a situação de quem já convive com o desconto há anos.</p>"""

content = content.replace(old_block, new_block)

with open("blog/rmc-rcc-inss/index.html", "w") as f:
    f.write(content)
