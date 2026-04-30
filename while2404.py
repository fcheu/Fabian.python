#Ejemplo y uso de while clase 2404
# cont=1
# while cont<=3:
#     print(f"Contador{cont}")
#     cont+=1

#Para comentar todo es ctrl + cierre de llave (al lado del enter)

# pin=3535

# code=int(input("Ingrese su pin: "))

# while pin!=code:
#     print("Error, intente otra vez")
#     code=int(input("Ingrese su pin: "))
# print("Pin correcto")

#Usando while pida al usuario un numero
#y muestre su tabla de multiplicar hasta el 10 

# num=int(input("Ingrese un numero: "))
# cont=1
# while cont<=10:
#     print(f"{num}x{cont}={num*cont}")
#     cont+=1

# #profe:
# num=int(input("Ingrese un numero: "))
# c=1
# while c<=10:
#     print(f"{num}x{c}={c*num}") #0 print(num + c "=" num * c)
#     c+=1 
# op=0
# total=0
# while op!=4:
#     print("Seleccione un producto:")
#     print("1.- PC Ryzen $800.000")
#     print("2.- LGTV 55 Pulgadas $450.000")
#     print("3.- Parlante JBL Pure Sound $90.000")
#     print("4.- Salir")
#     op=int(input())
#     match op:
#         case 1:
#             print("Tiene que pagar", 800000*1.19)
#             total+=800000*1.19
#         case 2:
#             print("Tiene que pagar", 450000*1.19)
#             total+=450000*1.19
#         case 3: 
#             print("Tiene que pagar", 90000*1.19)
#             total+=90000*1.19
#         case 4: 
#             print("Saliendo")
#             print(f"El total a pagar con IVA ES {round(total,2)}")
#         case _:
#             print("Opción inválida")

#calculadora:
# def suma():
#     n1=int(input("Ingrese su numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1+n2}")
# def resta():
#     n1=int(input("Ingrese su numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1-n2}")
# def multi():
#     n1=int(input("Ingrese su numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1*n2}")
# def divi():
#     n1=int(input("Ingrese su numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1/n2}")
# op=0
# while op!=5:
#     print("1.- Sumar")
#     print("2.- Restar")
#     print("3.- Multiplicar")
#     print("4.- Dividir")
#     print("5.- Salir")
#     op=int(input("Seleccione una operacion:"))
#     match op:
#         case 1:
#             suma()
#         case 2: 
#             resta()
#         case 3:
#             multi()
#         case 4: 
#             divi()
#         case 5: 
#             print("Saliendo")
#         case _: 
#             print("Opcion invalida")

#Seleccionar 3 programas que ya hemos hecho
#convertirlos en funcion
#ponerlos en un menu 
#y llamarlos desde su nombre

# def passw():
#     passw="shazam"
#     palabra=input("Ingrese su clave: ").lower()
#     if passw==palabra:
#         print ("Clave correcta")
#     else:
#         print("Clave invalida")
# def calculadora():
#     def suma():
#         n1=int(input("Ingrese su numero: "))
#         n2=int(input("Ingrese otro numero: "))
#         print(f"El resultado es {n1+n2}")
#     def resta():
#         n1=int(input("Ingrese su numero: "))
#         n2=int(input("Ingrese otro numero: "))
#         print(f"El resultado es {n1-n2}")
#     def multi():
#         n1=int(input("Ingrese su numero: "))
#         n2=int(input("Ingrese otro numero: "))
#         print(f"El resultado es {n1*n2}")
#     def divi():
#         n1=int(input("Ingrese su numero: "))
#         n2=int(input("Ingrese otro numero: "))
#         print(f"El resultado es {n1/n2}")
#     op=0
#     while op!=5:
#         print("1.- Sumar")
#         print("2.- Restar")
#         print("3.- Multiplicar")
#         print("4.- Dividir")
#         print("5.- Salir")
#         op=int(input("Seleccione una operacion:"))
#         match op:
#             case 1:
#                 suma()
#             case 2: 
#                 resta()
#             case 3:
#                 multi()
#             case 4: 
#                 divi()
#             case 5: 
#                 print("Saliendo")
#             case _: 
#                 print("Opcion invalida")
# def vocales():name=input("Ingrese su nombre:")
    # cont=0
    # vocales=0
    # cons=0
    # for i in name: 
    #     print(i)
    #     cont=cont+1
    #     if i in "aeiouAEIOU": 
    #         vocales=vocales+1
    #     elif i ==" ":
    #         cont-=1
    #     else: 
    #         cons=cons+1
    # print ("El total de letras es :", cont, ", la cantidad de vocales son: ", vocales, "y la cantidad de consonantes son: ", cons)
# op=0
# while op!=4:
#     print("Seleccione una opcion:")
#     print("1- Password")
#     print("2.- Calculadora")
#     print("3.- Vocales")
#     print("4.- Salir")
#     op=int(input())
#     match op:
#         case 1:
#             passw()
#         case 2:
#             calculadora()
#         case 3:
#             vocales()
#         case 4: 
#             print("Saliendo")
#         case _:
#             print("Opcion invalida")

#votatoon
# toon1=input("Ingrese el toon 1:")
# toon2=input("Ingrese el toon 2:")
# v1=0
# v2=0
# cant=int(input("¿Cuantos votantes son?:"))
# while cant>0:
#     voto=int(input(f"¿Por quien votará? 1.- {toon1} 2.- {toon2} "))
#     if voto==1:
#         v1+=1
#     elif voto==2:
#         v2+=1
#     else: 
#         print("Voto nulo")
#     cant-=1
# if v1>v2:
#     print(f"Ganó {toon1} con {v1} votos")
# elif v2>v1:
#     print(f"Ganó {toon2} con {v2} votos")
# else:

#     print("Hubo un empate")

import random

dado1=(random.randint(1,6))
dado2=(random.randint(1,6))
print("El primer dado salió", dado1)
print("El segundo dado salió", dado2)
if dado1==dado2:
    print("Va a la cárcel")
else:
    print("Avanza")
