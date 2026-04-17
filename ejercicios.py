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
        print(" ")
    else: 
        cons=cons+1
print ("El total de letras es :", cont, ", la cantidad de vocales son: ", vocales, "y la cantidad de consonantes son: ", cons)