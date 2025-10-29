def menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar una nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio mayor y menor")
    print("4. Terminar programa")

# Lista vacía
elementos = []

# Simulación de estructura do-while
while True:
    menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nuevo = input("Ingresa una nota: ")
        elementos.append(nuevo)
        print(f"'{nuevo}' ha sido agregado.")

    elif opcion == "2":
        if elementos:
            print("\nNotas actuales:")
            for i, e in enumerate(elementos, start=1):
                print(f"{i}. {e}")
        else:
            print("\nLa lista está vacía.")

    elif opcion == "3":
        if elementos:
            eliminar = input("Ingresa la nota que deseas eliminar: ")
            if eliminar in elementos:
                elementos.remove(eliminar)
                print(f"'{eliminar}' ha sido eliminado.")
            else:
                print(f"'{eliminar}' no está en la lista.")
        else:
            print("\nLa lista está vacía. No hay nada que eliminar.")

    elif opcion == "4":
        print("Saliendo del programa... ¡Hasta luego!")
        break  # Condición de salida: simula el 'while' del do-while

    else:
        print("Opción no válida. Intenta de nuevo.")
