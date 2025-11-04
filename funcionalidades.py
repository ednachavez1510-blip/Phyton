# menú_notas.py
# Programa para gestionar notas: agregar, mostrar, estadísticas, modificar y eliminar.

notas = []

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar una nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio, mayor y menor")
    print("4. Terminar programa")
    print("5. Modificar nota")
    print("6. Eliminar nota")

def pedir_entero(prompt, minimo=None, maximo=None):
    """Pide un entero al usuario; opcionalmente verifica rango."""
    while True:
        try:
            valor = int(input(prompt).strip())
            if minimo is not None and valor < minimo:
                print(f"🛑 Debe ser >= {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"🛑 Debe ser <= {maximo}.")
                continue
            return valor
        except ValueError:
            print("🛑 Entrada inválida. Ingrese un número entero.")
        except (EOFError, KeyboardInterrupt):
            raise

def pedir_numero(prompt):
    """Pide un número (float) al usuario."""
    while True:
        try:
            texto = input(prompt).strip()
            return float(texto)
        except ValueError:
            print("🛑 Entrada inválida. Ingrese un número (ej: 7.5).")
        except (EOFError, KeyboardInterrupt):
            raise

def agregar_nota():
    try:
        nota = pedir_numero("Ingrese la nota a agregar: ")
        # Si quieres validar rango escolar (0-10), descomenta las siguientes líneas:
        # if not (0 <= nota <= 10):
        #     print("🛑 La nota debe estar entre 0 y 10.")
        #     return
        notas.append(nota)
        print(f"✅ Nota {nota} agregada correctamente.")
    except (EOFError, KeyboardInterrupt):
        print("\n✋ Entrada interrumpida. Volviendo al menú.")

def mostrar_notas():
    if notas:
        print("\n--- LISTA DE NOTAS ---")
        for i, nota in enumerate(notas, start=1):
            print(f"Nota #{i}: {nota}")
    else:
        print("ℹ️ Aún no hay notas registradas.")

def calcular_estadisticas():
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

def modificar_nota():
    if not notas:
        print("ℹ️ No hay notas para modificar.")
        return
    mostrar_notas()
    try:
        indice = pedir_entero("Ingrese el número de la nota que desea modificar: ", minimo=1, maximo=len(notas)) - 1
        nueva = pedir_numero("Ingrese la nueva nota: ")
        # Validación opcional (descomentar si la quieres):
        # if not (0 <= nueva <= 10):
        #     print("🛑 La nota debe estar entre 0 y 10.")
        #     return
        viejo = notas[indice]
        notas[indice] = nueva
        print(f"✅ Nota #{indice+1} modificada de {viejo} a {nueva}.")
    except (EOFError, KeyboardInterrupt):
        print("\n✋ Entrada interrumpida. Volviendo al menú.")

def eliminar_nota():
    if not notas:
        print("ℹ️ No hay notas para eliminar.")
        return
    mostrar_notas()
    try:
        indice = pedir_entero("Ingrese el número de la nota que desea eliminar: ", minimo=1, maximo=len(notas)) - 1
        eliminado = notas.pop(indice)
        print(f"✅ Nota {eliminado} eliminada correctamente.")
    except (EOFError, KeyboardInterrupt):
        print("\n✋ Entrada interrumpida. Volviendo al menú.")

def main():
    while True:
        try:
            mostrar_menu()
            opcion = pedir_entero("Seleccione una opción (1-6): ", minimo=1, maximo=6)
            if opcion == 1:
                agregar_nota()
            elif opcion == 2:
                mostrar_notas()
            elif opcion == 3:
                calcular_estadisticas()
            elif opcion == 4:
                print("👋 Programa finalizado. ¡Hasta luego!")
                break
            elif opcion == 5:
                modificar_nota()
            elif opcion == 6:
                eliminar_nota()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Interrupción detectada. Saliendo del programa.")
            break

if __name__ == "__main__":
    main()