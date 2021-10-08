import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns

metadatos_figs = {'Author': '''Guillermo D'Angelo'''}

def size_font():
    "Setea fuentes y tamaños"
    size = 9
    font = {'fontname': 'Arial', 'fontsize': size}
    font_legend = font_manager.FontProperties(family='Arial', style='normal', size=10)
    return size, font, font_legend


def get_bottoms(lista):
    "Calcula los pisos en gráficas de barras apiladas"
    largo_lista=len(lista)
    bot = [[sum(col) for col in zip(*lista[0:i])] for i in range(largo_lista)]
    bot[0] = None
    return bot


def format_spines(color, ax):
    "Formatea spines"
    # oculta ejes superior y derecho
    [ax.spines[x].set_visible(False) for x in ["top", "right"]]
    # color de ejes inferior e izquierdo
    [ax.spines[x].set_color(color) for x in ["bottom", "left"]]

    return "Se formatearon los spines"


def format_ticks(labels, color, ind, font):
    "Formatea ticks y etiquetas"
    plt.xticks(ind, labels=labels, **font, color=color)
    plt.yticks(**font, color=color)
    plt.tick_params(axis='y',color=color)
    plt.tick_params(axis='x', bottom=False, labelbottom=True, color=color)

    return "Se formatearon los ticks"


def save_chart(name, metadatos_figs):
    "Guarda gráfica en PDF"
    plt.savefig('mapas_graficas/' + name,
                 bbox_inches= 'tight',
                 metadata = metadatos_figs)

    return print("Se guardó la gráfica en " + 'mapas_graficas/' + name)

def hide_spines(axis, todos=True):
    "Oculta spines"
    if todos==True:
        [axis.spines[i].set_visible(False) for i in ['right', 'top', 'left', 'bottom']]
    else:
        [axis.spines[i].set_visible(False) for i in ['right', 'top']]


def plot_gt(x, y, title, subtitle):
    fig = plt.figure()
    sns.regplot(x=x, y=y, line_kws={"color": "green"})
    plt.suptitle(title)
    plt.title(subtitle)
    plt.xlabel('Valores estimados')
    plt.ylabel('Groud truth')
