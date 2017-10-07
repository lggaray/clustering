import spacy 
import numpy as np 
import nltk 
import re 
import pickle 
import sklearn 
from collections import defaultdict 
from nltk.corpus import stopwords 
 
 
nlp = spacy.load('es') 
 
 
with open("lavoztextodump.txt", "r") as f: 
    corpus = f.read() 
 
# Tokenizing 
tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle') 
raw = tokenizer.tokenize(corpus) 
 
#limpiando 
clean = [] 
for sent in raw: 
    a = re.sub(r'&#\w+;', '', sent) 
    b = re.sub(r'[^\w]', ' ', a) 
    c = b.rstrip().lstrip() 
    clean.append(c) 
 
#Para sacar las letras que quedaron colgadas al principio 
last_clean = [] 
for a in clean: 
    aux = a.split() 
    if len(aux) != 0 and len(aux[0]) == 1: 
        if aux[0] not in {'A', 'Y', 'O'}: 
            del aux[0] 
    last_clean.append(aux) 
 
#flatten list 
flat = [] 
for s in last_clean: 
    for w in s: 
        flat.append(w) 
 
 
#Aprovechamos que tenemos una lista de palabras para poder contar su ocurrencia 
count = defaultdict() 
for w in flat: 
    if w not in count: 
        count[w] = 1 
    else: 
        count[w] += 1 
 
 
#Ahora volvemos a unir las palabras a la oración que pertenecen 
final = [] 
for i,s in enumerate(last_clean): 
    a = ' '.join(last_clean[i]) 
    final.append(a) 
 
 
#Pasamos las oraciones pre-procesadas a Spacy 
parsed_sents = [] 
for doc in nlp.pipe(final, batch_size=10000, n_threads=8): 
    parsed_sents.append(doc) 
 
#diccionario con las triplas de cada palabra 
dicc_trip = dict() 
for s in parsed_sents: 
    for w in s: 
        tags = [(w.text, w.dep_, w.head.text)] 
        if str(w) not in dicc_trip: 
            dicc_trip[str(w)] = tags 
        else: 
            dicc_trip[str(w)] += (tags) 
 
#lista de listas con tuplas de la forma (palabra, Pos) 
pos = [] 
for s in parsed_sents: 
    aux=[] 
    for w in s: 
        aux.append((w, w.pos_)) 
    pos.append(aux) 
 
 
 
for key, value in dicc_trip.items(): 
    aux = [] 
    for fst,snd,trd in value: 
        a = snd+'.'+trd 
        aux.append(a) 
        dicc_trip[key] = aux 
 
 
# Lista de etiquetas para cada oración 
tag_sents = [[(token.text,token.tag_,token.pos_) for token in parsedEx] for parsedEx in parsed_sents] 
 
 
tags_clean = [] 
for i,a in enumerate(tag_sents): 
    for fst,snd,trd in a: 
        aux = snd.split("|") 
        tgs = [] 
        for x in aux: 
            y = x.split("=") 
            if len(y) == 1: 
                tgs.append(y[0]) 
            else: 
                tgs.append((y[0], y[1])) 
        tags.append((fst, tgs, trd)) 
 
clean_info_word = [] 
for a in tag_sents: 
    for fst,snd,trd in a: 
        aux = snd.split("|") 
        clean_info_word.append((fst,aux,trd)) 
 
 
 
dicc_forward = defaultdict(list) 
dicc_backward = defaultdict(list) 
for tup in pos: 
    for j,(fst,snd) in enumerate(tup): 
        if j != 0: 
            dicc_backward[fst.text].append((tup[j-1][0].text, tup[j-1][1])) 
        else: 
            dicc_backward[fst.text].append(("[W.Start]", "[T.Start]")) 
        if j != len(tup)-1: 
            dicc_forward[fst.text].append((tup[j+1][0].text, tup[j+1][1])) 
        else: 
            dicc_forward[fst.text].append(("[W.End]", "[T.End]")) 
 
 
#lematizado 
lemma_dict = defaultdict(str) 
with open('lemmatization-es.txt') as f: 
    for line in f: 
        splited_line = line.split('\t') 
        lemma_dict[splited_line[1].strip()] = splited_line[0] 
 
 
def lemmatize(word): 
   return lemma_dict.get(word, word)  
 
 
#Creando el diccionario 
dicc = dict()
for fst,snd,trd in clean_info_word:
    features = defaultdict(int)
    pos = 'PoS__' + trd
    if fst.isalpha() and lemmatize(fst) not in dicc and fst in count and count[fst] > 50 and fst not in stopwords.words('spanish'):
        dicc[lemmatize(fst.lower())] = features
        features[pos] = 1
        for i in snd:
            features[i] = 1
        for i in dicc_trip[fst]:                 #diccionario de triplas
            features[i] = 1
        for i in dicc_backward[fst]:
            features[i[0]+"-1"] += 1
            features[i[1]+"-1"] += 1
        for i in dicc_forward[fst]:
            features[i[0]+"+1"] += 1
            features[i[0]+"+1"] += 1


    elif lemmatize(fst) in dicc:                        #la palabra ya se encuentra -> actualizo el dicc
        has_it = dicc[lemmatize(fst)]
        if pos in has_it:
            has_it[pos] += 1
        else:
            has_it[pos] = 1
        for tag in snd:
            if tag in has_it:
                has_it[tag] += 1
                has_it[tag] = 1
                has_it[tag] = 1


#Ahora preparamos la lista una lista de diccs para vectorizar
#Tambien vamos a guardar las palabras que vamos a vectorizar para poder recuperarlas mas tarde
lista_para_vectorizar = []
check_list = []
for key, value in dicc.items():
    check_list.append(key)
    lista_para_vectorizar.append(value)

file_name = "dicc_features"
with open(file_name, 'wb') as f:
    pickle.dump(lista_para_vectorizar, f)

file_Name = "check_list"
with open(file_Name, 'wb') as f:
    pickle.dump(check_list, f)
