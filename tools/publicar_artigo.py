#!/usr/bin/env python3
"""Gera a página de um artigo do blog a partir de um arquivo .md no padrão do projeto.

Uso:  python3 tools/publicar_artigo.py caminho/do/artigo.md [outro.md ...] [--data AAAA-MM-DD]

O .md precisa ter as seções "## Metadados" e "## Artigo" separadas por linhas "---".
O script cria blog/<slug>/index.html (a partir do modelo blog/o-que-e-rcc-inss/),
inclui o artigo em assets/js/blog-data.js e no sitemap.xml e, ao final, regenera a
lista estática do blog (tools/prerender_blog.py). As seções "Alterações em outras
páginas", "Imagem sugerida" e "Notas" do .md não são publicadas.
"""
import datetime, json, os, re, subprocess, sys, urllib.parse
import markdown

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELO = 'blog/o-que-e-rcc-inss/index.html'
SITE = 'https://lgouvea.com'
ESTILO_LINK = 'style="color: var(--primary-color); font-weight: 600; text-decoration: underline;"'
MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
MESES_ABREV = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
ICONES = {
    'cartao': '<rect x="2" y="4" width="20" height="16" rx="2" ry="2"/><line x1="2" y1="10" x2="22" y2="10"/><line x1="6" y1="16" x2="6.01" y2="16"/>',
    'documento': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/>',
    'escudo': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    'alerta': '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    'banco': '<rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>',
}
CLASSE_CATEGORIA = {'Direito Bancário': 'a-card-banner-direito-bancario', 'Direito Imobiliário': 'a-card-banner-direito-imobiliario'}


def ler_md(caminho):
    texto = open(caminho, encoding='utf-8').read()
    secoes = {}
    for parte in re.split(r'\n---\n', texto):
        m = re.search(r'^## (Metadados|Artigo|Alterações em outras páginas|Imagem sugerida|Notas para o Lucas)\s*$', parte, re.M)
        if m:
            secoes[m.group(1)] = parte[m.end():].strip()
    meta = dict(re.findall(r'^- \*\*(.+?):\*\* (.+)$', secoes['Metadados'], re.M))
    return meta, secoes['Artigo']


def md_para_html(md):
    html = markdown.markdown(md, extensions=['tables'])
    html = html.replace('<table>', '<div class="table-responsive">\n<table class="article-table">').replace('</table>', '</table>\n</div>')

    def link(m):
        href = m.group(1)
        externo = href.startswith('http') and not href.startswith(SITE)
        extra = ' target="_blank" rel="noopener noreferrer"' if externo else ''
        return f'<a href="{href}"{extra} {ESTILO_LINK}>'
    html = re.sub(r'<a href="([^"]+)">', link, html)
    return re.sub(r'\n(?=<(?:h2|h3|p|ul|ol|div class="table))', '\n\n', html)


def escolher_icone(slug):
    if re.search(r'rmc|rcc|cartao', slug): return 'cartao'
    if re.search(r'golpe|pix|fraude|med', slug): return 'escudo'
    if re.search(r'nao-reconhecid|golpista|falso', slug): return 'alerta'
    if re.search(r'extrato|refinanc|portabil|bloquear|contrato', slug): return 'documento'
    return 'banco'


def gerar(caminho, data_pub):
    meta, artigo = ler_md(caminho)
    slug, titulo, h1, desc = meta['Slug'], meta['Title'], meta['H1'], meta['Meta description']
    categoria = meta.get('Categoria', 'Direito Bancário')
    minutos = re.search(r'\d+', meta['Tempo de leitura']).group(0)
    d, m, a = re.search(r'(\d{2})/(\d{2})/(\d{4})', meta['Fontes verificadas em']).groups()
    verificado = f'{a}-{m}-{d}'
    assert len(titulo) <= 60, f'title longo ({len(titulo)}): {titulo}'
    assert len(desc) <= 160, f'meta description longa ({len(desc)})'
    assert '—' not in artigo, 'o artigo contém travessão'

    linhas = artigo.split('\n')
    assert linhas[0].startswith('# ') and linhas[0][2:].strip() == h1, 'H1 do artigo difere dos metadados'
    corpo = '\n'.join(linhas[1:]).strip()
    # a última seção "Precisa de ajuda ...?" vira a caixa de contato
    partes = re.split(r'\n## (Precisa de ajuda[^\n]*)\n', corpo)
    assert len(partes) == 3, 'seção final "Precisa de ajuda" não encontrada'
    corpo, cta_titulo, cta_texto = partes[0].strip(), partes[1].strip(), partes[2].strip()
    cta_html = md_para_html(cta_texto).replace(ESTILO_LINK, 'style="color: var(--color-primary); font-weight: 600; text-decoration: underline;"')
    cta_html = cta_html.replace('<p>', '<p style="margin-bottom: 20px;">', 1)
    mensagem = urllib.parse.quote(f'Olá, li o artigo "{h1}" no site e gostaria de uma orientação.', safe='')

    corpo_html = f'''<div class="article-body">

{md_para_html(corpo)}

<author-block></author-block>

<div class="article-cta" style="background-color: var(--bg-light); padding: 40px; border-radius: 8px; border-left: 6px solid #D6AF67; margin-top: 50px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
    <h2 style="margin-top: 0; font-size: 1.8rem; border-bottom: none; padding-bottom: 0;">{cta_titulo}</h2>
    {cta_html}
    <a href="https://wa.me/5516936180178?text={mensagem}" target="_blank" rel="noopener noreferrer" class="btn btn-darkblue">
        Falar pelo WhatsApp
    </a>
</div>
            </div>

'''
    s = open(os.path.join(RAIZ, MODELO), encoding='utf-8').read()
    i, j = s.find('<div class="article-body">'), s.find('            <!-- Botão de Voltar -->')
    cabeca, rodape = s[:i], s[j:]
    url = f'{SITE}/blog/{slug}/'

    def troca(padrao, novo, texto, n=1):
        res, k = re.subn(padrao, lambda _: novo, texto, flags=re.S)
        assert k == n, (padrao, k)
        return res
    cabeca = troca(r'<title>.*?</title>', f'<title>{titulo} | Lucas Gouvea</title>', cabeca)
    cabeca = troca(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', cabeca)
    cabeca = troca(r'<meta name="last-verified" content="[^"]*">', f'<meta name="last-verified" content="{verificado}">', cabeca)
    cabeca = troca(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', cabeca)
    cabeca = troca(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', cabeca)
    cabeca = troca(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{titulo}">', cabeca)
    cabeca = troca(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', cabeca)

    def bloco(obj):
        return '<script type="application/ld+json">\n' + '\n'.join('    ' + l for l in json.dumps(obj, ensure_ascii=False, indent=2).split('\n')) + '\n    </script>'
    artigo_ld = {
        '@context': 'https://schema.org', '@type': 'BlogPosting',
        'mainEntityOfPage': {'@type': 'WebPage', '@id': url},
        'headline': h1, 'description': desc,
        'author': {'@type': 'Person', 'name': 'Lucas Gouvea', 'url': SITE},
        'publisher': {'@type': 'Organization', 'name': 'Lucas Gouvea Sociedade Individual de Advocacia',
                      'logo': {'@type': 'ImageObject', 'url': f'{SITE}/assets/logo-horizontal-advogado.png'}},
        'datePublished': data_pub.isoformat(), 'dateModified': data_pub.isoformat(), 'articleSection': categoria,
    }
    trilha_ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': f'{SITE}/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': f'{SITE}/blog/'},
        {'@type': 'ListItem', 'position': 3, 'name': h1, 'item': url}]}
    cabeca = troca(r'<script type="application/ld\+json">.*?</script>\s*<script type="application/ld\+json">.*?</script>',
                   bloco(artigo_ld) + '\n    ' + bloco(trilha_ld), cabeca)
    cabeca, k0 = re.subn(r'(<h1 class="article-title"[^>]*>).*?</h1>', lambda mm: mm.group(1) + h1 + '</h1>', cabeca, flags=re.S); assert k0 == 1
    data_longa = f'{data_pub.day} de {MESES[data_pub.month - 1]}, {data_pub.year}'
    cabeca, k1 = re.subn(r'\n \d{1,2}º? de [A-Za-zç]+, \d{4}\n', lambda _: f'\n {data_longa}\n', cabeca); assert k1 == 1
    cabeca, k2 = re.subn(r'\n \d+ min de leitura\n', lambda _: f'\n {minutos} min de leitura\n', cabeca); assert k2 == 1
    cabeca, k3 = re.subn(r'<span>Direito Bancário</span>', lambda _: f'<span>{categoria}</span>', cabeca); assert k3 == 1
    cabeca, k4 = re.subn(r'(<span class="blog-category"[^>]*>)[^<]*</span>', lambda mm: mm.group(1) + categoria + '</span>', cabeca); assert k4 == 1
    assert 'o-que-e-rcc-inss' not in cabeca or slug == 'o-que-e-rcc-inss', 'sobrou referência ao artigo modelo'

    os.makedirs(os.path.join(RAIZ, 'blog', slug), exist_ok=True)
    open(os.path.join(RAIZ, 'blog', slug, 'index.html'), 'w', encoding='utf-8').write(cabeca + corpo_html + rodape)

    # lista do blog
    p = os.path.join(RAIZ, 'assets/js/blog-data.js'); b = open(p, encoding='utf-8').read()
    if f'url: "{slug}/"' not in b:
        icone = ICONES[escolher_icone(slug)]
        entrada = f'''const blogPosts = [
    {{
        id: "{slug}",
        category: "{categoria}",
        title: {json.dumps(h1, ensure_ascii=False)},
        excerpt: {json.dumps(desc, ensure_ascii=False)},
        date: "{data_pub.isoformat()}",
        dateDisplay: "{data_pub.day} {MESES_ABREV[data_pub.month - 1]}, {data_pub.year}",
        readTime: "{minutos} min leitura",
        url: "{slug}/",
        iconClass: "{CLASSE_CATEGORIA.get(categoria, 'a-card-banner-direito-bancario')}",
        svgIcon: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">{icone}</svg>'
    }},

'''
        assert b.startswith('const blogPosts = [\n')
        open(p, 'w', encoding='utf-8').write(entrada + b[len('const blogPosts = [\n'):])
    # sitemap
    p = os.path.join(RAIZ, 'sitemap.xml'); x = open(p, encoding='utf-8').read()
    if f'<loc>{url}</loc>' not in x:
        x = x.replace('</urlset>', f'''
  <url>
    <loc>{url}</loc>
    <lastmod>{data_pub.isoformat()}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>''')
        open(p, 'w', encoding='utf-8').write(x)
    return slug


if __name__ == '__main__':
    args = sys.argv[1:]
    data_pub = datetime.date.today()
    if '--data' in args:
        k = args.index('--data'); data_pub = datetime.date.fromisoformat(args[k + 1]); del args[k:k + 2]
    # o último da linha de comando fica no topo da lista do blog; por isso, gera em ordem inversa
    for caminho in reversed(args):
        print('gerado:', gerar(caminho, data_pub))
    subprocess.run([sys.executable, os.path.join(RAIZ, 'tools/prerender_blog.py')], check=True)
