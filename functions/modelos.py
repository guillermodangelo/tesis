from sklearn.metrics import r2_score, mean_squared_error
from IPython.display import Markdown as md
from functions.impresion import printmd


def get_gml_params(model, variables):
    "Accede a los parámetros alfa y beta dentro de los resutaldos del modelo"
    params = [model.params[i] for i in variables]
    params_str = [str(round(i, 4)) for i in params]
    return params, params_str

def print_params(variables, params_list):
    "Imprime los parámetros"
    return print("""alpha ({}) = {}\nbeta ({}) = {}
    """.format(variables[0], params_list[0], variables[1], params_list[1]))

def print_scores(df, gt, est, modelo):
    "Imprime r cuadrado y error mínimo cuadrático de un modelo"
    r2 = r2_score(df[gt], df[est])
    rmse = mean_squared_error(df[gt], df[est], squared=False)

    printmd('**Bondad de ajuste del modelo {}**'.format(modelo))
    printmd("$R²$ = " + round(r2, 4).astype(str))
    printmd("RMSE = " + round(rmse, 4).astype(str))


def print_scores_simple(ground_truth, estimation):
    "Imprime r cuadrado y error mínimo cuadrático de un modelo"
    r2 = r2_score(ground_truth, estimation)
    rmse = mean_squared_error(ground_truth, estimation, squared=False)
    
    printmd("$R²$ = " + round(r2, 4).astype(str))
    printmd("RMSE = " + round(rmse, 4).astype(str))