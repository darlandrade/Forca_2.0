import json

import requests
from bs4 import BeautifulSoup

url = 'https://www.infoescola.com/espanhol/partes-do-corpo-humano/'
# url = 'https://www.biologianet.com/curiosidades-biologia/frutas.htm'
# url = 'https://www.infoescola.com/espanhol/partes-do-corpo-humano/'

conn = requests.get(url)
soup = BeautifulSoup(conn.content, 'html.parser')

procura = soup.find_all('td')

teste = procura
ch = []
for x in procura[1::2]:
    ch.append(x.text)


# with open("Palavras.json", 'r') as ler_arquivo:
#     arquivo = json.load(ler_arquivo)
#     with open('Palavras.json', 'w') as salvar_arquivo:
#
#         lista = []
#         for a in frutas_separada:
#             lista.extend(a[1].split(', '))
#
#         arquivo["Fruta"] = lista
#         obj = json.dumps(arquivo, ensure)
#         salvar_arquivo.write(obj)

# with open("Palavras.json", 'r', ) as ler_arquivo:
#     arquivo = json.load(ler_arquivo)
#     with open('Palavras.json', 'w') as salvar_arquivo:
#
#         lista = []
#         for x in procura[1::2]:
#             lista.append(x.text)
#
#         arquivo["Corpo Humano"] = lista
#         obj = json.dumps(arquivo, ensure_ascii=False)
#         salvar_arquivo.write(obj)
