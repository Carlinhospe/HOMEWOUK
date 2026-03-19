
import csv
import os
import subprocess


class Nodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    

    def __init__(self):
        self.raiz = None
        self.tamaio = 0

    

    def insertar(self, valor):
        
        if self.raiz is None:
            self.raiz = Nodo(valor)
            self.tamaio += 1
            return True
        return self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
                self.tamaio += 1
                return True
            return self._insertar_rec(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
                self.tamaio += 1
                return True
            return self._insertar_rec(nodo.derecho, valor)
        return False  

    

    def buscar(self, valor):
        
        camino = []
        encontrado = self._buscar_rec(self.raiz, valor, camino)
        return encontrado, camino

    def _buscar_rec(self, nodo, valor, camino):
        if nodo is None:
            return False
        camino.append(nodo.valor)
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_rec(nodo.izquierdo, valor, camino)
        else:
            return self._buscar_rec(nodo.derecho, valor, camino)

 

    def eliminar(self, valor):
        
        self.raiz, eliminado = self._eliminar_rec(self.raiz, valor)
        if eliminado:
            self.tamaio -= 1
        return eliminado

    def _eliminar_rec(self, nodo, valor):
        if nodo is None:
            return None, False

        if valor < nodo.valor:
            nodo.izquierdo, eliminado = self._eliminar_rec(nodo.izquierdo, valor)
            return nodo, eliminado
        elif valor > nodo.valor:
            nodo.derecho, eliminado = self._eliminar_rec(nodo.derecho, valor)
            return nodo, eliminado
        else:
            
            if nodo.izquierdo is None and nodo.derecho is None:
                return None, True
            
            if nodo.izquierdo is None:
                return nodo.derecho, True
            if nodo.derecho is None:
                return nodo.izquierdo, True
            
            sucesor = nodo.derecho
            while sucesor.izquierdo:
                sucesor = sucesor.izquierdo
            nodo.valor = sucesor.valor
            nodo.derecho, _ = self._eliminar_rec(nodo.derecho, sucesor.valor)
            return nodo, True

    

    def inorden(self):
        
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecho, resultado)

    def preorden(self):
        resultado = []
        self._preorden_rec(self.raiz, resultado)
        return resultado

    def _preorden_rec(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_rec(nodo.izquierdo, resultado)
            self._preorden_rec(nodo.derecho, resultado)

    def postorden(self):
        resultado = []
        self._postorden_rec(self.raiz, resultado)
        return resultado

    def _postorden_rec(self, nodo, resultado):
        if nodo:
            self._postorden_rec(nodo.izquierdo, resultado)
            self._postorden_rec(nodo.derecho, resultado)
            resultado.append(nodo.valor)

    

    def convertir_a_binario(self):
        
        resultado = {}
        for val in self.inorden():
            if isinstance(val, int):
                resultado[val] = bin(val) if val >= 0 else "-" + bin(abs(val))
            else:
                resultado[val] = "N/A"
        return resultado

    

    def altura(self):
        return self._altura_rec(self.raiz)

    def _altura_rec(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self._altura_rec(nodo.izquierdo),
                       self._altura_rec(nodo.derecho))

    

    def cargar_csv(self, ruta):
        
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"Archivo no encontrado: {ruta}")

        valores = []
        errores = []

        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read(1024)
            archivo.seek(0)
            delim = ";" if contenido.count(";") > contenido.count(",") else ","
            lector = csv.reader(archivo, delimiter=delim)

            for num_linea, fila in enumerate(lector, 1):
                for celda in fila:
                    celda = celda.strip()
                    if not celda:
                        continue
                    try:
                        valores.append(int(celda))
                    except ValueError:
                        try:
                            valores.append(float(celda))
                        except ValueError:
                            errores.append(f"Linea {num_linea}: '{celda}'")

        insertados = 0
        duplicados = 0
        for v in valores:
            if self.insertar(v):
                insertados += 1
            else:
                duplicados += 1

        return insertados, duplicados, errores

   

    def limpiar(self):
        self.raiz = None
        self.tamaio = 0

   

    def mostrar_consola(self):
        
        if self.raiz is None:
            print("  (arbol vacio)")
            return
        print()
        self._imprimir(self.raiz, "", True)
        print()

    def _imprimir(self, nodo, prefijo, es_ultimo):
        if nodo is None:
            return
        conector = "└── " if es_ultimo else "├── "
        print(f"  {prefijo}{conector}[{nodo.valor}]")
        nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
        hijos = []
        if nodo.izquierdo:
            hijos.append(nodo.izquierdo)
        if nodo.derecho:
            hijos.append(nodo.derecho)
        for i, hijo in enumerate(hijos):
            self._imprimir(hijo, nuevo_prefijo, i == len(hijos) - 1)

   

    def generar_graphviz(self, nombre="arbol"):
        
        if self.raiz is None:
            print("  El arbol esta vacio, no se genera grafico.")
            return

        if not os.path.exists("output"):
            os.makedirs("output")

        self._cont_nulo = 0
        lineas = [
            "digraph ABB {",
            '    node [shape=circle, style=filled, fillcolor="#cce5ff",',
            '           fontname="Arial", fontsize=12, color="#004085"];',
            '    edge [color="#004085"];',
            f'    labelloc="t"; label="ABB - {self.tamaio} nodos, '
            f'altura {self.altura()}";',
            '    fontname="Arial"; fontsize=16;',
            ""
        ]

        self._nodos_dot(self.raiz, lineas)
        lineas.append("}")

        codigo = "\n".join(lineas)

        ruta_dot = f"output/{nombre}.dot"
        ruta_png = f"output/{nombre}.png"

        with open(ruta_dot, "w", encoding="utf-8") as f:
            f.write(codigo)

        try:
            subprocess.run(["dot", "-Tpng", ruta_dot, "-o", ruta_png],
                           check=True, capture_output=True)
            print(f"  Imagen generada: {ruta_png}")
        except FileNotFoundError:
            print(f"  Graphviz no instalado. Archivo DOT guardado en: {ruta_dot}")
        except subprocess.CalledProcessError as e:
            print(f"  Error al generar imagen: {e.stderr}")

        print(f"  Archivo DOT: {ruta_dot}")

    def _nodos_dot(self, nodo, lineas):
        if nodo is None:
            return

        nid = f"n{id(nodo)}"
        lineas.append(f'    {nid} [label="{nodo.valor}"];')

        if nodo.izquierdo or nodo.derecho:
            if nodo.izquierdo:
                lid = f"n{id(nodo.izquierdo)}"
                lineas.append(f"    {nid} -> {lid};")
                self._nodos_dot(nodo.izquierdo, lineas)
            else:
                self._cont_nulo += 1
                nulo = f"nulo{self._cont_nulo}"
                lineas.append(f"    {nulo} [shape=point, width=0.1];")
                lineas.append(f"    {nid} -> {nulo} [style=dashed];")

            if nodo.derecho:
                rid = f"n{id(nodo.derecho)}"
                lineas.append(f"    {nid} -> {rid};")
                self._nodos_dot(nodo.derecho, lineas)
            else:
                self._cont_nulo += 1
                nulo = f"nulo{self._cont_nulo}"
                lineas.append(f"    {nulo} [shape=point, width=0.1];")
                lineas.append(f"    {nid} -> {nulo} [style=dashed];")