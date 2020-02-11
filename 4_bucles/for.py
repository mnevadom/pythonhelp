

for i in [1, 2, 3]:
    print("hola")


for i in [1, 2, 3, "Mario"]:
    print(f"elemento: {i}")

#con tuplas, conjuntos, diccionarios...

diccionario = {"Mario":22, "Maria": 35}

for i in diccionario:
    print(f"elemento: {i}")
    print(f"{diccionario[i]}")
    print(f"{i} -> {diccionario[i]}")


for clave, valor in diccionario.items():
    print(f"{clave} -> {valor}")

unchar = "Mario"
for i in unchar
    print(f"{i}", end=" ")

# en el print le puedo poner el caracter q quiero al final

# con range
for i in range(50): 
    print(i)

for i in range(5, 10): 
    print(i)


for i in range(2, 10, 3): 
    print(i)

for i in range(2, 10, -3): 
    print(i)