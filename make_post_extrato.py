import re

with open("blog/churning-consignado-inss/index.html", "r") as f:
    template = f.read()

# Replace metadata
template = template.replace(
    "<title>Empréstimo Consignado Que Nunca Termina: Entenda o Churning | Lucas Gouvea</title>",
    "<title>Extrato de empréstimo consignado do INSS: como ler | Lucas Gouvea</title>"
)
template = template.replace(
    '<meta name="description" content="Refinanciamento sucessivo pode transformar um consignado em dívida sem fim. Entenda como identificar churning no extrato do INSS e o que a lei e o STJ dizem.">',
    '<meta name="description" content="Como emitir o extrato de empréstimo consignado do INSS (HISCON) e o que cada campo significa: contratos, margem, refinanciamentos e descontos.">'
)
template = template.replace(
    '<meta name="last-verified" content="2026-09-03">',
    '<meta name="last-verified" content="2026-09-12">'
)
template = template.replace(
    'href="https://lgouvea.com/blog/churning-consignado-inss/"',
    'href="https://lgouvea.com/blog/extrato-emprestimo-consignado-inss/"'
)
template = template.replace(
    'content="https://lgouvea.com/blog/churning-consignado-inss/"',
    'content="https://lgouvea.com/blog/extrato-emprestimo-consignado-inss/"'
)
template = template.replace(
    '<meta property="og:title" content="Empréstimo Consignado Que Nunca Termina: Entenda o Churning">',
    '<meta property="og:title" content="Extrato de empréstimo consignado do INSS: como ler">'
)
template = template.replace(
    '<meta property="og:description" content="Refinanciamento sucessivo pode transformar um consignado em dívida sem fim. Entenda como identificar churning no extrato do INSS e o que a lei e o STJ dizem.">',
    '<meta property="og:description" content="Como emitir o extrato de empréstimo consignado do INSS (HISCON) e o que cada campo significa: contratos, margem, refinanciamentos e descontos.">'
)

schema_old = """"headline": "Empréstimo Consignado Que Nunca Termina: Entenda o Churning",
      "description": "Refinanciamento sucessivo pode transformar um consignado em dívida sem fim. Entenda como identificar churning no extrato do INSS e o que a lei e o STJ dizem.","""
schema_new = """"headline": "Extrato de empréstimo consignado do INSS: como emitir e como ler cada campo",
      "description": "Como emitir o extrato de empréstimo consignado do INSS (HISCON) e o que cada campo significa: contratos, margem, refinanciamentos e descontos.","""
template = template.replace(schema_old, schema_new)

template = template.replace(
    '"datePublished": "2026-08-31"',
    '"datePublished": "2026-09-12"'
)
template = template.replace(
    '"dateModified": "2026-08-31"',
    '"dateModified": "2026-09-12"'
)

# Header
header_old = """<h1 class="article-title" data-aos="fade-up">Empréstimo Consignado Que Nunca Termina: Entenda o Churning</h1>
                
                <div class="article-meta" data-aos="fade-up" data-aos-delay="100">
                    <div class="article-meta-item">
                        <i data-lucide="user"></i> Dr. Lucas Gouvea
                    </div>
                    <div class="article-meta-item">
                        <i data-lucide="calendar"></i> 3 de Setembro, 2026
                    </div>
                    <div class="article-meta-item">
                        <i data-lucide="clock"></i> 6 min de leitura
                    </div>
                    <div class="article-meta-item" style="margin-left:auto;">
                        <span class="blog-category" style="margin:0;">Direito Bancário</span>
                    </div>
                </div>"""
                
header_new = """<h1 class="article-title" data-aos="fade-up">Extrato de empréstimo consignado do INSS: como emitir e como ler cada campo</h1>
                
                <div class="article-meta" data-aos="fade-up" data-aos-delay="100">
                    <div class="article-meta-item">
                        <i data-lucide="user"></i> Dr. Lucas Gouvea
                    </div>
                    <div class="article-meta-item">
                        <i data-lucide="calendar"></i> 12 de Setembro, 2026
                    </div>
                    <div class="article-meta-item">
                        <i data-lucide="clock"></i> 8 min de leitura
                    </div>
                    <div class="article-meta-item" style="margin-left:auto;">
                        <span class="blog-category" style="margin:0;">Direito Bancário</span>
                    </div>
                </div>"""
template = template.replace(header_old, header_new)

# Body injection
body_start = template.find('<div class="article-body">\n') + len('<div class="article-body">\n')
body_end = template.find('            </div>\n\n            <!-- Botão de Voltar -->')

new_content = """
<p>O <strong>extrato de empréstimo consignado do INSS</strong> reúne, em um único documento, todos os contratos averbados no benefício: empréstimos, cartão de crédito consignado e cartão consignado de benefício. É gratuito, sai em poucos minutos pelo Meu INSS e costuma ser o primeiro papel que se pede quando alguém desconfia de um desconto na aposentadoria.</p>

<p>O problema aparece depois. A pessoa emite o documento, olha para uma tabela com dez colunas e não sabe o que está vendo. Fica sabendo que existem contratos, mas não consegue dizer se aquilo faz sentido.</p>

<p>Este texto resolve as duas metades do problema. Primeiro, como emitir. Depois, e principalmente, o que cada campo significa, o que ele sugere e o que ele definitivamente não prova.</p>

<h2>O que é o extrato e por que também o chamam de HISCON</h2>

<p>O nome do serviço no Meu INSS é Extrato de Empréstimo Consignado. O apelido HISCON vem de histórico de consignações, que é como o sistema do INSS registra os descontos autorizados sobre o benefício.</p>

<p>O documento registra o que foi <strong>averbado</strong>, ou seja, o que o INSS aceitou registrar como desconto autorizado na folha do benefício. Constam operações em andamento, suspensas e já encerradas, com o banco responsável, as datas e os valores de cada uma.</p>

<p>Duas confusões comuns valem ser desfeitas logo:</p>

<ul>
    <li><strong>Extrato do consignado não é extrato bancário.</strong> Ele mostra o que é descontado do benefício, não o que entrou ou saiu da conta.</li>
    <li><strong>HISCON não é HISCRE.</strong> O HISCRE é o histórico de pagamentos do benefício, ou seja, quanto o INSS pagou mês a mês. Quando a discussão envolve valores efetivamente descontados ao longo do tempo, os dois documentos se completam.</li>
</ul>

<h2>Como emitir o extrato no Meu INSS</h2>

<p>O pedido é online, gratuito e o documento é gerado na hora:</p>

<ol>
    <li>Acesse o Meu INSS pelo site ou pelo aplicativo e entre com a sua conta gov.br.</li>
    <li>No campo "Do que você precisa?", digite <em>extrato de empréstimo</em>.</li>
    <li>Escolha o serviço Extrato de Empréstimo Consignado.</li>
    <li>Baixe o PDF e guarde o arquivo com a data no nome.</li>
</ol>

<p>Se o sistema estiver indisponível, o pedido pode ser feito pela Central 135, que atende de segunda a sábado, das 7h às 22h no horário de Brasília. O atendimento presencial existe, por agendamento, mas a espera é bem maior do que a emissão digital.</p>

<p>Quando quem pede não é o titular, a documentação muda: além dos documentos do beneficiário, é preciso apresentar identificação de quem representa e procuração pública ou no modelo do INSS, ou o termo de tutela, curatela ou guarda.</p>

<p>Uma recomendação prática: <strong>o extrato é uma fotografia do dia em que foi emitido</strong>. Se a sua dúvida envolve algo que mudou ao longo do tempo, emita o documento agora, guarde, e emita de novo quando houver qualquer alteração nos descontos.</p>

<h2>Como o documento é organizado</h2>

<p>O extrato tem três blocos, e cada um responde a uma pergunta diferente. Ler na ordem evita conclusão apressada.</p>

<h3>Bloco 1: os dados do benefício</h3>

<p>A primeira parte identifica o benefício: espécie, número, situação (ativo, suspenso ou cessado) e forma de pagamento, com o banco e a conta em que o benefício é depositado. Também informa se existe representante legal e se o benefício está <strong>liberado ou bloqueado para novas contratações</strong>.</p>

<p>Dois pontos costumam passar batido aqui.</p>

<p>O banco que paga o benefício não é, necessariamente, o banco do empréstimo. São coisas separadas, e muita gente atribui ao banco pagador um contrato feito com outra instituição.</p>

<p>E a informação sobre bloqueio importa mais do que parece. O beneficiário pode bloquear o próprio benefício para novas contratações de consignado, gratuitamente, pelo Meu INSS, e desbloquear depois se quiser contratar. Para quem já sofreu com oferta insistente por telefone, essa é a medida preventiva mais simples que existe.</p>

<h3>Bloco 2: margem consignável e base de cálculo</h3>

<p>A margem consignável é o <strong>percentual máximo do benefício que pode ser comprometido com descontos de operações consignadas</strong>. O extrato mostra a base de cálculo utilizada, quanto está comprometido e quanto ainda está disponível, por modalidade.</p>

<p>O percentual não é estável, e 2026 deixou isso evidente. A Lei 10.820/2003 fixa, para aposentadoria e pensão do Regime Geral, o limite de 45% do benefício, sendo 35% para empréstimos e financiamentos, 5% para o cartão de crédito consignado e 5% para o cartão consignado de benefício. Em 4 de maio de 2026, a Medida Provisória 1.355 reduziu esse total para 40% e eliminou a divisão obrigatória entre as modalidades. A MP não foi convertida em lei dentro do prazo de deliberação, encerrado em 31 de agosto de 2026, e perdeu a eficácia, o que fez a regra anterior voltar a valer.</p>

<p>Para quem recebe BPC/LOAS, a lei prevê limite próprio, de 35%, sendo 30% para empréstimos e 5% para cartão.</p>

<p><em>*Situação verificada em 12 de setembro de 2026. O tema segue em movimento no Congresso, então confira a regra vigente antes de concluir qualquer coisa.</em></p>

<p>Daí sai a regra de leitura mais importante deste bloco: <strong>o percentual relevante é o que estava em vigor na data de cada contratação, e não o de hoje</strong>. Comparar um contrato de 2019 com o limite atual leva a conclusão errada nas duas direções. Por isso, confira sempre a data de emissão do extrato antes de interpretar a tabela de margens.</p>

<h3>Bloco 3: a relação de contratos averbados</h3>

<p>É a parte mais longa e a que realmente responde à pergunta que levou você até o documento. Cada linha corresponde a uma operação averbada no benefício.</p>

<p>Aqui mora uma armadilha frequente: na mesma lista convivem produtos diferentes. Empréstimo consignado tem parcela fixa e prazo definido. Já o <a href="../../blog/rmc-rcc-inss/" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">cartão de crédito consignado (RMC) e o cartão consignado de benefício (RCC)</a> descontam um valor mínimo por mês, com saldo que gira, e por isso parecem não acabar nunca. Quem contratou achando que era empréstimo costuma descobrir a diferença anos depois, olhando este bloco.</p>

<h2>Como ler a linha de um contrato, campo a campo</h2>

<div class="table-responsive">
    <table class="article-table">
        <thead>
            <tr>
                <th>Campo</th>
                <th>O que é</th>
                <th>O que observar</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Banco / consignatária</strong></td>
                <td>A instituição que concedeu o crédito</td>
                <td>Confira se você reconhece a instituição e se ela é diferente do banco onde o benefício é pago</td>
            </tr>
            <tr>
                <td><strong>Número do contrato</strong></td>
                <td>A identificação da operação</td>
                <td>É por esse número que se pede o contrato ao banco e se identifica a operação em qualquer discussão</td>
            </tr>
            <tr>
                <td><strong>Situação</strong></td>
                <td>Ativo, suspenso, encerrado ou excluído</td>
                <td>Suspenso não é encerrado, e encerrado não significa necessariamente pago</td>
            </tr>
            <tr>
                <td><strong>Origem da averbação</strong></td>
                <td>Se a operação entrou como nova, refinanciamento ou portabilidade</td>
                <td>Indica se aquele contrato nasceu sozinho ou veio de outro anterior</td>
            </tr>
            <tr>
                <td><strong>Data da inclusão</strong></td>
                <td>Quando a operação foi registrada no INSS</td>
                <td>Serve como referência de data do contrato quando não se tem o contrato em mãos</td>
            </tr>
            <tr>
                <td><strong>Início e fim do desconto</strong></td>
                <td>Quando as parcelas começaram e terminaram</td>
                <td>A data do último desconto costuma ser mais relevante do que a data de exclusão</td>
            </tr>
        </tbody>
    </table>
</div>

<p>Depois dos campos de identificação vêm os valores: quantidade de parcelas, valor da parcela, IOF, valor emprestado e valor liberado. É neste ponto que a leitura fica interessante.</p>

<h3>Valor emprestado e valor liberado não são a mesma coisa</h3>

<p><strong>Valor liberado é o dinheiro que efetivamente ficou à disposição da pessoa.</strong> <strong>Valor emprestado é o capital total financiado</strong>, sobre o qual os juros da operação incidem. Quando os dois números são diferentes, a diferença é composta por valores que foram financiados junto com o crédito, como IOF, tarifas ou seguro.</p>

<p>Existe uma conferência simples que qualquer pessoa consegue fazer, e ela costuma ser o primeiro sinal concreto de que vale investigar o contrato:</p>

<ul>
    <li>some o valor liberado com o IOF que aparece na própria linha;</li>
    <li>compare o resultado com o valor emprestado;</li>
    <li>se sobrar diferença, há algo financiado que o extrato não discrimina.</li>
</ul>

<p>Um exemplo numérico ajuda. Se o valor liberado foi R$ 5.000,00, o IOF informado foi R$ 150,00 e o valor emprestado aparece como R$ 5.400,00, há R$ 250,00 dentro do financiamento que o documento não identifica. Esse valor pode corresponder a um seguro embutido ou a alguma tarifa.</p>

<p>Duas ressalvas honestas, porque as duas direções do erro são reais. A diferença, sozinha, <strong>não prova cobrança indevida</strong>: pode haver encargo regularmente contratado. E, no sentido contrário, usar o valor liberado como se fosse o capital financiado distorce qualquer cálculo de taxa de juros, produzindo um número artificialmente alto. Descobrir o que compõe essa diferença depende do contrato.</p>

<h3>Origem da averbação: nova, refinanciamento ou portabilidade</h3>

<p>Esse campo conta a história da operação.</p>

<p><strong>Averbação nova</strong> é uma operação que nasceu ali. <strong>Refinanciamento</strong> significa que uma dívida anterior foi liquidada com a contratação de outra, normalmente com prazo alongado e, às vezes, com algum troco liberado. <strong>Portabilidade</strong> é a transferência do contrato para outra instituição.</p>

<p>A leitura que importa é a sequência. Quando várias linhas aparecem como refinanciamento, em intervalos curtos, com valores liberados pequenos e saldo que não diminui, existe um padrão que merece análise individualizada. É exatamente esse encadeamento que se discute sob o nome de churning. Veja <a href="../../blog/churning-consignado-inss/" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">como identificar uma sequência de refinanciamentos sucessivos</a>.</p>

<h3>Encerrado não quer dizer quitado</h3>

<p>Um contrato encerrado ou excluído pode ter terminado por quitação, mas também por refinanciamento ou portabilidade. As colunas de exclusão trazem a data, a origem e o motivo, e são elas que diferenciam os três cenários.</p>

<p>Um indício útil: quando a data de exclusão de uma linha é praticamente a mesma da data de inclusão de outra, com frequência não houve dívida paga, e sim a mesma dívida continuando com número novo.</p>

<h2>O que costuma merecer uma segunda olhada</h2>

<p>Não existe lista de sinais que dispense análise do caso concreto. Ainda assim, estes são os pontos que, na prática, justificam abrir o contrato:</p>

<ul>
    <li><strong>Contrato que você não reconhece.</strong> Vale conferir se não é um refinanciamento de algo que você contratou ou um <a href="../../blog/golpe-do-pix-o-que-fazer/" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">empréstimo contratado durante um golpe</a>, antes de concluir que é fraude.</li>
    <li><strong>Descontos de cartão que a pessoa achava que eram empréstimo.</strong> Parcela pequena, sem data para acabar, geralmente identificada como RMC ou RCC.</li>
    <li><strong>Cadeia de refinanciamentos com troco baixo.</strong> Vários contratos sucessivos, pouco dinheiro liberado em cada um, prazo sempre esticando.</li>
    <li><strong>Soma dos descontos no limite ou acima dele.</strong> Lembrando que o limite a considerar é o da data de cada contratação.</li>
    <li><strong>Operação averbada em período em que já havia representante legal</strong> ou em que o benefício constava bloqueado para novas contratações.</li>
</ul>

<p>Nenhum desses pontos, isoladamente, é conclusão. Todos são motivo para buscar o documento seguinte.</p>

<h2>O que o extrato não mostra</h2>

<p>Esta é a parte que quase nenhum conteúdo sobre o assunto explica, e é a que evita frustração:</p>

<ul>
    <li><strong>não traz o contrato nem as cláusulas</strong> que foram assinadas;</li>
    <li><strong>não traz o Custo Efetivo Total</strong> da operação;</li>
    <li><strong>não mostra o que caiu na conta</strong>, apenas o que foi registrado como liberado;</li>
    <li><strong>não discrimina todos os encargos financiados</strong>, como já visto;</li>
    <li><strong>não registra o que está fora do benefício</strong>, como crédito pessoal comum ou cartão convencional.</li>
</ul>

<p>Onde buscar o que falta:</p>

<ul>
    <li><strong>o contrato</strong>, pelo próprio Meu INSS, para operações feitas em bancos parceiros a partir de outubro de 2021, ou diretamente com o banco, por canal que gere protocolo;</li>
    <li><strong>o extrato da conta</strong> em que o benefício é pago, no mês em que o dinheiro teria sido liberado;</li>
    <li><strong>o Registrato, do Banco Central</strong>, que reúne as operações de crédito registradas no CPF, inclusive as que não passam pelo benefício.</li>
</ul>

<h2>Encontrou algo que não reconhece: por onde começar</h2>

<p>A ordem abaixo existe por um motivo: cada passo produz um documento que o passo seguinte vai exigir.</p>

<ol>
    <li>Emita o extrato de empréstimo consignado e guarde o PDF com a data.</li>
    <li>Peça o contrato daquela operação, pelo Meu INSS ou ao banco, e guarde todos os protocolos, inclusive os pedidos que não forem respondidos.</li>
    <li>Junte o extrato da conta bancária do mês da suposta liberação do dinheiro.</li>
    <li>Registre a contestação no banco por um canal que gere número de protocolo. Se não houver solução, o consumidor.gov.br é o caminho administrativo seguinte.</li>
    <li>Avalie bloquear o benefício para novas contratações enquanto resolve a situação.</li>
    <li>Só então avalie a orientação jurídica em <a href="../../direito-bancario-sao-carlos/?utm_source=blog&utm_medium=artigo&utm_campaign=extrato-emprestimo-consignado-inss" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">análise de contratos de empréstimo consignado</a>, já com os documentos reunidos.</li>
</ol>

<p>Um alerta que vale repetir: <strong>a emissão do extrato e o bloqueio do benefício são gratuitos e feitos pelo próprio titular</strong>. Nenhuma empresa precisa ser contratada para isso, e cobrança para "liberar" ou "desbloquear" benefício é motivo de desconfiança.</p>

<h2>Perguntas que aparecem com frequência</h2>

<h3>O extrato de empréstimo consignado é o mesmo que o HISCON?</h3>
<p>Sim. HISCON é o nome do histórico de consignações dentro dos sistemas do INSS, e Extrato de Empréstimo Consignado é o nome do serviço no Meu INSS. Bancos, advogados e o próprio INSS usam os dois termos para o mesmo documento.</p>

<h3>Quem recebe BPC/LOAS também tem esse extrato?</h3>
<p>Sim, e o documento funciona da mesma forma. O que muda é a regra de margem, que a lei trata separadamente para o BPC, com limite total de 35%, sendo 5% reservados a cartão.</p>

<h3>Dá para conseguir o contrato pelo Meu INSS?</h3>
<p>Para operações realizadas em bancos parceiros a partir de outubro de 2021, sim. Contratos anteriores costumam depender de pedido direto ao banco. Quando o banco não entrega, os pedidos feitos e não atendidos passam a ter valor próprio, porque documentam a recusa.</p>

<h3>O extrato prova que eu contratei o empréstimo?</h3>
<p>O extrato prova que a operação foi averbada no benefício, com aquele banco, naquela data e naqueles valores. Isso não é a mesma coisa que provar que houve contratação válida, feita pelo titular e com informação adequada. São discussões diferentes, e é justamente por isso que o contrato continua sendo pedido.</p>

<h3>Preciso pagar alguém para emitir o extrato?</h3>
<p>Não. O serviço é gratuito no Meu INSS e o documento é gerado automaticamente no momento do pedido.</p>

<author-block></author-block>

<div class="article-cta" style="background-color: var(--bg-light); padding: 40px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 50px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h2 style="margin-top: 0; font-size: 1.8rem; border-bottom: none; padding-bottom: 0;">Ficou com dúvida sobre alguma linha do extrato?</h2>
    <p style="margin-bottom: 20px;">Se você encontrou um contrato que não reconhece, uma sequência de refinanciamentos ou um desconto de cartão que nunca termina, o passo seguinte é analisar a documentação. Veja <a href="../../#como-funciona" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">como funciona a análise documental de contratos bancários</a> ou fale diretamente com o escritório.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20emiti%20meu%20extrato%20do%20INSS%20e%20tenho%20d%C3%BAvidas%20sobre%20os%20contratos." target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Falar com a equipe
    </a>
</div>
"""

new_template = template[:body_start] + new_content + template[body_end:]

import os
os.makedirs("blog/extrato-emprestimo-consignado-inss", exist_ok=True)
with open("blog/extrato-emprestimo-consignado-inss/index.html", "w") as f:
    f.write(new_template)
