'''
Ejercicio 3:
Hacer un programa que pida un carácter e indique si es una vocal o no.
'''

letra = input("Digite un caracter: ").lower()

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print("Es una vocal")
else:
    print("No es una vocal")