---
title: 'Modelos de interacción espacial y migración interna en Uruguay. Avances del marco teórico.'
author: Guillermo D'Angelo
date: Abril 2020
footer: true
figureTitle: "Figura"
numbersections: true
<>toc: true
<> output: pdf_document
---
<div style="text-align: justify"> 


# Planteo del problema y pregunta de investigación


Tal cual se mencionó anteriormente, el estudio de las migraciones internas es pertinente para la Demografía en tanto la migración es uno de los factores del cambio demográfico. Asumiendo el componente espacial que implican los movimientos de población, el abordaje con ecnicas de la geografía humana se considera adecuado.


La pregunta general que guiará este trabajo de investigación es la siguiente: ¿cuál será la magnitud de la migración interna en Uruguay entre 2012 y el horizonte 2025?



# Objetivos

Objetivo general
- Generar escenarios de migración interna en Uruguay mediante la utilización de modelos de interacción espacial con base en los censos de 1996 y 2011.

Objetivos específicos
- Describir las migraciones internas en Uruguay según los censos 1985, 1996 y 2011.
- Explorar la aplicabilidad de distintos modelos de interacción espacial para la simulación de la migración interna.
- Desarrollar y aplicar un modelo de interacción espacial de las migraciones entre departamentos.
- Desarrollar y aplicar un modelo de interacción espacial de las migraciones entre localidades.
- Discutir la pertinencia de factores asociados a las migraciones internas.




Desde esta perspectiva, el presente proyecto se propone simular escenarios futuros de migración interna basados en los modelos de interacción espacial. En el Uruguay existe un antecedente de investigación utilizando modelos de interacción espacial4, pero orientada movilidad por trabajo. Sin embargo, existen varios antecedentes de la aplicación de la metodología al tema migraciones en otros países, por lo cual consideramos viable usar la metodología para el estudio de las migraciones internas del Uruguay y la simulación de escenarios posibles. El interés por las simulaciones y la aplicación de los modelos de interacción espacial no remite exclusivamente a un interés metodológico sino también en valor para, por ejemplo, orientar políticas de desarrollo urbano y ordenamiento territorial.




# Estrategias metodológicas y fuentes de información


La pirncipal fuente de información para el presente trabajo serán los censos 1985, 1996 y 2011 realizados por el Instituto Nacional de Estadística (INE).
En particular los censos 1996 y 2011 incorporaron algunas preguntas que serán pertinentes al presente trabajo y se presentan en el siguiente cuadro.

| Preguntas en censo 1996 | Preguntas en censo 2011 |
|---|---|
| En qué localidad o paraje vive habitualmente | Localización de la vivienda/hogar/persona |
| En qué localidad o paraje paso a vivir cuando nació | Lugar de nacimiento |
| "Si reside en Uruguay y nació en el extranjero, ¿en qué año llegó al Uruguay para vivir en él?" | Año de llegada a Uruguay |
|  | Período de llegada a Uruguay |
|  | Tiempo de residencia sin interrupciones en esta ciudad o localidad |
|  | Lugar de residencia anterior |
| En qué localidad o paraje vivía habitualmente hace 5 años en esta fecha | Lugar de residencia cinco años antes |


Se explorará la posibilidad de juntar micro-datos de varias Encuestas Continua de Hogares, que permitan una actualización de los datos a nivel departamental.

Con respecto a los datos geográficos, se utilizarán dos insumos básicos: la capa de departamentos y la de localidades del INE. Los departamentos son unidades geoestadística y político-administrativas de segundo nivel de gobierno, la localidades son unidades geoestadísticas que, en general, corresponden a zonas urbanas.

Según la revisión bibliográfica y de antecedentes, una de las variables necesarias para aplicar un modelo de interacción espacial es la distancia entre las unidades espaciales que se vayan a tomar en cuenta. Para ello es necesario el cálculo de una matriz de distancias origen-destino, y para el cálculo de dicha matriz se debe determinar un punto dentro de cada departamento que será tomado como origen-destino, a partir del cual se calcula la distancia hacia todos los demás puntos que representan los departamentos, y desde todos esos puntos hacia el primero.

En el caso de los departamentos, en lugar de tomar el centroide de cada polígono que conforma la unidad geoestadística, se optó por tomar el punto de la capital departamental según la capa de puntos de localidades INE. Dicha decisión se basa en que en general los centroides coinciden con zonas rurales poco pobladas, siendo que población se concentra en zonas puntuales, y la capitales departamentales ofician como proxy de dicho dato. A partir de estos 19 puntos se calculó la matriz origen-destino a través del la "Distance Matrix API", ofrecida por Google, y consultada mediante una función de Python. Este método es usado para obtener las distancias como si se fuera conduciendo un vehículo por calles y rutas, en lugar de la distancia euclidiana.

 Más avanzado el proyecto se seleccionará alguno de los métodos para calcular el centro de población de cada departamento (a partir del censo 2011) y se utilizará dicha capa de puntos en lugar de la localidades, aunque se considera que los cambios no sería sustanciales. La misma consideración aplica para el uso de otras técnicas para el cálculo de la matriz origen-destino.



[//]: # NOTAS:
[//]: #  Ver las distancias funcionales en el artículo de Plane 1984
[//]: # Ver determinantes de la migración interna, tal vez algo de internacional en el artículo de Mayda.


# Sobre los modelos de interacción espacial

"Doubly Constrained Model" (modelo de restricción doble)


- Usado cuando se conocen los valores en origen y en destino
- En este caso sabemos cuántos migrantes llegan a cada localidad y de que localidad provienen, para todas las localidades, por ende es el modelo más adecuado.
- Los otros modelos (no restringido, restringido en origen o restringido en destino) son más adecuados para cuando se desconocen los datos en origen, en destino o en ambos (por ej. si solo se conoce la magnitud del flujo)


"Doubly Constrained Model" (modelo de restricción doble)

$$T_{ij}= A_{i} O_{i} B_{j} D_{j} d_{\overline{ij}} \beta$$
$$O_{i} = \sum_{j} { T_{ij} }$$
$$D_{j} = \sum_{i} { T_{ij} }$$
$$A_{i} = \frac{1}{ \sum_{j} B_{j} D_{j} d_{\overline{ij}} \beta }$$
$$B_{j} = \frac{1}{ \sum_{i} A_{i} O_{i} d_{\overline{ij}} \beta }$$


</div>


