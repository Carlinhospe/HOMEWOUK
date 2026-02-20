# HOMEWOUK1
### Gerardo Josue Toledo Dondiego | 9490-24-6844 | Seccion B
---
# Lista Doblemente Enlazada en Python

Sistema interactivo de lista doblemente enlazada con interfaz de línea de comandos (CLI)
y visualización gráfica mediante Graphviz.


## Descripción

Este proyecto implementa una lista doblemente enlazada donde cada nodo almacena
información de un estudiante (nombre, apellido y carnet) e ncluye un menú interactivo
para realizar operaciones y genera imágenes PNG de la estructura después de cada
modificación.

---

## Estructura del Proyecto
PROYECTO/

── nodo.py | los datos del estudiante

── lista.py | Clase ListaDoble con los métodos principales

── visuali.py | Generador de imágenes con Graphviz

── main.py | entrada con el menú interactivo

── imagenes/ | Se crea automáticamente al ejecutar


---

## Requisitos

| Software   | Versión          | Instalación                                                       |
|------------|------------------|-------------------------------------------------------------------|
| Python     | 3.10 o superior  | [python.org](https://www.python.org/downloads/)                   |
| Graphviz   | 14.x             | [graphviz.org](https://graphviz.org/download/)                    |
| pip        | Incluido con Python | Se instala automáticamente con Python                          |

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/lista-doblemente-enlazada.git
cd lista-doblemente-enlazada

Ejecución
Bash

python main.py
Se mostrará el siguiente menú:

text

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
╚══════════════════════════════╝

Color	Significado
🟢 Verde	Nodo cabeza
🟡 Naranja	Nodo intermedio
🔵 Azul	Nodo cola
🟣 Morado	Nodo único
🔴 Rojo	NULL (extremos)
