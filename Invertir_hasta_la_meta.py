"""
Nombre: Ricardo Daniel Lazo
Ejercicio: 25175. Invertir hasta la meta
Descripción: Calcula el dinero acumulado mes con mes en una cuenta con interés compuesto del 6% anual hasta llegar a una meta.
"""

# Leer los datos de entrada línea por línea
inicial = float(input())
mensual = float(input())
meta = float(input())

mes = 0
total = inicial

# Imprimir el mes 0 con 6 decimales
print(f"{mes} {total:.6f}")

# Repetir mientras no lleguemos a la meta establecida
while total < meta:
    mes = mes + 1
    
    # El 6% anual equivale al 0.5% mensual (0.005)
    interes = total * 0.005 
    total = total + interes + mensual
    print(f"{mes} {total:.6f}")

