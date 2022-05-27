# Convertir un número en sistema decimal a binario
num_decimal = 29    # número que vamos a convertir

modulos = []        # lista para guardar los modulos

while num_decimal != 0:
    modulo = num_decimal % 2
    cociente = num_decimal // 2
    modulos.append(modulo)
    num_decimal = cociente

print(modulos)



