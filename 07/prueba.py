# print("Hola Osvaldo")  

# # creando variables

# titulo="Clima de hoy"  # String
# diaDelMes=13  # int
# mes=4       #int

# temperatura=22.3 # float

# llueve=False # boolean

# print(titulo)
# print("Temperatua actual:", temperatura, "grados")
# print(diaDelMes, "-", mes)

# # "rojo"=="verde" ---->False
# # 7>3 ---> True
# if llueve:  
#     print("Tiene que llevar paraguas")
# else:
#     print("puede llevar polera sin mangas")


# # pedir password y pin
# # Pida al usuario password en palabra que debe ser "temu"
# # ademas pida el pin que debe ser 3435
# # los dos deben estar correctos para acceder al sistema

# passw="temu"
# pin=3435

# palabra=input("Ingrese la palabra secreta: ")
# code=int(input("Ingrese el pin de 4 digitos: "))

# if code==pin and passw==palabra:
#     print("Acceso concedido")
# else:
#     print("Algo salio mal")

# ingreso=int(input("Ingrese su sueldo: "))

# print("1.- Básico")
# print("2.- Medio")
# print("3.- Superior")
# edu=int(input("Ingrese su nivel educacional: "))
# nacionalidad=input("Ingrese nacionalidad (chilena/ otra)")
# credito=0
# if ingreso>500000 and ingreso<=1000000:
#     credito=credito+300000
# elif ingreso>1000001 and ingreso<=1500000:
#     credito=credito+650000
# elif ingreso>1500001 :
#     credito=credito+1000000
# else:
#     print("no tiene sueldo suficiente")
# if edu==1:
#     print("NO TIENE BENEFICIO POR EDUCACION")
# elif edu==2:
#     credito=credito*1.3
# elif edu==3:
#     credito=credito*1.5

# if nacionalidad=="chilena":
#     credito=credito+300000
# else:
#     print("No tiene bono por nacionalidad")

# print("Su puntaje de credito es : ", credito)
import random

jugador1=input("Ingrese el nombre del jugador 1:")
jugador2=input("Ingrese el nombre del jugador 2:")
j1=100
j2=100
turno=1
while j1>0 and j2>0:
    punch=random.randint(7,18)
    if turno%2==1:
        print("Turno uno")
        print(jugador1, "hizo", punch, "de daño")
        print(jugador2, "tiene", j2-punch, "de HP")

    else:
        print("Turno dos")
        print(jugador2, "hizo", punch, "de daño")
        print(jugador1, "tiene", j1-punch, "de HP")
    turno+=1

if j1<=0:
    print(jugador2, "ganó")
elif j2<=0:
    print(jugador1, "ganó")