with open("index.html", "r") as f:
    content = f.read()

medico_start = content.find("<!-- Direito Médico -->")
imobiliario_end = content.find('</a>\n                    </div>', medico_start) + len('</a>\n                    </div>')

# Actually let's just find the entire blocks and replace them with empty strings.

import re

# Find the Direito Médico block
medico_pattern = r'<!-- Direito Médico -->.*?</div>\s*</div>'
# Wait, the closing div might be tricky. Let's just find it precisely using substring replacement.

target_medico = """                    <!-- Direito Médico -->
                    <div class="service-card" data-aos="fade-up" data-aos-delay="300">
                        <div class="service-card-decor"></div>
                        <div class="service-icon-box">
                            <i data-lucide="heart-pulse"></i>
                        </div>
                        <h3 class="service-title">Direito Médico</h3>
                        <p class="service-description">Assessoria jurídica em casos envolvendo erro médico, responsabilidade profissional, judicialização da saúde e defesa dos direitos do paciente.</p>
                        <ul class="service-bullets">
                            <li><i data-lucide="check"></i> Defesa em Erro Médico e Odontológico</li>
                            <li><i data-lucide="check"></i> Negativa de Cobertura de Planos de Saúde</li>
                            <li><i data-lucide="check"></i> Medicamentos e Cirurgias de Alto Custo</li>
                            <li><i data-lucide="check"></i> Defesa Ética de Profissionais da Saúde</li>
                        </ul>
                        <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C+Dr.+Lucas.+Gostaria+de+tirar+uma+d%C3%BAvida+sobre+Direito+M%C3%A9dico." target="_blank" class="service-link" rel="noopener noreferrer">
                            <span>Solicitar Assessoria</span>
                            <i data-lucide="arrow-right"></i>
                        </a>
                    </div>"""

target_imobiliario = """

                    <!-- Direito Imobiliário -->
                    <div class="service-card" data-aos="fade-up" data-aos-delay="400">
                        <div class="service-card-decor"></div>
                        <div class="service-icon-box">
                            <i data-lucide="home"></i>
                        </div>
                        <h3 class="service-title">Direito Imobiliário</h3>
                        <p class="service-description">Assessoria e consultoria jurídica especializada para garantir a segurança jurídica em negócios imobiliários, regularização de imóveis, proteção da posse, contratos e locações.</p>
                        <ul class="service-bullets">
                            <li><i data-lucide="check"></i> Elaboração e Análise de Contratos Imobiliários</li>
                            <li><i data-lucide="check"></i> Regularização de Imóveis e Usucapião</li>
                            <li><i data-lucide="check"></i> Assessoria em Compra, Venda e Locação</li>
                            <li><i data-lucide="check"></i> Ações de Defesa da Posse e Propriedade</li>
                        </ul>
                        <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C+Dr.+Lucas.+Gostaria+de+tirar+uma+d%C3%BAvida+sobre+Direito+Imobili%C3%A1rio." target="_blank" class="service-link" rel="noopener noreferrer">
                            <span>Solicitar Assessoria</span>
                            <i data-lucide="arrow-right"></i>
                        </a>
                    </div>"""

content = content.replace(target_medico, "")
content = content.replace(target_imobiliario, "")

with open("index.html", "w") as f:
    f.write(content)
