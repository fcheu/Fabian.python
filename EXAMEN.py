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
    