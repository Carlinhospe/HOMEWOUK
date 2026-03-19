
import os
import sys
from abb import ArbolBinarioBusqueda

MENU = """
======================================
   ARBOL BINARIO DE BUSQUEDA (ABB)
======================================
  1. Insertar valor
  2. Buscar valor
  3. Eliminar valor
  4. Cargar desde archivo CSV
  5. Convertir a binario
  6. Visualizar arbol
  7. Recorridos
  8. Limpiar arbol
  0. Salir
======================================"""


def leer_numero(mensaje):
    
    while True:
        entrada = input(mensaje).strip()
        if entrada.lower() in ("q", "cancelar"):
            return None
        try:
            return int(entrada)
        except ValueError:
            try:
                return float(entrada)
            except ValueError:
                print("  Numero no valido. Intente de nuevo (o 'q' para cancelar).")


def main():
    arbol = ArbolBinarioBusqueda()

    while True:
        print(MENU)
        if arbol.tamaio > 0:
            print(f"  Nodos: {arbol.tamaio} | Altura: {arbol.altura()}")
        else:
            print("  Arbol vacio")
        print()

        opcion = input("  Opcion: ").strip()

        
        if opcion == "1":
            print("\n  --- INSERTAR ---")
            valor = leer_numero("  Valor a insertar: ")
            if valor is None:
                print("  Cancelado.")
            elif arbol.insertar(valor):
                print(f"  Insertado: {valor}")
                arbol.mostrar_consola()
                arbol.generar_graphviz()
            else:
                print(f"  {valor} ya existe en el arbol.")

        
        elif opcion == "2":
            print("\n  --- BUSCAR ---")
            if arbol.tamaio == 0:
                print("  Arbol vacio.")
                continue
            valor = leer_numero("  Valor a buscar: ")
            if valor is None:
                print("  Cancelado.")
            else:
                encontrado, camino = arbol.buscar(valor)
                print(f"  Camino: {' -> '.join(map(str, camino))}")
                if encontrado:
                    print(f"  ENCONTRADO (profundidad {len(camino) - 1})")
                else:
                    print(f"  NO encontrado.")

        
        elif opcion == "3":
            print("\n  --- ELIMINAR ---")
            if arbol.tamaio == 0:
                print("  Arbol vacio.")
                continue
            print(f"  Valores: {arbol.inorden()}")
            valor = leer_numero("  Valor a eliminar: ")
            if valor is None:
                print("  Cancelado.")
            elif arbol.eliminar(valor):
                print(f"  Eliminado: {valor}")
                if arbol.tamaio > 0:
                    arbol.mostrar_consola()
                    arbol.generar_graphviz()
                else:
                    print("  El arbol quedo vacio.")
            else:
                print(f"  {valor} no existe en el arbol.")

        
        elif opcion == "4":
            print("\n  --- CARGAR CSV ---")

            
            csvs = [f for f in os.listdir(".") if f.endswith(".csv")]
            if csvs:
                print("  Archivos CSV disponibles:")
                for i, nombre in enumerate(csvs, 1):
                    print(f"    {i}. {nombre}")

            ruta = input("  Ruta del archivo (o numero de lista): ").strip()
            if ruta.lower() in ("q", "cancelar"):
                print("  Cancelado.")
                continue

            
            try:
                idx = int(ruta) - 1
                if 0 <= idx < len(csvs):
                    ruta = csvs[idx]
            except (ValueError, IndexError):
                pass

            
            if arbol.tamaio > 0:
                resp = input("  Limpiar arbol antes de cargar? (s/n): ").strip().lower()
                if resp in ("s", "si"):
                    arbol.limpiar()
                    print("  Arbol limpiado.")

            try:
                insertados, duplicados, errores = arbol.cargar_csv(ruta)
                print(f"\n  Resultado:")
                print(f"    Insertados: {insertados}")
                print(f"    Duplicados: {duplicados}")
                if errores:
                    print(f"    Ignorados:  {len(errores)}")
                    for e in errores[:3]:
                        print(f"      - {e}")
                if arbol.tamaio > 0:
                    arbol.mostrar_consola()
                    arbol.generar_graphviz()
            except FileNotFoundError as e:
                print(f"  Error: {e}")

        
        elif opcion == "5":
            print("\n  --- CONVERSION A BINARIO ---")
            if arbol.tamaio == 0:
                print("  Arbol vacio.")
                continue
            conversiones = arbol.convertir_a_binario()
            print(f"  {'Decimal':>10} | {'Binario'}")
            print(f"  {'-'*10}-+-{'-'*20}")
            for dec, bina in conversiones.items():
                print(f"  {dec:>10} | {bina}")

       
        elif opcion == "6":
            print("\n  --- VISUALIZAR ---")
            if arbol.tamaio == 0:
                print("  Arbol vacio.")
                continue
            print(f"  Nodos: {arbol.tamaio} | Altura: {arbol.altura()}")
            arbol.mostrar_consola()
            arbol.generar_graphviz()

        
        elif opcion == "7":
            print("\n  --- RECORRIDOS ---")
            if arbol.tamaio == 0:
                print("  Arbol vacio.")
                continue
            print(f"  Inorden:   {arbol.inorden()}")
            print(f"  Preorden:  {arbol.preorden()}")
            print(f"  Postorden: {arbol.postorden()}")

        
        elif opcion == "8":
            print("\n  --- LIMPIAR ---")
            if arbol.tamaio == 0:
                print("  Ya esta vacio.")
                continue
            resp = input(f"  Eliminar los {arbol.tamaio} nodos? (s/n): ").strip().lower()
            if resp in ("s", "si"):
                arbol.limpiar()
                print("  Arbol limpiado.")
            else:
                print("  Cancelado.")

        
        elif opcion == "0":
            print("\n  Hasta luego!\n")
            sys.exit(0)

        else:
            print("  Opcion no valida.")

        input("\n  Enter para continuar...")


if __name__ == "__main__":
    main()