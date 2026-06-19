notas=[4.6, 7.0, 3.4, 6.6, 3.9, 6.8]

#crear una funcion para poder pasarle la lista como parámetro
#y mostrar el promedio, ademas si aprueba o reprueba

# def calculaProm(notas):
#     promedio=sum(notas) / len(notas)
#     promedio=round(promedio,1)
#     print(f"El promedio es de:{promedio}")
#     if promedio>=4.0:
#         print("Aprueba")
#     else:
#         print("Reprueba")

# def calculaProm(n):
#     return round(sum(n)/len(n),1)
# print("El promedio es ",calculaProm(notas))

# print(max(notas))
# print(min(notas))

# calculaProm(notas)

peliculas=[
    {"titulo": "Inception", "Director": "Christopher Nolan",
     "genero": "Ciencia Ficcion", "año": 2010},
     {"titulo": "Jurassic Park", "Director": "Steven Spilberg",
     "genero": "Ciencia Ficcion", "año": 1993},
     {"titulo": "Se7en", "Director": "David Fincher",
     "genero": "Thriller", "año": 1997},

]

#crear un gestor de peliculas
#el titulo debe tener mas de 2 caracteres
#el año debe ser mayor a 1960 y debe ser menor al año actual
#el director debe tener nombre y apellido
#mostrar el siguiente menú 

def ingresarPelicula():
    titulo=input("Ingrese el nombre de la película: ")
    while titulo== " " or len(titulo)<2:
       print("Nombre invalido, debe tener mas de 2 caracteres")
       titulo=input("Ingrese el nombre de la película: ")
    director=input("Ingrese el nombre y apellido del director: ")
    apellido=director.split()
    while len(apellido)<2:
       print("Error el director debe tener nombre y apellido")
       director=input("Ingrese el nombre y apellido del director: ")
       apellido=director.split()
    genero=input("Ingrese el genero de la pelicula: ")
    año=int(input("Ingrese el año de la pelicula: "))
    while True:
        try:
           año=int(año)
           añoactual=int(input("Ingrese el año actual: "))
           if año>1960 and año<añoactual:
              break
           else: 
              print("Año invalido, debe ser mayor a 1960 y menor al año actual")
        except ValueError:
          print("Error, el año debe ser un numero entero")
        año=int(input("Ingrese el año de la pelicula: "))
    peliculas.append({"titulo": titulo, "director": director,
            "genero": genero, "año": año})
   
def mostrarPeliculas():
   if len(peliculas)==0:
      print("No hay peliculas")
   else:
      c=1
      for pelicula in peliculas:
         print(f"{c} .- {pelicula}")
         c+=1
         
def quitarPelicula():
   mostrarPeliculas()
   quitar=int(input("¿Cual pelicula desea quitar?: "))
   peliculas.pop(quitar-1)
   print("Pelicula eliminada")
   
def actualizarPelicula():
   mostrarPeliculas()
   actualizar=int(input("¿Cual pelicula desea actualizar?: "))-1
   if actualizar>=0 and actualizar<len(peliculas):
    peliculas[actualizar]["titulo"]=input("Nuevo titulo: ")
    peliculas[actualizar]["director"]=input("Nuevo director: ")
    peliculas[actualizar]["genero"]=input("Nuevo genero: ")
    peliculas[actualizar]["año"]=input("Nuevo año: ")
    print("Pelicula actualizada")
   else: 
      print("Pelicula no encontrada")
   
def mostrarTitulos():
    if len(peliculas)==0:
      print("No hay peliculas")
    else:
       c=1
       for pelicula in peliculas:
        print(f"{c} .- {pelicula["titulo"]}")
        c+=1 

def menuPeliculas():
   while True:
      try:
         print("1.- Ingresar pelicula")
         print("2.- Quitar pelicula")
         print("3.- Actualizar pelicula")
         print("4.- Mostrar peliculas")
         print("5.- Mostrar solo los titulos")
         print("6.- Salir")

         op=int(input("Seleccione una opcion: "))
         match op:
            case 1:
               ingresarPelicula()
            case 2:
               quitarPelicula()
            case 3:
               actualizarPelicula()
            case 4:
               mostrarPeliculas()
            case 5:
               mostrarTitulos()
            case 6:
               print("Saliendo del menu")
            case _:
                 print("Opcion invalida")
      except Exception as e:
           print("Error:",e)

menuPeliculas()