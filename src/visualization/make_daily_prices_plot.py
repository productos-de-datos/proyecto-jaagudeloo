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
    import pandas as pd
    import matplotlib.pyplot as plt

    precios_diarios = pd.read_csv('data_lake/business/precios-diarios.csv')
    precios_diarios['fecha'] = pd.to_datetime(precios_diarios['fecha'])
    x = precios_diarios.fecha
    y = precios_diarios.precio
    plt.figure(figsize=(16, 8))
    plt.plot(x, y, 'g', label='Promedios Diarios')
    plt.xlabel('Fecha')
    plt.ylabel('Precio en bolsa')
    plt.title('Promedios Diarios')
    plt.legend()
    plt.savefig('data_lake/business/reports/figures/daily_prices.png')

if __name__ == "__main__":
    import doctest

    doctest.testmod()
