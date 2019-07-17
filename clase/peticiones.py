import requests

KEY = "4e9fcd9d"
URL = "http://www.omdbapi.com/?apikey="
titulo = "The Matrix"

busqueda = URL + KEY + "&t=" + titulo
resultado = requests.get(busqueda)
print(resultado.json())


# Crear una funcion que reciba como parametro el nombre de una
# pelicula y que retorne el nombre del director de la pelicula
# usando el API de OMDB

def obtener_director(nombre_peli):
    busqueda = URL + KEY + "&t=" + nombre_peli
    resultado = requests.get(busqueda)
    return resultado.json()["Director"]

print(obtener_director("Titanic"))
