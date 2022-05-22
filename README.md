![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/image/header.png)

# Introducción

Las matemáticas están basadas en ideas primitivas tales que no existen palabras para definirlas, pero que todo mundo entiende. Y leyes de los números que no necesitan comprobación, de lo anterior se desarrolla una teoría libre de contradicciones.

Por conceptos primitivos vamos a entender a ideas básicos que no pueden ser explicados con palabras, pero la abstracción humana entiende. Es el caso de:

- Número
- Punto 
- Recta
- Plano
- Conjunto

## Leyes de los números

**Operador suma y producto**

El operador suma y producto son binarios, es decir, solamente se puede realizar con un par de elementos que cumplen las siguientes leyes de los números.

```
1. a + b = b + a. Conmutativa para la suma.
2. a + (b + c) = (a + b) + c. Asociativa para la suma.
3. a + 0 = 0 + a = a. Neutro aditivo.
4. 0 = a + (-a) = (-a) + a = 0. Inverso aditivo.
5. a*b = b*a. Conmutativa para el producto.
6. a*(b*c) = (a*b)*c. Asociativa para el producto.
7. a = 1*a = a*1 = a. Neutro multiplicativo.
8. 1 = a * (1/a) = (1/a) * a = 1. Inverso multiplicativo.
9. a * (b + c) = (a*b) + (a*c). Distributiva, esta propiedad es la combinación del operador suma con el operador producto.
```

**Ejemplos:**

```
- Conmutativa para la suma

	45 = 33 + 12 = 12 + 35 = 45
	28 = 7 + 21 = 21 + 7 = 28

- Asociativa para la suma

	12 = 3 + (5 + 4) = 3 + (9) = (3 + 5) + 4 = (8) + 4 = 12
	21 = 11 + (8 + 2) = 11 + (10) = (11 + 8) + 2 = (19) + 2 = 21

- Neutro aditivo

	17 = 17 + 0 = 0 + 17 = 17
	75 = 75 + 0 = 0 + 75 = 75
	
- Inverso aditivo

	0 = 34 + (-34) = (-34) + 34 = 0
	0 = 25 + (-25) = (-25) + 25 = 0

- Conmutativa para el producto
	
	30 = 5 * 6 = 6 * 5 = 30
	21 = 7 * 3 = 3 * 7 = 21

- Asociativa para el producto

	60 = (5 * 4) * 3 = (20) * 3 = 5 * (4 * 3) = 5 * (12) = 60
	70 = (2 * 5) * 7 = (10) * 7 = 2 * (5 * 7) = 2 * (35) = 70
	
- Neutro multiplicativo

	13 = 13 * 1 = 1 * 13 = 13
	23 = 23 * 1 = 1 * 23 = 23
	
- Inverso multiplicativo

	1 = 8 * (1/8) = (1/8) * 8 = 1
	1 = 19 * (1/19) = (1/19) * 19 = 1
	
- Ley Distributiva

	6 * (5 + 3) = (6 * 5) + (6 * 3) = (30) + (18) = 48
	7 * (4 + 5) = (7 * 4) + (7 * 5) = (28) + (35) = 63 
```

# Matemáticas Discretas

<p><em>From: <a href="https://es.wikipedia.org/wiki/Matem%C3%A1tica_discreta">Matemáticas Discretas Wikipedia</a></em></p>

Las **matemáticas discreta** es un área de la matemática encargada del estudio de los conjuntos discretos: finitos o infinitos numerables.

Las matemáticas discretas abordan varios temas entre ellos: informática teórica, teoría de la información, lógica, teoría de conjunto, combinatorio, teoría de grafos, teoría de distribuciones de probabilidades discretas, teoría de números. Pero antes de empezar revisemos cuales son los principales conjuntos que son numerables, y un ejemplo sencillo de como contarlos.

### El conjunto de los números naturales.

$$\mathbb{N} = \left\lbrace{1,~2,~3,~4,~5,~6, ...}\right\rbrace$$

Este conjunto es el más natural para el humano, y por ello su nombre. En la historia del hombre es la manera en que aprendió a contar. La manera de enumerarlos no necesita explicación. Por lo tanto el conjunto de los número naturales es un conjunto infinito numerable.

### El anillo de los números enteros.

$$\mathbb{Z} = \left\lbrace{...,-3,-2,-1,0,1,2,3, ...}\right\rbrace$$

Este conjunto en la historia del hombre causo conflicto, ya que por algunas sociedades no eran comprensibles los números negativos al grado de tener que ignorarlos. Actualmente no nos causan ninguna confusión y claramente podemos observar que se componen del conjunto de números $\mathbb{N}$ conjuntamente de sus respectivos inversos aditivos (Propiedad 4 de la ley de los números).

El nombre de anillo proviene de la manera de enumerarlos, los en listamos desde -$\infty$ hasta $\infty$. Ahora comenzamos el conteo en 0, seguido de 1, seguido de -1, y así sucesivamente. El resultado es un conjunto infinito numerable.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/image/integer.png)

### El conjutno de los números racionales.

Este conjunto tiene la sigiente descripción matemática.

$$\mathbb{Q} = \left\lbrace{\frac{p}{q}, q \neq 0~|~p, q \in \mathbb{Z}}\right\rbrace$$

Lo que dicho con palabras es, el conjunto de los números racionales, son aquellos que tienen la forma p entre q, donde q no puede ser 0, tal que p y q le perteneces a los enteros.

**Nota:** En mi experiencia personal, se que este conjunto es uno de los culpables por que a mucha gente no le gustan las matemáticas ya que en educación básica o primaria se nos enseña a operar con ellos y es el punto critico donde mucha gente deja de entender que esta pasando. Aunque te puedo comentar que si haces un pequeño esfuerzo por entender la presente definición muchas cosas te serán más fáciles.

Por otro lado, la manera de saber que este conjunto de número es numerable, es mediante el siguiente arreglo, donde por medio de ordenarlos por su numerador y denominador podemos estar seguros que estamos tomando a todos los números racionales y siguiendo el dibujo empezamos a contarlos. Por lo tanto el conjunto de los números racionales es un conjunto infinito numerable.

![](https://raw.githubusercontent.com/GabrielCourses/matematicas_discretas/main/image/racional.png)

Por último veamos un par de conjuntos los cuales no son un conjunto numerable.

## El conjunto de los números irracionales.

Si el conjunto de los números enteros negativos fue complicado para el hombre, el conjunto de los números irracionales fue aún más. El primer caso de estudio fue el del triángulo rectángulo cuyos catetos son igual a uno y su hipotenusa es igual a $\sqrt{2}$.

La definición de número irracional $\mathbb{I}$, son aquellos cuales tienen una cola de decimales no periódica infinita. Por mencionar algunos de estos números tenemos tenemos al número $\pi, \sqrt{2}, \sqrt{3}, \sqrt{5}, {\exp}$.

Finalmente el para el conjunto de los números reales tenemos que:

$$\mathbb{R} = \mathbb{I} \cup \mathbb{Q}$$

Y solo comentaremos que su representación gráfica es la recta real.