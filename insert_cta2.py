with open("blog/extrato-emprestimo-consignado-inss/index.html", "r") as f:
    content = f.read()

target = """<p>Nenhum desses pontos, isoladamente, é conclusão. Todos são motivo para buscar o documento seguinte.</p>"""

cta_2 = """
<div class="article-cta" style="background-color: var(--bg-light); padding: 40px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 50px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h2 style="margin-top: 0; font-size: 1.8rem; border-bottom: none; padding-bottom: 0;">Notou algum desses sinais no seu extrato?</h2>
    <p style="margin-bottom: 20px;">Cartões infinitos (RMC/RCC), refinanciamentos sucessivos e descontos acima do limite são indícios claros de que seu benefício pode estar sendo prejudicado. Nossa equipe jurídica atua em todo o Brasil resolvendo abusos em empréstimos consignados.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20estou%20lendo%20o%20artigo%20sobre%20o%20extrato%20do%20INSS%20e%20identifiquei%20sinais%20suspeitos%20nos%20meus%20descontos." target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Falar com um advogado
    </a>
</div>
"""

content = content.replace(target, target + "\n" + cta_2)

with open("blog/extrato-emprestimo-consignado-inss/index.html", "w") as f:
    f.write(content)
