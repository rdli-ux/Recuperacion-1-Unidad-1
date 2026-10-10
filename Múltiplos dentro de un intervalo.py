"""
Nombre: Ricardo Daniel Lazo
Ejercicio: F. Multiplos dentro de un intervalo
Descripción: Imprime todos los números enteros desde 'a' hasta 'b' que sean múltiplos de 'a'.
"""

# Leer los límites del intervalo
datos = input().split()
a = int(datos[0])
b = int(datos[1])

# Revisar todos los números en el rango
for i in range(a, b + 1):
    # Si el residuo de la división es 0, es múltiplo
    if i % a == 0:
        print(i, end=" ")
print()

