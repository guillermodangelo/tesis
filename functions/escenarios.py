
def calc_pbi(series, pbi_porc):
    "Estima PBI en base a crecimiento anual reportado"
    series_pond = series
    for i in pbi_porc:
        series_pond =+ series_pond + (series_pond * i)

    return round(series_pond).astype(int)