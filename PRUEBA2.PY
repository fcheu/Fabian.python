import random, time
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
# lata=0
# plancha=0
# print("Capturamos ", peces, "peces")
# for p in range(peces):
#     peso=random.randint(100,3000)
#     print("El peso del pz es de", peso)
#     if peso>800:
#         plancha+=1
#     else:
#         lata+=1
# print("Los peces enlatados son:", lata)
# print("Los peces a la plancha son:", plancha)



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

# peso=int(input("Ingrese el peso del producto en gramos:"))
# while peso<1:
#     print("Debe ser un número positivo")
#     peso=int(input("Ingrese el peso del producto en gramos:"))
# sodio=int(input("Ingrese el porcentaje de sodio del producto:"))
# while 1>sodio or sodio>100:
#     print("El porcentaje debe estar entre 1 y 100")
#     sodio=int(input("Ingrese el porcentaje de sodio del producto:"))
# venta=int(input("Venta: 1.- Internacional 2.- Nacional :"))
# while venta<1 or venta>2:
#     venta=int(input("Venta: 1.- Internacional 2.- Nacional :"))

# time.sleep(2)

# if peso<500:
#     lata="lata normal"
# elif 501<peso<1500:
#     lata="lata mediana"
# else:
#     lata="lata grande"

# if sodio<5:
#     sod=""
# elif sodio<5<8:
#     sod="lata especial"
# else: 
#     sod="lata acorazada"

# if venta==1:
#     sticker="sticker de validacion sanitaria"
# else:
#     sticker=""

# print(lata, sod, sticker)

#Ejercicio 1 — Clasificación de frutas

# Una empresa exportadora necesita clasificar cajas de frutas.

# Generar una cantidad aleatoria de cajas entre 8 y 15.
# Por cada caja se debe ingresar:
# Peso de la caja en kilos.
# El peso puede ser un valor absoluto
# Clasificar:
# 10 kilos o menos → caja pequeña
# Entre 11 y 25 kilos → caja mediana
# Más de 25 kilos → caja grande
# Contar:
# Cuántas cajas pequeñas hubo.
# Cuántas medianas.
# Cuántas grandes.

# caja=random.randint(8,15)
# caj1=0
# caj2=0
# caj3=0
# print("La cantidad de cajas son:", caja)
# for i in range(caja):
#     peso=int(input("Ingrese el peso de la caja en kilos:"))
#     print("El peso de la caja es de ", abs(peso))
#     if peso<=10:
#       caj1+=1
#     elif peso<=25:
#        caj2+=1
#     else:
#        caj3+=1

# print("Tenemos un total de", caj1, "cajas pequeñas,", caj2, "cajas medianas y", caj3, "cajas grandes")

# Ejercicio 2 — Control de equipaje en aeropuerto

# Un aeropuerto necesita revisar el peso de maletas.

# Por cada pasajero se debe ingresar:

# Peso de la maleta.
# El peso puede venir negativo por falla del sistema, por lo que debe corregirse usando abs().
# Tipo de vuelo:
# 1 = Nacional
# 2 = Internacional

# Clasificación:

# Hasta 15 kg → Equipaje liviano
# 16 a 25 kg → Equipaje normal
# Más de 25 kg → Equipaje pesado

# Además:

# Si es internacional, agregar “con revisión aduanera”.

# personas=random.randint(1,50)
# for p in range(personas):
#     peso=int(input("Ingrese el peso de su maleta:"))
#     peso=abs(peso)
#     vuelo=int(input("Su vuelo es: 1.- Nacional 2.- Internacionnal"))
#     while vuelo<1 or vuelo>2:
#         print("Ingrese el numero correcto")
#         vuelo=int(input("Su vuelo es: 1.- Nacional 2.- Internacionnal"))
#     if peso<15:
#         print("Equipaje liviano")
#     elif peso<=25:
#         print("Equipaje normal")
#     else peso>25:
#         print("Equipaje pesado")
    
#     if vuelo==2:
#         print("Con revision aduanera")
    
# Ejercicio 3 # — Control de temperatura de alimentos

# Una fábrica necesita controlar productos congelados.

# Generar una cantidad aleatoria de productos entre 5 y 12.
# Por cada producto ingresar:
# Temperatura registrada.
# Puede venir negativa o positiva, pero se debe trabajar con el valor absoluto usando abs().

# Clasificación:

# 0 a 10 grados → Producto frío
# 11 a 20 grados → Producto templado
# Más de 20 grados → Producto caliente

# Contar:

# Cuántos productos quedaron en cada categoría.

# produ=random.randint(5,12)
# frio=0
# templa=0
# cal=0
# print("El total de productos es", produ)
# for p in range(produ):
#     temp=int(input("Ingrese la temperatura registrada:"))
#     temp=abs(temp)
#     if 0<temp<=10:
#         print("Producto frio")
#         frio+=1
#     elif 11<=temp<=20:
#         print("Producto templado")
#         templa+=1
#     else:
#         print("Producto caliente")
#         cal+=1

# print("Existen ", frio, "productos frios", templa, "productos templados y", cal, "productos calientes")

# Ejercicio 4 #— Empresa de delivery

# Una empresa de delivery necesita clasificar pedidos según distancia.

# Se debe ingresar:

# Distancia recorrida.
# La distancia puede ingresarse negativa por error, usar abs().

# Clasificación:

# Hasta 3 km → Pedido cercano
# 4 a 10 km → Pedido normal
# Más de 10 km → Pedido lejano

# Además:

# Preguntar tipo de envío:
# 1 = Express
# 2 = Normal

# distancia=int(input("Ingrese la distancia recorrida:"))
# distancia=abs(distancia)

# if distancia<=3:
#     ped="pedido cercano"
# elif 4<=distancia>=10:
#     ped="pedido normal"
# else:
#     ped="pedido lejano"

# tipo=int(input("Tipo de envio: 1.- Express 2.-Normal "))
# while tipo<1 or tipo>2:
#     print("Seleccione el numero correcto")
#     tipo=int(input("Tipo de envio: 1.- Express 2.-Normal "))

# if tipo==1:
#     env="con prioridad"
# else:
#     env=""
# print("La distancia es de", distancia," y es un", ped,env)

# Ejercicio 5 #— Clasificación de botellas recicladas

# Una planta recicladora necesita clasificar botellas según peso.

# Generar aleatoriamente una cantidad de botellas entre 20 y 30.
# Ingresar peso de cada botella en gramos.
# El peso puede venir negativo, corregir usando abs().

# Clasificación:

# Menos de 250 gr → Botella liviana
# Entre 250 y 600 gr → Botella estándar
# Más de 600 gr → Botella pesada

# Contar cuántas hubo de cada tipo.

bottle=random.randint(20,30)
print("La cantidad de botellas son ", bottle)
bot1=0
bot2=0
bot3=0
for i in range(bottle):
    peso=int(input("Ingrese el peso en gramos"))
    peso=abs(peso)
    if peso<=250:
        print("Botella liviana")
        bot1+=1
    elif 250<peso<=600:
        print("Botella estándar")
        bot2+=1
    else:
        print("Botella pesada")
        bot3+=1

print("La cantidad de botellas livianas es de", bot1,"las estandar son", bot2, "y las pesadas son", bot3)

# Ejercicio 6 #— Sistema de notas corregidas

# Un profesor necesita corregir notas mal ingresadas.

# Por cada alumno ingresar:

# Nota.
# Si la nota viene negativa, usar abs() para corregirla.

# Clasificación:

# Menor a 40 → Reprobado
# Entre 40 y 59 → Aprobado
# 60 o más → Destacado

# Además:

# Preguntar asistencia:
# 1 = Completa
# 2 = Incompleta