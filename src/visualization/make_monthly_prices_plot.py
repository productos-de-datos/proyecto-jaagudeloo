"""
Módulo de gráfica precios promedio mensuales.
-------------------------------------------------------------------------------
En este módulo se carga el archivo precios-mensuales.csv,
y se efectúa una gráfica para observar el comportamiento general del valor
de la electridad en la bolsa de valores.

>>> make_monthly_prices_plot()

"""

def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.

    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.

    """
    #raise NotImplementedError("Implementar esta función")
    import pandas as pd
    import matplotlib.pyplot as plt

    precios_mensuales = pd.read_csv('data_lake/business/precios-mensuales.csv')
    precios_mensuales['fecha'] = pd.to_datetime(precios_mensuales['fecha'])
    x = precios_mensuales.fecha
    y = precios_mensuales.precio
    plt.figure(figsize=(16, 8))
    plt.plot(x, y, 'r', label='Promedios Mensuales')
    plt.xlabel('Fecha')
    plt.ylabel('Precio en bolsa')
    plt.title('Promedios Mensuales')
    plt.grid()
    plt.legend()
    plt.savefig('data_lake/business/reports/figures/monthly_prices.png')

if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()
    doctest.testmod()