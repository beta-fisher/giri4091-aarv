# Importar módulo requests
import json
import requests

url = "https://fakestoreapi.com/products"
response = requests.get(url)


json_formateado = json.dumps(response.json(), indent=4, ensure_ascii=False) 
print(response.json())


