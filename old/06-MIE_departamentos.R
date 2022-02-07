library(tidyr)
library(dplyr)
library(spdep)
library(sf)
library(rgdal)
library(spatialreg)


setwd('/home/guillermo/Documentos/GitHub/tesis/')

#setwd('C:/Users/user/Documents/GitHub/tesis')


# modelo poisson R
dd_deptos <- read.csv('tablas/dd_deptos.csv', sep=';')

# convierte distancia entre deptos de metros a kilómetros
dd_deptos$dist_km <- dd_deptos$dist/1000

# convierte largo del límite de metros a kilómetros
dd_deptos$largo_limite_km <- dd_deptos$largo_limite/1000

# reemplaza nulos del largo del límite por 0.0001
dd_deptos <- dd_deptos %>% replace_na(list(largo_limite_km = 0.0001))

# convierte PBI departamental a cientos de millones de pesos
dd_deptos$pbi_destino_millardos <- dd_deptos$pbi_destino/100000


# model poisson regression using glm()
# restringido en origen
# Atención!: NO UTLIZAR VARIABLES CON LOGARITMO APLICADO
model <- glm(personas_mig ~ nom_depto_orig + dummy_limit + largo_limite_km +
               pbi_destino_millardos + dist_km - 1 ,
               family = poisson(link = "log"),
               data = dd_deptos)
# resumen
summary(model)


# estimación
dd_deptos$fitted <- round(fitted(model),0)

CalcRSquared <- function(observed,estimated){
  r <- cor(observed,estimated)
  R2 <- r^2
  R2
}

CalcRSquared(dd_deptos$personas_mig, dd_deptos$fitted)



# convierte a matriz la estimación
mat = as.data.frame.matrix(xtabs(fitted ~ depto_origen + depto_destino, dd_deptos))
mat

######################
### SIN MONTEVIDEO ###
######################
dd_deptos_sin_mvo <- dd_deptos[dd_deptos$depto_origen !=1 & dd_deptos$depto_destino !=1,]

# model poisson regression using glm()
model <- glm(personas_mig ~ nom_depto_orig + dummy_limit + largo_limite_km +
               pbi_destino_miles_de_millones + dist_km -1,
                family = poisson(link = "log"),
                data = dd_deptos_sin_mvo)

# resumen
summary(model)

# intervalos de confianza
confint(model)

# estimación
dd_deptos_sin_mvo$fitted <- round(fitted(model), 0)

#r cuadrado
CalcRSquared(dd_deptos_sin_mvo$personas_mig, dd_deptos_sin_mvo$fitted)


# estimación como matriz
mat = as.data.frame.matrix(xtabs(fitted ~ depto_origen + depto_destino, dd_deptos_sin_mvo))
mat

####################
# Pesos espaciales #
####################

w = read.csv('tablas/matriz_deptos.csv', skip=2)

w$depto_origen <- NULL

w = as.matrix(w)

W = kronecker(w, w)
#W = w %x% w

WW = mat2listw(W)

listW = listw2mat(WW)

sasa <- list(WW)


# chequea identidad
# por alguna razón no funciona
identical(W, listW)

# este chequeo sí funciona
max(abs(W-listw2mat(WW)))


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

aux <- nb2listw(deptos_emp.nb)

aux2 <- listw2mat(aux)

# pesos espaciales
pesos <- nb2listw(deptos_emp.nb, zero.policy=TRUE, style="W")

pesos

names(pesos)

summary(unlist(pesos$weights))


set.seed(987654)
n <- length(deptos_emp.nb)
uncorr_x <- rnorm(n)
rho <- 0.5
autocorr_x <- invIrW(pesos, rho) %*% uncorr_x

moran_u <- moran.test(uncorr_x, listw = pesos)
# Moran's I test
moran.test(deptos_emp$empresas, listw = pesos)
#moran.test(deptos_emp$empresas, listw = pesos, randomisation = FALSE)

moran.plot(deptos_emp$empresas, listw = pesos)


locm <- localmoran(deptos_emp$empresas, listw = pesos)
locm



