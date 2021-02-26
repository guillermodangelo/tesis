def agrupar_df(df, col_tramo, col_sexo):
    """
    Esta función agrupa por tramos de edad 
    un pandas dataframe con datos del Censo 2011
    """
    
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