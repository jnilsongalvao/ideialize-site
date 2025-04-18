
import requests
from bs4 import BeautifulSoup
import json

BASE_URL = 'https://www.asiaimport.com.br'
CATEGORIAS = [
    '/brindes/mochilas-e-malas',
    '/brindes/escritorio',
    '/brindes/canecas-e-garrafas',
    '/brindes/eco',
    '/brindes/diversos'
]

produtos = []

for categoria in CATEGORIAS:
    url = BASE_URL + categoria
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    itens = soup.select('.product-block')
    for item in itens:
        nome = item.select_one('.product-name')
        imagem = item.select_one('img')
        descricao = item.select_one('.short-description')

        produtos.append({
            'nome': nome.text.strip() if nome else 'Produto sem nome',
            'imagem': imagem['data-src'] if imagem and 'data-src' in imagem.attrs else '',
            'descricao': descricao.text.strip() if descricao else 'Sem descrição.'
        })

with open('produtos.json', 'w', encoding='utf-8') as f:
    json.dump(produtos, f, ensure_ascii=False, indent=2)

print(f'{len(produtos)} produtos salvos em produtos.json.')
