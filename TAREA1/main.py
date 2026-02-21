from lista import ListaDo
from visuali import Visuali    


def menu():
    print("""
╔══════════════════════════════╗
║          OPCIONES            ║
╠══════════════════════════════╣
║  1. Insertar al principio    ║
║  2. Insertar al final        ║
║  3. Eliminar por carnet      ║
║  4. Buscar por carnet        ║
║  5. Mostrar lista            ║
║  6. Generar imagen           ║
║  0. Salir                    ║
╚══════════════════════════════╝""")


def pedir_datos():
    nombre   = input("  Nombre   : ").strip()
    apellido = input("  Apellido : ").strip()
    carnet   = input("  Carnet   : ").strip()
    return nombre, apellido, carnet


def main():
    lista = ListaDo()           
    vis   = Visuali()

    while True:
        menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre, apellido, carnet = pedir_datos()
            lista.insertar_al_principio(nombre, apellido, carnet)
            vis.generar(lista, "insertar_principio")

        elif opcion == "2":
            nombre, apellido, carnet = pedir_datos()
            lista.insertar_al_final(nombre, apellido, carnet)
            vis.generar(lista, "insertar_final")

        elif opcion == "3":
            carnet = input(" Carnet a eliminar: ").strip()
            lista.eliminar_por_valor(carnet)
            vis.generar(lista, "eliminar")

        elif opcion == "4":
            carnet = input(" Carnet a buscar: ").strip()
            lista.buscar(carnet)

        elif opcion == "5":
            lista.mostrar_lista()

        elif opcion == "6":
            vis.generar(lista, "manual")

        elif opcion == "0":
            print("👋 ¡Hasta luego! 👋")
            break

        else:
            print("❌❌ Opción no válida. ❌❌")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()