def cargar_data_eda():
    "Carga datos a ser usados en el EDA"
    import pandas as pd
    import numpy as np    
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


def cargar_data_metod():
    "Carga datos a ser usados en el apartado metodológico"
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
    # carga capa departamentos INE pg
    deptos = gpd.read_file('capas/ine_deptos.gpkg')
    # agrega centroides de departamentos
    deptos['centroide'] = deptos['geometry'].centroid
    # carga capa localidades INE pt
    localidad = gpd.read_file('capas/ine_localidades.gpkg')
    localidad.CODLOC = localidad.CODLOC.astype(int)
    # centro de población
    centro_pobl = gpd.read_file('capas/centro_poblacion.gpkg')
    # filtra capitales departamentales de las localidades INE
    capital = localidad[localidad.CAPITAL==True].reset_index(drop=True)
    
    return censo, pbi, md, deptos, localidad, centro_pobls, capital