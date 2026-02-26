# TAREA2
# Gerardo Josue Toledo Dondiego | 9490-24-6844 | Seccion B

## Programa Interactivo de Operaciones Matemáticas Recursivas

Programa desarrollado en Python que implementa diversas operaciones matemáticas
mediante funciones recursivas, presentadas a través de una interfaz de línea
de comandos.

---

## Programa


- [Cómo Ejecutar el Programa](#cómo-ejecutar-el-programa)
- [Opciones del Menú](#opciones-del-menú)
- [Guía de Pruebas](#guía-de-pruebas)
  - [1. Convertir a Binario](#1-convertir-a-binario)
  - [2. Contar Dígitos](#2-contar-dígitos)
  - [3. Raíz Cuadrada Entera](#3-raíz-cuadrada-entera)
  - [4. Convertir a Decimal desde Romano](#4-convertir-a-decimal-desde-romano)
  - [5. Suma de Números Enteros](#5-suma-de-números-enteros)
- [Estructura del Proyecto](#estructura-del-proyecto)
---

### python main.py


---

#### Opción	Función	Entrada Esperada

1	Convertir a Binario	Número entero

2	Contar Dígitos	Número entero

3	Raíz Cuadrada Entera	Número entero positivo

4	Convertir a Decimal desde Romano	Número romano (texto)

5	Suma de Números Enteros	Número entero positivo

6	Salir del programa	-

---


### 1. Convertir a Binario
Seleccionar la opción 1 e ingresar un número entero.

Entrada-Resultado Esperado

0 	/ 0

1 	/ 1

5	/  101

10	/  1010

13	/  1101

---
### 2. Contar Dígitos
Seleccionar la opción 2 e ingresar un número entero.

Entrada-Resultado 

5	    /   1 dígito

42	  /   2 dígitos

100	  /   3 dígitos

4527	 /  4 dígitos

---
### 3. Raíz Cuadrada Entera
Seleccionar la opción 3 e ingresar un número positivo.

Entrada	/ Resultado	/ Verificación

0	       /         0	     /      0² = 0

1	       /         1	     /      1² = 1

4	       /         2	     /      2² = 4

16	     /         4	     /      4² = 16

20	     /         4	     /      4² = 16

---
### 4. Convertir a Decimal desde Romano
Seleccionar la opción 4 e ingresar un número romano.

Caracteres válidos: I, V, X, L, C, D, M

Entrada	Resultado

I /	1

IV /	4

IX	/ 9

XIV /	14

XL /	40

XC /	90

MCMXIV /	1914

---

### 5. Suma de Números Enteros
Seleccionar la opción 5 e ingresar un número positivo.

Entrada	/ Resultado /Operación

0	/0	/0

1	/1	/0 + 1

5	/15	/0 + 1 + 2 + 3 + 4 + 5

10	/55	/0 + 1 + 2 + ... + 10

100	/5050	/0 + 1 + 2 + ... + 100

-------
---

main.py
│

├────────── Funciones Recursivas

│   ├── convertir_a_binario(numero)

│   ├── contar_digitos(numero)

│   ├── calcular_raiz_cuadrada(numero, candidato)

│   ├── raiz_cuadrada_entera(numero)

│   ├──convertir_a_decimal(romano)

│   └── suma_numeros_enteros(numero)

│
├──────────────── Funciones de Validación

│   ├── validar_entero(mensaje)

│   ├── validar_entero_positivo(mensaje)

│   └── validar_romano(mensaje)

│
├────────────────── Funciones de Interfaz

│   ├── mostrar_menu()

│   ├── opcion_binario()

│   ├── opcion_contar_digitos()

│   ├── opcion_raiz_cuadrada()

│   ├── opcion_romano_decimal()

│   └── opcion_suma_enteros()

│
└──────────── main() 
















