Instituto de Investigaciones en Inteligencia Artificial - Universidad Veracruzana

**Análisis de algoritmos**

**Tarea 7**

**Calculo de π usando el método de Montecarlo**

1) Generar los puntos aleatorios usando congruencia lineal.
1) Generar los puntos usando secuencia de Halton.
1) Generar  los  puntos  usando  el  generador  de  puntos  de  su  lenguaje  de programación.

Para cada caso graficar las curvas de convergencia.

Analizar y determinar que método fue mas preciso.


Realizando pruebas, se modifico el k con diferentes valores para ver que resultados se obtenían en cada caso, las graficas obtenidas son las siguientes:

K=10

![](Aspose.Words.64e08cd7-2792-42d1-8179-8a37d6acf14d.001.png)

K=100

![](Aspose.Words.64e08cd7-2792-42d1-8179-8a37d6acf14d.002.png)

K=1000

![](Aspose.Words.64e08cd7-2792-42d1-8179-8a37d6acf14d.003.png)

K=10000

![](Aspose.Words.64e08cd7-2792-42d1-8179-8a37d6acf14d.004.png)

K=100000

![](Aspose.Words.64e08cd7-2792-42d1-8179-8a37d6acf14d.005.png)

Como se puede ver con k=10, el valor obtenido con los tres métodos es el mas alejado de π, mientras que cada que va aumentando el valor de K va aumentando la precisión de los métodos, sin embargo, el de la congruencia lineal, aunque se utilizaron los valores dados en wikipedia para el generador de números aleatorios de C++. En el caso del generador de la secuencia de Halton se utilizo una base de dos para generar los puntos en ambas dimensiones, y se puede apreciar que el valor de π calculado va convergiendo alrededor del valor de π dado por la librería math de python, que es justo lo esperado, siendo el mejor método ya que su valor es mas cercano a π y se puede apreciar mejor en el caso de K=100000 ya que llega un momento donde la linea ya es muy semejante a la linea horizontal del valor de π, mientras que el generador de python también se estabiliza alrededor del valor de π, sin embargo comparado con la secuencia de Halton tarda mas iteraciones en estabilizarse. En general los tres métodos logran acercarse al valor real de  π con buena precisión, solamente cambiando el numero de iteraciones necesarias para cada uno de los métodos para poder reducir su error.
Análisis de algoritmos
