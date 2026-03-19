# DATOS

| Nombre | Carnet | 
|--------|--------|
| Gerardo Josue Toledo Dondiego | 9490_24_6844 |
---

# Árbol Binario de Busqueda (ABB) - Programa Interactivo

## Descripcion

Programa interactivo en Python que permite crear, manipular y visualizar
un arbol Binario de Busqueda (ABB) a traves de una interfaz de linea de
comandos, genera automaticamente la representacion grafica del arbol
usando Graphviz.

---

## Ejecucion
python main.py

---


## Funcionalidades

| Opción | Función | Descripción |
|:------:|---------|-------------|
| 1 | Insertar | Agrega un valor numérico al árbol |
| 2 | Buscar | Busca un valor y muestra el camino recorrido |
| 3 | Eliminar | Elimina un valor manejando los 3 casos (hoja, un hijo, dos hijos) |
| 4 | Cargar CSV | Lee números desde un archivo `.csv` indicando la ruta |
| 5 | Convertir a binario | Muestra cada valor del árbol en representación binaria |
| 6 | Visualizar | Muestra el árbol en consola y genera el gráfico Graphviz |
| 7 | Recorridos | Muestra Inorden, Preorden y Postorden |
| 8 | Limpiar | Elimina todos los nodos del árbol |
| 0 | Salir | Cierra el programa |

---


## Notas

No se permiten valores duplicados en el árbol.

La eliminación utiliza el sucesor inorden cuando el nodo tiene dos hijos.

Cada operación de inserción, eliminación y carga actualiza automáticamente

el archivo Graphviz.

Los archivos generados se guardan en la carpeta output/.


