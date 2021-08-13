import pandas as pd
import geopandas as gpd
import numpy as np

def _odline(orig, dest, geo, zonecode):
    return LineString([deptos[geo[zonecode] == orig].centroid.values[0], geo[geo[zonecode] == dest].centroid.values[0]])


def odflow(flowdata, origin, destination, flow_value, geo, zonecode):
    "Makes a geodataframe of flows"
    # First make all the lines
    lines = flowdata.apply(lambda x: _odline(x[origin], x[destination], geo, zonecode), axis=1)
    # Now get the series of flow values
    flows = flowdata[[flow_value, origin, destination]]
    # Now return a geodataframe
    return gpd.GeoDataFrame(flows, geometry=lines, crs = geo.crs)


def centro_medio(df, campo_depto, campo_poblacion):
    "Calcula el centro medio de población"
    x_mean = []
    y_mean = []

    for n in range (1, 20): # itera sobre departamentos
        _df = df.loc[df[campo_depto]==n].reset_index()

        rango = range(_df.shape[0])
        x = [_df.loc[i].geometry.centroid.x * _df.loc[i][campo_poblacion] for i in rango]
        y = [_df.loc[i].geometry.centroid.y * _df.loc[i][campo_poblacion] for i in rango]

        x_mean.append(np.int64((sum(x) / _df[campo_poblacion] .sum())))
        y_mean.append(np.int64((sum(y) / _df[campo_poblacion] .sum())))
        
    return x_mean, y_mean