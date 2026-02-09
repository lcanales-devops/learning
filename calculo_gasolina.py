# Script para calcular el rendimiento del Hyundai Veloster 2013
print("--- Calculadora de Rendimiento ---")

# 'float' permite que el usuario use decimales (ej: 10.5)
distancia = float(input("¿Cuántos kilómetros recorriste? "))
gasolina = float(input("¿Cuántos litros de gasolina usaste? "))

# Realizamos la operación matemática
rendimiento = distancia / gasolina

# Mostramos el resultado con un mensaje claro
print(f"Tu Veloster está rindiendo {rendimiento} km por litro.")
