import requests

# Token particular para consulta do site https://www.cepaberto.com/
headers = {'Authorization': 'Token token=7d62143aca9ee4e8d27195a83a92cadd'}

# lista de ceps a consultar
cep = ["72115035", "01001000"]

#variáveis globais
geos = {}
cep_ok = []

#loop para consultar a api do CEP e conseguir suas long e lat, devolvendo em um dicinário python
for i in cep:
  url = "http://www.cepaberto.com/api/v3/cep?cep=" + str(i)
  response = requests.get(url, headers=headers)
  json = response.json()
  Coordinates = {"Cep": i, "Longitude": json['longitude'], "Latitude": json['latitude']}
  # geos.update(Coordinates)
  cep_ok.append(Coordinates)
  

for j in cep_ok:
  print(j)
