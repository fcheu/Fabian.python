#Pregunte al usuaio su nombre y muestre sus letras, y su cantidad de letras
name=input("Ingrese su nombre:")
cont=0
vocales=0
cons=0
for i in name: 
    print(i)
    cont=cont+1
    if i in "aeiouAEIOU": 
        vocales=vocales+1
    elif i ==" ":
         cont-=1
    else: 
        cons=cons+1
print ("El total de letras es :", cont, ", la cantidad de vocales son: ", vocales, "y la cantidad de consonantes son: ", cons)

# Preguntar cantidad de votantes
# Poner los dos candidatos: Dexter / Samurai Jack
# Preguntar en cada iteracion, por quien votara 
# Mostrar al final quien gano la votacion

print("Cuantos votantes son: ")
v1=0
v2=0
voto=print()
for i in voto:
    print ('''
           ¿Por quien votará? 
           1.- Dexter
           2.- Samurai Jack
           ''')
    if voto in "Dexter":
        v1=v1+1
    else:
        v2=v2+1
