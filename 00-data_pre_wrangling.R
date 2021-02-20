# guarda como RData
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
          'PERPH02',
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

rm(p)
gc()

# guarda como CSV
write.csv(p_filter, file=gzfile('personas_censo_2011.gz'), row.names=F)

write.csv(p_filter, file='personas_censo_2011.csv', row.names=F)


