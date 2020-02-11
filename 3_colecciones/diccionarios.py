# desordenados. Con clave y valor

diccionario = {}

diccionario = {"azul" : "blue", "amarillo" : "yellow"}

print(diccionario)

print(diccionario["azul"])

# agregar. y esto es desordenado siempre
diccionario["verde"] = "green"
diccionario["azul"] = "Bluuue"

del(diccionario["verde"])


diccionario2 = {"Mario": [22, 1.85], "Maria" : [31, 1.50]}

# o con tuplas tb

diccionario3 = {10: "Dybala", 7:"CR"}

print(diccionario3[10])

# si lo pones entre corchetes y no existe peta!
print(diccionario3.get(11, "no existe jugador con ese dorsal"))

print(10 in diccionario3)

print(diccionario3.keys())
print(diccionario3.values())
print(diccionario3)
print(diccionario3.items())
