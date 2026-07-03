#Funciones guia examen

autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}

#funcion para mostrar todos los autos 

def mostrarAutos(d):
    for id, vehiculo in d.items():
        print(f"{id}: {vehiculo}")
    print("-"*50)
mostrarAutos(autos)

#Muestra solo autos vendidos
def autosVendidos(d):
    for id, vehiculo in d.items():
        if operaciones[id][-1]!='Pendiente': #-1 pq es el ultimo valor de mi lista 
            print(f"{id}: {vehiculo}")

def autosVendidos_marca(d, marca):
    total=0
    for id, vehiculo in d.items():
        if vehiculo[0].lower() == marca.lower():
            if operaciones[id][-1]!= 'Pendiente':
                total+=1
    print(f'El número total de autos vendidos de la marca {marca.upper()} es {total}')

def busqueda_por_anio(anio_min, anio_max):
    elementos_encontrados = []
    for id_auto, datos in autos.items():
        marca = datos[0]
        modelo = datos[1]
        anio = datos[2]
        if anio_min <= anio <= anio_max:
            if operaciones[id_auto][1] != 'Pendiente':
                elementos_encontrados.append(f'{marca} {modelo} -- {id_auto}')
    
    if elementos_encontrados:
        elementos_encontrados.sort()
        print(elementos_encontrados)
    else:
        print('No se han encontrado elementos')

def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][-1]=nueva_fecha
        return True
    else:
        return False
while True:
    id=input("Ingrese el id del auto: ")
    fecha=input("Ingrese la fecha de venta: ")
        
    if actualizar_fecha_venta(id,fecha):
        print("Exito, nueva fecha de venta actualizada")
    else: 
        print("Metio mal las manos")
    next=input("¿Desea actualizar otro vehiculo (s/n)?")
    if next.lower()=="n":
        break

def validaString(m):
    if m=="" and m==" ": 
        return True
    else: 
        return False
    
def validaAño(a):
    if a<1900:
        return True
    else: 
        return False
    
def validaRanking(r):
    if r>=1 and r<=5:
        return False
    else: 
        return True

def nuevoAuto(d):
    id=input("Ingrese el ID: ")
    if validaString(id):
        print("Dato invalido")
        return 
    marca=input("Ingrese la marca: ")
    if validaString(marca):
        print("Dato invalido")
        return 
    modelo=input("Ingrese el modelo: ")
    if  validaString(modelo):
        print("Dato invalido")
        return
    año=int(input("Ingrese el año: "))
    if validaAño(año):
        print("El año debe ser mayor a 1900")
        return 
    ranking=int(input("Ingrese el ranking: "))
    if validaRanking(ranking):
        print("El ranking debe estar entre 1 y 5")
        return 
    fecha=input("Ingrese la fecha (dd-mm-yyyy): ")
    if validaString(fecha):
        return
    autos[id]=[marca, modelo, año, ranking]
    operaciones[id]=[fecha, 'Pendiente']
mostrarAutos(autos)
nuevoAuto(autos)
mostrarAutos(autos)
def eliminar_auto(id_auto):
    if id_auto in autos:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else: 
        return False

#Hacer un menu con todas las funciones que hicimos en clase
#debe tener manejo de errores (try-except)
def menuAutos():
    while True:
        try:
            print("-"*60)
            print("1.- Mostrar autos")
            print("2.- Ver autos vendidos")
            print("3.- Ver autos vendidos por marca")
            print("4.- Buscar auto por año")
            print("5.- Actualizar fecha de venta")
            print("6.- Agregar nuevo auto")
            print("7.- Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    mostrarAutos()
                case 2:
                    autosVendidos()
                case 3:
                    autosVendidos_marca()
                case 4:
                    busqueda_por_anio()
                case 5:
                    actualizar_fecha_venta() 
                case 6: 
                     busca = input("¿Qué color busca?: ")
                     resultado = dispColores(pinturas, busca)
                     print(resultado)
                case 7:
                    print("Saliendo...")
                case _:
                    print("Opcion invalida")
        except Exception as e:
            print("Error: ", e)