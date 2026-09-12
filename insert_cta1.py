with open("blog/extrato-emprestimo-consignado-inss/index.html", "r") as f:
    content = f.read()

target = """<p>Duas ressalvas honestas, porque as duas direções do erro são reais. A diferença, sozinha, <strong>não prova cobrança indevida</strong>: pode haver encargo regularmente contratado. E, no sentido contrário, usar o valor liberado como se fosse o capital financiado distorce qualquer cálculo de taxa de juros, produzindo um número artificialmente alto. Descobrir o que compõe essa diferença depende do contrato.</p>"""

cta_1 = """
<div class="article-cta" style="background-color: var(--bg-light); padding: 40px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 50px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h2 style="margin-top: 0; font-size: 1.8rem; border-bottom: none; padding-bottom: 0;">Encontrou valores embutidos no seu extrato?</h2>
    <p style="margin-bottom: 20px;">Se você fez a conta e notou uma diferença não explicada entre o valor liberado e o valor que está sendo cobrado, pode haver seguros ou tarifas indevidas embutidas. Fale com nossa equipe para analisarmos o seu contrato.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20estou%20lendo%20o%20artigo%20sobre%20o%20extrato%20do%20INSS%20e%20identifiquei%20uma%20diferen%C3%A7a%20nos%20valores%20do%20meu%20empr%C3%A9stimo." target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Solicitar análise contratual
    </a>
</div>
"""

content = content.replace(target, target + "\n" + cta_1)

with open("blog/extrato-emprestimo-consignado-inss/index.html", "w") as f:
    f.write(content)
