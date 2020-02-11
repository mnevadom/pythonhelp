# no pueden haber duplicados

conjunto = set()

# si no lo indicamos con set antes se cree q es un diccionario q tb es con {}
# esto es cuando lo inicias vacio
# si le metes valores de una vez ya sabe lo q es
conjunto = {}

conjunto = {1, 2, 3, "Hola"}

# pero NO puede tener mas colecciones dentro, como una lista 

conjunto.add(89)

# los valores son desordenados

#eliminando elementos
conjunto.discard(2)

conjunto.clear()

print(conjunto)

print(3 in conjunto)

print(3 not in conjunto)



# -----

a = {1, 2, 3}
b = {3, 5, 6}

print(a==b)
print(len(a))

# union de conjuntos
c = a | b

# o solo coger lo comun
c = a & b

# diferencia , solo los de A
c = a - b

# diferencia simetrica, los que esten en ambos sin coincidir
c = a ^ b

c = {1, 2, 3, 4, 5}

print(a.issubset(c))
print(c.issuperset(a))

print(a.isdisjoint(b)) # que sean disconexos sin elementos en comun

# conjuntos inmutables
a = frozenset({8, 9, 4})
