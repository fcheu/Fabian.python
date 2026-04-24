##ejemplo y ecplicacion de match
# op=0
# total=0
# while op!=4:
#     print("1.- Radio sterero Sony $70.000")
#     print("2.- LGTV 55 pulgadas Super gamer $500.000 ")
#     print("3.- PS5 $580.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print("El precio a pagar es ", 70000*1.19)
#             total+=70000*1.19
#         case 2:
#             print("El precio a pagar es ", 500000*1.19)
#             total+=500000*1.19
#         case 3:
#             print("El precio a pagar es ", 580000*1.19)
#             total+=580000*1.19
#         case 4:
#             print(f"Su total a pagar es {total}")
#         case _:
#             print("Opcion Inválida")  # opcion por defecto
name="Carlos"
def saludo():
    print("Hola como van?")
def chao():
    print(f"YA nos vamos? { name}")

def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1+n2}")
def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1-n2}")
def multi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1*n2}")
def divi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1/n2}")


# def 

op=0
while op!=5:
    op=int(input('''Ingrese una operacion
                        1.-Suma
                        2.-Resta
                        3.-Mutltiplicacion
                        4.-Division
                        5.-Salir
                        '''))
    match op:
        case 1:
            suma()
        case 2:
            resta()
        case 3:
            multi()
        case 4:
            divi()
        case 5:
            print("Saliendo del programa")
        case _:
            print("Opción Inválida")
    
op=0
while op!=4:
    print('''
        1.- Programa 1
        2.- Programa 2
        3.- Programa 3
        4.- Salir''')


