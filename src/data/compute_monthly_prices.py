"""
Módulo de cálculo de precios promedio mensuales.
-------------------------------------------------------------------------------
En este módulo se toma el archivo precios-horarios.csv, con la finalidad de obtener por cada mes el precio
promedio que tuvo la electricidad en la bolsa nacional.

>>> compute_monthly_prices()

"""

def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd

    precios_horarios = pd.read_csv(f'data_lake/cleansed/precios-horarios.csv')
    precios_horarios['fecha'] = pd.to_datetime(precios_horarios['fecha'])
    precios_horarios.set_index('fecha', inplace = True)
    precios_mensuales = precios_horarios.resample('M').mean()
    precios_mensuales_sin_hora = precios_mensuales.drop(['hora'], axis=1)
    precios_mensuales_sin_hora.to_csv(f'data_lake/business/precios-mensuales.csv', header = True, index = True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
