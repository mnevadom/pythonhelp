

def saludar2():
    print("Hola amigos")

def saludar(nombre):
    print(f"hola {nombre}")


saludar2()
saludar("Mario")

def tabla_multipl(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num*i}")


tabla_multipl(3)