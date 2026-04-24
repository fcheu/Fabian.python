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
            total+=800000*1.19
        case 2:
            print("Tiene que pagar", 450000*1.19)
            total+=450000*1.19
        case 3: 
            print("Tiene que pagar", 90000*1.19)
            total+=90000*1.19
        case 4: 
            print("Saliendo")
            print(f"El total a pagar con IVA ES {round(total,2)}")
        case _:
            print("Opción inválida")