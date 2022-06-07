# ==================================================================
def decimal_a_binario(numero_decimal):
    numero_binario = 0
    posicion = 1

    while numero_decimal != 0:
        numero_binario = numero_binario + numero_decimal % 2 * posicion
        numero_decimal //= 2
        posicion *= 10

    return numero_binario
