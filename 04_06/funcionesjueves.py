# def saludo ():
#     print ("Hola Zelda")
# name="Link"
# def chao():
#     print ("Chao", name)

# def suma():
#     n1=int(input("Inrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1+n2}")


''' Puede tener algo entre parentecis como puede no tenerla
si no ponemos algo entre parentesis es sin retorno
'''
#create 
#read
#update
#delete

# def sumaRet():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     return n1+n2
# res=sumaRet()*4
# print("El resultado es", res)

#Con argumento y sin retorno

# def SaludoMe(name):
#     print("Hola", name)

# SaludoMe("Ganon")

# def mitadPrecio(precio):
#     print("el precio es", precio/2)

# pre=sumaRet()
# mitadPrecio(pre)

#Con argumento y con retorno

# def sumaRetArg(n1,n2):
#     return n1+n2
# n1=int(input("Inrese un numero: "))
# n2=int(input("Ingrese otro numero: "))
# print ("El resultado de la suma es", sumaRetArg(n1,n2))

#Crear una calculadora para las 4 operaciones
#basicas usando funciones. Estas deben tener argument y return 

# def suma(n1, n2):
#     return n1 + n2

# def resta(n1, n2):
#     return n1 - n2

# def multiplicacion(n1, n2):
#     return n1 * n2

# def division(n1, n2):
#     return n1 / n2

# print("1.- Suma")
# print("2.- Resta")
# print("3.- Multiplicacion")
# print("4.- Division")

# op = int(input("Seleccione una opción: "))

# n1 = int(input("Ingrese un numero: "))
# n2 = int(input("Ingrese otro numero: "))

# match op:
#     case 1:
#         print("La suma es", suma(n1, n2))
#     case 2:
#         print("La resta es", resta(n1, n2))
#     case 3:
#         print("La multiplicacion es", multiplicacion(n1, n2))
#     case 4:
#         if n2 != 0:
#             print("La division es", division(n1, n2))
#         else:
#             print("No se puede dividir por cero")
#     case _:
#         print("Opción inválida")


#profe:

# while True:
#     try:
#         print("1.- Suma")
#         print("2.- Resta")
#         print("3.- Multiplicacion")
#         print("4.- Division")
#         print("5.- Salir")

#         op = int(input("Ingrese una opcion: "))

#         match op:
#             case 1:
#                 num1 = int(input("Ingrese un numero: "))
#                 num2 = int(input("Ingrese otro numero: "))
#                 resultado = suma(num1, num2)
#                 print("Resultado:", resultado)

#             case 2:
#                 num1 = int(input("Ingrese un numero: "))
#                 num2 = int(input("Ingrese otro numero: "))
#                 resultado = resta(num1, num2)
#                 print("Resultado:", resultado)

#             case 3:
#                 num1 = int(input("Ingrese un numero: "))
#                 num2 = int(input("Ingrese otro numero: "))
#                 resultado = multiplicacion(num1, num2)
#                 print("Resultado:", resultado)

#             case 4:
#                 num1 = int(input("Ingrese un numero: "))
#                 num2 = int(input("Ingrese otro numero: "))

#                 while num2 == 0:
#                     print("No se puede dividir por cero.")
#                     num2 = int(input("Ingrese otro numero: "))

#                 resultado = division(num1, num2)
#                 print("Resultado:", resultado)

#             case 5:
#                 print("Saliendo...")
#                 break

#             case _:
#                 print("Opción inválida")

#     except Exception as e:
#         print("Error:", e)

#uSO Y EXPLICACION DE LISTAS

# lista=[91, -7, 44, 88, 14]
# print(lista)
# print(lista[3])
# for i in lista:
#     print(i*2)

# pokemons=["Leafeon", "Glaceon", "Sylveon", "Espeon", "Umbreon"]
# print(pokemons[2])
# print(len(pokemons[2]))
# for p in pokemons:
#     print(p.upper())

frutas=["Frutilla", "Arandano", "Frambuesa", "Sandia", "Mora"]
print(frutas)
#como puedo ejecutar el codigo para que me muestre cuales terminan en a
for f in frutas:
    if f[-1].lower()=="a":
        print(f"La fruta {f} termina con a")
    else: 
        print(f"La fruta {f} no termina en a")