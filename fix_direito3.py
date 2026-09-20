with open("direito-bancario-sao-carlos/index.html", "r") as f:
    content = f.read()

target = """                <div class="problem-card" data-aos="fade-up" data-aos-delay="550">
                    <p>"Foi contratado um empréstimo em meu nome"</p>
                    <a href="../#contato" class="btn-outline">Analisar caso</a>
                </div>"""

new_target = """                <div class="problem-card" data-aos="fade-up" data-aos-delay="550">
                    <p>"Foi contratado um empréstimo em meu nome"</p>
                    <a href="../#contato" class="btn-outline">Analisar caso</a>
                </div>
                <div class="problem-card" data-aos="fade-up" data-aos-delay="575">
                    <p>"Abriram uma conta bancária no meu nome"</p>
                    <a href="../#contato" class="btn-outline">Analisar caso</a>
                </div>"""

content = content.replace(target, new_target)

with open("direito-bancario-sao-carlos/index.html", "w") as f:
    f.write(content)
