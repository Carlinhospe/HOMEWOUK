import csv
import os
import sys
from graphviz import Digraph

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class NodoBTree:
    def __init__(self, hoja=True):
        self.claves = []
        self.hijos = []
        self.hoja = hoja

class ArbolB:
    def __init__(self, grado):
        if grado < 3:
            raise ValueError("El grado debe ser al menos 3.")
        self.grado   = grado
        self.max_cl  = grado - 1        
        self.min_cl  = self.max_cl // 2 
        self.raiz    = NodoBTree()
        self.total_claves = 0

    def _lleno(self, n):
        return len(n.claves) == self.max_cl

    def buscar(self, k, n=None):
        n = n or self.raiz
        i = 0
        while i < len(n.claves) and k > n.claves[i]:
            i += 1
        if i < len(n.claves) and k == n.claves[i]:
            return (n, i)
        return None if n.hoja else self.buscar(k, n.hijos[i])

    def insertar(self, k):
        if self.buscar(k):
            return False
        if self._lleno(self.raiz):
            nueva = NodoBTree(hoja=False)
            nueva.hijos.append(self.raiz)
            self._dividir(nueva, 0)
            self.raiz = nueva
        self._ins(self.raiz, k)
        self.total_claves += 1
        return True

    def _ins(self, n, k):
        i = len(n.claves) - 1
        if n.hoja:
            n.claves.append(None)
            while i >= 0 and k < n.claves[i]:
                n.claves[i + 1] = n.claves[i]
                i -= 1
            n.claves[i + 1] = k
        else:
            while i >= 0 and k < n.claves[i]:
                i -= 1
            i += 1
            if self._lleno(n.hijos[i]):
                self._dividir(n, i)
                if k > n.claves[i]:
                    i += 1
            self._ins(n.hijos[i], k)

    def _dividir(self, padre, i):
        mid  = self.max_cl // 2
        lleno = padre.hijos[i]
        nuevo = NodoBTree(hoja=lleno.hoja)
        padre.claves.insert(i, lleno.claves[mid])
        padre.hijos.insert(i + 1, nuevo)
        nuevo.claves = lleno.claves[mid + 1:]
        lleno.claves = lleno.claves[:mid]
        if not lleno.hoja:
            nuevo.hijos = lleno.hijos[mid + 1:]
            lleno.hijos = lleno.hijos[:mid + 1]

    def eliminar(self, k):
        if not self.raiz.claves:
            print("El arbol esta vacio."); return False
        ok = self._del(self.raiz, k)
        if ok:
            if not self.raiz.claves and not self.raiz.hoja:
                self.raiz = self.raiz.hijos[0]
            self.total_claves -= 1
        else:
            print(f"Clave '{k}' no encontrada.")
        return ok

    def _del(self, n, k):
        i = 0
        while i < len(n.claves) and k > n.claves[i]:
            i += 1
        if i < len(n.claves) and k == n.claves[i]:
            if n.hoja:
                n.claves.pop(i); return True
            return self._del_interno(n, i)
        if n.hoja:
            return False
        ultimo = (i == len(n.claves))
        if len(n.hijos[i].claves) <= self.min_cl:
            self._rellenar(n, i)
            if ultimo and i > len(n.claves):
                i -= 1
        return self._del(n.hijos[i], k)

    def _del_interno(self, n, i):
        k = n.claves[i]
        if len(n.hijos[i].claves) > self.min_cl:
            p = self._extremo(n.hijos[i], False)
            n.claves[i] = p
            return self._del(n.hijos[i], p)
        if len(n.hijos[i + 1].claves) > self.min_cl:
            s = self._extremo(n.hijos[i + 1], True)
            n.claves[i] = s
            return self._del(n.hijos[i + 1], s)
        self._fusionar(n, i)
        return self._del(n.hijos[i], k)

    def _extremo(self, n, izq):
        while not n.hoja:
            n = n.hijos[0] if izq else n.hijos[-1]
        return n.claves[0] if izq else n.claves[-1]

    def _rellenar(self, n, i):
        if i > 0 and len(n.hijos[i - 1].claves) > self.min_cl:
            self._rotar_der(n, i)
        elif i < len(n.claves) and len(n.hijos[i + 1].claves) > self.min_cl:
            self._rotar_izq(n, i)
        else:
            self._fusionar(n, i if i < len(n.claves) else i - 1)

    def _rotar_der(self, n, i):
        h, herm = n.hijos[i], n.hijos[i - 1]
        h.claves.insert(0, n.claves[i - 1])
        n.claves[i - 1] = herm.claves.pop()
        if not herm.hoja:
            h.hijos.insert(0, herm.hijos.pop())

    def _rotar_izq(self, n, i):
        h, herm = n.hijos[i], n.hijos[i + 1]
        h.claves.append(n.claves[i])
        n.claves[i] = herm.claves.pop(0)
        if not herm.hoja:
            h.hijos.append(herm.hijos.pop(0))

    def _fusionar(self, n, i):
        h, herm = n.hijos[i], n.hijos[i + 1]
        h.claves.append(n.claves.pop(i))
        h.claves.extend(herm.claves)
        if not h.hoja:
            h.hijos.extend(herm.hijos)
        n.hijos.pop(i + 1)

    def inorden(self, n=None, res=None):
        if res is None: res = []
        n = n or self.raiz
        for i in range(len(n.claves)):
            if not n.hoja: self.inorden(n.hijos[i], res)
            res.append(n.claves[i])
        if not n.hoja: self.inorden(n.hijos[-1], res)
        return res

    def altura(self, n=None):
        n = n or self.raiz
        return 0 if n.hoja else 1 + self.altura(n.hijos[0])

    def graficar(self, nombre="arbol_b"):
        dot = Digraph()
        dot.attr("graph",
                 label=f"Arbol B | Grado={self.grado} | Max claves={self.max_cl} | Min claves={self.min_cl} | Total={self.total_claves} | Altura={self.altura()}",
                 fontsize="12", labelloc="t")
        dot.attr("node", shape="record", fontsize="10")
        cnt = [0]

        def agregar(n):
            nid = f"n{cnt[0]}"; cnt[0] += 1
            if n.hoja:
                lbl = "|".join(f"<f{j}> {n.claves[j]}" for j in range(len(n.claves)))
                dot.node(nid, f"{{{lbl}}}", style="filled", fillcolor="lightblue")
            else:
                partes = ["<p0>"]
                for j, k in enumerate(n.claves):
                    partes += [f"<k{j}> {k}", f"<p{j+1}>"]
                dot.node(nid, "{" + "|".join(partes) + "}", style="filled", fillcolor="lightyellow")
            if not n.hoja:
                for j, hijo in enumerate(n.hijos):
                    hid = agregar(hijo)
                    dot.edge(f"{nid}:p{j}", hid)
            return nid

        agregar(self.raiz) if self.raiz.claves else dot.node("v", "Arbol vacio", shape="ellipse")
        os.makedirs(os.path.join(BASE_DIR, "output"), exist_ok=True)
        ruta = os.path.join(BASE_DIR, "output", nombre)
        dot.render(ruta, format="png", cleanup=True)
        print(f"Grafico guardado en: output/{nombre}.png")


def _info_csv(archivo, clave, descripcion):
    columnas = []
    ruta = os.path.join(BASE_DIR, archivo)
    if os.path.exists(ruta):
        with open(ruta, newline="", encoding="utf-8") as f:
            columnas = csv.DictReader(f).fieldnames or []
    return {"columna_clave": clave, "descripcion": descripcion, "columnas": columnas}

ARCHIVOS_CSV_INFO = {
    "productos.csv"    : _info_csv("productos.csv",     "codigo_producto", "Catalogo de productos (130 registros)"),
    "empleados.csv"    : _info_csv("empleados.csv",     "id_empleado",     "Registro de empleados (115 registros)"),
    "transacciones.csv": _info_csv("transacciones.csv", "id_transaccion",  "Historial de transacciones (160 registros)"),
    "estudiantes.csv"  : _info_csv("estudiantes.csv",   "id_estudiante",   "Registro de estudiantes (110 registros)"),
}

def cargar_csv(arbol, ruta, columna=None):
    nb = os.path.basename(ruta)
    if not os.path.isabs(ruta):
        abs_r = os.path.join(BASE_DIR, ruta)
        if os.path.exists(abs_r): ruta = abs_r
    if not os.path.exists(ruta):
        print(f"Archivo no encontrado: {ruta}"); return 0
    if columna is None and nb in ARCHIVOS_CSV_INFO:
        columna = ARCHIVOS_CSV_INFO[nb]["columna_clave"]
        print(f"Columna detectada: '{columna}'")
    ins = omit = 0
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        cols = lector.fieldnames or []
        if not columna: columna = cols[0]
        if columna not in cols:
            print(f"Columna '{columna}' no existe. Disponibles: {cols}"); return 0
        print(f"Columna en uso: '{columna}'")
        for fila in lector:
            raw = fila.get(columna, "").strip()
            if not raw: omit += 1; continue
            try: val = int(raw)
            except ValueError:
                try: val = float(raw)
                except ValueError: val = raw
            if arbol.insertar(val): ins += 1
            else: omit += 1
    print(f"Insertados: {ins} | Omitidos: {omit}")
    return ins

def mostrar_csvs():
    print("\nArchivos CSV del proyecto:")
    encontrados = 0
    for arch, info in ARCHIVOS_CSV_INFO.items():
        existe = os.path.exists(os.path.join(BASE_DIR, arch))
        print(f"  [{'OK' if existe else 'NO'}] {arch} — {info['descripcion']} — clave: {info['columna_clave']}")
        if existe: encontrados += 1
    if not encontrados:
        print("  No se encontraron archivos. Ejecute: python generar_csv.py")

def pedir_clave(msg="Ingrese la clave: "):
    raw = input(msg).strip()
    if not raw: return None
    try: return int(raw)
    except ValueError:
        try: return float(raw)
        except ValueError: return raw

def configurar():
    print("\nConfiguracion del Arbol B")
    print("  El GRADO define el maximo de claves por nodo.")
    print("  Max claves = grado - 1  |  Min claves = max // 2")
    while True:
        try:
            g = int(input("Ingrese el grado (>= 3): ").strip())
            if g >= 3:
                print(f"  Grado {g} -> Max claves: {g-1} | Min claves: {(g-1)//2}")
                return g
            print("Debe ser >= 3.")
        except ValueError:
            print("Ingrese un entero valido.")

def menu(arbol):
    print("\n" + "=" * 50)
    print(f"  MENU  |  Grado={arbol.grado}  Max={arbol.max_cl}  Min={arbol.min_cl}  Claves={arbol.total_claves}")
    print("=" * 50)
    for n, op in enumerate(["Insertar clave","Buscar clave","Eliminar clave","Cargar CSV",
                             "Mostrar en orden","Informacion del arbol","Generar grafico",
                             "Reiniciar arbol"], 1):
        print(f"  {n}. {op}")
    print("  0. Salir")
    print("=" * 50)

def main():
    print("=" * 50)
    print("   ARBOL B CONFIGURABLE — PYTHON")
    print("=" * 50)
    arbol = ArbolB(configurar())

    while True:
        menu(arbol)
        op = input("Opcion: ").strip()

        if op == "1":
            k = pedir_clave()
            if k is None: print("Clave invalida.")
            elif arbol.insertar(k): print(f"'{k}' insertada. Total: {arbol.total_claves}")
            else: print(f"'{k}' ya existe.")

        elif op == "2":
            k = pedir_clave()
            if k is None: print("Clave invalida.")
            else:
                res = arbol.buscar(k)
                if res: print(f"'{k}' encontrada — nodo: {res[0].claves} — indice: {res[1]}")
                else:   print(f"'{k}' no encontrada.")

        elif op == "3":
            k = pedir_clave()
            if k is None: print("Clave invalida.")
            elif arbol.eliminar(k): print(f"'{k}' eliminada. Total: {arbol.total_claves}")

        elif op == "4":
            mostrar_csvs()
            ruta = input("Ruta del CSV: ").strip()
            if not ruta: continue
            nb = os.path.basename(ruta)
            if nb in ARCHIVOS_CSV_INFO:
                print("Columnas disponibles:")
                for c in ARCHIVOS_CSV_INFO[nb]["columnas"]:
                    marca = " <-- recomendada" if c == ARCHIVOS_CSV_INFO[nb]["columna_clave"] else ""
                    print(f"  - {c}{marca}")
            col = input("Columna (Enter = automatico): ").strip() or None
            cargar_csv(arbol, ruta, col)

        elif op == "5":
            if not arbol.total_claves: print("El arbol esta vacio.")
            else:
                cl = arbol.inorden()
                print(f"Total: {len(cl)}")
                print(cl if len(cl) <= 60 else f"{cl[:30]} ... {cl[-30:]}")

        elif op == "6":
            print(f"Grado         : {arbol.grado}")
            print(f"Max claves    : {arbol.max_cl}  (grado - 1)")
            print(f"Min claves    : {arbol.min_cl}  (max // 2)")
            print(f"Total claves  : {arbol.total_claves}")
            print(f"Altura        : {arbol.altura()}")
            if arbol.total_claves:
                cl = arbol.inorden()
                print(f"Min / Max     : {cl[0]} / {cl[-1]}")
                print(f"Raiz          : {arbol.raiz.claves}")

        elif op == "7":
            if not arbol.total_claves: print("El arbol esta vacio.")
            else:
                nombre = input("Nombre del archivo [arbol_b]: ").strip() or "arbol_b"
                try: arbol.graficar(nombre)
                except Exception as e: print(f"Error al graficar: {e}")

        elif op == "8":
            if input("Reiniciar? Se perderan los datos (s/n): ").strip().lower() == "s":
                arbol = ArbolB(configurar())
                print(f"Arbol reiniciado. Grado={arbol.grado} Max={arbol.max_cl} Min={arbol.min_cl}")

        elif op == "0":
            print("Saliendo..."); sys.exit(0)

        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()