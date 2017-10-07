# Clustering con Spacy

En este directorio podemos encontrar los archivos usados en el servidor para hacer __word clustering__ usando el corpus de *La Voz del Interior*.
- Por un lado tenemos *preparing_data.py* : En este archivo nos encargamos del
  pre-procesamiento y armado de diccionario de features.
- Luego tenemos *clustering.py* : Donde seguimos con el resto del pipeline
  (vectorización, normalización, reducción de dimensionalidad y clustering)
- Por ultimo estan dispnibles los *pickle*. Son archivos donde estan guardados
  los distintos output acorde al cambio de los hiper-parametros (ie, clusters).
  El primer número representa la cantidad de clusters y el segundo número la
  cantidad de dimensiones.

  __Nota__: Seguir los pasos del archivo *install.txt* para poder abrir y
  explorar los distintos clusters.
