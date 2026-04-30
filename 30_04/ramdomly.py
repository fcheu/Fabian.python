#Uso y ejemplo de random 
#Importar librerias
#Randint para numero aleatorio; genera un numero aletorio del 1 al 10
#ponerlo en una variable

import random
# num=(random.randint(1,10))
# print(num)
# for i in range(num):
#     print("Hola Daniel")
# import random
# dado=(random.randint(1,6))
# print("El dado salió:", dado)

#Crear una tabla de multiplicar 
# de 1 a 24, mostrar la tabla 
# import random
# num=(random.randint(1,24))
# for i in range (num):
#     print(num, "x" , i+1 , "=", num*(i+1))
    

# tirar 2 dados y si sale par 
# se va a la carcel, sino avanza 

# dado1=(random.randint(1,6))
# dado2=(random.randint(1,6))
# print("El primer dado salió", dado1)
# print("El segundo dado salió", dado2)
# if dado1==dado2:
#     print("Va a la cárcel")
# else:
#     print("Avanza")

#Se genera un golpe aleatorio entre 10 y 70 
# si el golpe tiene mas de 50 de fuerza es um golpe critico
#sino, no es muy efectivo

# strike=random.randint(10,70)
# if strike>50:
#     print("Golpe crítico. Daño:", strike)
# else:
#     print("El golpe no fue muy efectivo. Daño:", strike)

#3 personas juegan golf
# cada persona tiene la posibilidad de golpear
# y la distancia varia entre 60 y 190
# mostrar al final, el golpe mas fuerte 
import time
# jugador1=random.randint(60,190)
# jugador2=random.randint(60,190)
# jugador3=random.randint(60,190)
# time.sleep(1)

# print("El jugador 1 golpeó", jugador1,"metros")
# print("El jugador 2 golpeó", jugador2,"metros")
# print("El jugador 3 golpeó", jugador3,"metros")
# time.sleep(3)

# if jugador1>jugador2 and jugador1>jugador3:
#     print("El jugador 1 tuvo el golpe mas fuerte, que fue de:", jugador1,"metros")
# elif jugador2>jugador1 and jugador2>jugador3:
#     print("El jugador 2 tuvo el golpe mas fuerte, que fue de:", jugador2, "metros")
# else:
#     print("El jugador 3 tuvo el golpe mas fuerte, que fue de:", jugador3, "metros")

#tiempo de espera

#Killer instinc 

#Dos peleadores se piden al inicio de la pelea
#cada peleador inicia con 100 de HP
#se debe hacer una pelea por turnos
#y cada golpe varia entre 7 y 18
#se termina el match cuando uno de los 2
#tiene su HP menor o igual a 0
#BONUS: mostrar barras de energia de cada peleador 

jugador1=input("Ingrese el nombre del jugador 1:")
jugador2=input("Ingrese el nombre del jugador 2:")
j1=100
j2=100
turno=1
while j1 > 0 and j2 > 0:
    punch = random.randint(7,18)
    if turno % 2 == 1:
        j2 -= punch
        if j2 < 0:
            j2 = 0
        print("Turno uno")
        print(jugador1, "hizo", punch, "de daño")
        print(jugador2, "tiene", j2, "de HP")
    else:
        j1 -= punch
        if j1 < 0:
            j1 = 0
        print("Turno dos")
        print(jugador2, "hizo", punch, "de daño")
        print(jugador1, "tiene", j1, "de HP")
    turno += 1
    time.sleep(1)

if j1 <= 0:
    print(jugador2, "ganó")
elif j2 <= 0:
    print(jugador1, "ganó")

#turnos:
# turno=1
# if turno%2==0:
#     print("Turno uno")
# else:
#     print("Turno dos")