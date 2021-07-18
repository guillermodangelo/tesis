library(tidyr)
library(spdep)
library(sf)
library(rgdal)
library(spatialreg)

setwd('/home/guillermo/Documentos/GitHub/tesis/')

# modelo poisson R
dd_deptos <- read.csv('tablas/dd_deptos.csv')

# reemplaza nulos dell largo del límite por 0.0001
dd_deptos <- dd_deptos %>% replace_na(list(largo_limite = 0.0001))

# model poisson regression using glm()
model <- glm(personas_mig ~ nom_depto_orig + dummy_limit + log(largo_limite) +
               log_pbi_destino + pbi_porcen_des + log_dist -1,
               family = poisson(link = "log"),
               data = dd_deptos)

# resumen
summary(model)

# estimación
dd_deptos$fitted <- round(fitted(model),0)

dd_deptos$fitted


######################
### SIN MONTEVIDEO ###
######################
dd_deptos_sin_mvo <- dd_deptos[dd_deptos$depto_origen !=1 & dd_deptos$depto_destino !=1,]

# model poisson regression using glm()
model <- glm(personas_mig ~ nom_depto_orig + dummy_limit + log(largo_limite) +
               log_pbi_destino + pbi_porcen_des + log_dist -1,
                family = poisson(link = "log"),
                data = dd_deptos_sin_mvo)

# resumen
summary(model)

# estimación
dd_deptos_sin_mvo$fitted <- fitted(model)

dd_deptos_sin_mvo$fitted



#### PESOS ESPACIALES

w = read.csv('tablas/matriz_deptos.csv', skip=2)

w$depto_origen <- NULL

w = as.matrix(w)

W = kronecker(w,w)
WW = mat2listw(W)

identical(W, listw2mat(WW) )

sum(W-listw2mat(WW))

# MEpois1 <- ME(counts~Municipio.o+Municipio.d+prom, data=tabla,
#               family="poisson", listw=WW, alpha=0.7, verbose=TRUE)

# MEpois1 <- ME(personas_mig ~ nom_depto_orig + dummy_limit + log(largo_limite) +
#                 log_pbi_destino + pbi_porcen_des + log_dist -1,
#                 family = poisson(link = "log"), listw=WW, alpha=0.7, verbose=TRUE)

model <- glm(personas_mig ~ nom_depto_orig + dummy_limit + log(largo_limite) +
               log_pbi_destino + pbi_porcen_des + log_dist -1,
               family = poisson(link = "log"),
             listw=WW, 
                data = dd_deptos_sin_mvo)


# retazo eugenia
# W=kronecker(w,w)
# WW=mat2listw(W)
# 
# identical(W,listw2mat(WW))
# 
# sum(W-listw2mat(WW))
# 
# 
# MEpois1 <- ME(counts~Municipio.o+Municipio.d+prom, data=tabla,
#               family="poisson", listw=WW, alpha=0.7, verbose=TRUE)
# str(MEpois1)
# dim(MEpois1$vectors)


deptos <- st_read("capas/ine_deptos_generalizada.gpkg")
#plot(deptos)

empresas <- read.csv('tablas/empresas_por_depto.csv', sep=';')

deptos_emp <-merge(deptos, empresas, by.x='cod_ine', by.y='DPTO')

# vecindad
deptos_emp.nb <- poly2nb(deptos_emp)

# pesos espaciales
pesos <- nb2listw(deptos_emp.nb, zero.policy=TRUE, style="W")

pesos

names(pesos)

summary(unlist(pesos$weights))


# Moran's I test
moran.test(deptos_emp$empresas, listw = pesos)
#moran.test(deptos_emp$empresas, listw = pesos, randomisation = FALSE)

moran.plot(deptos_emp$empresas, listw = pesos)


locm <- localmoran(deptos_emp$empresas, listw = pesos)
locm



