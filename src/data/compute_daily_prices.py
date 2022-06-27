"""
Módulo de cálculo de precios promedio diarios.
-------------------------------------------------------------------------------
En este módulo se toma el archivo precios-horarios.csv, con la finalidad de obtener por cada día el precio
promedio que tuvo la electricidad en la bolsa nacional.

>>> compute_daily_prices()

"""

def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd

    precios_horarios = pd.read_csv(f'data_lake/cleansed/precios-horarios.csv')
    precios_diarios = precios_horarios.groupby('fecha').mean()
    precios_diarios_sin_hora = precios_diarios.drop(['hora'], axis=1)
    precios_diarios_sin_hora.to_csv(f'data_lake/business/precios-diarios.csv', header = True, index = True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
