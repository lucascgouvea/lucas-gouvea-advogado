with open("direito-bancario-sao-carlos/index.html", "r") as f:
    content = f.read()

target = """                <!-- Busca e Apreensão -->
                <div class="service-card-page" data-aos="fade-up" data-aos-delay="150">
                    <h3>Busca e Apreensão</h3>
                    <ul>
                        <li>Análise da situação e orientação jurídica</li>
                        <li>Defesa em ações de busca e apreensão</li>
                        <li>Avaliação das alternativas jurídicas cabíveis</li>
                        <li>Análise de contratos de financiamento relacionados ao veículo</li>
                    </ul>
                </div>"""

new_target = """                <!-- Busca e Apreensão -->
                <div class="service-card-page" data-aos="fade-up" data-aos-delay="150">
                    <h3>Busca e Apreensão</h3>
                    <ul>
                        <li>Análise da situação e orientação jurídica</li>
                        <li>Defesa em ações de busca e apreensão</li>
                        <li>Avaliação das alternativas jurídicas cabíveis</li>
                        <li>Análise de contratos de financiamento relacionados ao veículo</li>
                    </ul>
                    <p style="margin-top: 15px; font-size: 0.95rem;"><a href="../blog/busca-e-apreensao-veiculo/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Saiba o que fazer ao ser citado</a> e o que pode ser <a href="../blog/revisional-financiamento-veiculo/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">discutido na análise contratual</a>.</p>
                </div>"""

content = content.replace(target, new_target)

with open("direito-bancario-sao-carlos/index.html", "w") as f:
    f.write(content)
