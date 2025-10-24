# Programa para calcular el área total y el volumen de un cubo

print("=== Cálculo del área total y volumen de un cubo ===")

# Solicitar la longitud del lado del cubo
lado = float(input("Ingresa la longitud del lado del cubo: "))

# Calcular área total y volumen
area_total = 6 * (lado ** 2)
volumen = lado ** 3

# Mostrar resultados
print("\n=== Resultados ===")
print(f"Área total del cubo: {area_total:.2f}")
print(f"Volumen del cubo: {volumen:.2f}")