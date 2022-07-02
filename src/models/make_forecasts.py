"""
Modulo de creación de pronósticos
----------------------------------------
Este modulo crea el archivo .csv que contiene los precios promedio diarios reales y pronosticados

>>> make_forecasts()

"""
def test_train_datasets_1(data_frame, porcentaje):
    n = round(len(data_frame)*porcentaje)
    data_train = data_frame[:-n]
    data_test  = data_frame[-n:]
    return data_train, data_test

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    #raise NotImplementedError("Implementar esta función")

    import pandas as pd
    import os
    import pickle
    #from sklearn.ensemble import RandomForestRegressor
    #from skforecast.ForecasterAutoreg import ForecasterAutoreg

    precios_diarios = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    precios_diarios['fecha'] = pd.to_datetime(precios_diarios['fecha'], format='%Y-%m-%d')
    precios_diarios['dia_mes'] = pd.to_numeric(precios_diarios['dia_mes'])
    precios_diarios = precios_diarios.set_index('fecha')
    precios_diarios = precios_diarios.asfreq('D')
    precios_diarios = precios_diarios.sort_index()
    precios_diarios.index = pd.DatetimeIndex(precios_diarios.index).to_period('D')

    data_train, data_test = test_train_datasets_1(precios_diarios, 0.3)

    estimador =  pickle.load('/src/models/precios-diarios.pkl', 'rb')
    
    pasos = len(data_test)

    precio_proyectado = estimador.forecast(pasos, exog = data_test[['dia_mes']])

    predicciones =  pd.DataFrame(precio_proyectado)

    data_pred = pd.concat([data_test.loc[:, ['precio']], predicciones], axis=1, join = 'inner')
    data_pred = data_pred.reset_index()
    data_pred.columns = ['fecha', 'precio_promedio_real', 'precio_promedio_pred']

    data_pred.to_csv('data_lake/business/forecasts/precios-diarios.csv', index = False)

if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
