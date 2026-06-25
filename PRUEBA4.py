# listado = [3, 6.5, 4, 5,["Link", "Zelda"], {"pkmn":"Weeddle"}]
# #          0   1   2  3        4                  5 

# print(listado[5]["pkmn"])#muestra weeddle, porque es el valor del key "pkmn"

# for e in listado:
#     print(e)


# listado.append({"dia": "lunes", "temp": 25.7, "humedad": 29})
# print("-"*50)
# input()
# for e in listado:
#     print(e)


pinturas=[
    {"color": "verde", "capacidad": 1500, "formato": "tarro"},
    {"color": "azul", "capacidad": 1500, "formato": "tarro" },
    {"color": "blanco", "capacidad": 3500, "formato": "tinaja"},
    {"color": "purpura", "capacidad": 500, "formato": "bolsa"} 
]

def mostrarPinturas():
    if len(pinturas)<1: 
        print("no hay pinturas para mostrar")
    else:
        c=1
        for p in pinturas:
            print(f"{c}.- {p}")
            c+=1

def quitarPinturas():
    mostrarPinturas()
    elemento=int(input("¿Que pintura va a eliminar?: "))
    pinturas.pop(elemento-1)

def agregarPinturas():
    color=input("¿Que color será?: ")
    capacidad=int(input("¿Que capacidad será?: "))
    formato=input("¿Qué formato será?: ")
    pinturas.append({"color": color, "capacidad": capacidad, "formato": formato})

def actualizarPinturas():
    mostrarPinturas()
    elemento=int(input("¿Que pintura actualizará?: "))
    print("1.- color")
    print("2.- capacidad")
    print("3.- formato")
    dato=int(input("¿Que dato de la pintura actualizará?: "))
    if dato==1:
        nuevoValor=input("Ingrese el nuevo color: ")
        pinturas[elemento-1]["color"]=nuevoValor
    elif dato==2:
        nuevoValor=int(input("Ingrese la nueva capacidad: "))
        pinturas[elemento-1]["capacidad"]=nuevoValor
    elif dato==3:
        nuevoValor=input("Ingrese el nuevo formato: ")
        pinturas[elemento-1]["formato"]=nuevoValor
    else:
        print("dato invalido")

def mayorCapacidad(lista):
    listaCapacidad=[]
    for p in lista:
        listaCapacidad.append(p["capacidad"])
    return max(listaCapacidad)



def menuPinturas():
    while True:
        try:
            print("-"*60)
            print("1.- Agregar pintura")
            print("2.- Quitar pintura")
            print("3.- Actualizar pintura")
            print("4.- Mostrar pinturas")
            print("5.- Mostrar mayor capacidad")
            print("6.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregarPinturas()
                case 2:
                    quitarPinturas()
                case 3:
                    actualizarPinturas()
                case 4:
                    mostrarPinturas()
                case 5:
                    print(f"El recipiente con mayor capacidad tiene: {mayorCapacidad(pinturas)}")
                case 6:
                    print("Saliendo...")
                case _:
                    print("Opcion invalida")
        except Exception as e:
            print("Error: ", e)