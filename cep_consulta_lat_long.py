import requests

# Gerar token particular para consulta do site https://www.cepaberto.com/
headers = {'Authorization': 'Token token=XXXXXXXXXX'}

# lista de ceps a consultar
cep = ["01001000", "XXXXXX"]

# variáveis globais
cep_ok = []

# loop para consultar a api do CEP e conseguir suas long e lat, devolvendo em um dicinário python
for i in cep:
    url = "http://www.cepaberto.com/api/v3/cep?cep=" + str(i)
    response = requests.get(url, headers=headers)
    json = response.json()
    Coordinates = {
        "Cep": i, "Longitude": json['longitude'], "Latitude": json['latitude']}
    cep_ok.append(Coordinates)


for j in cep_ok:
    print(j)
