# Lista para almacenar las notas (puedes usar números enteros o decimales)

notas = []

# Inicializamos la variable que guardará la opción elegida por el usuario

opcion = None 



# Definición de una función para mostrar el menú

def mostrar_menu():

    """Muestra las opciones del menú principal."""

    # Imprime una línea de separación y el título

    print("\n--- MENÚ PRINCIPAL ---")

    # Imprime las opciones disponibles

    print("1. Agregar una nota")

    print("2. Mostrar todas las notas")

    print("3. Calcular promedio, mayor y menor")

    print("4. Terminar programa")
    
    print("5. Modificar nota")
    
    print("6. Eliminar nota")

    

# Simulación del bucle do-while en Python:

# El bucle 'while True' crea un ciclo infinito que se ejecuta al menos una vez.

# La única forma de salir será con un 'break' (opción 4).

while True:

    # Llama a la función para mostrar las opciones del menú

    mostrar_menu()

    

    # Bloque para manejar la entrada del usuario y posibles errores

    try:

        # Solicita al usuario que ingrese la opción y la convierte a entero

        opcion = int(input("Seleccione una opción (1-6): "))

    # Si la entrada no puede convertirse a entero (ej: el usuario escribe "hola")

    except ValueError:

        # Imprime un mensaje de error y usa 'continue'

        print("🛑 ¡Opción inválida! Por favor, ingrese un número del 1 al 6.")

        # 'continue' salta el resto del código del bucle y vuelve a la línea 'while True'

        continue 

        

    # Estructura condicional (if/elif/else) para ejecutar la acción según la opción

    if opcion == 1:
    # --- Agregar nota ---
    try:
        nota = float(input("Ingrese la nota a agregar: "))
        notas.append(nota)
        print(f"✅ Nota {nota} agregada correctamente.")
    except ValueError:
        print("🛑 ¡Entrada inválida! Debe ingresar un número para la nota.")

elif opcion == 2:
    # --- Mostrar todas las notas ---
    if notas:
        print("\n--- LISTA DE NOTAS ---")
        for i, nota in enumerate(notas):
            print(f"Nota #{i+1}: {nota}")
    else:
        print("ℹ️ Aún no hay notas registradas.")

elif opcion == 3:
    # --- Calcular promedio, mayor y menor ---
    if notas:
        promedio = sum(notas) / len(notas)
        mayor = max(notas)
        menor = min(notas)
        print("\n--- RESULTADOS ---")
        print(f"📊 Promedio de notas: {promedio:.2f}")
        print(f"⭐ Nota más alta: {mayor}")
        print(f"⬇️ Nota más baja: {menor}")
    else:
        print("ℹ️ No hay notas registradas para calcular estadísticas.")

elif opcion == 4:
    # --- Terminar programa ---
    print("👋 Programa finalizado. ¡Hasta luego!")
    break

elif opcion == 5:
    # --- Modificar nota ---
    if notas:
        print("\n--- MODIFICAR NOTA ---")
        for i, nota in enumerate(notas):
            print(f"{i+1}. {nota}")
        try:
            indice = int(input("Ingrese el número de la nota que desea modificar: ")) - 1
            if 0 <= indice < len(notas):
                nueva_nota = float(input("Ingrese la nueva nota: "))
                notas[indice] = nueva_nota
                print("✅ Nota modificada correctamente.")
            else:
                print("🛑 Número fuera de rango.")
        except ValueError:
            print("🛑 Entrada inválida. Debe ingresar números válidos.")
    else:
        print("ℹ️ No hay notas para modificar.")

elif opcion == 6:
    # --- Eliminar nota ---
    if notas:
        print("\n--- ELIMINAR NOTA ---")
        for i, nota in enumerate(notas):
            print(f"{i+1}. {nota}")
        try:
            indice = int(input("Ingrese el número de la nota que desea eliminar: ")) - 1
            if 0 <= indice < len(notas):
                nota_eliminada = notas.pop(indice)
                print(f"✅ Nota {nota_eliminada} eliminada correctamente.")
            else:
                print("🛑 Número fuera de rango.")
        except ValueError:
            print("🛑 Entrada inválida. Debe ingresar un número válido.")
    else:
        print("ℹ️ No hay notas para eliminar.")

else:
    print("🛑 Opción fuera del rango (1-6). Intente nuevament