# -*- coding: utf-8 -*-
"""
@author: christian
"""

count = 0 
wordlist = []

def leer_archivo():
    archi=open('texto.txt','r', encoding='latin1')
    lineas=archi.read()
    archi.close()
    return lineas


texto = leer_archivo()
texto = texto.strip()
texto = texto.split()


for word in texto:
    word = word.lower()
    if word == "harry,":
        word = "harry"
    if word == "harry.":
        word= "harry"
    if word == "harry":
        count = count + 1
print('Harry', count)
totalwords = len(texto)
print('Total de palabras:',totalwords)

    
    

