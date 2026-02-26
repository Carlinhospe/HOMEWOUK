
def convertir_a_binario(numero):
    if numero  < 0:
        return "-" + convertir_a_binario(-numero)
    if numero == 0:
        return "0"
    if numero == 1:
        return "1"
    return convertir_a_binario(numero // 2) + str(numero % 2)


def contar_digitos(numero):
    numero = abs(numero)
    if numero < 10:
        return 1
    return 1 + contar_digitos(numero // 10)




def calcular_raiz_cuadrada(numero, candidato):
    if candidato * candidato > numero:
        return candidato - 1
    if candidato * candidato == numero:
        return candidato
    return calcular_raiz_cuadrada(numero, candidato + 1)


def raiz_cuadrada_entera(numero):
    if numero < 0:
        return None
    if numero == 0:
        return 0
    return calcular_raiz_cuadrada(numero, 1)



def convertir_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    if len(romano) == 0:
        return 0
    if len(romano) == 1:
        return valores[romano]
    if valores[romano[0]] < valores[romano[1]]:
        return -valores[romano[0]] + convertir_a_decimal(romano[1:])
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:]) 


def suma_numeros_enteros(numero):
    if numero == 0:
        return 0
    return numero + suma_numeros_enteros(numero - 1)





def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("    Error: debe ingresar un numero entero valido.\n")




def validar_entero_positivo(mensaje):
    while True:
        valor = validar_entero(mensaje)
        if valor >= 0:
            return valor
        print("    Error: debe ingresar un numero positivo o cero.\n")



def validar_romano(mensaje):
    caracteres_validos = set("IVXLCDM")
    while True:
        valor = input(mensaje).strip().upper()
        if valor == "":
            print("    Error: No puede estar vacio el campo.\n")
            continue
        if all(c in caracteres_validos for c in valor):
            return valor
        print("    Error: Solo se permiten caracteres romanos (I,V,X,L,C,D,M).\n")


def mostrar_menu():
    print("\n" + "=" * 50)
    print("   OPERACIONES MATEMATICAS RECURSIVAS")
    print("=" * 40)
    print("  1. Convertir a Binario")
    print("  2. Contar los Digitos")
    print("  3. Raiz Cuadrada Entera")

    print("  4. Convertir a Decimal de Romano")
    print("  5. Suma de Numeros Enteros")
    print("  6. Salir")
    print("-" * 40)


def opcion_binario():
    print("\n   CONVERTIR A BINARIO ")
    numero = validar_entero("  Ingrese un numero entero: ")
    resultado = convertir_a_binario(numero)
    print(f"\n  El numero {numero} en binario es: {resultado}")




def opcion_contar_digitos():
    print("\n   CONTAR DIGITOS ")
    numero = validar_entero("  Ingrese un numero entero: ")
    resultado = contar_digitos(numero)
    print(f"\n  El numero {numero} tiene {resultado} digitos")


def opcion_raiz_cuadrada():
    print("\n   RAIZ CUADRADA ENTERA ")
    numero = validar_entero_positivo("  Ingrese un numero positivo: ")
    resultado = raiz_cuadrada_entera(numero)
    print(f"\n  La raiz cuadrada entera de {numero} es: {resultado}")
    print(f"    (Verificacion: {resultado}^2 = {resultado ** 2})")



def opcion_romano_decimal():
    print("\n   Convertir romano a decimal ")
    romano = validar_romano("  Ingrese un numero romano: ")
    resultado = convertir_a_decimal(romano)
    print(f"\n  El numero romano {romano} equivale a: {resultado}")



def opcion_suma_enteros():
    print("\n   Suma de enteros positivos ")
    numero = validar_entero_positivo("  Ingrese un numero entero positivo: ")
    resultado = suma_numeros_enteros(numero)
    print(f"\n  La suma desde 0 hasta {numero} es: {resultado}")
    print(f"    (0 + 1 + 2 + ... + {numero} = {resultado})")





def main():
    print("\n" + "=" * 56)
    print("   PROGRAMA DE RECURSIVIDAD - 9490-24-6844")
    print("=" * 56)

    opciones = {
        "1": opcion_binario,
        "2": opcion_contar_digitos,
        "3": opcion_raiz_cuadrada,
        "4": opcion_romano_decimal,
        "5": opcion_suma_enteros
    }

    while True:
        mostrar_menu()
        eleccion = input("  Seleccione una opcion (1-6): ").strip()

        if eleccion == "6":
            print("\n  Gracias y Adiosin !!")
            print("=" * 56 + "\n")
            break
        elif eleccion in opciones:
            opciones[eleccion]()
            input("\n  Presione ENTER para continuar...")
        else:
            print("\n  Opcion no valida. Elija entre 1 y 6.")


if __name__ == "__main__":
    main()