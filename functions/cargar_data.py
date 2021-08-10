import pandas as pd
import numpy as np
import geopandas as gpd


def pad(df, series, nzfill):
    series_padded = df[series].astype(str).str.zfill(nzfill)
    return series_padded


def get_codseg(df):
    codseg = df.DPTO.astype(str) + pad(df, 'SECC', 2) + pad(df, 'SEGM', 3)
    return codseg

    
def cargar_censo_96():
    "Carga datos del Censo INE 1996"
    # Datos censales
    censo96 = pd.read_csv('tablas/personas_censo_1996.gz', compression='gzip', header=0, sep=',', quotechar='"')
    return censo96


def cargar_marco_96():
    "Carga datos del marco censal INE 1996"
    # Datos censales
    file = 'marcos_censales/MARCO96.xls'
    marco96 = pd.read_excel(file)
    marco96['codseg'] = get_codseg(marco96)
    
    return marco96


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


def cargar_censo_muestra(muestra, variables):
    "Carga muestra datos del Censo INE 2011"
    # Datos censales
    censo = pd.read_csv('tablas/personas_censo_2011.gz', compression='gzip', header=0, sep=',', quotechar='"', usecols=variables)
    # reemplaza el valor 5555 en edad (variable PERNA01) por NaNs
    censo.loc[censo.PERNA01 == 5555, 'PERNA01'] = np.nan

    return censo.sample(muestra).reset_index(drop=True)


def cargar_censo_vars(variables):
    "Carga datos del Censo INE 2011"
    # Datos censales
    censo = pd.read_csv('tablas/personas_censo_2011.gz', compression='gzip', header=0, sep=',', quotechar='"', usecols=variables)
    return censo


def cargar_censo_nrows(nrows):
    "Carga muestra datos del Censo INE 2011"
    # Datos censales
    censo = pd.read_csv('tablas/personas_censo_2011.gz', compression='gzip', header=0, sep=',', quotechar='"', nrows=nrows)
    # reemplaza el valor 5555 en edad (variable PERNA01) por NaNs
    censo.loc[censo.PERNA01 == 5555, 'PERNA01'] = np.nan

    return censo


def cargar_migrantes_internos():
    "Carga datos de migrantes internos recientes del Censo INE 2011"
    df = pd.read_csv('tablas/censo_2011_migrantes_internos.gz', compression='gzip', header=0, sep=',', quotechar='"')

    return df


def recuperar_poblacion_2011():
    "Recupera DF con cantidad de habitantes por departamento según censo 2011"
    depid = list(range(1,20))
    poblacion = [1318755,
                73377,
                520173,
                84698,
                123203,
                57084,
                25050,
                67047,
                58815,
                164298,
                113107,
                54765,
                103473,
                68088,
                124861,
                108304,
                82594,
                90051,
                48134]
    data_tuples = list(zip(depid, poblacion))
    return pd.DataFrame(data_tuples, columns=['DPTO','poblacion'])


def recuperar_poblacion_2011_5años():
    "Recupera DF con cantidad de habitantes de 5 años y más por departamento según censo 2011"
    depid = list(range(1,20))
    poblacion = [1236133,
                 67863,
                 484060,
                 78717,
                 115155,
                 53162,
                 23449,
                 62665,
                 55247,
                 153019,
                 104855,
                 50375,
                 95688,
                 63563,
                 115058,
                 100827,
                 76894,
                 83814,
                 44939]
    data_tuples = list(zip(depid, poblacion))
    return pd.DataFrame(data_tuples, columns=['DPTO','poblacion'])


def recuperar_poblacion_1996():
    "Recupera DF con cantidad de habitantes por departamento según censo 1996"
    depid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    poblacion =  [1344839,
                 75059,
                 443053,
                 82510,
                 120241,
                 55716,
                 25030,
                 66503,
                 61085,
                 127502,
                 111509,
                 51713,
                 98472,
                 70292,
                 117597,
                 96664,
                 81557,
                 84919,
                 49502]
    data_tuples = list(zip(depid, poblacion))
    return pd.DataFrame(data_tuples, columns=['DPTO','poblacion'])


def recuperar_poblacion_1996_5años():
    """Recupera DF con cantidad de habitantes de 5 o más años por departamento según censo 1996.
       Calculado por Macadar y Dominguez (2008)"""
    depid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    poblacion =  [1187111,
                    63587,
                    384620,
                    70939,
                    104493,
                    48296,
                    22120,
                    58308,
                    53526,
                    109399,
                    96318,
                    44456,
                    83233,
                    60922,
                    99613,
                    84679,
                    71254,
                    72781,
                    43071]
    data_tuples = list(zip(depid, poblacion))
    return pd.DataFrame(data_tuples, columns=['DPTO','poblacion'])


def cargar_pbi():
    "Carga datos de PBI departamental (OPP)"  
    cols = ['DPTO', 'miles_de_pesos', 'porcentaje_pbi']
    pbi = pd.read_csv('tablas/pbi_departamental.csv', usecols=cols, decimal=',')
    
    return pbi


def recuperar_empresas_por_depto():
    """Recupera DF con cantidad de empresas industriales por departamento
    a 2013, según datos del OTU (OPP)"""
    depid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    empresas =  [3124, 55, 563, 88, 60, 40, 28, 101, 54, 188, 144, 54, 67, 62, 97, 154, 85, 61, 38]
    data_tuples = list(zip(depid, empresas))
    return pd.DataFrame(data_tuples, columns=['DPTO','empresas'])



def recuperar_parti_pbi():
    """Recupera DF con cantidad participación percentual en el PBI
    de cada departamento.
    Fuente: Observatorio Territorio Uruguay - OPP en base a diversas fuentes"""
    depid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    porc_pbi =  [49.1, 1.5, 10.5, 1.9, 4.9, 1.5, 0.8, 2.0, 1.6, 5.7, 2.7, 2.6, 2.1, 1.9, 2.7, 3.1, 2.2, 2.1, 1.2]
    data_tuples = list(zip(depid, porc_pbi))
    return pd.DataFrame(data_tuples, columns=['DPTO','porc_pbi'])


def cargar_vecindad():
    "Carga datos sobre vecindad de deptos"  
    # Vecindad
    vecindad = pd.read_csv('tablas/deptos_vecinos.csv')
    
    return vecindad


def cargar_matriz_distancias():
    "Carga matriz de distancias entre centros de población"
    # matriz de distancias
    md = pd.read_csv('tablas/df_distancias_centro_poblacion.csv')
    md.drop(['latlon_ori', 'latlon_des'], axis=1, inplace=True)
    return md

def cargar_matriz_dist_loc():
    "Carga matriz de distancias entre localidades INE 2011"
    cols = ['cod_ori', 'cod_des', 'cod', 'distancia_m']
    md = pd.read_csv('tablas/df_distancias_localidades.csv', usecols=cols)
    return md

def cargar_datos_geo():
    "Carga capas de información geográfica"
    # carga capa departamentos INE pg
    deptos = gpd.read_file('capas/ine_deptos.gpkg')
    # carga capa departamentos INE con geometrías simplificadas
    deptos_sim = gpd.read_file('capas/ine_deptos_generalizada.gpkg')
    # agrega centroides de departamentos
    deptos['centroide'] = deptos['geometry'].centroid
    # carga capa localidades INE pt
    localidad = gpd.read_file('capas/ine_localidades.gpkg')
    localidad.CODLOC = localidad.CODLOC.astype(int)
    # centro de población
    centro_pobl = gpd.read_file('capas/centro_poblacion.gpkg')
    # filtra capitales departamentales de las localidades INE
    capital = localidad[localidad.CAPITAL==True].reset_index(drop=True)
    
    return deptos, deptos_sim, localidad, centro_pobl, capital


def cargar_data_eda():
    "Carga datos a ser usados en el EDA" 
    censo = cargar_censo()
    pbi = cargar_pbi()
    md = cargar_matriz_distancias()

    return censo, pbi, md


def filter_df_censo(df):
    "Filtra datos del censo para quedarse solo con migrantes internos recientes"
    mgr = df.loc[df.PERMI07 == 3].reset_index(drop=True)
    # identifica depto de residencia anterior, creando var "depto_origen"
    mgr.insert(0, 'depto_origen', mgr.loc[:,('PERMI07_2')])
    # convierte a integer
    mgr.loc[:,('depto_origen')] = mgr.loc[:,('depto_origen')].astype(int)
    # renombra DPTO
    mgr.rename(columns={'DPTO': 'depto_destino'}, inplace=True)
    # agrega código de localidad de origen
    mgr['loc_origen'] = (mgr.depto_origen.astype('str') + mgr.PERMI07_3.astype(int).astype(str).str.zfill(3))
    # agrega código de localidad de destino
    mgr['loc_destino'] = (mgr.depto_destino.astype('str') + mgr.LOC.astype(str).str.zfill(3)).astype(int)

    return mgr


def cargar_nombres():
    list_names = ['Montevideo', 'Artigas', 'Canelones', 'Cerro Largo', 'Colonia', 'Durazno',
                  'Flores', 'Florida', 'Lavalleja','Maldonado', 'Paysandú', 'Río Negro', 'Rivera',
                  'Rocha', 'Salto', 'San José', 'Soriano', 'Tacuarembó', 'Treinta y Tres']
    
    return list_names


def cargar_matriz_deptos():
    "Carga matriz de migrantes internos entre deptos"
    matrix = pd.read_csv('tablas/matriz_deptos.csv', skiprows=2, index_col='depto_origen').values.tolist()   
    return matrix


def format_depto(df, column):
    "Formatea strings de departameto, AM y total"
    deptos_dict = {
        'AREA METRO': 'Área metropolitana',
        'MONTEVIDEO': 'Montevideo',
        'ARTIGAS': 'Artigas',
        'CANELONES': 'Canelones',
        'CERRO LARGO': 'Cerro Largo',
        'COLONIA': 'Colonia',
        'DURAZNO': 'Durazno',
        'FLORES': 'Flores',
        'FLORIDA': 'Florida',
        'LAVALLEJA': 'Lavalleja',
        'MALDONADO': 'Maldonado',
        'PAYSANDU': 'Paysandú',
        'RIO NEGRO': 'Río Negro',
        'RIVERA': 'Rivera',
        'ROCHA': 'Rocha',
        'SALTO': 'Salto',
        'SAN JOSE': 'San José',
        'SORIANO': 'Soriano',
        'TACUAREMBO': 'Tacuarembó',
        'TREINTA Y TRES': 'Treinta y Tres',
        'TOTAL':'Total',
        'Total':'Total'
        }

    return df[column].map(deptos_dict)


def decode_depto(df, column):
    "Decodifica departamento INE"
    deptos_dict = {
    1: 'MONTEVIDEO',
    2: 'ARTIGAS',
    3: 'CANELONES',
    4: 'CERRO LARGO',
    5: 'COLONIA',
    6: 'DURAZNO',
    7: 'FLORES',
    8: 'FLORIDA',
    9: 'LAVALLEJA',
    10: 'MALDONADO',
    11: 'PAYSANDU',
    12: 'RIO NEGRO',
    13: 'RIVERA',
    14: 'ROCHA',
    15: 'SALTO',
    16: 'SAN JOSE',
    17: 'SORIANO',
    18: 'TACUAREMBO',
    19: 'TREINTA Y TRES'
        }
    return df[column].map(deptos_dict)


def decode_depto_short(array):
    "Decodifica departamento INE, abreviado"
    deptos_dict = {
    1:	'Mvdeo.',
    2:	'Artigas',
    3:	'Can.',
    4:	'C. Largo',
    5:	'Colonia',
    6:	'Durazno',
    7:	'Flores',
    8:	'Florida',
    9:	'Lavalleja',
    10:	'Maldonado',
    11:	'Paysandú',
    12:	'R. Negro',
    13:	'Rivera',
    14:	'Rocha',
    15:	'Salto',
    16:	'San José',
    17:	'Soriano',
    18:	'Tacuarembó',
    19:	'T. y Tres'
        }
    return array.map(deptos_dict)



def loc_decode(df):
    "Decodifica codlocs INE"
    locs = pd.read_csv('tablas/localidades_censales_2011.csv',
                  dtype= {'departamento': str,'localidad': str, 'codloc': str,},
                  usecols=['departamento','localidad','codloc'])
                  
    merge_loc = df.merge(locs, left_on='loc_destino', right_on='codloc').drop('codloc', axis=1)

    return  merge_loc


def codif_diada_depto(df):
    "Codifica díadas por departamento"
    cod_depto_destino_str = df['depto_destino'].astype(str).str.zfill(2)
    cod_diada_depto = (df['depto_origen'].astype(str) + cod_depto_destino_str).astype(int)
    return cod_diada_depto