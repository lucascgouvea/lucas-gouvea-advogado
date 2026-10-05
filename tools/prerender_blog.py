#!/usr/bin/env python3
"""Grava a lista de artigos em HTML dentro de blog/index.html.

A lista do blog é montada no navegador por assets/js/blog-list.js a partir de
assets/js/blog-data.js. Este script grava a mesma lista já pronta no HTML, para que os
links dos artigos existam mesmo sem JavaScript (buscadores, leitores e pré-visualizações).
Rode depois de qualquer mudança em blog-data.js:  python3 tools/prerender_blog.py
"""
import html, json, os, re, subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INICIO, FIM = '<!-- lista-estatica:inicio -->', '<!-- lista-estatica:fim -->'
CALENDARIO = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>'
RELOGIO = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>'
SETA = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>'

dados = subprocess.run(['node', '-e', "const fs=require('fs');const src=fs.readFileSync('assets/js/blog-data.js','utf8').replace('const blogPosts','globalThis.blogPosts');eval(src);console.log(JSON.stringify(globalThis.blogPosts));"],
                       cwd=RAIZ, capture_output=True, text=True, check=True).stdout
posts = sorted(json.loads(dados), key=lambda p: p['date'], reverse=True)  # ordenação estável, como no navegador
e = html.escape
cards = []
for p in posts:
    cards.append(f'''
                    <article class="a-card">
                        <div class="a-card-banner {p['iconClass']}">
                            <div class="a-card-banner-icon">{p['svgIcon']}</div>
                            <div class="a-card-banner-bottom">
                                <span class="a-card-category">{p['svgIcon'].replace('stroke-width="1.2"', 'stroke-width="2"')} {e(p['category'])}</span>
                            </div>
                        </div>
                        <div class="a-card-body">
                            <h2 class="a-card-title"><a href="{p['url']}">{e(p['title'])}</a></h2>
                            <p class="a-card-excerpt">{e(p['excerpt'])}</p>
                            <div class="a-card-footer">
                                <div class="a-card-meta"><span>{CALENDARIO} {e(p['dateDisplay'])}</span><span>{RELOGIO} {e(p['readTime'])}</span></div>
                                <a href="{p['url']}" class="a-card-read">Ler artigo {SETA}</a>
                            </div>
                        </div>
                    </article>''')
bloco = f'<blog-list class="articles-grid">{INICIO}{"".join(cards)}\n                {FIM}</blog-list>'
caminho = os.path.join(RAIZ, 'blog/index.html'); s = open(caminho, encoding='utf-8').read()
s, n = re.subn(r'<blog-list[^>]*>.*?</blog-list>', lambda _: bloco, s, count=1, flags=re.S)
assert n == 1, 'elemento <blog-list> não encontrado em blog/index.html'
open(caminho, 'w', encoding='utf-8').write(s)
print(f'lista estática do blog: {len(posts)} artigos')
