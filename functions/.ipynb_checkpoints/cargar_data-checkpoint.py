def cargar_data_eda():
    "Carga datos a ser usados en el EDA"
    
    import pandas as pd
    import numpy as np
    import geopandas as gpd
    
    # Datos censales
    censo = pd.read_csv('tablas/personas_censo_2011.gz', compression='gzip', header=0, sep=',', quotechar='"')
    # reemplaza el valor 5555 en edad (variable PERNA01) por NaNs
    censo.loc[censo.PERNA01 == 5555, 'PERNA01'] = np.nan

    # PBI departamental
    pbi = pd.read_csv('tablas/pbi_departamental.csv')

    # matriz de distancias
    md = pd.read_csv('tablas/df_distancias_centro_poblacion.csv')
    md.drop(['latlon_ori', 'latlon_des'], axis=1, inplace=True)

    return censo, pbi, md