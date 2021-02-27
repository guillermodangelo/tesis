def agrupar_por_tramos(df, col_tramo, col_edad, col_sexo):
    """
    Esta función agrupa por tramos, edad y sexo
    un pandas dataframe con datos del Censo 2011
    para ser usado para graficar pirámides de población
    """
    import pandas as pd
    import numpy as np
    
    # genera lista con cortes, para reclasificar el dataframe
    bins = [0 if i==-1 else i for i in range(-1,95,5)]

    # etiquetas con los tramos de edad usuales en pirámides de población
    labels = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
             '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '+95']

    # calcula tramos de edad
    df[col_tramo] = pd.cut(df[col_edad], bins= bins, include_lowest=False, labels=labels[:19])
    df[col_tramo] = np.where(df[col_edad] > 94 , labels[-1], df[col_tramo])
    df[col_tramo] = np.where(df[col_edad] == 0 ,  labels[0], df[col_tramo])

    # agrupa
    df_group = df.groupby([col_sexo, col_tramo]).size().reset_index()
    
    # renombra vars
    df_group.rename(columns={col_sexo: 'sexo', 0:'personas'}, inplace=True)
    
    # calcula porcentajes
    df_group['porc_pers'] = (df_group.personas / df_group.personas.sum())*100
    
    # pasa varones a negativo para grafica a la izquierda del eje central
    df_group.loc[df_group.sexo == 1, 'personas'] = -df_group['personas']
    df_group.loc[df_group.sexo == 1, 'porc_pers'] = -df_group['porc_pers']
    
    # genera etiqueta del sexo
    df_group['sexo_label'] = np.where(df_group['sexo'] ==1, 'varones', 'mujeres')
    
    return df_group


def agrupar_por_edades(df, col_edad):
    "Agrupa edades para graficar"
    
    import pandas as pd
    import numpy as np
    
    # agrupa
    df_group = df.groupby([col_edad]).size().reset_index()
    # renombra vars
    df_group.rename(columns={col_edad: 'edad', 0:'personas'}, inplace=True)
    # calcula porcentajes
    df_group['porc_pers'] = (df_group.personas / df_group.personas.sum())*100
    # genera vectores de edades del 0 asl 111, para pegar   
    col_pegue = pd.DataFrame(np.arange(0, 112), columns=['edad'])
    # pega con edades
    df_group_pegue = col_pegue.merge(df_group, how='left', on='edad')
    
    return df_group_pegue



def grupos_de_edad(df, col_edad):
    "Calcula porcentaje de personas por grupos de edad: 0 a 3, 4 a 17, 18 a 64 y >64 "
    import pandas as pd
    import numpy as np
    df.loc[df[col_edad].between(0,   3),  'grupo_edad'] = 1
    df.loc[df[col_edad].between(4, 17),  'grupo_edad'] = 2
    df.loc[df[col_edad].between(18, 64),  'grupo_edad'] = 3
    df.loc[df[col_edad] > 64,  'grupo_edad'] = 4
    df_group = df.groupby(['grupo_edad']).size().reset_index()
    
    # renombra vars
    df_group.rename(columns={0:'personas'}, inplace=True)
    # calcula porcentajes
    df_group['porc_pers'] = (df_group.personas / df_group.personas.sum())*100
    # enlista resultados
    lista_valores = df_group.porc_pers.values.tolist()
    
    # chequea que todos lo tramos de edad tengan valor, o pone 0 en la lista
    if sum(df.grupo_edad==1) == 0:
        lista_valores.insert(0, 0)
    if sum(df.grupo_edad==2) == 0:
        lista_valores.insert(1, 0)
    if sum(df.grupo_edad==3) == 0:
        lista_valores.insert(2, 0)
    if sum(df.grupo_edad==4) == 0:
        lista_valores.insert(3, 0)
    
    return lista_valores


def grupos_de_dependencia(df, col_edad):
    "Calcula porcentaje de personas por grupos de edad: 0 a 14, 15 a 64 y >64 "
    import pandas as pd
    import numpy as np
    df.loc[df[col_edad].between(0,   14),  'grupo_edad'] = 1
    df.loc[df[col_edad].between(15, 64),  'grupo_edad'] = 2
    df.loc[df[col_edad] > 64,  'grupo_edad'] = 3
    df_group = df.groupby(['grupo_edad']).size().reset_index()
    
    # renombra vars
    df_group.rename(columns={0:'personas'}, inplace=True)
    # calcula porcentajes
    df_group['porc_pers'] = (df_group.personas / df_group.personas.sum())*100
    # enlista resultados
    lista_valores = df_group.porc_pers.values.tolist()
    
    # chequea que todos lo tramos de edad tengan valor, o pone 0 en la lista
    if sum(df.grupo_edad==1) == 0:
        lista_valores.insert(0, 0)
    if sum(df.grupo_edad==2) == 0:
        lista_valores.insert(1, 0)
    if sum(df.grupo_edad==3) == 0:
        lista_valores.insert(2, 0)
    
    return lista_valores

