with open("blog/conta-aberta-com-documento-falso/index.html", "r") as f:
    content = f.read()

cta1 = """</ol>

<div class="article-cta" style="background-color: var(--bg-light); padding: 30px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 30px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h3 style="margin-top: 0; font-size: 1.5rem; border-bottom: none; padding-bottom: 0;">Muitas etapas para resolver sozinho?</h3>
    <p style="margin-bottom: 20px;">Se você já descobriu a fraude e precisa de apoio para mapear os danos, exigir os documentos e proteger seu nome de restrições indevidas, nós podemos ajudar.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20li%20o%20artigo%20sobre%20conta%20aberta%20com%20documento%20falso%20e%20gostaria%20de%20uma%20an%C3%A1lise%20do%20meu%20caso." target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Falar com advogado agora
    </a>
</div>

<h2>O dossiê de abertura: o que pedir antes de encerrar a conta</h2>"""

cta2 = """<p>O que sobra é a demonstração da regularidade do procedimento de abertura, e esse ônus é da instituição, não de quem teve o nome usado.</p>

<div class="article-cta" style="background-color: var(--bg-light); padding: 30px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 40px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h3 style="margin-top: 0; font-size: 1.5rem; border-bottom: none; padding-bottom: 0;">O banco se isentou de responsabilidade?</h3>
    <p style="margin-bottom: 20px;">As instituições financeiras respondem objetivamente pela falha na segurança (Súmula 479/STJ). Nossa equipe analisa os protocolos da abertura da conta para responsabilizar o banco pelos danos gerados.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20li%20o%20artigo%20sobre%20conta%20aberta%20com%20documento%20falso%20e%20gostaria%20de%20uma%20an%C3%A1lise%20do%20meu%20caso." target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Exigir reparação
    </a>
</div>

<h2>E quando você pagou para uma conta aberta com documentos falsos?</h2>"""

content = content.replace("</ol>\n\n<h2>O dossiê de abertura: o que pedir antes de encerrar a conta</h2>", cta1)
content = content.replace("<p>O que sobra é a demonstração da regularidade do procedimento de abertura, e esse ônus é da instituição, não de quem teve o nome usado.</p>\n\n<h2>E quando você pagou para uma conta aberta com documentos falsos?</h2>", cta2)

with open("blog/conta-aberta-com-documento-falso/index.html", "w") as f:
    f.write(content)
