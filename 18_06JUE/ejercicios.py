#Gestor de pacientes#
#corchete es una lista, llave es un diccionario#
#indice -1 es el ultimo elemento de una lista
#.append es para agregar un elemento a la lista, se agrega exactamente igual
#al codigo inicial
#agregar un paciente con los datos que ingresa el usuario
def menuPacientes():
    pacientes=[
        {"nombre": "Aquiles Baeza", "prevision": "Fonasa",
        "temperatura":34.6, "grave": False},
    ]

    listadeNombres=[]
    for ln in pacientes: 
        listadeNombres.append(ln["nombre"])
    print(listadeNombres)
    
    def validTemp(t):
        if t>39:
            return True
        else:
            return False #return?
        
    pacientes.append({"nombre": "Alan Brito", "prevision": "Isapre",
        "temperatura":39.6, "grave": True})
    
    def agregarPaciente():
        nombre=input("Ingrese el nombre del paciente(8 caracteres): ")
        while nombre==" " or len(nombre)<9:
            print("Nombre invalido, debe tener 8 caracteres y no debe estar vacio")
            nombre=input("Ingrese el nombre del paciente(8 caracteres): ")
        prevision=input("Ingrese la prevision del paciente(fonasa, isapre, fodesa): ")
        while prevision.lower not in ("fonasa", "isapre", "fodesa"):
            print("Prevision invalida, ingrese una de estas: fonasa, isapre, fodesa")
            prevision=input("Ingrese la prevision del paciente(fonasa, isapre, fodesa): ")
        temperatura=float(input("Ingrese la temperatura del paciente: "))
        pacientes.append({"nombre": nombre, "prevision": prevision,
            "temperatura":temperatura, "grave": validTemp(temperatura)})

    def eliminarPaciente():
        mostrarPacientes()
        eliminar=int(input("¿Que paciente desea eliminar?: "))
        pacientes.pop(eliminar-1)#eliminar-1 porque todos los indices parten en 1
        print("paciente eliminado")
        
    def mostrarPacientes():
        if len(pacientes)==0:
            print("No hay pacientes")
        else:
            c=1
            for paciente in pacientes:
                print(f"{c} .- {paciente}")
                c+=1

    def pagarAtencion():
        mostrarPacientes()
        pagar=int(input("¿Cual paciente desea pagar?:"))
        pacientes=pacientes.lower[pagar-1]["prevision"]
        if pacientes=="fonasa":
            total=25000*0.46
        elif pacientes=="isapre":
            total=25000*0.73 #para que me de el total debo usar el resto del % original
        elif pacientes=="fodesa":
            total=25000*0.875
        else:
            print("Prevision invalida")
        print("Su total a pagar es: ", total)
    def tomarTemperatura():
        mostrarPacientes()
        p=int(input("¿A que paciente le tomará la temperatura?: "))
        temp=float(input("Ingrese la temperatura: "))
        pacientes[p-1]["temperatura"]=temp
        pacientes[p-1]["grave"]=validTemp(temp)
        print("Temperatura y estado actualizado")
    while True:
        try:
            print("1.- Agregar Paciente")
            print("2.- Quitar Paciente")
            print("3.- Tomar temperatura")
            print("4.- Pagar atención")
            print("5.- Mostrar Pacientes")
            print("6.- Salir")
            op=int(input("Ingrese una opcion: "))
            match op:
                case 1:
                    agregarPaciente()
                case 2:
                    eliminarPaciente()
                case 3:
                    tomarTemperatura()
                case 4:
                    pagarAtencion()
                case 5:
                    mostrarPacientes()
                case 6:
                    print("Saliendo del sistema")
                case _:
                    print("Opcion invalida")
        
        except Exception as e:
            print("Error", e)

menuPacientes()

#remove(escribo todo el elemento que quiero eliminar y todo de hacer match)
#si pongo .pop(numero del indice) asi remuevo desde el indice

def validarEstados
for p in pacientesHospital:
    (p["grave"])=validarEstado(p["temperatura"])

pacientes[1]["Temperatura"]=39.6
pacientes[2]["Temperatura"]=36.4
input("Cambios de temperatura")
validarEstados(pacientes)


listado=[4,6,{"pokemon":"Eeve"},67,6]
#        0 1         2          3  4
