# Árbol AVL 

| Nombre | Carnet | 
|--------|--------|
| Gerardo Josue Toledo Dondiego | 9490_24_6844 |



## Estructura del proyecto

    TAREA4/
     ├── prueba.py               ← archivo principal
     ├── mis_datos/              ← carpeta con CSV
     │    ├── dp.csv
     │    ├── dm.csv
     │    └── dg.csv
     └── avl_graphviz/           ← se crea automáticamente
          ├── arbol.dot
          └── arbol.png

---

## Cómo ejecutar

    Entrar a la carpeta del proyecto
    cd TAREA4

    Ejecutar
    python AVLIL.py

---

## Menú principal

esto en pantalla:

      ──────────────────────────────────────────────────
                   ÁRBOL AVL
      ──────────────────────────────────────────────────
      Nodos: 0  |  Altura: 0
      ──────────────────────────────────────────────────

      [1] Insertar      [2] Buscar      [3] Eliminar
      [4] Cargar CSV    [5] Visualizar  [6] Info árbol
      [7] Limpiar árbol [0] Salir

      ──────────────────────────────────────────────────

      Opción:

---

# Opciones explicadas

### 1 Insertar
Ingresa uno o varios números separados por coma, 
el árbol se balancea automáticamente y se actualiza el PNG.

      Número(s) separados por coma: 10, 20, 5, 15
      10 insertado.
      20 insertado.
      5 insertado.
      15 insertado.
      

### 2 Buscar
Indica si el número existe o no en el árbol.

      Número a buscar: 20
      [✓] 20 SÍ está en el árbol.

      Número a buscar: 99
      [✗] 99 NO está en el árbol.

### 3 Eliminar
Elimina uno o varios números separados por coma.

      Número(s) separados por coma: 20
      [✓] 20 eliminado.
      

### 4 Cargar CSV
Muestra los CSVs disponibles y carga el que se elija.


      CSVs disponibles:

      Ruta del CSV: mis_datos\datos_mediano.csv
      ¿Limpiar árbol antes? (s/n): s
      Árbol limpiado.
      Insertados: 15  |  Errores: 0
     

### 6 Info árbol
Muestra número de nodos, altura y recorrido in-orden.

      Nodos  : 7
      Altura : 3
      Inorden: [3, 5, 7, 10, 15, 20, 30]

### 7 Limpiar árbol
Vacía el árbol por completo (pide confirmación antes de hacerlo).

      ¿Seguro? (s/n): s
      Árbol limpiado.

---

### Colores de los nodos

| Color     | Factor de balance |                                         |
|-----------|-------------------|-----------------------------------------|
| 🟢 Verde  | FB = 0            | Perfectamente balanceado                |
| 🟠 Naranja| FB = ±1           | Levemente inclinado                     |
| 🔴 Rojo   | FB = ±2           | Desbalanceado este no debería verse en AVL |


