tupla = (4, "Hola", 5.3, [12, 2, 5])

# pero no se pueden agregar ni modificar sus valores

print(tupla[1])

#mostrando es igual q la lista

print(tupla.count(6))

lista = list(tupla)

tupla2 = tuple(lista)