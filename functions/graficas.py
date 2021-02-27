def get_bottoms(lista):
    "Calcula los pisos en gráficas de barras apiladas"
    largo_lista=len(lista)
    bot = [[sum(col) for col in zip(*lista[0:i])] for i in range(largo_lista)]
    bot[0] = None
    return bot