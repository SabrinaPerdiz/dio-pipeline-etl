import pandas as pd
import requests as rq
from googletrans import Translator

url_base = 'https://favqs.com/api'

def get_quotes(filtro):
  headers = {'Authorization':'Token token="5bb1866fa53ba1f2147d49e08c338df9"',
             'Content-Type':'application/json'}
  response = rq.get(f'{url_base}/quotes/?filter={filtro}&type=tag', headers = headers) 
  trata_json(response.json())

def trata_json(json):
  cru = pd.io.json.json_normalize(json)
  lista = cru.values.tolist()
  cont = 0
  while cont < len(lista[0][2]):
    print(tradutor.translate(lista[0][2][cont]['body'], src='en', dest='pt').text+' - '+lista[0][2][cont]['author'])
    cont += 1

tradutor = Translator()
tema = tradutor.translate(input('Insira o tema da frase: '), src='pt', dest='en').text
get_quotes(tema)


