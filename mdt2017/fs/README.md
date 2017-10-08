# Práctico de feature selection

### Introducción

La idea de este práctico es hacer *feature selection* con métodos supervisados.
Para esta tarea se utilizó el [wikicorpus](https://cs.famaf.unc.edu.ar/~ccardellino/resources/wikicorpus/es/) parseado y con codificación utf-8 de *Cristian Cardellino*.

### Proceso
* Sampleo del corpus:

Para realizar el sampleo aleatorio siemplemente se tomaron las primeras 150k lineas del archivo *wikicorpus_01* (limitado por la capacidad de la máquina). El archivo estaba dividido por artículos, y a su vez también dividido por palabras. Cada artículo correspondía a una sección diferente a la del artículo anterior, por esta razón solo bastó tomar todas las lineas posibles, ya que el sampleo sería "aleatorio".
* Descripción del corpus anotado:

Cada linea del wikicorpus es del estilo:

>Juega jugar VMM02S0 00727813

Definido de la siguiente manera:

    1.Palabra

    2.Lema

    3.Pos tag

    4.Synset

    
* Descripción del corpus NO anotado:

Como corpus no anotado se utilizó el mismo del práctico uno, es decir, articulos del diaron *La Voz del Interior*.
La organización de este archivo es simple: cada artículo era separado por un guión medio(-), luego, la primera linea anunciaba el título del artículo, mientras que la segunda era el artículo en si, el cual se encontraba descripto en solo una linea.

* Librerías utilizadas:
    - __SKlearn__: *"Simple and efficient tools for data mining and data analysis"*
    La gran mayoría de herramientas utilizadas fueron obtenidas de esta librería. Entre estas herramientas tenemos:
        - *DictVectorizer*: "Transforms lists of feature-value mappings to vectors." Este método fué utilizado para transformar nuestro diccionario de features en una matriz.
        - *Normalize*: "Scale input vectors individually to unit norm (vector length)." Este método fué utilizado para normalizar nuestra matriz.
        - *SelectKBest*: "The SelectKBest class just scores the features using a function and then removes all but the k highest scoring features". Método utilizado para la selección de features supervisada.
        - *KMeans*: Algortimo encargado del clustering.
    - __NLTK__: "NLTK is a leading platform for building Python programs to work with human language data." Esta herramiente fué utilizada solo para eliminar las *stopwords* de nuestro corpus.
    - __DefaultDict__: Diccionarios optimizados en Python.
    - __Islice__: Utilizada para tomar las primeras *N* lineas del archivo.
    - __Spacy__: Libreria MUY útil para *PLN*. Utilizada por el método *NO supervisado* para obtener tags, Pos tags y triplas de dependencia.


* Técnica supervisada de feature selection:

Como bien se mencionó antes, utilizamos una de las funciones de __sklearn__, [SelectKBest](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest).
Como función de clasificación se eligió [chi2](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html#sklearn.feature_selection.chi2). Y como cantidad de features(*K*) se eligió el 70% de las features totales.
* Técnica no supervisada de feature selection:

Como se describió en el informe del práctico 1, para feature selection no supervisada se utilizó tambien una función de __sklearn__, en particular [TruncatedSVD](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html) (aka LSA). Como cantidad de dimensiones se comenzó provando con 100 y se llego hasta 500. A modo prueba y error, se llegó a la conclusión que 300 dimensiones devolvía el mejor resultado.

* Discusión cualitativa:

Algunos de los clusters obtenidos usando como clase el sentido de la palabra:
>{'granada', 'manchester', 'céspedes', 'parís', 'downingtown', 'cayo', 'putumayo', 'tlalpan', 'tlaltizapán', 'stuttgart', 'utc', 'viena', 'manila', 'vancouver', 'jacksonville', 'alabama', 'bacadéhuachi', 'haarlem', 'newcastle', 'glasgow', 'copenhague', 'gama', 'reinosa', 'álamos', 'zacatecas', 'bethesda', 'chicago', 'leeds', 'bristol', 'asturias', 'ibanez', 'londres', 'hamburgo', 'berlin', 'palmyra', 'estocolmo', 'oxford', 'envigado'}

>{'nuevamente', 'brillantemente', 'completamente', 'absolutamente', 'bastante', 'sumamente', 'frecuentemente', 'solamente', 'empty', 'biológicamente', 'automáticamente', 'dramáticamente', 'naturalmente', 'obviamente', 'prácticamente', 'drásticamente', 'esencialmente', 'temporalmente', 'mayoritariamente', 'bien', 'tan', 'usualmente', 'popularmente', 'históricamente', 'flood', 'fácilmente', 'constantemente', 'extremadamente', 'quizás', 'oficialmente', 'altamente', 'aparentemente', 'típicamente', 'totalmente', 'formalmente'}

>{'enterrar', 'equipar', 'elaborar', 'preclasificado', 'remover', 'traspasar', 'transferir', 'emigrar', 'decorar', 'obsesionar', 'firmar', 'asignar', 'reconstruir', 'idear', 'editar', 'manchar', 'amurallar', 'prohibir', 'conocer', 'elevar', 'diseñar', 'reclamar', 'comprar', 'concebir', 'armar', 'atrapar', 'rodar', 'apropiar', 'nombrar', 'herir', 'elogiar', 'apasionar', 'acoplar', 'adiestrar', 'condenar', 'contratar', 'sobrevivir', 'encarcelar', 'seleccionar', 'acuñar', 'involucrar', 'reorganizar', 'asustar', 'confirmar', 'solicitar', 'curvar', 'cesar', 'galardonar', 'relacionar', 'presionar', 'inaugurar', 'fusilar', 'filmar', 'lanzar', 'registrar', 'cerrar', 'promulgar', 'conceder', 'poblar', 'esparcir', 'confundir', 'sepultar', 'vestir', 'escoger', 'citar', 'catalogar', 'mezclar', 'crecer', 'emplear'}

>{'enorme', 'consecuente', 'simple', 'implacable', 'frágil', 'alucinante', 'grave', 'doble', 'breve', 'consiguiente', 'impresionante', 'sugerente', 'sublime', 'brutal', 'agradable', 'cuádruple', 'notable', 'gran', 'sutil', 'inusual'}

>{'rival', 'humanista', 'esquimal', 'aspirante', 'guionista', 'moralista', 'alienígenas', 'artista', 'not', 'portavoz', 'interfaz', 'congresista', 'novelista', 'habitante', 'punta', 'fabricante', 'piloto', 'atleta', 'ninja', 'but', 'guía', 'jinete', 'mar', 'policía', 'inmigrante', 'estudiante', 'element', 'defensa', 'agente', 'guitarrista', 'tenista', 'testigo', 'azúcar', 'cliente', 'solista', 'fan', 'cantante', 'periodista', 'amante', 'líder', 'futbolista', 'adolescente', 'juez', 'protagonista', 'aprendiz', 'batería'}

-   Podemos observar que estos clusters están formados por grupos de sustantivos, adjetivos, verbos, sustantivos propios, etc.

Algunos de los clusters obtenidos usando como clase el PoS tag de la palabra:

>{'pastilla', 'píldoras', 'píldora', 'tableta'}

>{'debían', 'debió', 'deberían', 'deberá', 'debe', 'deben', 'debería', 'debía'}

>{'ocupan', 'pobladas', 'ocuparon', 'ocupados', 'vivieron', 'poblados', 'ocupa', 'ocupar', 'ocupó', 'ocupado', 'habitado', 'vivió', 'ocupadas', 'viven'}

>{'llamando', 'llamaron', 'llaman', 'llamar', 'llamaban', 'llamado', 'llamó', 'llamadas', 'llamados'}

>{'encontraron', 'observó', 'encontró', 'encontraba', 'descubrieron', 'encontraban', 'encontrar', 'observan', 'observar', 'observa', 'encuentra', 'descubren', 'descubriendo', 'descubre', 'encuentran', 'descubrió', 'encontrará'}

>{'usaba', 'utilizando', 'usado', 'usa', 'usada', 'USA', 'usar', 'use', 'utilizaba', 'emplea', 'utilizaron', 'empleado', 'usan', 'usando', 'utilizada', 'usaban', 'usados', 'utilizado', 'utiliza', 'utilizan', 'utilizó', 'utilizar'}

>{'Bachelor', 'north', 'Art', 'Hour', 'Way', 'east', 'empty', 'implementation', 'west', 'end', 'Because', 'south', 'Sephardim', 'Proceedings', 'Old', 'Journal'}

-   Podemos obvservar que en estos clusters los grupos son formados por una palabra, distintas conjugaciones de la misma y sinónimos.

    *Nota*: Teniendo en cuenta los resultados obtenidos, podemos deducir que nuestro corpus quedó chico para este método, ya que quedaron clusters chicos, de la forma que acabamos de mencionar, y el resto son clusters más grandes donde el agrupamiento parece no tener sentido. Es decir, necesitamos un corpus significativamente más grande para poder formar más clusters con sentido. 

Primer comentario a tener en cuenta es que para el método que utiliza como clase el sentido, se utiliza una *check_list* (lista utilizada para recuperar las palabras despues de ser llevadas a un espacio vectorial) con los lemas de las palabras, mientras que en el método que utiliza como clase el PartofSpeech tagging (PoS tagging), ésta *check_list* esta compuesta por las palabras en si (no los lemas).
En segundo lugar, podemos observar (teniendo en cuenta lo dicho anteriormente) que hay una clara diferencia en el resultado dependiendo de la clase que utilicemos. Por un lado tenemos una agrupamiento más morfosintáctico (synset) y por otro lado un agrupamiento mas semántico (PoS tag).

### Conclusión

* Si lo que buscamos es un __agrupamiento morfosintáctico__, entonces deberiamos utilizar como clase el __sentido de la palabra__.
* Si lo que buscamos es un __agrupamiento semántico__, entonces deberíamos utilizar como clase el __PartofSpeech tagging__.

Finalmente, abstrayendonos de los corpus utilizados, tanto para el *método supervisado* como para el *no supervisado*, podemos concluir en que éste último es más general, es decir, más útil para la exploración de datos, ya que, como vimos en el práctico 1, podemos obtener clusters tanto morfosintácticos como semánticos (siempre y cuando utilicemos como check_list las palabras y no el lema). Por otro lado, el *método supervisado* es más específico, es decir, podemos elegir la clase de acuerdo a nuestra necesidad, lo cuál tiene sentido ya que tenemos un resultado al cual queremos llegar y/o comparar.
