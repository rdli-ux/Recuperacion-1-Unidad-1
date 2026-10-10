"""
Nombre: Ricardo Daniel Lazo
Ejercicio: B. ¿Bubulu-cuántos instructores hay?
Descripción: Dada una lista de nombres de instructores separados por espacios, cuenta e imprime la cantidad total.
"""

# Leer toda la entrada y separarla en palabras (instructores)
instructores = input().split()
contador = 0

# Contar cuántos elementos hay en la lista
for instructor in instructores:
    contador = contador + 1

# Imprimir el total
print(contador)

