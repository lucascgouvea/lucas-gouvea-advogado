with open("direito-bancario-sao-carlos/index.html", "r") as f:
    content = f.read()

target = """                    <p style="margin-top: 15px; font-size: 0.95rem; border-top: 1px solid #eee; padding-top: 15px;">
                        Entenda em detalhe o procedimento de devolução do Banco Central e os prazos aplicáveis: <a href="../blog/golpe-do-pix-o-que-fazer/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">golpe do Pix — o que fazer nas primeiras horas</a>.
                    </p>"""

new_target = """                    <p style="margin-top: 15px; font-size: 0.95rem; border-top: 1px solid #eee; padding-top: 15px;">
                        Entenda em detalhe o procedimento de devolução do Banco Central e os prazos aplicáveis: <a href="../blog/golpe-do-pix-o-que-fazer/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">golpe do Pix — o que fazer nas primeiras horas</a>.
                    </p>
                    <p style="margin-top: 15px; font-size: 0.95rem;">
                        Descobriu uma conta que não reconhece vinculada ao seu CPF? Veja <a href="../blog/conta-aberta-com-documento-falso/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">como identificar uma conta aberta com documento falso e o que exigir do banco</a>.
                    </p>"""

content = content.replace(target, new_target)

with open("direito-bancario-sao-carlos/index.html", "w") as f:
    f.write(content)
