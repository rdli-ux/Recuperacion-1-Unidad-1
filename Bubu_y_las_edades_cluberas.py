"""
Nombre: Ricardo Daniel Lazo
Ejercicio: A. Bubu y las edades cluberas
Descripción: Dada una lista de edades, imprime las edades distintas (sin repeticiones) ordenadas de mayor a menor.
"""

# Leer las edades de la entrada
edades = input().split()
edades_sin_repetir = []

# Guardar solo las edades que no estén repetidas en una nueva lista
for edad in edades:
    if edad not in edades_sin_repetir:
        edades_sin_repetir.append(edad)

# Convertir a enteros para poder ordenar los números matemáticamente
edades_enteros = []
for edad in edades_sin_repetir:
    edades_enteros.append(int(edad))

# Ordenar la lista de mayor a menor
edades_enteros.sort(reverse=True)

# Regresar a formato de texto para imprimir exactamente como pide el problema
resultado = []
for edad in edades_enteros:
    resultado.append(str(edad))

# Imprimir la lista final
print(resultado)
