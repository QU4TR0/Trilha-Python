import http.client
import pandas as pd
import json
import requests

conn = http.client.HTTPSConnection("real-time-amazon-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "be7e7a9aacmshb7e3d2d1deb9c15p167af0jsn3e6d28827f75",
    'x-rapidapi-host': "real-time-amazon-data.p.rapidapi.com"
}

conn.request("GET", "/products-by-category?category_id=2478868012&page=1&country=BR&sort_by=RELEVANCE&product_condition=ALL&is_prime=false&deals_and_discounts=NONE", headers=headers)

res = conn.getresponse()
data = res.read()

dados = data.decode('utf-8')

json_string = dados[dados.find('products:'):-1]
dados_format = json.loads(json_string)

df = pd.DataFrame(dados_format)

print(df)