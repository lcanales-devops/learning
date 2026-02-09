"""
Script: Calculador de Consumo de Combustible
Autor: Luciano Canales
Descripción: Ejercicio de lógica de programación para calcular 
el rendimiento de combustible basado en entradas del usuario.
"""

print("--- Sistema de Cálculo de Rendimiento Vehicular ---")

# Solicitud de datos con validación implícita de punto flotante
try:
    distancia = float(input("Ingrese la distancia recorrida (km): "))
    gasolina = float(input("Ingrese la cantidad de combustible consumido (litros): "))

    # Cálculo del rendimiento (km/l)
    rendimiento = distancia / gasolina

    print(f"\nResultado: El rendimiento del vehículo es de {rendimiento:.2f} km por litro.")
    
except ZeroDivisionError:
    print("Error: Los litros consumidos no pueden ser cero.")
except ValueError:
    print("Error: Por favor ingrese solo valores numéricos.")
