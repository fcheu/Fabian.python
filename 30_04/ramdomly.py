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

jugador1=random.randint(60,190)
jugador2=random.randint(60,190)
jugador3=random.randint(60,190)

print("El jugador 1 golpeó", jugador1,"metros")
print("El jugador 2 golpeó", jugador2,"metros")
print("El jugador 3 golpeó", jugador3,"metros")

if jugador1>jugador2 and jugador1>jugador3:
    print("El jugador 1 tuvo el golpe mas fuerte, que fue de:", jugador1,"metros")
elif jugador2>jugador1 and jugador2>jugador3:
    print("El jugador 2 tuvo el golpe mas fuerte, que fue de:", jugador2, "metros")
else:
    print("El jugador 3 tuvo el golpe mas fuerte, que fue de:", jugador3, "metros")

