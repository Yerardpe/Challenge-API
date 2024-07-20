import requests
import json

def hacer_peticion(url):
    response = requests.request("GET", url)
    tiempo_respuesta = response.elapsed.total_seconds()
    codigo_respuesta = response.status_code 


    data = response.json()
    
    for personaje in data["results"]:
        if personaje["status"]  == "Alive":
            personajes_vivos.append(personaje["name"])
        if personaje["status"] == "Dead":
            personajes_muertos.append(personaje["name"])
                   
    if data["info"]["next"]:
        hacer_peticion(data["info"]["next"])
            

    #print(json.dumps(data, indent=2))
    print(f"url consultada:{url}")
    print(f"Tiempo de respuesta:{tiempo_respuesta} segundos")
    print(f"Codigo de respuesta: {codigo_respuesta}")


url = "https://rickandmortyapi.com/api/character"
personajes_vivos = []
personajes_muertos = []
print("realizando consultas ...")
hacer_peticion(url)
print("===================================================================================")

print(f"Hay {len(personajes_vivos)} personajes_vivos:{personajes_vivos}")
print("===================================================================================")
print(f"Hay {len(personajes_muertos)} personajes_muertos:{personajes_muertos}")

