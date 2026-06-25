# def suma(a, b):
#     print(a+b)

# suma(22, 363)

# notas1=[6.3,6.8, 3.7, 2.1]
# notas2=[6.3,1.8, 3.9, 2.1]

# def creaProm(n):
#    return round(sum(n)/len(n),1)


# print("El promedio del notas 1 es", creaProm(notas1))
# print("El promedio del notas 2 es", creaProm(notas2))

nums=[20, 3, 7, 11, 67, 64. -8]

def buscaNumeros(lista, num):
    for n in lista:
        if n==num:
            return "Numero encontrado"
    return "No se encontro el numero", num
numeroBuscar=int(input("Ingrese el numero a buscar: "))
print(buscaNumeros(nums, numeroBuscar))

