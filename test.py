import spacy

nlp = spacy.load("es_core_news_sm")
"""""
#lista de tokens
tokens = ["me","y","me","gustó"]

#tokens unidos 
texto = " ".join(tokens)

#Procesamos el texto con spacy
doc=nlp(texto)

#Guardamos los tokens lemmanizados
lista_tokens_lema=[token_lema.lemma_ for token_lema in doc]

#print("tokens procesados")
#print(lista_tokens_lema)

lista_tokens_no_repetidos=[]

for token in lista_tokens_lema:
    if token not in lista_tokens_no_repetidos:
        lista_tokens_no_repetidos.append(token)

#print(lista_tokens_no_repetidos)
tokens = [["me", "y", "me", "gustó"], ["Me", "Jugue", "muchisimo"]]

def process_tokens(lista_tokens):

    #Unimos la lista de tokens 
    texto = " ".join(lista_tokens)

    #Procesamos el texto con spacy
    processing_text=nlp(texto)

    #Creamos una lista nueva con los tokens procesados 
    lista_tokens_lema=[token_lema.lemma_ for token_lema in processing_text]

    #Creamos una lista vacia en donde guardaremos los tokens 
    lista_tokens_no_repetidos=[]

    for token in lista_tokens_lema:
        if token not in lista_tokens_no_repetidos:
            lista_tokens_no_repetidos.append(token)
    
    return lista_tokens_no_repetidos
"""

def process_tokens(lista_tokens):

    #Unimos la lista de tokens 
    texto = " ".join(lista_tokens)

    #Procesamos el texto con spacy
    processing_text=nlp(texto)

    #Creamos una lista nueva con los tokens procesados 
    lista_tokens_lema=[token_lema.lemma_ for token_lema in processing_text]

    #Creamos una lista vacia en donde guardaremos los tokens 
    lista_tokens_no_repetidos=[]

    for token in lista_tokens_lema:
        if token not in lista_tokens_no_repetidos:
            lista_tokens_no_repetidos.append(token)
    
    return lista_tokens_no_repetidos


#lista_token_procesados=[]
tokens = [["decia", "y", "me", "gustó"], ["Me", "Jugue", "muchisimo"]]


#for sublilista in tokens:
 #   lista_token_procesados.append(process_tokens(sublilista))

lista_token_procesados=[process_tokens(sublilista) for sublilista in tokens]
print(lista_token_procesados)




