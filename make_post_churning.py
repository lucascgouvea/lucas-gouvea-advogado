import re

with open("blog/rmc-rcc-inss/index.html", "r") as f:
    template = f.read()

# Replace metadata
template = template.replace(
    "<title>RMC e RCC no INSS: o que são e como identificar o desconto | Lucas Gouvea</title>",
    "<title>Churning no Consignado do INSS: Por Que a Dívida Não Acaba | Lucas Gouvea</title>"
)
template = template.replace(
    '<meta name="description" content="Entenda o que é RMC, como ela difere do RCC, por que o desconto no benefício do INSS não acaba e quais documentos verificar antes de agir. Guia completo.">',
    '<meta name="description" content="Refinanciamento sucessivo pode transformar um consignado em dívida sem fim. Entenda como identificar churning no extrato do INSS e o que a lei e o STJ dizem.">'
)
template = template.replace(
    '<meta name="last-verified" content="2026-08-31">',
    '<meta name="last-verified" content="2026-09-03">'
)
template = template.replace(
    'href="https://lgouvea.com/blog/rmc-rcc-inss/"',
    'href="https://lgouvea.com/blog/churning-consignado-inss/"'
)
template = template.replace(
    'content="https://lgouvea.com/blog/rmc-rcc-inss/"',
    'content="https://lgouvea.com/blog/churning-consignado-inss/"'
)
template = template.replace(
    '<meta property="og:title" content="RMC e RCC no INSS: o que são e como identificar o desconto">',
    '<meta property="og:title" content="Churning no Consignado do INSS: Por Que a Dívida Não Acaba">'
)
template = template.replace(
    '<meta property="og:description" content="Entenda o que é RMC, como ela difere do RCC, por que o desconto no benefício do INSS não acaba e quais documentos verificar antes de agir. Guia completo.">',
    '<meta property="og:description" content="Refinanciamento sucessivo pode transformar um consignado em dívida sem fim. Entenda como identificar churning no extrato do INSS e o que a lei e o STJ dizem.">'
)

schema_old = """"headline": "RMC e RCC no benefício do INSS: o que são, como identificar no extrato e o que fazer",
      "description": "Entenda o que é RMC, como ela difere do RCC, por que o desconto no benefício do INSS não acaba e quais documentos verificar antes de agir. Guia completo.","""
schema_new = """"headline": "Churning no consignado do INSS: como o refinanciamento sucessivo transforma um empréstimo em dívida sem fim",
      "description": "Refinanciamento sucessivo pode transformar um consignado em dívida sem fim. Entenda como identificar churning no extrato do INSS e o que a lei e o STJ dizem.","""
template = template.replace(schema_old, schema_new)

# Header
header_old = """<h1 class="article-title" data-aos="fade-up">RMC e RCC no benefício do INSS: o que são, como identificar no extrato e o que fazer</h1>
                
                <div class="article-meta" data-aos="fade-up" data-aos-delay="100">
                    <div class="article-meta-item">
                        <i data-lucide="user"></i> Dr. Lucas Gouvea
                    </div>
                    <div class="article-meta-item">
                        <i data-lucide="calendar"></i> 31 de Agosto, 2026
                    </div>
                    <div class="article-meta-item">
                        <i data-lucide="clock"></i> 8 min de leitura
                    </div>
                    <div class="article-meta-item" style="margin-left:auto;">
                        <span class="blog-category" style="margin:0;">Direito Bancário</span>
                    </div>
                </div>"""
                
header_new = """<h1 class="article-title" data-aos="fade-up">Churning no consignado do INSS: como o refinanciamento sucessivo transforma um empréstimo em dívida sem fim</h1>
                
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
template = template.replace(header_old, header_new)

# Body injection
body_start = template.find('<div class="article-body">\n') + len('<div class="article-body">\n')
body_end = template.find('            </div>\n\n            <!-- Botão de Voltar -->')

new_content = """
<p>Existe um padrão que aparece com frequência no extrato de consignados de aposentados e pensionistas do INSS: um contrato é aberto, alguns meses depois é liquidado por um "refinanciamento", um novo contrato é aberto com prazo reiniciado, e o ciclo se repete. Anos depois, o desconto mensal continua praticamente do mesmo tamanho, mas o saldo devedor nunca chega perto de zero.</p>

<p>Esse padrão tem nome técnico: <strong>churning</strong>, também chamado de giro de carteira. Ele é diferente do problema tratado no <a href="../../blog/rmc-rcc-inss/">nosso guia sobre RMC e RCC</a> — ali a dívida não termina porque o produto é um cartão de crédito consignado, com fatura mínima que nunca amortiza. Aqui, o produto costuma ser o empréstimo consignado comum, com parcelas fixas e prazo definido. O problema não está na estrutura do produto — está no que acontece com ele ao longo do tempo.</p>

<h2>O que é churning e por que não é a mesma coisa que RMC ou RCC</h2>

<p><strong>Churning é a prática de liquidar repetidamente um contrato de consignado em vigor para abrir um novo, sem que essa sequência gere vantagem real ao beneficiário — mas gerando, a cada operação, uma nova comissão para quem intermediou a contratação.</strong></p>

<p>A diferença para a RMC e o RCC importa porque muda a estratégia de análise:</p>

<ul>
    <li>Na RMC/RCC, a dívida não termina porque o desconto mensal paga apenas o mínimo de uma fatura de cartão, que roda no rotativo. O problema é estrutural ao produto.</li>
    <li>No churning, cada contrato individual até poderia terminar normalmente — o problema é que ele é interrompido antes disso, substituído por outro que reinicia o prazo e, frequentemente, embute o saldo devedor anterior acrescido de novos encargos.</li>
</ul>

<p>As três formas mais comuns pelas quais isso acontece:</p>

<ol>
    <li><strong>Refinanciamento</strong>, em que o saldo devedor do contrato vigente é incorporado a um novo contrato com prazo reiniciado.</li>
    <li><strong>Portabilidade</strong> usada como pretexto — o beneficiário autoriza a transferência do contrato para outro banco, mas a operação é estruturada, na prática, como recontratação com condições piores.</li>
    <li><strong>Migração entre modalidades</strong> — conversão de RCC para RMC ou o inverso, sem vantagem real para o beneficiário, mas gerando nova comissão para o correspondente.</li>
</ol>

<p>Nem toda sequência de refinanciamentos é irregular. Existem situações em que refinanciar reduz genuinamente a taxa de juros ou resolve uma necessidade financeira pontual do beneficiário. O que diferencia o refinanciamento legítimo do churning é a análise concreta dos números — e é para isso que servem os documentos que este artigo explica como reunir.</p>

<h2>Como o ciclo de refinanciamento sucessivo funciona na prática</h2>

<h3>O refinanciamento "oferecido" pelo próprio banco</h3>

<p>A forma mais comum começa com contato ativo da instituição ou de um correspondente, oferecendo "liberar mais dinheiro" ou "reduzir a parcela" a partir do contrato já existente. O beneficiário, muitas vezes sem entender que está liquidando um contrato para abrir outro, aceita.</p>

<p>O que acontece tecnicamente: o saldo devedor do contrato antigo é quitado com o valor do novo contrato, e a diferença — se houver — é depositada como "troco". O prazo é reiniciado do zero. Se isso se repete a cada 12, 18 ou 24 meses, o beneficiário nunca chega ao fim de um contrato — ele está sempre no início de outro.</p>

<h3>A portabilidade usada como pretexto de recontratação</h3>

<p>A portabilidade de consignado é um direito do beneficiário, regulada pelo Banco Central, e existe justamente para permitir a migração para condições melhores sem custo. O problema aparece quando ela é usada como veículo de recontratação: o consumidor autoriza a portabilidade acreditando que vai reduzir a taxa, mas o que ocorre, na prática, é uma nova operação de crédito com características de refinanciamento — reinício de prazo, novo cálculo de encargos, e nem sempre com a taxa que foi anunciada no contato.</p>

<p>A Instrução Normativa PRES/INSS nº 213/2026 trouxe uma mudança relevante para esse ponto específico, tratada na próxima seção.</p>

<h3>A averbação sem qualquer contato com o titular</h3>

<p>Existe uma modalidade mais grave, na qual o consentimento deixa de ser sequer simulado. Correspondentes bancários com acesso a plataformas de averbação processam o refinanciamento sem qualquer contato com o titular do benefício, gerando comissão imediata para quem intermediou a operação. O beneficiário só percebe quando compara os extratos de meses diferentes e nota um novo contrato que não reconhece ter solicitado.</p>

<p>Essa hipótese se sobrepõe, em parte, ao tema de <a href="../../blog/golpe-do-pix-o-que-fazer/">empréstimo não reconhecido tratado no golpe do Pix</a> — a diferença é que, no consignado, o crédito muitas vezes nem chega a ser transferido para uma conta controlada por terceiro: ele é usado para quitar o contrato anterior, e o beneficiário nunca vê o dinheiro em nenhuma etapa.</p>

<h2>Por que o saldo devedor não diminui mesmo depois de anos pagando</h2>

<p>A explicação está na mecânica de cada refinanciamento, não em uma cobrança isolada irregular. Cada novo contrato:</p>

<ul>
    <li>Incorpora o saldo devedor do contrato anterior como principal;</li>
    <li>Aplica encargos e, em muitos casos, IOF e tarifas sobre esse novo principal, maior que o valor originalmente recebido pelo beneficiário;</li>
    <li>Reinicia a contagem do prazo, o que — mesmo mantendo uma parcela mensal parecida — faz o total de juros pago ao longo do tempo crescer de forma que não é intuitiva para quem olha apenas o valor da parcela.</li>
</ul>

<p>Um indício numérico direto: se, ao longo de um extrato de vários anos, o <strong>valor total efetivamente recebido pelo beneficiário em cada operação</strong> (a diferença entre o novo contrato e a quitação do anterior) é sistematicamente pequeno frente ao valor total do novo contrato, isso é característico de um refinanciamento que serviu majoritariamente para quitar o saldo anterior — não para atender a uma necessidade de crédito do beneficiário.</p>

<div class="article-cta" style="background-color: var(--bg-light); padding: 40px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 50px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h2 style="margin-top: 0; font-size: 1.8rem; border-bottom: none; padding-bottom: 0;">Identificou essa prática no seu extrato?</h2>
    <p style="margin-bottom: 20px;">Se o seu saldo devedor parece não diminuir ou o seu consignado já foi refinanciado várias vezes, envie sua documentação para nossa equipe realizar uma análise técnica sem compromisso.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20identifiquei%20refinanciamentos%20sucessivos%20no%20meu%20consignado%20e%20gostaria%20de%20uma%20an%C3%A1lise." target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Falar com a equipe
    </a>
</div>

<h2>O que a Instrução Normativa INSS nº 213/2026 mudou — e o que ela não mudou</h2>

<p>Em 17 de agosto de 2026, o INSS publicou a <strong>Instrução Normativa PRES/INSS nº 213/2026</strong>, alterando a IN nº 138/2022, que disciplina as consignações em benefícios previdenciários.</p>

<p>O que a norma trouxe de relevante para este tema:</p>

<ul>
    <li><strong>Prazo de confirmação da portabilidade</strong>: a instituição consignatária proponente passa a ter até <strong>20 dias</strong>, contados da autorização do titular, para confirmar a operação de portabilidade — sob pena de cancelamento automático. Isso reduz a janela em que uma portabilidade pode ficar "em aberto" de forma indefinida.</li>
    <li><strong>Reforço documental</strong>: bancos precisam apresentar a documentação prevista para a operação, sob risco de interrupção dos descontos e dos repasses.</li>
    <li><strong>Fechamento da brecha dos 90 dias iniciais</strong>: a norma consolidou, no papel, a vedação total à contratação de empréstimo consignado nos primeiros 90 dias de um benefício recém-concedido — impedindo a prática de contratar consignado antes mesmo da confirmação formal do bloqueio inicial.</li>
</ul>

<p><strong>O que a norma não trouxe</strong>, e que é o ponto central para quem investiga churning: <strong>não há, na IN 213/2026, nenhuma carência ou período de resfriamento específico para o refinanciamento de um contrato já em vigor.</strong> A vedação dos 90 dias vale para a primeira contratação após a concessão do benefício — não impede que um contrato ativo há seis meses seja refinanciado, depois novamente refinanciado oito meses mais tarde, e assim sucessivamente. Essa é, tecnicamente, a lacuna regulatória que sustenta o modelo de negócio do churning: a lei trata a portabilidade e a contratação inicial, mas não trata a frequência de refinanciamento de contratos já averbados.</p>

<p><em>* Informação verificada em 03/09/2026. Como esta é uma instrução normativa recente, sujeita a regulamentação complementar, recomenda-se checar o texto vigente antes de fundamentar qualquer decisão.</em></p>

<h2>O que o STJ está discutindo nos Temas 1.414 e 1.328</h2>

<p>Em 10 de março de 2026, a Segunda Seção do Superior Tribunal de Justiça afetou ao rito dos recursos repetitivos o <strong>Tema 1.414</strong> (REsp 2.224.599, REsp 2.215.851, REsp 2.224.598 e REsp 2.215.853, relator ministro Raul Araújo), com <strong>suspensão nacional</strong> de todos os processos que discutam questão jurídica idêntica.</p>

<p>O Tema 1.414 nasceu tratando de cartão de crédito consignado, mas sua abrangência interessa diretamente a quem discute churning: um dos pontos que o STJ vai decidir é justamente <strong>o dever de informação nos casos em que o consumidor alega ter pretendido contratar apenas um empréstimo consignado, e as consequências do prolongamento indeterminado da dívida diante de descontos que não bastam para amortizar o saldo, em contraposição aos juros do refinanciamento</strong>. É, na prática, a mesma lógica de dívida perpétua discutida neste artigo — ainda que a controvérsia afetada trate formalmente do produto cartão.</p>

<p>Em conjunto, corre o <strong>Tema Repetitivo 1.328</strong>, também na Segunda Seção, sobre a existência de dano moral presumido (<em>in re ipsa</em>) na hipótese de invalidação desses contratos.</p>

<p>Três pontos que merecem clareza, porque circula muita informação incorreta:</p>

<ol>
    <li><strong>Nenhum dos dois temas tem tese fixada.</strong> Até o fechamento deste texto, o STJ não decidiu o mérito.</li>
    <li><strong>A suspensão atinge o andamento dos recursos</strong>, não impede o ajuizamento de novas ações discutindo refinanciamento sucessivo.</li>
    <li>Como o julgamento afetado trata tecnicamente de <strong>cartão de crédito consignado</strong>, e não do empréstimo consignado tradicional refinanciado sucessivamente, a aplicação direta do precedente a casos de churning em empréstimo comum dependerá de como o STJ delimitar o alcance da tese — outro motivo para não tratar esse precedente como solução automática hoje.</li>
</ol>

<h2>Como identificar o padrão no seu extrato de consignados (HisCon)</h2>

<p>O documento central da análise é o <strong>extrato de empréstimos consignados do INSS</strong>, também chamado de HisCon (Histórico de Consignações), obtido gratuitamente pelo aplicativo ou site Meu INSS, com login gov.br do próprio titular.</p>

<p>Passo a passo:</p>

<ol>
    <li><strong>Liste todos os contratos</strong>, ativos e encerrados, com data de averbação e data de encerramento (quando houver).</li>
    <li><strong>Verifique a causa do encerramento de cada contrato.</strong> O HisCon costuma indicar se a baixa ocorreu por quitação normal ou por liquidação antecipada — este último é o sinal que interessa.</li>
    <li><strong>Compare a data de encerramento de um contrato com a data de abertura do seguinte.</strong> Encerramentos e aberturas no mesmo dia, ou em dias muito próximos, indicam refinanciamento em cadeia.</li>
    <li><strong>Anote o valor liberado em cada novo contrato e o valor usado para quitar o anterior.</strong> A diferença entre os dois é o que o beneficiário efetivamente recebeu naquela operação — muitas vezes uma fração pequena do valor total do novo contrato.</li>
    <li><strong>Some o total de meses em que houve desconto ativo desde o primeiro contrato da sequência</strong>, e compare com o total de "troco" efetivamente recebido ao longo de toda a cadeia. É esse comparativo, e não o valor de uma parcela isolada, que revela o tamanho real do problema.</li>
</ol>

<h2>Refinanciamento legítimo x churning: o que muda na análise</h2>

<div class="table-responsive">
    <table class="article-table">
        <thead>
            <tr>
                <th>Critério</th>
                <th>Refinanciamento legítimo</th>
                <th>Padrão de churning</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Iniciativa</strong></td>
                <td>Geralmente do próprio beneficiário, por necessidade identificável</td>
                <td>Contato ativo recorrente do banco ou correspondente</td>
            </tr>
            <tr>
                <td><strong>Frequência</strong></td>
                <td>Pontual, com anos de intervalo</td>
                <td>Repetida, muitas vezes a cada 12–24 meses</td>
            </tr>
            <tr>
                <td><strong>Valor liberado (troco)</strong></td>
                <td>Proporção relevante do novo contrato</td>
                <td>Fração pequena frente ao saldo incorporado</td>
            </tr>
            <tr>
                <td><strong>Efeito na taxa</strong></td>
                <td>Redução real e comprovável</td>
                <td>Taxa igual, maior, ou vantagem não demonstrada</td>
            </tr>
        </tbody>
    </table>
</div>

<h2>Sinais de que a sequência de refinanciamentos pode ser irregular</h2>

<ul>
    <li>Contratos sucessivos com intervalo curto e valor de troco desproporcionalmente pequeno frente ao valor total contratado;</li>
    <li>Ausência de qualquer registro de contato do beneficiário solicitando o novo crédito;</li>
    <li>Refinanciamento realizado por correspondente diferente do banco original, sem explicação de como os dados foram obtidos;</li>
    <li>Beneficiário idoso ou com dificuldade de compreensão do processo, sem apoio de terceiro no momento da contratação;</li>
    <li>Ausência do contrato assinado quando solicitado formalmente à instituição.</li>
</ul>

<h2>O que fazer ao identificar o padrão</h2>

<p>O primeiro passo não é decidir se vai acionar a Justiça — é reunir a documentação que permite responder, com precisão, três perguntas: quantos contratos existiram nessa cadeia, quanto o beneficiário efetivamente recebeu em cada um, e quanto já foi pago em descontos até hoje. Sem esses números, qualquer avaliação jurídica fica incompleta.</p>

<p>Documentos a reunir:</p>

<ol>
    <li>Extrato de empréstimos consignados (HisCon), com histórico completo de contratos ativos e encerrados;</li>
    <li>Extrato de pagamento de benefício, mostrando os descontos mês a mês;</li>
    <li>Cópia de cada contrato da sequência, solicitada formalmente ao banco;</li>
    <li>Comprovantes de depósito de cada "troco" recebido;</li>
    <li>Registro de qualquer contato (ligação, mensagem) que originou cada refinanciamento, se houver.</li>
</ol>

<h2>Perguntas frequentes sobre churning no consignado</h2>

<h3>Refinanciar um consignado é sempre errado?</h3>
<p>Não. Refinanciar pode ser uma decisão financeira válida quando reduz genuinamente a taxa de juros ou atende a uma necessidade real do beneficiário, com valor liberado relevante. O que caracteriza irregularidade é o padrão repetido, sem vantagem líquida demonstrável, associado à geração de comissão a cada operação.</p>

<h3>Um correspondente bancário pode refinanciar meu contrato sem eu perceber?</h3>
<p>A averbação de crédito consignado exige autorização do titular via aplicativo Meu INSS, com validação por biometria facial ou, na ausência dela, por login gov.br. Na prática, no entanto, há relatos de averbações processadas com pouco ou nenhum contato efetivo com o beneficiário — o que reforça a importância de conferir o extrato periodicamente, e não apenas quando surge um problema visível.</p>

<h3>Existe prazo para contestar refinanciamentos antigos?</h3>
<p>A prescrição é um dos pontos mais controvertidos do tema. A posição majoritária nos tribunais aplica o prazo de dez anos (prescrição decenal), por se tratar de pretensão fundada em nulidade. Existe também argumento minoritário, mas tecnicamente defensável, de que pretensões declaratórias de nulidade não se sujeitam a prazo prescricional. Diante dessa divergência, contratos antigos merecem análise individual — não é seguro presumir, de antemão, que o prazo já se esgotou.</p>

<author-block></author-block>

<div class="article-cta" style="background-color: var(--bg-light); padding: 40px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 50px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h2 style="margin-top: 0; font-size: 1.8rem; border-bottom: none; padding-bottom: 0;">O que vem depois de reunir a documentação?</h2>
    <p style="margin-bottom: 20px;">Se você identificou uma sequência de refinanciamentos no seu extrato de consignados, o passo seguinte é analisar a documentação. Veja <a href="../../#como-funciona" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">como funciona a análise documental do escritório</a> ou fale diretamente com a equipe.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20identifiquei%20refinanciamentos%20sucessivos%20no%20meu%20consignado%20e%20gostaria%20de%20uma%20an%C3%A1lise." target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Falar com a equipe
    </a>
</div>
"""

new_template = template[:body_start] + new_content + template[body_end:]

with open("blog/churning-consignado-inss/index.html", "w") as f:
    f.write(new_template)
