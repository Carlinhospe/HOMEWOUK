
# TAREA1
## Gerardo Josue Toledo Dondiego | 9490-24-6844 | Seccion B
---
### Lista Doblemente Enlazada en Python

Sistema interactivo de lista doblemente enlazada con interfaz de línea de comandos (CLI)
y visualización gráfica mediante Graphviz.


### Descripción

Este proyecto implementa una lista doblemente enlazada donde cada nodo almacena
información de un estudiante (nombre, apellido y carnet) e ncluye un menú interactivo
para realizar operaciones y genera imágenes PNG de la estructura después de cada
modificación.

---

### Estructura del Proyecto
PROYECTO/

── nodo.py | los datos del estudiante

── lista.py | Clase ListaDoble con los métodos principales

── visuali.py | Generador de imágenes con Graphviz

── main.py | entrada con el menú interactivo

── imagenes/ | Se crea automáticamente al ejecutar


---

### Requisitos

| Software   | Versión          | Instalación                                                       |
|------------|------------------|-------------------------------------------------------------------|
| Python     | 3.10 o superior  | [python.org](https://www.python.org/downloads/)                   |
| Graphviz   | 14.x             | [graphviz.org](https://graphviz.org/download/)                    |
| pip        | Incluido con Python | Se instala automáticamente con Python                          |

---

Ejecución

python main.py

Se mostrará el
menú

---
# Ejemplo de Uso
## Insertar al principio

Opción: 1
  Nombre   : Carlos
  Apellido : López
  Carnet   : 2024001

[Carlos López | 2024001] insertado al principio.
Imagen guardada → imagenes/01_insertar_principio.png

---
## Insertar al final

Opción: 2
  Nombre   : María
  Apellido : García
  Carnet   : 2024002

[María García | 2024002] insertado al final.
Imagen guardada → imagenes/02_insertar_final.png

---
## Mostrar lista

Opción: 5

[Carlos López | 2024001] <-> [María García | 2024002]
None ← cabeza | cola → None  (2 nodo/s)
   
---
## Buscar por carnet

Opción: 4
  Carnet a buscar: 2024001

Encontrado en posición 1: [Carlos López | 2024001]

## Eliminar por carnet

Opción: 3
  Carnet a eliminar: 2024001

Nodo con carnet '2024001' eliminado.
Imagen guardada → imagenes/03_eliminar.png

---

Color	Significado

🟢 Verde	Nodo cabeza

🟡 Naranja	Nodo intermedio

🔵 Azul	Nodo cola

🟣 Morado	Nodo único

🔴 Rojo	NULL (extremos)



