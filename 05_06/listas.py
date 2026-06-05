# juguetes=["yoyo", "tetris"]
# def mostrar():
#     c=1
#     for j in juguetes: 
#         print(c, "-", j)
#         c+=1
#         print("-"*30)
# def actualizar ():
#     mostrar()
#     print ("¿Que juguete desea actualizar?: ")
#     index=int(input(""))
#     print("Ingrese el nombre del juguete: ")
#     nuevoJuguete=input("Ingrese el nombre del juguete: ")
#     juguetes[index-1]=nuevoJuguete
# def menuJuguetes():  
#     while True: 
#         try:
#             print("1.- Agregar juguete")
#             print("2.- Eliminar juguete")
#             print("3.- Actualizar juguete")
#             print("4.- Mostrar juguetes")
#             print("5.- Salir")
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     ju=input("Agregue un juguete: ")
#                     juguetes.append(ju)
#                 case 2:
#                     mostrar()
#                     eliminar=int(input("Elimine un juguete: "))
#                     juguetes.pop(eliminar-1)
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     print("Saliendo")
#                     break 
#                 case _:
#                     print("Opcion inválida")
#         except Exception as e:
#             print("Error: ", e)

# menuJuguetes()

###########################################

num=input("Ingrese numeros enteros separados por espacio:")
listaNum=num.split() #Para hacerlos lista
listaNumInt=[]
pares=[]
impares=[]
for n in listaNum:
    listaNumInt.append(int(n)) #tengo mi lista de numeros int
    print(n)
for p in listaNumInt:
    if p%2==0:
        pares.append(p)
    else:
        impares.append(p)
print(f"Los numeros pares son {pares}")
print(f"Los numeros impares son {impares}")