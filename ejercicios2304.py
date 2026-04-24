#print ("Hola Daniel "*3)
#n="daniel"
#print (n[2])


#name1="Catalina Pinochet"
#name2=" Vicente "

#print(name2.strip())
#print(name1.lower())
#print(name1.upper())
#print(name1.replace("Pinochet", "Frei"))
#print(name1.find("Pinochet"))


#lower: minusculas
#upper: mayusculas todas las letras
#replace: para cambiar una palabra en concreto por otra que se indica luego de la coma
#find: Para encontrar la palabra que ponemos entre comillas, en este caso
#Pinochet; que se encuentra en la posicion 9, ya que parte del 0 (siendo 0 la C de Catalina)
#Indice comienza con el 0 y no por el 1; porque es un lenguaje binario --> 0 en binario: 000
#1 en binario: 0001, 2 en binario: 0010

#Pedir la clave al usuario y verificar
#que sea SHAZAM independiente de su case
#(Sin importar si son mayusculas o minusculas)

#passw="shazam"
#palabra=input("Ingrese su clave: ").lower()
#if passw==palabra:
#    print ("Clave correcta")
#else:
#    print("Clave invalida")

#Crear un nombre de usuario y verificar que su largo esté entre 4 y 10 caracteres
 
#print("Usuario fuera de rango") 

#Crear un pin y que este tenga exacta,ente 4 digitos



#profe:

# pin=int(input("Ingrese un pin de 4 digitos"))
# if len(str(pin))==4:
#     print("Pin creado")
# else:
#     print("Pin invalido")

# nombreu=input("Ingrese su nombre de usuario: ")
# print(len(nombreu))
# if len(nombreu)>=4 and len(nombreu)<=10:
#     print("Dentro de rango")
# else:
#     print("Fuera de rango")

# #profe:

# nombre=input("Ingrese su nombre de usuario:")
# if 4<len(nombre)>10:
#     print("Usuario correcto")
# else:pin=input("Ingrese su pin: ")
# print(len(pin))
# if len(pin)==4:
#     print("Pin aceptable")
# else: 
#     print("Pin invalido, fuera de rango")

#clase2404

op=0
total=0
while op!=4:
    print("1.- PC Ryzen $800.000")
    print("2.- LGTV 55 Pulgadas $450.000")
    print("3.- Parlante JBL Pure Sound $90.000")
    print("4.- Salir")
    op=int(input())
    match op:
        case 1:
            print("Tiene que pagar", 800000*1.19)
        case 2:
            print("Tiene que pagar", 450000*1.19)
        case 3: 
            print("Tiene que pagar", 90000*1.19)
        case 4: 
            print("Saliendo")
        case _:
            print("Opción inválida")