"""
Modulo de creación de pronósticos
----------------------------------------
Este modulo crea el archivo .csv que tendrá la finalidad de ser empleado para hacer los modelos de predicción

>>> make_forecasts()

"""


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
    #from sklearn.ensemble import RandomForestRegressor
    #from skforecast.ForecasterAutoreg import ForecasterAutoreg

    precios_diarios = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    precios_diarios['fecha'] = pd.to_datetime(precios_diarios['fecha'], format='%Y-%m-%d')
    precios_diarios['dia_mes'] = pd.to_numeric(precios_diarios['dia_mes'])
    precios_diarios = precios_diarios.set_index('fecha')
    precios_diarios = precios_diarios.asfreq('D')
    precios_diarios = precios_diarios.sort_index()
    precios_diarios.index = pd.DatetimeIndex(precios_diarios.index).to_period('D')


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
