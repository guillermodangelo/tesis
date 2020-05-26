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


Pregunta general: ¿Cuál será la magnitud de la migración interna en Uruguay entre 2012 y el horizonte 2025?


# Fuentes de información

- Censos 1985, 1996 y 2011


| Preguntas en censo 1996 | Preguntas en censo 2011 |
|---|---|
| En qué localidad o paraje vive habitualmente | Localización de la vivienda/hogar/persona |
| En qué localidad o paraje paso a vivir cuando nació | Lugar de nacimiento |
| "Si reside en Uruguay y nació en el extranjero, ¿en qué año llegó al Uruguay para vivir en él?" | Año de llegada a Uruguay |
|  | Período de llegada a Uruguay |
|  | Tiempo de residencia sin interrupciones en esta ciudad o localidad |
|  | Lugar de residencia anterior |
| En qué localidad o paraje vivía habitualmente hace 5 años en esta fecha | Lugar de residencia cinco años antes |



- ECH: posbildad de juntar varias ECH para tener datos que actualicen la matriz entre departamentos



# Estrategias metodológicas

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


