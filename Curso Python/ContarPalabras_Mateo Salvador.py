#Mateo Salvador GR1
#Lectura de palabras texto Harry Potter
h=0
p=0
def leer():
    archi=open('C:/Users/Mateo/Jupiter ALDA/Procesamiento/Curso_Python/Curso Python/texto.txt','r', encoding='latin1')
    lineas=archi.read()
    archi.close()
    return lineas
texto = leer()
texto = texto.strip()
texto = texto.split()
for palabra in texto:
    palabra = palabra.lower()
    if palabra == "harry,":
        palabra = "harry"
    if palabra == "harry.":
        palabra= "harry"
    if palabra== "harry":
        h = h + 1
for palabra in texto:
    palabra = palabra.lower()
    if palabra == "potter,":
        palabra = "potter"
    if palabra == "potter.":
        palabra= "potter"
    if palabra== "potter":
        p = p + 1
print('Harry', h)
print('Potter', p)