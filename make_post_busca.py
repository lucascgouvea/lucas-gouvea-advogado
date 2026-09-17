import os

with open("blog/revisional-financiamento-veiculo/index.html", "r") as f:
    template = f.read()

# Replace metadata
template = template.replace(
    "<title>Juros De Financiamento De Veículo: O Que Pode Ser Revisto? | Lucas Gouvea</title>",
    "<title>Busca e Apreensão de Veículo: o Que Fazer ao Ser Citado | Lucas Gouvea</title>"
)
template = template.replace(
    '<meta name="description" content="Entenda o que uma revisional de financiamento de veículo pode discutir: juros, tarifas, seguro e encargos, e o que a ação não resolve na prática.">',
    '<meta name="description" content="Foi citado em ação de busca e apreensão de veículo? Entenda os prazos legais, o que é purgar a mora e quando contestar faz sentido no seu caso.">'
)
template = template.replace(
    'href="https://lgouvea.com/blog/revisional-financiamento-veiculo/"',
    'href="https://lgouvea.com/blog/busca-e-apreensao-veiculo/"'
)
template = template.replace(
    'content="https://lgouvea.com/blog/revisional-financiamento-veiculo/"',
    'content="https://lgouvea.com/blog/busca-e-apreensao-veiculo/"'
)
template = template.replace(
    '<meta property="og:title" content="Juros De Financiamento De Veículo: O Que Pode Ser Revisto?">',
    '<meta property="og:title" content="Busca e Apreensão de Veículo: o Que Fazer ao Ser Citado">'
)
template = template.replace(
    '<meta property="og:description" content="Entenda o que uma revisional de financiamento de veículo pode discutir: juros, tarifas, seguro e encargos, e o que a ação não resolve na prática.">',
    '<meta property="og:description" content="Foi citado em ação de busca e apreensão de veículo? Entenda os prazos legais, o que é purgar a mora e quando contestar faz sentido no seu caso.">'
)

schema_old = """"headline": "Juros De Financiamento De Veículo: O Que Pode Ser Revisto?",
      "description": "Entenda o que uma revisional de financiamento de veículo pode discutir: juros, tarifas, seguro e encargos, e o que a ação não resolve na prática.","""
schema_new = """"headline": "Busca e apreensão de veículo: o que fazer ao ser citado pelo banco",
      "description": "Foi citado em ação de busca e apreensão de veículo? Entenda os prazos legais, o que é purgar a mora e quando contestar faz sentido no seu caso.","""
template = template.replace(schema_old, schema_new)

# Header
header_old = """<h1 class="article-title" data-aos="fade-up">Juros De Financiamento De Veículo: O Que Pode Ser Revisto?</h1>
                
                <div class="article-meta" data-aos="fade-up" data-aos-delay="100">
                    <div class="article-meta-item">
                        <i data-lucide="user"></i> Dr. Lucas Gouvea
                    </div>
                    <div class="article-meta-item">
                        <i data-lucide="calendar"></i> 12 de Setembro, 2026
                    </div>"""
                
header_new = """<h1 class="article-title" data-aos="fade-up">Busca e apreensão de veículo: o que fazer ao ser citado pelo banco</h1>
                
                <div class="article-meta" data-aos="fade-up" data-aos-delay="100">
                    <div class="article-meta-item">
                        <i data-lucide="user"></i> Dr. Lucas Gouvea
                    </div>
                    <div class="article-meta-item">
                        <i data-lucide="calendar"></i> 17 de Setembro, 2026
                    </div>"""
template = template.replace(header_old, header_new)

# Body injection
body_start = template.find('<div class="article-body">\n') + len('<div class="article-body">\n')
body_end = template.find('            </div>\n\n            <!-- Botão de Voltar -->')

new_content = """
<p>Receber uma citação de busca e apreensão costuma gerar a sensação de que o tempo já se esgotou. Não é bem assim. Existem prazos específicos, contados de formas que a maioria das pessoas desconhece, e a forma como cada etapa é conduzida influencia diretamente se o veículo pode ser recuperado.</p>

<div class="article-cta" style="background-color: var(--bg-light); padding: 30px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 30px; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h3 style="margin-top: 0; font-size: 1.4rem; border-bottom: none; padding-bottom: 0;">Foi notificado ou o veículo foi apreendido?</h3>
    <p style="margin-bottom: 20px;">Se você já foi citado, os prazos são muito curtos e correm mesmo sem aviso pessoal. Procure orientação jurídica imediatamente, antes de decidir pagar, ignorar ou contestar por conta própria.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20recebi%20uma%20a%C3%A7%C3%A3o%20de%20busca%20e%20apreens%C3%A3o%20e%20gostaria%20de%20orienta%C3%A7%C3%A3o" target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Falar com advogado agora
    </a>
</div>

<h2>O que é a ação de busca e apreensão por alienação fiduciária</h2>

<p>Quando um veículo é financiado com <strong>alienação fiduciária</strong>, a propriedade do bem fica, formalmente, com a instituição financeira até o pagamento da última parcela. O devedor tem apenas a posse direta, na condição de depositário. Essa estrutura, prevista no <a href="https://www2.camara.leg.br/legin/fed/declei/1960-1969/decreto-lei-911-1-outubro-1969-375229-publicacaooriginal-1-pe.html" target="_blank" rel="noopener">Decreto-Lei nº 911/1969</a>, existe justamente para dar ao credor um caminho rápido de retomada em caso de inadimplência.</p>

<p>Havendo mora comprovada, o banco pode pedir a busca e apreensão do veículo, e o juiz pode conceder a medida de forma liminar, ou seja, antes mesmo de ouvir o devedor. É por isso que, na prática, muitas pessoas só tomam conhecimento do processo quando o veículo já foi apreendido ou quando a citação chega.</p>

<h2>Notificação, citação e execução da liminar: entenda cada etapa</h2>

<p>Três momentos diferentes costumam ser confundidos, e essa confusão é uma das principais causas de perda de prazo.</p>

<ul>
    <li>A <strong>notificação extrajudicial</strong> é anterior ao processo. O banco comprova a mora por carta registrada ou protesto do título, conforme o artigo 2º, parágrafo 2º, do Decreto-Lei 911/69. Essa etapa não abre prazo judicial, apenas formaliza o inadimplemento para viabilizar a ação.</li>
    <li>A <strong>execução da liminar</strong> ocorre quando o veículo é efetivamente apreendido, por oficial de justiça ou por empresa contratada para esse fim.</li>
    <li>A <strong>citação</strong> é o ato pelo qual o devedor é formalmente comunicado do processo e convocado para se defender. Ela pode acontecer no mesmo momento da apreensão do bem ou em data diferente.</li>
</ul>

<p>A distinção importa porque, como será explicado a seguir, o prazo mais crítico do processo não começa a contar da citação.</p>

<h2>Quando começa a contar o prazo de 5 dias para purgar a mora</h2>

<p>O artigo 3º, parágrafo 1º, do Decreto-Lei 911/69 prevê que, cinco dias após executada a liminar, a propriedade e a posse plena do veículo se consolidam em nome do credor, caso a dívida não tenha sido paga integralmente até então.</p>

<p>Durante décadas houve controvérsia sobre o marco inicial dessa contagem: alguns entendiam que o prazo deveria correr da ciência pessoal do devedor, outros, da própria execução da liminar. Em agosto de 2025, a 2ª Seção do Superior Tribunal de Justiça pacificou a questão em julgamento de recurso repetitivo (Tema 1.279, REsp 2.126.264/MS, relator ministro Antonio Carlos Ferreira), fixando a seguinte tese:</p>

<p><strong>"Nas ações de busca e apreensão de bens alienados fiduciariamente, o prazo de 5 dias para pagamento da integralidade da dívida, previsto no art. 3º, parágrafo 1º, do Decreto-Lei nº 911/69, começa a fluir a partir da data da execução da medida liminar."</strong></p>

<p>Essa tese vale para todos os processos em curso no país, por força do rito dos recursos repetitivos.</p>

<h3>Por que a execução da liminar, e não a citação, é o marco inicial</h3>

<p>O raciocínio do STJ se apoia em dois pontos. Primeiro, o artigo 397 do Código Civil trata da chamada mora <em>ex re</em>: o simples vencimento da obrigação sem pagamento já constitui a mora, independentemente de notificação judicial. Segundo, a norma especial do Decreto-Lei 911/69 prevalece sobre a regra geral do Código de Processo Civil quanto à contagem de prazos, pelo critério da especialidade.</p>

<p>Na prática, isso significa que o relógio pode começar a correr antes mesmo de o devedor saber, com certeza, que foi citado. Por isso, ao identificar o veículo apreendido ou receber qualquer comunicação sobre o processo, o prazo já deve ser tratado como estando em curso.</p>

<div class="article-cta" style="background-color: var(--bg-light); padding: 40px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 50px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h2 style="margin-top: 0; font-size: 1.8rem; border-bottom: none; padding-bottom: 0;">Seu veículo já foi levado pelo oficial de justiça?</h2>
    <p style="margin-bottom: 20px;">Você tem apenas 5 dias a partir desse momento para purgar a mora. Qualquer atraso significará a perda definitiva da propriedade. Entre em contato urgente para analisar a petição inicial e a dívida cobrada.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20meu%20ve%C3%ADculo%20foi%20apreendido%20e%20preciso%20de%20atendimento%20urgente" target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Solicitar análise de urgência
    </a>
</div>

<h2>O que significa pagar a integralidade da dívida</h2>

<p>Um erro recorrente é acreditar que pagar apenas as parcelas atrasadas resolve a situação. Não resolve. Desde a alteração promovida pela Lei 10.931/2004, e confirmada pelo STJ no Tema 722 (REsp 1.418.593/MS), a purgação da mora exige o pagamento da <strong>integralidade da dívida</strong>, considerando os valores apresentados e comprovados pelo credor na petição inicial, e não apenas as prestações vencidas.</p>

<p>Isso inclui, normalmente, parcelas vencidas e vincendas, encargos contratuais e os valores discriminados pelo próprio banco no processo. Pagar parcialmente, dentro do prazo de 5 dias, não impede a consolidação da propriedade em nome do credor.</p>

<h2>Purgar a mora ou contestar: as duas estratégias possíveis</h2>

<p>A partir daqui, a decisão deixa de ser sobre prazo e passa a ser sobre estratégia. Cada caminho tem uma lógica diferente.</p>

<h3>Purgar a mora para reaver o veículo</h3>

<p>Se o objetivo é manter o bem e existem condições financeiras (próprias ou por meio de um acordo) para isso, o pagamento integral da dívida apresentada pelo credor, dentro dos 5 dias, extingue a ação e devolve o veículo livre de ônus. Essa via não discute a legalidade dos valores cobrados, apenas quita o que foi apresentado.</p>

<h3>Contestar para discutir a regularidade da cobrança</h3>

<p>O devedor também tem 15 dias, contados a partir da juntada aos autos do mandado de citação cumprido, para apresentar contestação. Nela é possível questionar a regularidade da notificação de mora, a correção dos valores cobrados e, quando cabível, a abusividade de cláusulas do próprio contrato de financiamento. Contestar não devolve o veículo automaticamente, mas pode reverter a ação, afastar cobranças indevidas ou reduzir o valor devido.</p>

<h3>É possível combinar as duas providências</h3>

<p>Sim. Purgar a mora recupera o veículo de imediato; contestar discute o mérito da dívida. Um cliente pode pagar o valor apresentado para reaver o bem e, na sequência ou em ação própria, questionar judicialmente encargos que considere abusivos, buscando a restituição da diferença. A combinação depende da análise de cada contrato e da urgência em relação ao veículo.</p>

<h2>É possível discutir juros abusivos dentro da própria ação</h2>

<p>É possível, mas com uma condição importante. A Súmula 381 do STJ estabelece que, em contratos bancários, o juiz não pode reconhecer de ofício a abusividade de cláusulas. Isso significa que, se o devedor quiser discutir juros, tarifas ou encargos dentro da ação de busca e apreensão, essa discussão precisa ser levantada expressamente na contestação, com indicação concreta das cláusulas questionadas. O juiz não vai procurar irregularidades por conta própria.</p>

<p>Quem já está analisando o contrato sob esse ângulo pode se beneficiar de uma leitura complementar sobre <a href="../../blog/revisional-financiamento-veiculo/" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">revisão de juros e encargos em financiamento de veículo</a>, que detalha como identificar, no próprio contrato, o que pode ser questionado.</p>

<h2>Documentos que fazem diferença na análise do caso</h2>

<p>Antes de decidir entre purgar, contestar ou combinar as duas providências, alguns documentos precisam estar reunidos:</p>

<ul>
    <li>contrato de financiamento com todas as cláusulas e anexos;</li>
    <li>extrato de pagamentos realizados, incluindo comprovantes de parcelas já pagas;</li>
    <li>notificação extrajudicial de mora, se recebida;</li>
    <li>mandado de citação e a petição inicial da ação, com a planilha de valores apresentada pelo banco;</li>
    <li>boletim de ocorrência, se o veículo foi apreendido em circunstância que gerou dúvida sobre a regularidade do procedimento.</li>
</ul>

<p>A análise conjunta desses documentos é o que permite saber, com segurança, se os valores cobrados na inicial correspondem ao contrato e se há espaço real para questionamento.</p>

<h2>Armadilhas comuns depois da apreensão do veículo</h2>

<p>Algumas situações costumam pegar o devedor desprevenido:</p>

<ul>
    <li><strong>Contar o prazo a partir da citação, e não da apreensão.</strong> Como visto, o prazo de 5 dias corre da execução da liminar, o que pode significar menos tempo do que parece.</li>
    <li><strong>Pagar apenas as parcelas atrasadas, achando que isso basta.</strong> Não purga a mora e não impede a consolidação da propriedade.</li>
    <li><strong>Deixar o prazo de contestação passar por acreditar que "já perdeu o veículo".</strong> Mesmo sem o bem, a contestação pode discutir valores, gerar direito à restituição de diferenças ou impedir cobranças posteriores indevidas.</li>
    <li><strong>Assumir risco de prisão por não devolver o bem.</strong> Não existe mais essa possibilidade no ordenamento brasileiro: a Súmula Vinculante 25 do STF declarou ilícita a prisão civil do depositário infiel em qualquer modalidade de depósito, incluída a alienação fiduciária.</li>
</ul>

<h2>O que acontece se o devedor não fizer nada</h2>

<p>Passado o prazo de 5 dias sem pagamento integral, a propriedade e a posse do veículo se consolidam definitivamente em nome do credor, que pode vendê-lo, inclusive antes do trânsito em julgado da ação, sem efeito suspensivo em eventual agravo. Se, mais adiante, a ação for julgada improcedente e o veículo já tiver sido alienado, o artigo 3º, parágrafo 6º, do Decreto-Lei 911/69 prevê multa de 50% do valor originalmente financiado em favor do devedor, mas essa é uma consequência excepcional, não uma garantia de resultado.</p>

<p>Não fazer nada também não afasta a possibilidade de o banco cobrar, depois, eventual saldo remanescente entre o valor da dívida e o valor obtido com a venda do bem, dependendo de como o contrato e a ação foram estruturados.</p>

<h2>Financiamento de imóvel segue o mesmo procedimento</h2>

<p>Não. Ainda que o financiamento de imóvel também possa envolver alienação fiduciária, o procedimento de retomada é outro: rege-se pela Lei 9.514/1997, com intimação pelo cartório de registro de imóveis e leilão extrajudicial, sem a estrutura de busca e apreensão judicial descrita aqui. Quem enfrenta atraso em financiamento habitacional deve buscar orientação específica para esse regime, que tem prazos e consequências próprios. Conheça a <a href="../../#atuacao" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">atuação do escritório em outras áreas relacionadas</a> para entender qual frente trata cada tipo de contrato.</p>

<p>Se você identificou esse tipo de situação nos seus documentos, o passo seguinte é reunir contrato, extrato de pagamentos e a petição inicial da ação para uma análise individualizada. Veja como funciona a <a href="../../direito-bancario-sao-carlos/?utm_source=blog&utm_medium=artigo&utm_campaign=busca-e-apreensao-veiculo" style="color: var(--color-primary); font-weight: 600; text-decoration: underline;">atuação do escritório em defesa em ações de busca e apreensão</a> ou fale diretamente com a equipe.</p>

<author-block></author-block>

<div class="article-cta" style="background-color: var(--bg-light); padding: 40px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 50px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h2 style="margin-top: 0; font-size: 1.8rem; border-bottom: none; padding-bottom: 0;">Precisa de ajuda com uma ação de busca e apreensão?</h2>
    <p style="margin-bottom: 20px;">Cada dia perdido reduz suas opções legais de recuperar o veículo ou de questionar abusos no contrato. Apresente seu caso para nossa equipe e receba orientação rápida.</p>
    <a href="https://wa.me/5516936180178?text=Ol%C3%A1%2C%20recebi%20uma%20a%C3%A7%C3%A3o%20de%20busca%20e%20apreens%C3%A3o%20e%20gostaria%20de%20orienta%C3%A7%C3%A3o" target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Falar com a equipe
    </a>
</div>
"""

new_template = template[:body_start] + new_content + template[body_end:]

os.makedirs("blog/busca-e-apreensao-veiculo", exist_ok=True)
with open("blog/busca-e-apreensao-veiculo/index.html", "w") as f:
    f.write(new_template)
