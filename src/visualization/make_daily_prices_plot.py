"""
Módulo de gráfica precios promedio diarios.
-------------------------------------------------------------------------------
En este módulo se carga el archivo precios-diarios.csv,
y se efectúa una gráfica para observar el comportamiento general del valor
de la electridad en la bolsa de valores.

>>> make_daily_prices_plot()

"""

def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    #raise NotImplementedError("Implementar esta función")
    import os
    import pandas as pd

    precios_diarios = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    fig_precios_diarios = precios_diarios.plot(x = 'fecha', y = 'precio', xlabel = 'fecha', ylabel = 'precio', kind = 'line', figsize = (16,8), grid = True, title = 'Promedios Diarios').get_figure()
    fig_precios_diarios.savefig('data_lake/business/reports/figures/daily_prices.png')

if __name__ == "__main__":
    import doctest

    doctest.testmod()
