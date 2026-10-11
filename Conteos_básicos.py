"""
Nombre: Ricardo Daniel Lazo
Ejercicio: 11339. Conteos básicos
Descripción: Este programa lee dos números enteros (A y B) y devuelve los números de uno en uno iniciando desde A hasta B.
"""
# Leer los dos números ingresados en la misma línea y separarlos
datos = input().split()
a = int(datos[0])
b = int(datos[1])

# Usar un ciclo for para contar desde el número inicial 'a' hasta el final 'b'
for i in range(a, b + 1):
    # Imprimir el número actual en cada vuelta del ciclo
    print(i)
