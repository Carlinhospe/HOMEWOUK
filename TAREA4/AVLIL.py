import csv
import os
import subprocess

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

class ABB:
    def __init__(self):
        self.raiz = None
        self.total_nodos = 0

    def insertar(self, valor):
        if self.buscar(valor):
            print(f" {valor} ya existe.")
            return
        self.raiz = self._ins(self.raiz, valor)
        self.total_nodos += 1

    def _ins(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._ins(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._ins(nodo.der, valor)
        return nodo

    def buscar(self, valor):
        return self._bus(self.raiz, valor)

    def _bus(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        return self._bus(nodo.izq, valor) if valor < nodo.valor else self._bus(nodo.der, valor)

    def eliminar(self, valor):
        if not self.buscar(valor):
            return False
        self.raiz = self._eli(self.raiz, valor)
        self.total_nodos -= 1
        return True

    def _eli(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izq = self._eli(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eli(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            if nodo.der is None:
                return nodo.izq
            suc = self._min_nodo(nodo.der)
            nodo.valor = suc.valor
            nodo.der = self._eli(nodo.der, suc.valor)
        return nodo

    def _min_nodo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def esta_vacio(self):
        return self.raiz is None

    def inorden(self):
        res = []
        self._ino(self.raiz, res)
        return res

    def _ino(self, nodo, res):
        if nodo:
            self._ino(nodo.izq, res)
            res.append(nodo.valor)
            self._ino(nodo.der, res)


class AVL(ABB):
    def _rot_der(self, z):
        y = z.izq
        T3 = y.der
        y.der = z
        z.izq = T3
        z.altura = 1 + max(self._altura(z.izq), self._altura(z.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        return y

    def _rot_izq(self, z):
        y = z.der
        T2 = y.izq
        y.izq = z
        z.der = T2
        z.altura = 1 + max(self._altura(z.izq), self._altura(z.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        return y

    def _fb(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0

    def insertar(self, valor):
        if self.buscar(valor):
            print(f" {valor} ya existe.")
            return
        self.raiz = self._ins_avl(self.raiz, valor)
        self.total_nodos += 1
        print(f" {valor} insertado.")

    def _ins_avl(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._ins_avl(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._ins_avl(nodo.der, valor)
        else:
            return nodo

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        fb = self._fb(nodo)

        if fb > 1 and valor < nodo.izq.valor:
            return self._rot_der(nodo)
        if fb < -1 and valor > nodo.der.valor:
            return self._rot_izq(nodo)
        if fb > 1 and valor > nodo.izq.valor:
            nodo.izq = self._rot_izq(nodo.izq)
            return self._rot_der(nodo)
        if fb < -1 and valor < nodo.der.valor:
            nodo.der = self._rot_der(nodo.der)
            return self._rot_izq(nodo)

        return nodo

    def eliminar(self, valor):
        if not self.buscar(valor):
            print(f"  {valor} no existe.")
            return False
        self.raiz = self._eli_avl(self.raiz, valor)
        self.total_nodos -= 1
        print(f"  [✓] {valor} eliminado.")
        return True

    def _eli_avl(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izq = self._eli_avl(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eli_avl(nodo.der, valor)
        else:
            if nodo.izq is None:
                return nodo.der
            if nodo.der is None:
                return nodo.izq
            suc = self._min_nodo(nodo.der)
            nodo.valor = suc.valor
            nodo.der = self._eli_avl(nodo.der, suc.valor)

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        fb = self._fb(nodo)

        if fb > 1 and self._fb(nodo.izq) >= 0:
            return self._rot_der(nodo)
        if fb > 1 and self._fb(nodo.izq) < 0:
            nodo.izq = self._rot_izq(nodo.izq)
            return self._rot_der(nodo)
        if fb < -1 and self._fb(nodo.der) <= 0:
            return self._rot_izq(nodo)
        if fb < -1 and self._fb(nodo.der) > 0:
            nodo.der = self._rot_der(nodo.der)
            return self._rot_izq(nodo)

        return nodo

    def info(self):
        print(f"\n  Nodos  : {self.total_nodos}")
        print(f"  Altura : {self._altura(self.raiz)}")
        print(f"  Inorden: {self.inorden()}")


class Visualizador:
    def __init__(self, arbol: AVL):
        self.arbol   = arbol
        
        self.base    = os.path.dirname(os.path.abspath(__file__))
        self.carpeta = os.path.join(self.base, "avl_graphviz")
        self.DOT     = os.path.join(self.carpeta, "arbol.dot")
        self.PNG     = os.path.join(self.carpeta, "arbol.png")
        os.makedirs(self.carpeta, exist_ok=True)

    def actualizar(self):
        self._escribir_dot()
        self._compilar_png()

    def _escribir_dot(self):
        lineas = [
            "digraph ArbolAVL {",
            '    graph [label="Árbol AVL" fontsize=18 fontname="Helvetica" bgcolor="#1e1e2e"];',
            '    node  [shape=circle style=filled fontcolor=white fontname="Helvetica" fontsize=13];',
            '    edge  [color="#aaaaaa" penwidth=1.5];',
            "",
        ]

        if self.arbol.esta_vacio():
            lineas.append(' vacio [label="vacío" shape=plaintext fontcolor=white];')
        else:
            self._nodos_dot(self.arbol.raiz, lineas)

        lineas.append("}")

        with open(self.DOT, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))

    def _nodos_dot(self, nodo, lineas, padre=None):
        if nodo is None:
            return

        fb    = self.arbol._fb(nodo)
        color = "#27AE60" if fb == 0 else "#E67E22" if abs(fb) == 1 else "#E74C3C"
        etiq  = f"{nodo.valor}\\nH={nodo.altura}  FB={fb:+d}"

        lineas.append(f' n{nodo.valor} [label="{etiq}" fillcolor="{color}"];')

        if padre is not None:
            lineas.append(f"n{padre.valor} -> n{nodo.valor};")

        for lado, hijo in [("L", nodo.izq), ("R", nodo.der)]:
            if hijo is None and (nodo.izq is not None or nodo.der is not None):
                nid = f"nulo_{lado}_{nodo.valor}"
                lineas.append(
                    f'    {nid} [label="" shape=point width=0.12'
                    f' style=filled fillcolor="#555555"];'
                )
                lineas.append(f"    n{nodo.valor} -> {nid};")

        self._nodos_dot(nodo.izq, lineas, nodo)
        self._nodos_dot(nodo.der, lineas, nodo)

    def _compilar_png(self):
        try:
            subprocess.run(
                ["dot", "-Tpng", self.DOT, "-o", self.PNG],
                check=True, capture_output=True,
            )
            print(f"  [✓] PNG actualizado → {self.PNG}")
            self._abrir()
        except FileNotFoundError:
            print("   Graphviz no instalado.")
            print(f"   DOT guardado en: {self.DOT}")
            print("   Pega el contenido en: https://dreampuf.github.io/GraphvizOnline/")
        except subprocess.CalledProcessError as e:
            print(f"   Error Graphviz: {e.stderr.decode()}")

    def _abrir(self):
        try:
            if os.name == "nt":
                os.startfile(self.PNG)
            elif os.uname().sysname == "Darwin":
                subprocess.Popen(["open", self.PNG])
            else:
                subprocess.Popen(["xdg-open", self.PNG])
        except Exception:
            pass


class CSV:
    
    BASE = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def _resolver_ruta(ruta: str) -> str:
    
        if os.path.isabs(ruta):
            return ruta
        ruta_py = os.path.join(CSV.BASE, ruta)
        if os.path.exists(ruta_py):
            return ruta_py
        ruta_cwd = os.path.abspath(ruta)
        if os.path.exists(ruta_cwd):
            return ruta_cwd
        return ruta_py

    @staticmethod
    def cargar(arbol: AVL, ruta: str):
        ruta_real = CSV._resolver_ruta(ruta)

        if not os.path.exists(ruta_real):
            print(f"   No existe: {ruta_real}")
            print(f"   Archivos CSV encontrados en '{CSV.BASE}':")
            encontrados = []
            for raiz_dir, _, archivos in os.walk(CSV.BASE):
                for arch in archivos:
                    if arch.endswith(".csv"):
                        rel = os.path.relpath(os.path.join(raiz_dir, arch), CSV.BASE)
                        encontrados.append(f"      • {rel}")
            if encontrados:
                print("\n".join(encontrados))
            else:
                print(" (ninguno encontrado) ")
            return 0

        ok = err = 0
        with open(ruta_real, newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            primera = next(lector, None)
            if primera:
                for c in primera:
                    try:
                        arbol.insertar(int(c.strip()))
                        ok += 1
                    except ValueError:
                        pass 

            for fila in lector:
                for c in fila:
                    c = c.strip()
                    if c:
                        try:
                            arbol.insertar(int(c))
                            ok += 1
                        except ValueError:
                            err += 1

        print(f"  Insertados: {ok}  |  Errores: {err}")
        return ok

class CLI:
    SEP = "─" * 50

    def __init__(self):
        self.arbol = AVL()
        self.vis   = Visualizador(self.arbol)

    def run(self):
        while True:
            self._encabezado()
            print("  [1] Insertar      [2] Buscar      [3] Eliminar")
            print("  [4] Cargar CSV    [5] Visualizar  [6] Info árbol")
            print("  [7] Limpiar árbol [0] Salir")
            print(f"\n  {self.SEP}")
            op = input("\n  Opción: ").strip()

            if   op == "1": self._insertar()
            elif op == "2": self._buscar()
            elif op == "3": self._eliminar()
            elif op == "4": self._cargar_csv()
            elif op == "5": self._visualizar()
            elif op == "6": self.arbol.info()
            elif op == "7": self._limpiar()
            elif op == "0": print("\n  Hasta luego \n"); break
            else: print("  Opción inválida.")

            input("\n  Enter para continuar...")

    def _encabezado(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n  {self.SEP}")
        print("           ÁRBOL AVL ")
        print(f"  {self.SEP}")
        print(f"  Nodos: {self.arbol.total_nodos}  |  Altura: {self.arbol._altura(self.arbol.raiz)}")
        print(f"  {self.SEP}\n")

    def _insertar(self):
        entrada = input("  Número(s) separados por coma: ").strip()
        for p in entrada.split(","):
            try:
                self.arbol.insertar(int(p.strip()))
            except ValueError:
                print(f"  '{p.strip()}' no es entero.")
        self.vis.actualizar()

    def _buscar(self):
        try:
            v = int(input("  Número a buscar: ").strip())
            r = self.arbol.buscar(v)
            print(f"  [{'✓' if r else '✗'}] {v} {'SÍ' if r else 'NO'} está en el árbol.")
        except ValueError:
            print("  Ingresa un entero.")

    def _eliminar(self):
        if self.arbol.esta_vacio():
            print("  El árbol está vacío.")
            return
        entrada = input("  Número(s) separados por coma: ").strip()
        for p in entrada.split(","):
            try:
                self.arbol.eliminar(int(p.strip()))
            except ValueError:
                print(f"  '{p.strip()}' no es entero.")
        self.vis.actualizar()

    def _cargar_csv(self):
        
        base = os.path.dirname(os.path.abspath(__file__))
        csvs = []
        for raiz_dir, _, archivos in os.walk(base):
            for arch in archivos:
                if arch.endswith(".csv"):
                    rel = os.path.relpath(os.path.join(raiz_dir, arch), base)
                    csvs.append(rel)

        if csvs:
            print("  CSVs disponibles:")
            for c in csvs:
                print(f"    • {c}")
        else:
            print("  (no se encontraron CSVs)")

        ruta = input("\n  Ruta del CSV: ").strip()
        if not ruta:
            print("  No ingresaste ninguna ruta.")
            return

        if input("  ¿Limpiar árbol antes? (s/n): ").strip().lower() == "s":
            self.arbol = AVL()
            self.vis   = Visualizador(self.arbol)
            print("  Árbol limpiado.")

        CSV.cargar(self.arbol, ruta)
        self.vis.actualizar()

    def _visualizar(self):
        if self.arbol.esta_vacio():
            print(" El árbol está vacío.")
            return
        self.vis.actualizar()

    def _limpiar(self):
        if input("  ¿Seguro? (s/n): ").strip().lower() == "s":
            self.arbol = AVL()
            self.vis   = Visualizador(self.arbol)
            print("  Árbol limpiado.")


if __name__ == "__main__":
    CLI().run()