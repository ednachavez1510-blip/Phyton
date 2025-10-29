def menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar una calificación")
    print("2. Mostrar todas las calificaciones")
    print("3. Calcular promedio, mayor y menor")
    print("4. Terminar programa")

# Lista para guardar las calificaciones
calificaciones = []

# Simulación de estructura do-while
while True:
    menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        try:
            cal = float(input("Ingresa una calificación (0-100): "))
            if 0 <= cal <= 100:
                calificaciones.append(cal)
                print(f"Calificación {cal} agregada correctamente.")
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Debes ingresar un número válido.")

    elif opcion == "2":
        if calificaciones:
            print("\nCalificaciones registradas:")
            for i, c in enumerate(calificaciones, start=1):
                print(f"{i}. {c}")
        else:
            print("No hay calificaciones registradas aún.")

    elif opcion == "3":
        if calificaciones:
            promedio = sum(calificaciones) / len(calificaciones)
            mayor = max(calificaciones)
            menor = min(calificaciones)
            print("\nResultados:")
            print(f"Promedio: {promedio:.2f}")
            print(f"Calificación más alta: {mayor}")
            print(f"Calificación más baja: {menor}")
        else:
            print("No hay calificaciones para calcular estadísticas.")

    elif opcion == "4":
        print("Programa terminado. ¡Hasta luego!")
        break  # Sale del bucle (simulando el 'while' del do-while)

    else:
        print("Opción no válida. Intenta de nuevo.")
