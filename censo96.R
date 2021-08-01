ruta = '/mnt/hd/censo1996/MICRODATOS SPSS=CD/'
setwd(ruta)

library(foreign)

path = file.path(ruta, "pob_96.sav")
censo = read.spss(path, to.data.frame=TRUE)


setwd("/mnt/hd/censo1996/")





save(censo, file="personas_censo_96.RData")



unique(censo$hace5aqui)

unique(censo$hac5depc)


censo$hac5depc_int = strtoi(censo$hac5depc)

colnames(censo)

unique(censo$hac5depc_int)


flujos_deptos96 = subset(censo, hace5aqui!='2')

flujos_deptos96 = subset(flujos_deptos96, hac5depc_int<=19)



unique(flujos_deptos96$hac5depc_int)
unique(flujos_deptos96$hace5aqui)

flujos_deptos96 = flujos_deptos96[flujos_deptos96$dpto != flujos_deptos96$hace5aqui, ]

nrow(flujos_deptos96)

