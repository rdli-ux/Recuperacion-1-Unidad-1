"""
Nombre: Ricardo Daniel Lazo
Ejercicio: C. Palabra palindroma
Descripción: Lee una palabra e indica si es palíndroma (se lee igual de izquierda a derecha y viceversa) imprimiendo SI o NO.
"""

# Leer la palabra de entrada
palabra = input()
palabra_invertida = ""

# Invertir la palabra usando un for para concatenar al revés
for letra in palabra:
    palabra_invertida = letra + palabra_invertida

# Comparar si ambas palabras son idénticas
if palabra == palabra_invertida:
    print("SI")
else:
    print("NO")

