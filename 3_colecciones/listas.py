# listas

lista = []

listaRellena = ["lunes", "Martes", "Miercoles", "jueves", [1, 2, 3], True, 49, 2.34]

print(listaRellena[0])

# me lo recorre desde detras
print(listaRellena[-1])

# la de 0, 1 y 2
print(listaRellena[0:3])
# desde el ppio
print(listaRellena[:4])
print(listaRellena[2:])

print(listaRellena[1:3])

print(listaRellena)

print(len(listaRellena))

listaRellena.append(23)

listaRellena.insert(1, 3)

listaRellena.extend([1, 2, 3, 4, 5])

list2 = listaRellena + [9, 2]

print(3 in list2)

list2.index("lunes")

lista3 = listaRellena * 2

listaRellena.sort(reverse=true)