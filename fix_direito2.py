with open("direito-bancario-sao-carlos/index.html", "r") as f:
    content = f.read()

target = """                    <li>Documentos relacionados à busca e apreensão;</li>
                    <li>Comprovantes de descontos realizados no benefício e documentos pessoais (quando necessários para a análise).</li>
                </ul>"""

new_target = """                    <li>Documentos relacionados à busca e apreensão;</li>
                    <li>Relatórios do Registrato do Banco Central (Contas e Relacionamentos, Empréstimos e Financiamentos e Chaves Pix), <a href="../blog/conta-aberta-com-documento-falso/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">úteis para localizar relações bancárias que você não reconhece</a>;</li>
                    <li>Comprovantes de descontos realizados no benefício e documentos pessoais (quando necessários para a análise).</li>
                </ul>"""

content = content.replace(target, new_target)

with open("direito-bancario-sao-carlos/index.html", "w") as f:
    f.write(content)
