# Practico de clustering

### Introducción 
La intención de este práctico es poder comprender y construir un pipeline para hacer clustering. 
El corpus utilizado para esta tarea fue el de La Voz del Interior.

### Pipeline
1) *Pre-procesamiento:*

El pre-procesamiento del corpus fué lo más trabajoso. En primer lugar, se debe leer el archivo para ver como se encuentra organizado, y en base a eso determinar de que manera se deben tratar los textos. Teninedo esto en cuenta, se avanza con el tokenizado del texto, usando la libreria __nltk__. De esta manera, nuestro corpus ahora es una lista de oraciones. Luego, con ayuda de la libreria __re__ se utilizan *expresiones regulares* para deshacerse de caracteres no necesarios para esta tarea. Dejando una lista de oraciones limpia, lista para pasar a la siguiente etapa.

2) *Diccionario de features:* 

Los tipos de features utilizados fueron:
    - Lema de la palabra
    - POS tag de la palabra
    - Si palabra comienza con mayúscula o no
    - Palabra anterior
    - Tag de la palabra anterior
    - Palabra siguiente
    - Tag de la palabra siguiente
    
    Para lematizar, se utilizo [este](http://www.lexiconista.com/datasets/lemmatization/) diccionario, extraído de la pagina __lexiconista__.
    Para el POS tag se utilizó [StanfordPOSTagger](http://www.nltk.org/_modules/nltk/tag/stanford.html) de la librería __nltk__.
    Para obtener tag y palabra anterior/siguiente se implementó una función propia.
    
    Luego de obtener esta información, se procede al armado de una lista de diccionarios, donde cada uno correspondia a los features de determinada palabra.



3) *Vectorización:*

    Para realizar esta tarea, en un primer momento se utilizó __word2vect__ de la libreria [gensim](https://radimrehurek.com/gensim/models/word2vec.html).
    Pero luego de un par de intentos de clustering, se podía observar que varios clusters carecían de sentido y los *hiperparámetros* que se podían modificar no impactaban mucho en el resultado final. Esto se debe, principalmente, a que el mismo algoritmo, de alguna forma, seleccionaba los features, es decir, no se tenía control sobre ellos.
    
    Teniendo en cuenta esto, se procedió a la utilización de la función __DictVectorizer__ de la libreria [sklearn](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html), en la cual es posible poder elegir los tipos de features que queremos que se tengan en cuenta.
    
4) *Reducción de dimensionalidad:*

Para poder reducir dimensiones utilicé __TrucatedSVD__ de la libreria [sklearn](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html). 
Se probaron dimensiones en un rango de 100 a 500.

5) *Clustering:*

En un principio se intentó implementar el algoritmo __KMeans__, pero luego, al compararlo con el que ya se encuentra implementado en libreria __sklearn__, se llegó a la conclución de que la implementación realizada no era muy buena. Finalmente, para la tarea de clusterizado utilizó [KMeans](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) ya implementado.
Se comenzó probando de a 10 clusters y así se fué avanzando hasta llegar a 40, donde los clusters que se forman tienen bastante sentido.

# Output
A continuación presentaré algunos de los clusters formados.
*Nota: El input es UNA PARTE del corpus, no es el corpus completo.*

>{'Clara', 'Coordinadora', 'Alejandro', 'Gobierno', 'María', 'Martínez', 'Nicolás', 'Somos', 'Ipem', 'Ministerio', 'Ateneo', 'Isabel', 'Villa', 'Fábrica', 'Deán', 'Rodolfo', 'Cornú', 'Pedro', 'Manuel', 'Jerónimo'}

En este cluster podemos observar que se agrupan __entidades__ (nombres propios).
*Nota: Hay varias entidades que quedan fuera del cluster*.

>{'fue', 'se', 'molestan', 'vino', 'sostiene', 'ya', 'llevan', 'calificaron', 'levantaban', 'en', 'han', 'están', 'mantiene', 'les', 'anticipa', 'ver', 'sea', 'abrimos', 'vivimos', 'más'}

En este cluster podemos observar que se agrupan __verbos__.

>{'se', 'Los', 'le', 'Me', 'lo', 'les', 'te', 'nos', 'los', 'la', 'me'}

En este cluster podemos observar que se agrupan __pronombres personales__.
Observar que al no sacar las *stopwords* se forma este tipo de clusters.

>{'o', 'pero', 'y'}

En este cluster podemos observar que se agrupan __conectores__.

>{'radio', 'felicidad', 'reclamo', 'entrada', 'pasión', 'misma', 'vida', 'anteproyecto', 'normativa', 'medida', 'unidad', 'toma', 'tiempo', 'secreto', 'luna', 'muerte', 'duración', 'forma', 'mujer', 'edad', 'tormenta', 'ley'}

En este cluster podemos observar que se agrupan __sustantivos__.

>{'fue', 'fueron', 'es', 'Somos', 'son', 'sido', 'somos', 'ser'}

Por último, quería mostrar este cluster ya que me pareció muy interesante. Podemos obvservar que son todas conjugaciones del verbo __ser__. Esto se debe a que utilizo como feature el lema, pero a la hora de relacionar el vector con la palabra original, esta última no se encuentra lematizada.

*Nota: Estós clusters fueron los que quedaron mejor formados luego de jugar mucho con la cantidad de dimensiones y el número de clusters*.

# Conclusión

Finalmente podemos observar que los clusters quedaron formados *relativamente* bien, utilizando 300 dimensiones y 40 clusters. 
De igual forma, estos resultados podrían mejorar significativamente al agregar *triplas de dependencia* como un tipo de feature extra. 
Como parte del siguiente práctico, se implementarán dichas triplas y luego se realizará __feature selection__.
