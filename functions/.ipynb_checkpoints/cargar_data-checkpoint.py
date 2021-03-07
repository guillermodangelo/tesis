import pandas as pd
import numpy as np
import geopandas as gpd


def pad(df, series, nzfill):
    series_padded = df[series].astype(str).str.zfill(nzfill)
    return series_padded
    
    
def cargar_censo():
    "Carga datos del Censo INE 2011"
    # Datos censales
    censo = pd.read_csv('tablas/personas_censo_2011.gz', compression='gzip', header=0, sep=',', quotechar='"')
    # reemplaza el valor 5555 en edad (variable PERNA01) por NaNs
    censo.loc[censo.PERNA01 == 5555, 'PERNA01'] = np.nan
    # crea código de hogar
    censo['HOGCOD'] = censo.DPTO.astype(str) + pad(censo, 'LOC', 3) + pad(censo, 'SECC', 2) + pad(censo, 'SEGM', 3) + pad(censo, 'VIVID', 4) + pad(censo, 'HOGID', 2)
    # mueve columna a la sexta posición
    cols = list(censo.columns.values)
    cols.insert(6, cols.pop(-1))
    censo = censo[cols]

    return censo


def cargar_pbi():
    "Carga datos de PBI departamental (OPP)"  
    # PBI departamental
    pbi = pd.read_csv('tablas/pbi_departamental.csv')
    
    return pbi


def cargar_matriz_distancias():
    "Carga matriz de distancias entre centros de población"
    # matriz de distancias
    md = pd.read_csv('tablas/df_distancias_centro_poblacion.csv')
    md.drop(['latlon_ori', 'latlon_des'], axis=1, inplace=True)

    return md


def cargar_datos_geo():
    "Carga capas de información geográfica"
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
    
    return deptos, localidad, centro_pobl, capital
    


def cargar_data_eda():
    "Carga datos a ser usados en el EDA" 
    censo = cargar_censo()
    pbi = cargar_pbi()
    md = cargar_matriz_distancias()

    return censo, pbi, md



def cargar_data_metod():
    "Carga datos a ser usados en el apartado metodológico"
    censo = cargar_censo()
    pbi = cargar_pbi()
    md = cargar_matriz_distancias()
    deptos, localidad, centro_pobls, capital = cargar_datos_geo()
    
    return censo, pbi, md, deptos, localidad, centro_pobls, capital