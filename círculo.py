# Programa para calcular el área y el perímetro de un círculo

print("=== Cálculo del área y perímetro de un círculo ===")

# Solicitar el radio del círculo
radio = float(input("Ingresa el radio del círculo: "))

# Calcular el área y el perímetro
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

# Mostrar resultados
print("\n=== Resultados ===")
print(f"Área del círculo: {area:.2f}")
print(f"Perímetro (circunferencia): {perimetro:.2f}")