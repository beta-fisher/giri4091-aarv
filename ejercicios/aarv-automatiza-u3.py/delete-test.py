import requests

def DeleteProduct():
    noProduct = (input("Ingresa el valor del número del producto: ")) 
    url = "https://fakestoreapi.com/products/"+noProduct

    response = requests.delete(url)

    if response.status_code == 200:
        print("Producto eliminado exitosamente :D")
        print(response.json())
    else:
        print("Error al eliminar el producto ;(())")
        print(response.status_code)
        print(response.text)
        
DeleteProduct()