![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/maya.png)

# Sistema numérico

En aritmética, álgebra y análisis matemático, un **sistema númerico** es un conjunto provisto de dos operaciones que verifican ciertas condiciones relacionadas con las propiedades conmutativa, asociativa y distributiva. El conjunto de los número enteros, los racionales o los reales son ejemplo de sistemas numéricos, aunque los matemáticos han creado muchos otros sistemas numéricos más abstractos para diversos fines. Además debes tenerse en cuenta que dado un sistema numérico existen diversas formas de representarlo, por ejemplo, en los enteros podemos usar la representación decimal, la binaria, la hexadecimal, etc. En los racionales podemos optar por expresarlos de manera decimal o como fracción de enteros, etc.

Los sistemas numéricos se caracterizan por tener una **estructura algebraica** (monoide, anillo, cuerpo, álgebra sobre un cuerpo), satisfacer **propiedades de orden** (orden total, buen orden) y **propiedades topológicas** y analíticas (densidad, metrizabilidad, completitud) adicionales.

# Sistema binario

El **sitema binario,** también llamado **sistema diádico** en ciencias de la computación, es un sistema de numeración en el que los números son representados utilizando únicamente dos cifras: 0(cero) y 1 (uno). Es uno de los sistemas que utilizan las computadoras, debido a que estas trabajan internamente con dos niveles de voltaje, por lo cual su sistema de numeración natural es el sistema binario.

### Conversión entre binario y decimal

**Decimal a binario**

Se divide el número del sistema decimal entre **2,** cuyo resultado entero se vuelve a dividir entre 2, y así sucesivamente hasta que el dividendo sea menor que el divisor, 2. Es decir, cuando el número a dividir sea 1 finaliza la división.

A continuación se ordena desde el último cociente hasta el primer resto, simplemente se colocan en orden inverso a como aparecen en la división. Este será el número binario que buscamos.

**Ejemplo**

Transformar el número decimal 131 en binario.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/convertir131.png)

Ordenamos los residuos, del último al primero: 10000011. En sitema binario, 131 se escribe 10000011.

**Ejemplo**

Transforma el número 100 en binario.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/convertir100.png)

Otra forma de conversión consiste en método parecido a la factorización en numeros primos. Es relativamente fácil dividir cualquier número entre 2. Este método consiste también en divisiones sucesivas. Dependiendo de si el número es par o impar, colocamos un cero o un uno en la columna de la derecha. Si es impar, le restamos uno y seguimos dividiendo entre dos, hasta que ya no sea posible y se coloca el número 1. Después solo nos queda tomar el último resultado de la columna izquierda y todos los de la columna de la derecha y ordenar los dígitos de abajo hacia arriba.

**Ejemplo**

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/100_2.png)

**Ejemplo**

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/convertir77.png)

## Decimal a Binario en Python

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/binario.png)

Una forma sencilla de convertir decimal en binario en Python es dividir sucesivamente el número decimal entre 2 e ir guardando el módulo, resto o residuo de cada división hasta obtener cero en el cociente. Finalmente se concatenan todos los módulos en orden inverso

Vamos a recordar como hacemos esta operación en papel.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/paper.png)

### Paso 1. Hacer la división entera del número decimal entre 2.

Este paso tendremos que repetirlo en **bucle** para obtener el número deseado.

Se trata de dividir el número original entre 2. Además, necesitamos dos número distintos, resultado de esta división: el **cociente** y el **módulo** (también llamado resto o residuo).

Es por esto que necesitamos utilizar la división entera, no sirve la división típica.

En Pyton3 el símbolo de la división entera es la barra doble //. Si aplicas una sola barra / obtendrás el resultado de la división real y en este caso no es la que ocupamos, ya que necesitamos obtener de manera separada el cociente y el módulo.

Veamos unos ejemplo del uso de la división entera, es decir, la consola nos devolvera solamente el cociente entero.

<center>
<img align='center' src="https://media.giphy.com/media/XNQ19v5A5RJCRwM2yN/giphy.gif">
</center>

Ahora, para obtener el módulo se ocupa el operador **%**, en este caso la consola regresa el residuo o módulo. Hacemos los mismos ejemplo para comparar resultados.


**Binario a decimal**

1. Comience por el lado izquierdo del número binario. Multiplique cada digito por 2 elevado a la potencia consecutiva (comenzando por la potencia 0, es decir, $2^0$).
2. Después de realizar cada una de las multiplicaciones, súmelas todas y el número resultante será el equivalente al sistema decimal.

**Ejemplo**

Los número ubicados en la parte superior del número binario indican la potencia a la que hay que elevar el número 2.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/sist_numericos/image/convertir_decimal.png)




