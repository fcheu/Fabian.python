# especialistas=0
# residentes=0

# while True:
#     try:
#         cantidad=int(input("¿Cuantos medicos desea registrar?: "))
#         if cantidad>0:
#             break 
#         else:
#             print("Debe ser un numero entero positivo para continuar")
#     except ValueError:
#         print("Registro medico invalido, ingrese un numero entero posivito")
# for i in range(cantidad):
#     print(f"Registro medico {i+1}")
#     while True:
#         nombre=input("Ingrese el nombre del medico: ")
#         if len(nombre)>=6 and " " not in nombre:
#             break 
#         else: 
#             print("Nombre invalido, solo debe tener 6 caracteres y ningun espacio")
#     while True: 
#         try:
#             experiencia=int(input("Ingrese los años de experiencia: "))
#             if experiencia>0:
#                 break
#             else:
#                 print("¡Error clínico! Ingresa un número entero positivo para la experiencia")
#         except ValueError:
#             print("¡Error clínico! Ingresa un número entero positivo para la experiencia")
#     if experiencia>5: 
#         categoria="Especialista Senior"
#         especialistas+=1
#     else: 
#         categoria="Especialista junior"
#         residentes+=1
# print(f"¡El hospital cuenta con {especialistas} Especialistas Senior y {residentes} Residentes Junior! ¡Sistema listo para operar!")


#######################################################################################################################################

# stock=120
# prestamos_activos=0
# historial_prestamos=0

# print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

# while True: 
#     print("MENÚ PRINCIPAL")
#     print("1. Libros disponibles")
#     print("2. Realizar préstamo")
#     print("3. Devolver préstamo")
#     print("4. Historial de préstamos")
#     print("5. Salir")
#     opcion=input("Seleccione una opción: ")

#     if opcion == "1":
#         print(f"Libros disponibles: {stock}")
#     elif opcion == "2":
#         try:
#             cantidad=int(input("Cantidad de libros a prestar: "))
#             if cantidad<=0:
#                 print("Debe ingresar una cantidad mayor a 0")
#             elif cantidad > stock:
#                 print("No hay suficientes libros disponibles.")
#             else:
#                 stock -= cantidad
#                 prestamos_activos += cantidad
#                 historial_prestamos += cantidad

#                 print("Préstamo realizado correctamente.")

#         except ValueError:
#             print("Ingrese un número válido.")
#     elif opcion == "3":
#         try:
#             cantidad = int(input("Cantidad de libros a devolver: "))

#             if cantidad <= 0:
#                 print("Debe ingresar una cantidad mayor que 0.")

#             elif stock + cantidad > 120:
#                 print("La devolución supera la capacidad máxima de la biblioteca.")

#             else:
#                 stock += cantidad
#                 prestamos_activos -= cantidad

#                 print("Devolución realizada correctamente.")

#         except ValueError:
#             print("Ingrese un número válido.")
#     elif opcion == "4":

#         print(f"Préstamos activos: {prestamos_activos}")
#         print(f"Total de préstamos realizados: {historial_prestamos}")

#     elif opcion == "5":

#         print("Gracias por utilizar nuestro software, hasta la próxima.")
#         break

#     else:
#         print("Opción inválida.")

#####################################################################################

# especialistas=0
# residentes=0

# while True:
#     try:
#         cantidad=int(input("¿Cuantos medicos desea registrar?: "))
#         if cantidad>0:
#             break
#         else:
#             print("Registro medico invalido, ingresa un entero positivo para continuar")
#     except ValueError:
#         print("Registro medico invalido, ingresa un entero positivo para continuar")
# for i in range(cantidad):
#     print(f"Registro medico {i+1}")
#     while True: 
#         nombre=input("Ingrese el nombre del profesional")
#         if len(nombre)>=6 and " " not in nombre:
#             break
#         else:
#             print("El nombre debe tener al menos 6 caracteres y no debe incluir espacios")
#     while True: 
#         try:
#             experiencia=int(input(f"Ingrese los años de experiencia de {nombre}: "))
#             if experiencia>0:
#                 break
#             else:
#                 print("Error clinico, ingresa un numero entero positivo para la experiencia")
#         except ValueError:
#             print("Error clinico, ingresa un numero entero positivo para la experiencia")
#     if experiencia>5:
#         categoria="Especialista Senior"
#         especialistas+=1
#     else:
#         categoria="Residente Junior"
#         residentes+=1
#     print(f"{nombre} ha sido clasificado como {categoria}")
# print("==RESUMEN==")
# print(f"Especialistas senior: {especialistas}")
# print(f"Residentes junior: {residentes}")
# print(f"El hospital cuenta con {especialistas} especialistas senior y {residentes} residentes junior, sistema listo para operar")

stock=120
prestamos_activos=0
historial=0

print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while True:
    print("MENU PRINCIPAL")
    print("1. Libros disponibles")
    print("2. Realizar prestamo")
    print("3. Devolver prestamo")
    print("4. Historial de prestamo")
    print("5. Salir")

    try:
        opcion=int(input("Seleccione una opcion: "))
        if opcion<1 or opcion>5:
            print("Opcion invalida, ingrese un numero entero entre 1 al 5")
    except ValueError:
        print("Error, debe ingresar un numero entero")
    match opcion:
        case 1:
            print(f"Cantidad actual de libros en la biblioteca: {stock}")
        case 2:
            try:
                cantidad=int(input("Cantidad de libros a prestar: "))
                if cantidad<=0:
                    print("Debe ser un numero mayor a 0")4
                elif cantidad > stock:
                    print("No hay suficientes libros disponibles")
                else: 
                    stock-=cantidad
                    prestamos_activos+=cantidad
                    historial+=cantidad
                    print("Prestamo realizado correctamente")
            except ValueError:
                print("Ingrese un numero valido")
        case 3:
            try:
                cantidad = int(input("Cantidad de libros a devolver: "))
                if cantidad <= 0:
                    print("Debe ingresar una cantidad mayor que 0.")
                elif stock + cantidad > 120:
                    print("La devolución supera la capacidad máxima de la biblioteca.")
                else:
                    stock += cantidad
                    prestamos_activos -= cantidad
                    print("Devolución realizada correctamente.")
            except ValueError:
                print("Ingrese un número válido.")
        case 4:
            print(f"Préstamos activos: {prestamos_activos}")
            print(f"Total de préstamos realizados: {historial}")

        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break
        case _:
            print("Opción inválida.") 
