from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from collections import defaultdict
import pickle
import sklearn

with open('check_list', 'rb') as f:
    check_list = pickle.load(f)

with open('dicc_features', 'rb') as g:
    lista_para_vectorizar = pickle.load(g)


#Vectorizado
v = DictVectorizer()
X = v.fit_transform(lista_para_vectorizar)

#Normalización

Y = sklearn.preprocessing.normalize(X)


#Reducción de dimensionalidad
svd = TruncatedSVD(n_components=300, n_iter=7, random_state=42)
svd.fit_transform(Y)


#Clustering

km = KMeans(n_clusters=80, random_state=0)
km.fit(Y)


labels = km.predict(Y)

#Clusters obtenidos
clusters = defaultdict(set)
for i, label in enumerate(labels):
    clusters[label].add(check_list[i])
#print(clusters)


file_name = "dicc_cluster"
with open(file_name, 'wb') as h:
    pickle.dump(clusters, h)
