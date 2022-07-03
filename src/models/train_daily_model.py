"""
Modulo de creación entrenamiento de modelo
----------------------------------------
En este módulo se parten los datos en entrenamiento y prueba, y se pronostican los datos de prueba
obteniendo unos precios promedio diarios pronosticados

>>> train_daily_model()

"""


def test_train_datasets_1(data_frame, porcentaje):
    n = round(len(data_frame)*porcentaje)
    data_train = data_frame[:-n]
    data_test  = data_frame[-n:]
    return data_train, data_test


def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    #raise NotImplementedError("Implementar esta función")
    import os
    import pickle
    import pandas as pd
    import statsmodels.api as st

    precios_diarios = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    precios_diarios['fecha'] = pd.to_datetime(precios_diarios['fecha'], format='%Y-%m-%d')
    precios_diarios['dia_mes'] = pd.to_numeric(precios_diarios['dia_mes'])
    precios_diarios = precios_diarios.set_index('fecha')
    precios_diarios = precios_diarios.asfreq('D')
    precios_diarios = precios_diarios.sort_index()
    precios_diarios.index = pd.DatetimeIndex(precios_diarios.index).to_period('D')

    # Se parten los datos para entrenamiento y prueba
    data_train, data_test = test_train_datasets_1(precios_diarios, 0.3)

    forecaster = st.tsa.statespace.SARIMAX(
    endog = data_train[['precio']],
    exog = data_train[['dia_mes']],
    enforce_stationarity = False,
    enforce_invertibility = False,
    )

    model = forecaster.fit()
    pickle.dump(model, open('src/models/precios-diarios.pkl', 'wb'))

if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
