from IPython.display import Markdown as md, display, Math

def printmd(string):
    "Imprime texto en markdown"
    display(md(string))

def printmath(string):
    "Imprime ecuaciones"
    display(Math(string))
