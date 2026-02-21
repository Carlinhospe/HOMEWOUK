import os
from graphviz import Digraph


class Visuali:
    def __init__(self):     
        self.carpeta = "imagenes"
        self.contador = 0
        os.makedirs(self.carpeta, exist_ok=True)

    def generar(self, lista, operacion="estado"):
        self.contador += 1
        nombre = f"{self.contador:02d}_{operacion}"
        ruta = os.path.join(self.carpeta, nombre)

        grafo = Digraph(
            format="png",
            graph_attr={
                "rankdir": "LR",
                "bgcolor": "#F0F4F8",
                "label": f"Operación: {operacion}  |  Nodos: {lista.tamanio}",
                "fontsize": "13",
            },
            node_attr={"shape": "record", "fontname": "Arial", "fontsize": "11"},
        )

        if lista.cabeza is None:
            grafo.node("vacio", "Lista vacía", shape="rectangle",
                       style="filled", fillcolor="#CCCCCC")

        else:
           
            for n_id, label in [("null_izq", "NULL"), ("null_der", "NULL")]:
                grafo.node(n_id, label, shape="rectangle",
                           style="filled,rounded",
                           fillcolor="#E74C3C", fontcolor="white")

            
            nodos = []
            actual = lista.cabeza
            while actual:
                nodos.append(actual)
                actual = actual.siguiente

                       # cabeza / medio / final
            colores = ["#2ECC71", "#F39C12", "#3498DB"]   

            for i, nodo in enumerate(nodos):
                nid = f"n{i}"
                if len(nodos) == 1:
                    color = "#9B59B6"          
                elif i == 0:
                    color = colores[0]         
                elif i == len(nodos) - 1:
                    color = colores[2]         
                else:
                    color = colores[1]         

                label = (
                    f"{{<p> ◄ |"
                    f"{{ {nodo.nombre} {nodo.apellido} | {nodo.carnet} }}|"
                    f"<n> ► }}"
                )
                grafo.node(nid, label, style="filled",
                           fillcolor=color, fontcolor="white")

            grafo.edge("null_izq", "n0:p", color="#E74C3C", style="dashed")

            
            for i in range(len(nodos) - 1):
                grafo.edge(f"n{i}:n", f"n{i+1}:p",
                           label="sig", color="#2C3E50")
                grafo.edge(f"n{i+1}:p", f"n{i}:n",
                           label="ant", color="#8E44AD", style="dashed")

            
            grafo.edge(f"n{len(nodos)-1}:n", "null_der",
                       color="#E74C3C", style="dashed")

        grafo.render(ruta, cleanup=True)
        print(f" Imagen guardada → {ruta}.png")