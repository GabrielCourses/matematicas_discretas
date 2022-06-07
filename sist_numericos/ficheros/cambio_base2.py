# ===========================================================
# Cambio de base, de decimal a binario
# Comenzamos eligiendo un número en base decimal
numero_decimal = 29

modulos = []

while numero_decimal != 0:
    modulos.append(numero_decimal % 2)
    numero_decimal //= 2

modulos = modulos[::-1]
print(modulos)

