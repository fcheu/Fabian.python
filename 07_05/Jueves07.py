import random, time
# num=random.randint(1,9)
# while abs(-3)!=num:
#     num=random.randint(1,9)
#     print (num)
#     time.sleep(1)

# n1=int(input("Ingrese el valor del limite inferior:"))
# n2=int(input("Ingrese el valor del limite superior:"))
# #validar que el limite superior sea mayor al limite inferior
# while n1>=n2:
#     print("Error, el limite superior debe ser mayor")
#     n2=int(input("Ingrese el valor del limite superior:"))
# num=random.randint(n1,n2)
# print(num)
    
#Realizar las clasificacion de peces
# Generar una candidad aleatoria de captura de peces
# entre 10 y 20
# Capturar peces y clasificarlos por su peso
# para saber como se venderan
# 800 grs o menos, a lata
# 801 grs o mas, a la plancha (max 3000)
# Contar cuando quedaron a la pancha y 
# cuantos quedatos para embasar en lata

# peces=random.randint(10,20)
# plancha=0
# lata=0
# print("Capturamos ", peces, "peces")
# time.sleep(2)
# for i in range(peces):
#     peso=random.randint(100,3000)
#     print("El peso del pez es de", peso)
#     if peso>800:
#         plancha+=1
#     else:
#         lata+=1
# print("La cantidad de peces a la plancha son:", plancha)
# print("La cantidad de peces a enlatar:", lata)

# Fabrica de enlatados
# Se necesita hacer el algoritomo de productos enlatados
# Se debe consultar el peso del producto( en gramos) ( solo valores positivos)
# El porcentaje de sodio en él ( solo valores entre 1 y 100)
# y si se va a vender nacional o internacionalmente
# Considerar los criterios en la siguiente tabla

# menos de 500 grs, lata normal
# 501 hassta 1500 bgr, lata mediana
# 1501 y mas , lata grande
# si el sodio es menos de 5%, lata queda igual
# si es entre 5% y 8% lata especial
# si tiene 9% o mas, lata acorazada
# a las latas internacionales, se le debe pegar 
# un sticker de validacion sanitaria

# Ej:800, 7%, 2==> lata mediana especial con sticker sanitario

peso=int(input("Ingrese el peso del producto en gramos:"))
while peso<=0: #ojo <=0 para validar que sea un numero positivo, pq le estoy diciendo que 
#mientras el numero sea menor o igual a 0 no puedo continuar
    print("Peso debe ser positivo")
    peso=int(input("Ingrese el peso del producto en gramos:"))
sodio=int(input("Ingrese el porcentaje de sodio del producto:"))
while sodio<1 or sodio>100: #escribo lo que no debe pasar para que luego en print pongo "error" o "fuera de rango"
    print("Porcentaje fuera del rango")
    sodio=int(input("Ingrese el porcentaje de sodio del producto:"))
venta=int(input("Venta: 1.- Nacional , 2.- Internacional:"))
while venta<1 or venta>2:
    venta=int(input("Venta 1.- Nacional , 2 Internacional:"))
#validaciones estan ya en el ejercicio

if peso<500:
    lata="Lata normal"
elif 500<peso<1501:
    lata="Lata mediana"
else:
    lata="Lata grande"

if sodio<5:
    sod=""
elif 5<sodio<=8:
    sod="especial" 
elif sodio>8:
    sod="acorazada"

if venta==1:
    sticker=""
else:
    sticker="con sticker sanitario"

print(lata,sod,sticker)




