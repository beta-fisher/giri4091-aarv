# Importar módulo requests
import requests


url = "https://fakestoreapi.com/products"
response = requests.get(url)


print('Tipo Contenido')
print(response.headers['Content-Type'])