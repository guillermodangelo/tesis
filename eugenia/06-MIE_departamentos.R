library(tidyr)

# modelo poisson R
dd_deptos <- read.csv('dd_deptos.csv')


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


