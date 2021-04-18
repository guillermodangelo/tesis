# guarda como RData (corre en Ubuntu)
library(foreign)
setwd("/mnt/c1e28322-6237-43a1-bcf0-c89831b4d46d/censo2011")

p <- read.dbf("Personas.dbf")

save(p, file="personas_censo.RData")
rm(list=ls())
gc()

setwd("/home/guille/Documentos/proy_municipios_censo")
load("personas_censo.RData")

save(p, file="personas_censo.RData")

rm(p)
gc()

# recarga
library(foreign)
setwd("/mnt/c1e28322-6237-43a1-bcf0-c89831b4d46d/censo2011")
load("personas_censo.RData")



vars <- c('DPTO',
          'LOC',
          'SECC',
          'SEGM',
          'VIVID',
          'TIPO_VIVIE',
          'HOGID',
          'PERPH02',
          'PERPA01',
          'PERER02',
          'PERNA01',
          'PERNA02',
          'PERMI01',
          'PERMI01_1',
          'PERMI01_2',
          'PERMI01_3',
          'PERMI01_4',
          'PERMI02',
          'PERMI02_1',
          'PERMI05',
          'PERMI05_1',
          'PERMI06',
          'PERMI06_1',
          'PERMI06_2',
          'PERMI06_3',
          'PERMI06_4',
          'PERMI07',
          'PERMI07_1',
          'PERMI07_2',
          'PERMI07_3',
          'PERMI07_4',
          'PERED00',
          'PERED01',
          'PERED02',
          'PERED02_1',
          'PERED02_2',
          'PERED02_3',
          'PERED02_4',
          'PERED03_R',
          'PERED03_1',
          'PERED03_2',
          'PERED04_R',
          'PERED05_R',
          'PERED06_R',
          'CODIGO_CAR',
          'PERED08',
          'NIVELEDU_R')


p_filter <- p[vars]

save(p_filter, file="personas_censo_migrac.RData")

gc()

# guarda como GZIP
write.csv(p_filter, file=gzfile('personas_censo_1996.gz'), row.names=F)

setwd("/home/guillermo/Documentos/GitHub/tesis/tablas")

write.csv(p_filter, file=gzfile('personas_censo_1996.gz'), row.names=F)

#write.csv(p_filter, file='personas_censo_2011.csv', row.names=F)




# censo 1996 (corre en Windows)
library(foreign)

setwd("C:/Users/user/Documents/censo1996/MICRODATOS DBF=CD/CPV96 CD75/")

p <- read.dbf("pob_96.DBF")

save(p, file="personas_censo_96.RData")
rm(list=ls())
gc()

# carga lo ya guardado
setwd("C:/Users/user/Documents/censo1996/MICRODATOS DBF=CD/CPV96 CD75/")
load("personas_censo_96.RData")

vars <- c('DPTO',
          'LOC',
          'SECC',
          'SEGM',
          'VIVIENDA',
          'TIPVIV',
          'HOGARVIV',
          'PARENTESCO',
          'SEXO',
          'EDAD',
          'HACE5AQUI',
          'HAC5DEPC',
          'HAC5LOC'
       )


p_filter <- p[vars]

save(p_filter, file="personas_censo_96_migrac.RData")


# guarda como GZIP
write.csv(p_filter, file=gzfile('personas_censo_1996.gz'), row.names=F)

setwd("C:/Users/user/Documents/GitHub/tesis/tablas")

write.csv(p_filter, file=gzfile('personas_censo_1996.gz'), row.names=F)


