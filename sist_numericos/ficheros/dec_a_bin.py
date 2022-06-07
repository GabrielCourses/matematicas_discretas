# ==================================================================
# Comenzamos eligiendo un número en base decimal
numero_decimal = 29

# El numero binario es el que iremos construyendo en el bucle
# La posición nos ayuda a efectuar el calculo aritmetico
numero_binario = 0
posicion = 1

while numero_decimal != 0:
    numero_binario = numero_binario + numero_decimal % 2 * posicion
    numero_decimal //= 2
    posicion *= 10
    
print(numero_binario)
