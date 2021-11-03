library(tidyverse)
library(viridis)
library(patchwork)
library(circlize)
library(networkD3)

# Load dataset from github
#data <- read.table("https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/13_AdjacencyDirectedWeighted.csv", header=TRUE)

setwd('/home/guillermo/Documentos/GitHub/tesis/')
data <- read.csv('tablas/dd_deptos.csv', sep=';')

cols <- c('nom_depto_orig', 'nom_depto_des', 'personas_mig')
data <- data[cols]

data$nom_depto_des <-  paste0(data$nom_depto_des, "_")

colnames(data) <- c("source", "target", "value")


# From these flows we need to create a node data frame: it lists every entities involved in the flow
nodes <- data.frame(name=c(as.character(data$source),
                           as.character(data$target)) %>% unique())

# With networkD3, connection must be provided using id, not using real name like in the links dataframe.. So we need to reformat it.
data$IDsource=match(data$source, nodes$name)-1 
data$IDtarget=match(data$target, nodes$name)-1

# prepare colour scale
ColourScal ='d3.scaleOrdinal() .range(["#FDE725FF","#B4DE2CFF","#6DCD59FF","#35B779FF","#1F9E89FF","#26828EFF","#31688EFF","#3E4A89FF","#482878FF","#440154FF"])'

# Make the Network
sankeyNetwork(Links = data, Nodes = nodes,
              Source = "IDsource", Target = "IDtarget",
              Value = "value", NodeID = "name", 
              sinksRight=FALSE,
              colourScale=ColourScal, nodeWidth=40, fontSize=10, nodePadding=20)

