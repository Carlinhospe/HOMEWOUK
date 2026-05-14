# Árbol B Configurable en Python
# TAREA6
## Gerardo Josue Toledo Dondiego | 9490-24-6844 | Seccion B

Implementación de un **Árbol B** con grado configurable, carga masiva desde 4 archivos CSV y visualización gráfica mediante Graphviz.



---

## Estructura del Proyecto


├── btree.py Programa principal

├── productos.csv 130 registros

├── empleados.csv 115 registros

├── transacciones.csv 160 registros

├── estudiantes.csv 110 registros

├── output/ Gráficos PNG generados automaticamente

└── README.md



---


## Como ejecutar y probar

| Paso | Acción |
| 1 | Ejecuta `python btree.py` |
| 2 | Ingresa el grado que desees para el árbol |

> usa la convención estándar:
> | Propiedad | Fórmula | Ejemplo grado 6 |
> |---|---|---|
> | Máximo claves por nodo | `grado - 1` | 5 |
> | Mínimo claves por nodo | `max // 2` | 2 |


---

## Instrucciones precisas para cargar los archivos CSV incluidos

| Archivo | Registros | Columna clave automática |
|---|---|---|
| productos.csv | 130 | `codigo_producto` |
| empleados.csv | 115 | `id_empleado` |
| transacciones.csv | 160 | `id_transaccion` |
| estudiantes.csv | 110 | `id_estudiante` |

**Procedimiento:**
1.  Desde el menú selecciona la **opción 4**
2.  Escribe el nombre del archivo (ej: `empleados.csv`)
3.  Presiona **Enter** cuando te pida la columna. El programa detecta todo automaticamente.



---

## Operaciones del menú

| Opción | Funcionalidad |
|---|---|
| 1 | Insertar clave manual |
| 2 | Buscar clave |
| 3 | Eliminar clave |
| 4 | Cargar CSV |
| 5 | Listar claves en orden |
| 6 | Ver datos del árbol (grado, altura, total) |
| 7 | Generar gráfico PNG |
| 8 | Reiniciar con nuevo grado |
| 0 | Salir |


---

## Generación de representación gráfica

1.  Selecciona la **opción 7**
2.  Ingresa el nombre para el archivo
3.  La imagen se guarda inmediatamente en la carpeta `output/`

El gráfico distingue:
| Elemento | Color |
|---|---|
| Nodos hoja | Azul claro |
| Nodos internos | Amarillo claro |
| Título | Muestra grado, max/min claves, total y altura |
