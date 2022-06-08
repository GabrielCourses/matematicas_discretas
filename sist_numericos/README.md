![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/maya.png)

# Sistema numérico

En aritmética, álgebra y análisis matemático, un **sistema númerico** es un conjunto provisto de dos operaciones que verifican ciertas condiciones relacionadas con las propiedades conmutativa, asociativa y distributiva. El conjunto de los número enteros, los racionales o los reales son ejemplo de sistemas numéricos, aunque los matemáticos han creado muchos otros sistemas numéricos más abstractos para diversos fines. Además debes tenerse en cuenta que dado un sistema numérico existen diversas formas de representarlo, por ejemplo, en los enteros podemos usar la representación decimal, la binaria, la hexadecimal, etc. En los racionales podemos optar por expresarlos de manera decimal o como fracción de enteros, etc.

Los sistemas numéricos se caracterizan por tener una **estructura algebraica** (monoide, anillo, cuerpo, álgebra sobre un cuerpo), satisfacer **propiedades de orden** (orden total, buen orden) y **propiedades topológicas** y analíticas (densidad, metrizabilidad, completitud) adicionales.

# Sistema binario

El **sistema binario,** también llamado **sistema diádico** en ciencias de la computación, es un sistema de numeración en el que los números son representados utilizando únicamente dos cifras: 0 (cero) y 1 (uno). Es uno de los sistemas que utilizan las computadoras, debido a que estas trabajan internamente con dos niveles de voltaje, por lo cual su sistema de numeración natural es el sistema binario.

## Cambio de base, de sistema decimal a binario.

Se divide el número del sistema decimal entre <coode>2</code>, cuyo resultado entero se vuelve a dividir entre <code>2</code>, y así sucesivamente hasta que el dividendo sea menor que el divisor, 2. Es decir, cuando el número a dividir sea 1 finaliza la división.

A continuación se ordena desde el último cociente hasta el primer resto, simplemente se colocan en orden inverso a como aparecen en la división. Este será el número binario que buscamos.

**Ejemplo**

Transformar el número decimal $131_{(10)}$ en binario.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/convertir131.png)

Ordenamos los residuos, del último al primero: $10000011_{(2)}$. En sistema binario, $131_{(10)}$ se escribe $10000011_{(2)}$.

**Ejemplo**

Transforma el número $100_{(10)}$ a binario.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/convertir100.png)

Otra forma de conversión consiste en método parecido a la factorización en numeros primos. Es relativamente fácil dividir cualquier número entre 2. Este método consiste también en divisiones sucesivas. Dependiendo de si el número es par o impar, colocamos un cero o un uno en la columna de la derecha. Si es impar, le restamos uno y seguimos dividiendo entre dos, hasta que ya no sea posible y se coloca el número 1. Después solo nos queda tomar el último resultado de la columna izquierda y todos los de la columna de la derecha y ordenar los dígitos de abajo hacia arriba.

**Ejemplo**

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/100_2.png)

**Ejemplo**

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/convertir77.png)

## Cambio de base en Python

Una forma sencilla de convertir decimal en binario en Python es dividir sucesivamente el número decimal entre <code>2</code> e ir guardando el módulo, resto o residuo de cada división hasta obtener cero en el cociente. Finalmente se concatenan todos los módulos en orden inverso.

Es conveniente reconocer cada uno de los elementos o participantes en la conversión de base, recordando el algoritmo de la división.

### Algoritmo de la división.

Antes de empezar escribir código, revisemos el algoritmo de la división y como encontrar sus elemento en python. 

**División entera**

En <code>Pyton3</code> el símbolo de la división entera es la barra doble <code>//</code>. Si aplicas una sola barra <code>/</code> obtendrás el resultado de la división real y en este caso no es la que ocupamos, ya que necesitamos obtener de manera separada el cociente y el módulo.

Veamos unos ejemplo del uso de la división entera, es decir, la consola nos devolverá solamente el cociente entero.

<center>
<img src="https://media.giphy.com/media/XNQ19v5A5RJCRwM2yN/giphy.gif">
</center>

Ahora, para obtener el módulo se ocupa el operador <code>%</code>, en este caso la consola regresa el residuo, resto o módulo. Hacemos los mismos ejemplo para comparar resultados.

<center>
<img src="https://media.giphy.com/media/7jQsk1jcOSTTaTv7Qt/giphy.gif">
</center>

Dado cualquier número $b\in\mathbb{Z}$ podemos encontrar un par de números $p,q\in\mathbb{Z}$ que multiplicados y sumado otro número <code>r</code> tal que <code>0<=r<p</code>, entonces <code>b=pq+r</code>

**Algoritmo de la división**

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/division.png)

Y tomando los ejemplos anteriores, comprobamos que:

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/dem.png)

Los ejemplos anteriores, los puedes revisar en el archivo: alg_division.txt de la carpeta **ficheros**.

### Bucle y Listas en Python.

**Guardar el módulo obtenido en la división previa**. Como este es un proceso iterativo donde vamos a guardar diversos módulos lo mejor es **crear una lista e ir almacenándolos en ella.**

Para esto vamos a crear una lista vacía llamada <code>modulos</code>, y con el método <code>append()</code> agregamos cada <code>modulo</code> calculado a la lista <code>modulos</code>, es decir, <code>modulos.append(modulo)</code>

Antes de seguir avanzando, te invito a que revises ejemplos sobre listas y el método <code>append</code>. <a href="https://github.com/gabrielfernando01/basics_in_python/tree/master/basics" target="_PLANK">Ejemplos de listas y bucles en Python.</a>

### Escribir el código.

Los procesos **iterativos** se resuelven con el uso de **bucles o ciclos,** para este caso vamos a tomar dos aspectos principales:

1. Cada que realizamos la **división entera**, el **cociente** obtenido pasa a ser el número que ocupamos en la siguiente iteración.
2. Detenemos el bucle cuando el **cociente obtenido es igual a 0.**  

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/modulos.png)

El código de la imagen anterior está guardado en la carpeta ficheros como script con el nombre: modulos.py

**Como ejecutar un script en la terminal**

Debes estar ubicado en el la misma carpeta donde se encuentra tu script, ahí escribes el siguiente comando:

```
$ python modulos.py
```

Desde IPython:

```
In [43]: %run modulos.py
```

De esta manera el resultado obtenido es:

```
[1, 0, 1, 1, 1]
```

Si hasta ahora has abstraído cada uno de los elementos del proceso del cambio de base, entonces podrás notar que con el siguiente código se puede **optimizar un poco más** de la siguiente manera:

```
# Comenzamos eligiendo un número en base decimal
numero_decimal = 29

modulos = []

while numero_decimal != 0:
    modulos.append(numero_decimal % 2)
    numero_decimal //= 2
```

**Invertir los módulos guardados**

Si imprimiéramos el bloque de código anterior sabemos que la lista almaceno los módulos de principio a fin, pero para obtener el número en en base binaria lo necesitamos en sentido inverso.

Una manera es agregar la siguiente línea de código: <code>modulos = modulos[::-1]</code>

Otra manera también mas inmediata de atacar el problema es con el método <code>insert</code> que **permite introducir un elemento en la lista en la posición que eligamos**. Para nuestro caso, queremos almacenar siempre en la primera posición, para que los modulos ya guardados se vayan recorriendo a la derecha.

Veamos como funciona este método:

```
>>> lista = []
>>> lista.insert(0,1)
>>> lista.insert(0,2)
>>> lista.insert(0,3)
>>> print(lista)
[3, 2, 1]
```

Ahora que ya sabemos como funciona, lo usamos en nuestro código:

```
# Comenzamos eligiendo un número en base decimal
numero_decimal = 29

modulos = []

while numero_decimal != 0:
    modulos.insert(0, numero_decimal % 2)
    numero_decimal //= 2
```

**Concatenar los módulos**

Nos damos cuenta que lo que tenemos es una lista de números ya ordenada lo cual nos debe facilitar hacer la conversión. Es decir, una manera es:

- Multiplicar cada digito por 10 elevado a su posición y sumar los resultados. En otras palabras, el número que ocupa las unidades lo elevamos a $10^{0}$, el de las decenas a $10^{1}$, el de las centenas por $10^{2}$ y así sucesivamente para al final sumarlos.
- Otra manera es convertir los elementos a carácter cada que los vamos almacenando y usar la operación <code>join</code> de la manera <code>''.join(modulos)</code> y al final convertir la concatenación a entero con la función <code>int:int(''.join(modulos))</code>.

Lo haremos de la primera forma, y ocuparemos el mismo bucle para ya no ocupar la lista. Aunque tenemos que declarar un par de variables muy sencillas para hacer las multiplicaciones y sumas.

```
# Comenzamos eligiendo un número en base decimal
numero_decimal = 29

numero_binario = 0
posicion = 1

while numero_decimal != 0:
    numero_binario = numero_binario + numero_decimal % 2 * posicion
    numero_decimal //= 2
    posicion *= 10
    
print(numero_binario)
```

De esta manera hemos convertido $29_{10} = 11101_{2}$. Pero si estamos programando (automatizando) lo que queremos es hacerlo para cualquier número, para esto creamos la función que convierta cualquier numero decimal a binario.

```
def decimal_a_binario(numero_decimal):
    numero_binario = 0
    posicion = 1

    while numero_decimal != 0:
        numero_binario = numero_binario + numero_decimal % 2 * posicion
        numero_decimal //= 2
        posicion *= 10

    return numero_binario
```

para ejecutar nuestra función:

```
print(decimal_a_binario(23))
```

***
## Convertir de Sistema binario a decimal

1. Comience por el lado izquierdo del número binario. Multiplique cada digito por 2 elevado a la potencia consecutiva (comenzando por la potencia 0, es decir, $2^{0}$).
2. Después de realizar cada una de las multiplicaciones, sumamos todas y el número resultante será el equivalente al sistema decimal.

**Ejemplo**

Los número ubicados en la parte superior del número binario indican la potencia a la que hay que elevar el número 2.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/convertir_decimal.png)




