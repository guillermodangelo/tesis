def export_csvt(lista, filename):
    "Exporta lista a archivo csvt para usars con QGIS"
    campos_str = ','.join([str(elem) for elem in campos])
    with open(filename, 'w') as f:
        f.write(str(campos_str) + "\n")