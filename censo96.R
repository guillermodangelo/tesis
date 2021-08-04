library(foreign)
library(haven)

# con el SPSS
ruta = '/mnt/hd/censo1996/MICRODATOS SPSS=CD/'
setwd(ruta)
path = file.path(ruta, "pob_96.sav")
censo = read.spss(path, to.data.frame=TRUE)

unique(censo$hace5aqui)
unique(censo$hac5depc)

# convierte a integer el depto de origen
unique(censo$hac5depc_int)

flujos_deptos96 = subset(censo, hace5aqui!='2')
unique(flujos_deptos96$hac5depc_int)

eliminar = c('  ', '30','99','40','70','35','31','32','80','90','60', '99')

flujos_deptos96 <- flujos_deptos96[!flujos_deptos96$hac5depc %in% eliminar, ]

unique(flujos_deptos96$hac5depc)
unique(flujos_deptos96$dpto)


flujos_deptos96 = flujos_deptos96[flujos_deptos96$dpto != flujos_deptos96$hac5depc, ]

nrow(flujos_deptos96)
# 193567 flujos, algo está mal




#### con el DBF
ruta = '/mnt/hd/censo1996/MICRODATOS DBF=CD/'
setwd(ruta)
path = file.path(ruta, "pob_96.DBF")
censo = read.dbf(path)

unique(censo$HACE5AQUI)
unique(censo$HAC5DEPC)

censo$HACE5AQUI = as.character(censo$HACE5AQUI)
censo$HAC5DEPC = as.character(censo$HAC5DEPC)
censo$DPTO = as.character(censo$DPTO)

unique(censo$HAC5DEPC)
unique(censo$DPTO)

flujos_deptos96 = subset(censo, is.na(censo$HACE5AQUI))


eliminar = c('30','99','40','70','35','31','32','80','90','60','99')

flujos_deptos96 = flujos_deptos96[!flujos_deptos96$HAC5DEPC %in% eliminar, ]
flujos_deptos96 = flujos_deptos96[complete.cases(flujos_deptos96$HAC5DEPC), ]

flujos_deptos96 = flujos_deptos96[flujos_deptos96$DPTO != flujos_deptos96$HAC5DEPC, ]


unique(flujos_deptos96$HAC5DEPC)

unique(flujos_deptos96$DPTO)

nrow(flujos_deptos96)

table(flujos_deptos96$HAC5DEPC, flujos_deptos96$DPTO)
