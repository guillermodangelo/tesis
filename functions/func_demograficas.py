def indice_mascul(df, var_sexo, redondeo):
    "Calcula el índice de masculinidad sobre datos de personas del Censo INE 2011"
    import pandas as pd
    
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