# op=0
# total=0
# while op!=4:
#     print("1.- PC $500.000")
#     print("2.- LGTV 55 pulgadas $450.000")
#     print("3.- Microondas Mademsa $100.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print("El total a pagar es ",500000*1.19 )
#             total+=500000*1.19
#         case 2:
#             print("El total a pagar es ",450000*1.19 )
#             total+=450000*1.19
#         case 3:
#             print("El total a pagar es ",100000*1.19 )
#             total+=100000*1.19
#         case 4:
#             print("Saliendo")
#             print("El total a pagar es", total)
#         case _:
#             print("Opción inválida")


# Calculadora

#  + - * /

def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"EL resultado es {n1+n2}")

def resta():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"EL resultado es {n1-n2}")
def multi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"EL resultado es {n1*n2}")
def divi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"EL resultado es {n1/n2}")

def calculadora():
    op=0
    while op!=5:
        print("1.- suma")
        print("2.- resta")
        print("3.- Multiplicacion")
        print("4.- Division")
        print("5.- Salir")
        print("Seleccione una opcion")
        op=int(input())
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
                print("Saliendo")
                
            case _:
                print("Opción inválida")

def tabla():
    num=int(input("Ingrese un numero: "))

    for i in range(10):
        print(num, "x" , i+1 , "=", num*(i+1))
        

def MultiProme():
    notas=int(input("Ingrese la cant de notas: "))
    suma=0
    for i in range(notas):
        n=float(input(f"Ingrese la nota {i+1}: "))
        suma=suma+n
    prom=suma/notas
    print("El promedio es",round(prom,1) )

    if prom>=4:
        print("Alumno aprobado")
    else:
        print("Alumno reprobado")

def programas():
    op=0
    while op!=4:
        print('''
        1.- MultiPRomedio
        2.- Caluladora
        3.- Tabla Multi
        4.- Salir
        ''')
        op=int(input("Seleccione su opcion: "))
        match op:
            case 1:
                MultiProme()
            case 2:
                calculadora()
            case 3:
                tabla()
            case 4:
                print("Saliendo")
                
            case _:
                print("Opción inválida")

programas()
