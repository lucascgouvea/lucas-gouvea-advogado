with open("direito-bancario-sao-carlos/index.html", "r") as f:
    content = f.read()

target = """                <div class="service-card-page" data-aos="fade-up" data-aos-delay="100">
                    <h3>Contratos de Financiamento</h3>
                    <ul>
                        <li>Financiamento de veículos</li>
                        <li>Financiamento de imóveis (financiamento imobiliário)</li>
                        <li>Revisão contratual</li>
                        <li>Análise de juros e encargos</li>
                        <li>Parcelas em atraso e inadimplência</li>
                        <li>Questões relacionadas ao contrato de financiamento</li>
                    </ul>"""

new_p = """                    <p style="margin-top: 15px; font-size: 0.95rem;">Veja, em detalhe, <a href="../blog/revisional-financiamento-veiculo/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">o que pode ser discutido em uma revisional de financiamento de veículo</a>.</p>"""

content = content.replace(target, target + "\n" + new_p)

with open("direito-bancario-sao-carlos/index.html", "w") as f:
    f.write(content)
