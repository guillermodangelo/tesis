library(tidyr)
library(dplyr)
library(spdep)
library(sf)
library(rgdal)
library(spatialreg)
library(foreign)
library(stargazer)

# ubuntu
setwd('/home/guillermo/Documentos/GitHub/tesis/')

# windows
#setwd("C:/Users/user/Documents/GitHub/tesis")

# eugenia
#setwd("C:/Users/Eugenia/Dropbox/d'angelo")


# modelo poisson R
dd_deptos <- read.csv('tablas/dd_deptos.csv', sep=";", dec=",")

# convierte largo del límite de metros a kilómetros
dd_deptos$largo_limite_km <- dd_deptos$largo_limite/1000

# reemplaza nulos del largo del límite por 0.0001
dd_deptos <- dd_deptos %>% replace_na(list(largo_limite_km = 0.0001))

# convierte PBI departamental a miles de millones de pesos
dd_deptos$pbi_destino_millardos <- dd_deptos$pbi_destino/100000

dd_deptos$nom_depto_orig <- as.factor(dd_deptos$nom_depto_orig)

# model poisson regression using glm()
# restringido en origen
model <- glm(personas_mig ~ nom_depto_orig + dummy_limit + log(largo_limite_km) +
               log(pbi_destino_millardos) + log(dist_km) - 1 ,
               family = poisson(link = "log"),
               data = dd_deptos)

# resumen
summary(model)

# exporta resumen a Latex
stargazer(model, title="MIE restringido en origen",
          out="tablas/poisson_rest_origen.tex",
          dep.var.caption='Variable dependiente',
          header=FALSE, align=FALSE, ci=TRUE, df=TRUE,
          table.placement = "H", single.row=TRUE, no.space=TRUE)

# intepretación de coeficientes con variables con logaritmos, por ejemplo un aumento
# de un 10%, q=1.1

q = 1.1
(q^coefficients(model)[20:23]-1)*100
(q^coefficients(model)-1)*100

# ERROR CON LOS COEF??

# o sea al aumentar un 10% el largo del límite, aumentan los flujos de salida un 2.92%
# al aumentar un 10% el pbi aumentaría en promedio los flujos un 10.07%
# al aumentar la distancia un 10%, los flujos de salida decaen en un 2.05% en promedio

# la dummie del límite da raro, es negativo, como que estar en la frontera hace que en
# promedio los flujos de salida decaigan. Esto puede ser porque está Montevideo adentro.

# las dummies dan todas positivas, incluidas Montevideo, como que son todas expulsoras.

# PASO SIGUIENTE, estimar el modelo con Montevideo con categoría de referencia. Para ello se debe
# agregar la constante y avisarle que tome como categoría de referencia a Montevideo.
dd_deptos$nom_depto_orig <- relevel(dd_deptos$nom_depto_orig, ref = "MONTEVIDEO")

model1 <- glm(personas_mig ~ nom_depto_orig + dummy_limit + log(largo_limite_km) +
               log(pbi_destino_millardos) + log(dist_km),
              family = poisson(link = "log"),
              data = dd_deptos)

# resumen
summary(model1)

q = 1.1
(q^coefficients(model1)[20:23]-1)*100
(q^coefficients(model1)-1)*100

# exporta resumen a Latex
titulo = "MIE restringido en origen con Montevideo como categoría de referencia"
stargazer(model1, title=titulo,
          out="tablas/poisson_rest_origen_MVO_ref.tex",
          dep.var.caption='Variable dependiente',
          header=FALSE, align=FALSE, ci=TRUE, df=TRUE,
          table.placement = "H", single.row=TRUE, no.space=TRUE)

# la interpretación es similar, pero los parámetros de las dummy son más razonables de interpretar
# quedan todos negativos respecto a Montevideo, o sea si se está en un departamento
# del interior, los flujos de salida en promedio decaen, si se los compara con Montevideo.



# me queda la duda ahora de si usar la distancia en lugar del logaritmo, es más fácil de interpretar

# por último pruebo el modelo de la binomial negativa en este contexto, a ver si mejora la predicción

library(MASS)
model2 <- glm.nb(personas_mig ~ nom_depto_orig + dummy_limit + log(largo_limite_km) +
                log(pbi_destino_millardos) + log(dist_km),
              data = dd_deptos)
# resumen
summary(model2)


# medidas de ajuste
library(Metrics)

rmse0=rmse(dd_deptos$personas_mig, fitted(model))
rmse2=rmse(dd_deptos$personas_mig, fitted(model2))

rmse0
rmse2

model$aic
model2$aic

# es mejor el Poisson según el RMSE
