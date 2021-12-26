library(tidyr)
library(dplyr)
#library(spdep)
#library(sf)
#library(rgdal)
#library(spatialreg)
library(foreign)
library(stargazer)
library(Metrics)
library(MASS)
library(MLmetrics)
library(ggplot2)


# modelo poisson R
dd_deptos <- read.csv('tablas/dd_deptos.csv', sep=";", dec=",")

# convierte largo del límite de metros a kilómetros
dd_deptos$largo_limite_km <- dd_deptos$largo_limite/1000

# reemplaza nulos del largo del límite por 0.0001
dd_deptos <- dd_deptos %>% replace_na(list(largo_limite_km = 0.0001))

# convierte PBI departamental a miles de millones de pesos
dd_deptos$pbi_destino_millardos <- dd_deptos$pbi_destino/100000

# convierte variable de límites s tipo logical
dd_deptos$dummy_limit <- as.logical(dd_deptos$dummy_limit)

# convierte unidades de población a miles
dd_deptos$pob_destino <- dd_deptos$pob_destino/1000
dd_deptos$pob_origen <- dd_deptos$pob_origen/1000

# nombre de deptos a factor
dd_deptos$nom_depto_orig <- as.factor(dd_deptos$nom_depto_orig)



# model poisson regression using glm()
# restringido en origen
model <- glm(personas_mig ~
             nom_depto_orig +
             log_pob_destino_k +
             log_edad_prom_des + 
             log_pbi_destino_millardos +
             log_porc_ocupados_des + 
             log_dist_km -1 ,
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


plot(dd_deptos$personas_mig, fitted(model))

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

model1 <- glm(personas_mig ~ nom_depto_orig + dummy_limit +
                log(largo_limite_km) + log(pbi_destino_millardos) +
                log(dist_km),
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
model2 <- glm.nb(personas_mig ~ nom_depto_orig +
                                dummy_limit +
                                log(largo_limite_km) +
                                log(pbi_destino_millardos) +
                                log(dist_km),
                  data = dd_deptos)
# resumen
summary(model2)


# medidas de ajuste

rmse0=rmse(dd_deptos$personas_mig, fitted(model))
rmse1=rmse(dd_deptos$personas_mig, fitted(model1))

rmse0
model$aic

rmse1
model1$aic


R2_Score(fitted(model), dd_deptos$personas_mig)

R2_Score(fitted(model1), dd_deptos$personas_mig)

# es mejor el Poisson según el RMSE


##################
### Escenarios ###
##################

# recarga datos
dd_deptos <- read.csv('tablas/dd_deptos.csv', sep=";", dec=",")
dd_deptos$largo_limite_km <- dd_deptos$largo_limite/1000
dd_deptos <- dd_deptos %>% replace_na(list(largo_limite_km = 0.0001))
dd_deptos$pbi_destino_millardos <- dd_deptos$pbi_destino/100000
dd_deptos$nom_depto_orig <- as.factor(dd_deptos$nom_depto_orig)
dd_deptos$dummy_limit <- as.logical(dd_deptos$dummy_limit)
dd_deptos$pob_destino <- dd_deptos$pob_destino/1000
dd_deptos$pob_origen <- dd_deptos$pob_origen/1000

# carga PBI
pbi2021 <- read.csv('tablas/pbi_2021.csv')

# actualiza PBI
dd_escen <- merge(dd_deptos, pbi2021, by="depto_destino")
dd_escen$pbi_destino_millardos <- dd_escen$pbi_destino_2021/100000

# reduce las distancias
dd_escen$dist_km <- dd_escen$dist_km*0.85

# aumenta la población en destino
dd_deptos$pob_destino <- dd_deptos$pob_destino*1.3

# predice con las nuevas variables
dd_escen$pred_mig <- predict(model, newdata = dd_escen, type = "response")

migrantes  = dd_escen$personas_mig
prediccion = dd_escen$pred_mig

plot(migrantes, prediccion)


dd_escen['depto_origen']


migrantes_sin_mvo <- dd_escen[which(dd_escen$depto_origen > 1
                                    & dd_escen$depto_destino > 1), "personas_mig"]

prediccion_sin_mvo <- dd_escen[which(dd_escen$depto_origen > 1
                                    & dd_escen$depto_destino > 1), "pred_mig"]



plot(migrantes_sin_mvo, prediccion_sin_mvo)
