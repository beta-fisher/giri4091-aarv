# Importar módulo requests
import requests


url = "https://fakestoreapi.com/products"
response = requests.get(url)


print('Status code')
print(response.status_code)
