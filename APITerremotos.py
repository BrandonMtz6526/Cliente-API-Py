# Brandon de Jesus Martinez Jimenez 
# Laboratorio para el Despliegue de Aplicaciones Empresariales
# Profesor: Carlos Rafael Levy Rojas 
# 
# Cliente de una API
# Instrucciones:
# Realice un cliente que consulte la api de Terremotosde la USGS
# https://earthquake.usgs.gov/fdsnws/event/1/


import requests

# URL de la API
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2024-09-01&endtime=2024-11-02&minmagnitude=6"
# Solicitud GET a la URL 
respuesta = requests.get(url)

# Verificamos que la solicitud fue exitosa
if respuesta.status_code == 200:
    # Convertir la respuesta JSON a un diccionario
    terremotos = respuesta.json()
    
    # Iterar sobre cada terremoto en los datos obtenidos
    for terremoto in terremotos["features"]:
        lugar = terremoto["properties"]["place"]
        magnitud = terremoto["properties"]["mag"]
        tiempo = terremoto["properties"]["time"]
        
        # Imprimir los valores
        print(f"Lugar: {lugar}")
        print(f"Magnitud: {magnitud}")
        print(f"Tiempo (timestamp): {tiempo}\n")
else:
    print(f"Error en la solicitud: {respuesta.status_code}")
