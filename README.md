### Cliente de una API

- Realice un cliente que consulte la api de Terremotosde la USGS
-  https://earthquake.usgs.gov/fdsnws/event/1/


###En que consiste

Utilizamos el url de la API con el format para que se realice en las fechas entre el 01 de septiembre y el 01 de noviembre, solo se mostraran terremotos con magnitudes igual o mayor a 6.

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2024-09-01&endtime=2024-11-02&minmagnitude=6"

La iteración de los datos unicamente nos mostrara el lugar del terremoto, la magnitud que tuvo y el tiempo en que se reporto el terremoto.
    
    for terremoto in terremotos["features"]:
        lugar = terremoto["properties"]["place"]
        magnitud = terremoto["properties"]["mag"]
        tiempo = terremoto["properties"]["time"]
        
        print(f"Lugar: {lugar}")
        print(f"Magnitud: {magnitud}")
        print(f"Tiempo (timestamp): {tiempo}\n")
	

###Resultados.

![ice_screenshot_20241106-182014](https://github.com/user-attachments/assets/b869b3dd-328a-4a11-96fe-fc25e1ab2fd1)
