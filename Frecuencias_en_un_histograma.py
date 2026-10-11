"""
Nombre: Ricardo Daniel Lazo
Ejercicio: 12149. Frecuencias en un histograma
Descripción: Dada una matriz de ceros y unos que representa un histograma, calcula y muestra la altura de cada barra.
"""

# Leer n (filas) y m (columnas)
datos = input().split()
n = int(datos[0])
m = int(datos[1])

# Crear una lista de ceros para guardar las alturas de cada columna
alturas = [0] * m

# Leer cada fila y sumar los unos encontrados
for i in range(n):
    fila = input().split()
    for j in range(m):
        if fila[j] == '1':
            alturas[j] = alturas[j] + 1

# Imprimir el resultado separado por espacios
for j in range(m):
    print(alturas[j], end=" ")
print()
