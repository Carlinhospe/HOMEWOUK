from nodo import Nodo


class ListaDo:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

        self.tamanio += 1
        print(f"{nuevo} insertado al principio.")

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.cola is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

        self.tamanio += 1
        print(f"{nuevo} insertado al final.")

    def eliminar_por_valor(self, carnet):
        actual = self.cabeza

        while actual:
            if actual.carnet == carnet:
                
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior

                self.tamanio -= 1
                print(f"{actual} eliminado.")
                return True

            actual = actual.siguiente

        print(f" Carnet '{carnet}' no fue encontrado.")
        return False

    def mostrar_lista(self):
        if self.cabeza is None:
            print("Lista vacía.")
            return

        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(str(actual))
            actual = actual.siguiente

        print("📋 " + " <-> ".join(nodos))
        print(f"    None ← cabeza | cola → None  ({self.tamanio} nodo/s)")

    def buscar(self, carnet):
        actual = self.cabeza
        pos = 1
        while actual:
            if actual.carnet == carnet:
                print(f"encontrado en posición {pos}: {actual}")
                return actual
            actual = actual.siguiente
            pos += 1

        print(f"Carnet '{carnet}' no fue encontrado.")
        return None