# =========================================================================
# Convertir un número en base 10 a base 2.
# Paso 1. Hacer la división entera del número en base 10 entre 2.
# Ejemplos de división entera, es decir, solo obtenemos el cociente entero.
10 // 4
6 // 3
15 // 2

# Ahora veamos ejemplos del operador % (modulo).
10 % 4
6 % 3
15 % 2

# Usamos el algoritmo de la división para probar nuestros resultados
10 == 4 * (10 // 4) + (10 % 4)
6 == 3 * (6 // 3) + (6 % 3)
15 == 2 * (15 // 2) + (15 % 2)



