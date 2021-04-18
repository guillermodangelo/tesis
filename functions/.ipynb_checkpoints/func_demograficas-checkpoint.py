import pandas as pd

def indice_mascul(df, var_sexo, redondeo):
    "Calcula el índice de masculinidad sobre datos de personas del Censo INE 2011"
    
    # filtra varones y mujeres
    varones = df.loc[df[var_sexo] ==1].count()[0] 
    mujeres = df.loc[df[var_sexo] ==2].count()[0]
    # calcula el índice
    ind_masc = (varones/mujeres)*100
    
    return round(ind_masc, redondeo)

def porcentaje_sexo(df, var_sexo):
    "Calcula el porcentaje por sexo de un dataframe"
    # filtra varones y mujeres
    varones_prop = (df.loc[df[var_sexo] ==1].count()[0])/df.shape[0]*100
    mujeres_prop = (df.loc[df[var_sexo] ==2].count()[0])/df.shape[0]*100

    return (varones_prop, mujeres_prop)


def get_cam(df, Mij='Mij', Mji='Mji', Pi='Pi', Pj='Pj'):
    """
    Calcula el coeficiente de atracción mutua para un dataframe con los campos
    Mij = migrantes de i a j
    Mji = migrantes de j a i
    Pi  = población de i
    Pj  = población de j
    """
    cam = (df[Mij] + df[Mji]) / (df[Pi] + df[Pj]) * 1000
    cam_round = round(cam).astype(int)
    return cam_round