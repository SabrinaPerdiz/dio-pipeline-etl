import pandas as pd
import requests as rq
from googletrans import Translator

url_base = 'https://favqs.com/api'

#Extração
tradutor = Translator()
tema = input('Insira o tema da frase: ') 
tema_en = tradutor.translate(tema, src='pt', dest='en').text
headers = {'Authorization':'Token token="5bb1866fa53ba1f2147d49e08c338df9"',
           'Content-Type':'application/json'}
response = rq.get(f'{url_base}/quotes/?filter={tema_en}&type=tag', headers = headers) 
cru = pd.io.json.json_normalize(response.json())

#Transformação
lista = cru.values.tolist()
cont = 0
frases = []
autores = []
while cont < len(lista[0][2]):
  frases.append(tradutor.translate(lista[0][2][cont]['body'], src='en', dest='pt').text)
  autores.append(lista[0][2][cont]['author'])
  cont += 1
dicionario = {'Frases':frases,'Autores':autores}
df = pd.DataFrame(dicionario)

#Carregamento
df.to_csv(f'frases_{tema}.csv', sep=';', index=False)
print('Finalizado!')


