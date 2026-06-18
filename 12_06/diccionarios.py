# uso y eplicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# # print(alumno)
# # print(alumno["carrera"])

# for key ,value in alumno.items():
#     print(f"{key}= {value} ")
# print("---Cambios de datos---")
# # for dato ,valor in alumno.items():
# #     print(dato, valor )
# alumno["email"]="shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key ,value in alumno.items():
#     print(f"{key}= {value} ")

# productos={
#     1:{"nombre": "Control Inalambrico",
#        "categoria": "Electronica",
#        "precio": 45000},
#     2:{"nombre": "Pilas Recargables",
#        "categoria": "Insumos",
#        "precio": 5000},
#     3:{"nombre": "Pasta Termica",
#        "categoria": "Computacion",
#        "precio": 7000},
# }

# print(productos[1]["nombre"])

'''
Crear un diccionario de trabajadores 
'''

##CRUD DE VEGETALES

# vegetales={
#    1:"Maracuyá",2:"Pera",3:"Cebolla",7:"Papa"
# }

# print(list(vegetales.keys())[-1])


# def agregarVegetales():
#    print("-"*20)
#    agregar=input("Ingrese un vegetal: ")
#    nuevoKey=list(vegetales.keys())[-1]
#    vegetales[nuevoKey+1]=agregar
# def mostrarVegetales():
#    print("-"*40)
#    for num, nombre in vegetales.items():
#          print(f"{num}.- {nombre} ")
# def eliminarVegetal():
#    mostrarVegetales()
#    borrar=int(input("Cual vegetal borrará?: "))
#    del vegetales[borrar]
# def actualizarVegetal():
#    mostrarVegetales()
#    act=int(input("Cual vegetal actualizará?: "))
#    vegetales[act]=input("Ingrese nuevo nombre: ")

# def vegetalesMenu():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Comprar")
#          print("6.- Crear Boleta y Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarVegetales()
#                case 2:
#                   eliminarVegetal()
#                case 3:
#                   actualizarVegetal()
#                case 4:
#                   mostrarVegetales()
#                case 5:
#                   comprar()
#                case 6:
#                   crearBoleta()
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)

# # vegetalesMenu()

# ##Diccionario con diccionarios
# productosDicc={
#    1:{"nombre": "Maracuyá", "precio": 3000},
#    2:{"nombre": "Pera", "precio": 1500},
#    3:{"nombre": "Cebolla", "precio": 1200}
# }
# carrito=[]
# productosDicc[4]={"nombre": "Piña", "precio": 3500}
# def agregarProducto():
#    print("Cual es el nombre del producto?")
#    nombre = input()
#    print("cual es el precio?")
#    precio = int(input())
#    nuevoKey=list(productosDicc.keys())
#    nuevoKey.sort()
#    productosDicc[nuevoKey[-1]+1]= {"nombre": nombre, "precio": precio}
# def MostrarProducto():
#    for key, producto in productosDicc.items():
#       print(f"{key} .{producto}")
# def eliminarProducto():
#    MostrarProducto()
#    borrar=int(input("Cual Producto borrará?: "))
#    del productosDicc[borrar]
# def actualizarProducto():
#    MostrarProducto()
#    num=int(input("Que producto desea actualizar?: "))

#    nombre=input("Cual es el nombre nuevo?: ")
#    precio=int(input("Cual es el precio nuevo?: "))
#    productosDicc[num]={"nombre": nombre, "precio": precio}


# def comprar():
#     while True:
#         MostrarProducto()
#         try:
#            com=int(input("Que producto va a comprar?:"))
#            if com==0:
#               break
#            if com in productosDicc.keys():
#               carrito.append(productosDicc[com])
#         except Exception as e:
#            print ("Error:", e)

# def crearBoleta():
#    total=0
#    print("-"*30, "0", "-"*30)
#    for prod in carrito:
#       print(f"{prod["nombre"]}___${prod["precio"]}")
#       print("-"*30, "0", "-"*30)
#       print(f"El total neto es{total} y el IVA es {total*0.19}")
#       print(f"El total a pagar es {total*0.19}")
#       print("Gracias por venir a minimarket Bender")
#       print("-"*30, "0", "-"*30)
# # print(productosDicc[2]["precio"])  # precio de la pera
# # print(productosDicc[3]["nombre"])  # nombre de la cebolla

# # for num, veg in productosDicc.items():
# #     print(f"{num}.- {veg}")

# ##Lista con diccionarios
# productosList=[
#    {"nombre": "Maracuyá", "precio": 3000}, #0
#    {"nombre": "Pera", "precio": 1500},     #1  
#    {"nombre": "Cebolla", "precio": 1200}   #2
# ]

# print(productosList[2]["precio"]) #precio de la cebolla
# print(productosList[0]["nombre"]) #nombre de la naracuya



# def vegetalesMenuDiccionario():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Comprar")
#          print("6.- Crear Boleta y Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarVegetales()
#                case 2:
#                   eliminarVegetal()
#                case 3:
#                   actualizarVegetal()
#                case 4:
#                   mostrarVegetales()
#                case 5:
#                   comprar()
#                case 6:
#                   crearBoleta()
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)
# vegetalesMenuDiccionario()

#Cambiar la funcion actualizar para que solo 
# actualice una solo key 
# Ademas, crear un CRUD pero con la lista 
# de diccionarios.

peliculas={
   1:{"nombre": "Obsession", "año": 2026, "director": "Curry Barker", "calificación": 0},
   2:{"nombre": "Hokum", "año": 2026, "director": "Damian McCarthy", "calificacion": 0},
   3:{"nombre" : "Backrooms", "año": 2026, "director": "Kane Parsons", "calificacion": 0},
   4:{"nombre": "Hereditary", "año": 2018, "director": "Ari Aster", "calificacion": 0}
}

def calificarPelicula():
   codigo=int(input("Ingrese codigo de la pelicula: "))
   if codigo in peliculas:
      nota=float(input("Ingrese la calificacion (1-5 estrellas): "))
      peliculas[codigo]["calificacion"]=nota
      print("Calificacion actualizada")
   else:
      print("Pelicula no encontrada")

def mostrarPeliculas():
   if len(peliculas)==0:
      print("No hay peliculas registradas")
      return 
   for codigo, datos in peliculas.items():
      print(f"codigo:{codigo} Nombre:{datos['nombre']} Año: {datos['año']} Director: {datos['director']} Calificacion:{datos['calificacion']}")
def agregarPelicula():
   codigo=max(peliculas.keys()) + 1
   nombre=input("Ingrese nombre: ")
   año=int(input("Ingrese año: "))
   director=input("Ingrese el director: ")
   peliculas[codigo]={"nombre":nombre,"año":año,"director": director,"calificaciones": 0}
   print("Pelicula agregada correctamente")

def menuPeliculas():
   while True:
      try:
         print("1.- Calificar pelicula")
         print("2.- Mostrar peliculas")
         print("3.- Agregar pelicula")
         print("4.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
            case 1:
               calificarPelicula()
            case 2:
               mostrarPeliculas()
            case 3:
               agregarPelicula()
            case 4:
               print("Saliendo del sistema")
               break
            case _:
                 print("Opcion invalida")
      except Exception as e:
           print("Error:",e)
menuPeliculas()