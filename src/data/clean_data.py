"""
Módulo de limpieza de datos.
-------------------------------------------------------------------------------
En este módulo se toman los archivos .csv de la carpeta raw y se concatenan en un único archivo precios-horarios.csv,
con la finalidad de tener un vector de datos de precio por cada hora de cada día.

>>> clean_data()

"""

def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    #raise NotImplementedError("Implementar esta función")
    import os
    import pandas as pd

    contenido_raw = os.listdir('data_lake/raw')
    anio_inicial = 1995
    anio_final = 2021

    archivo_inicial = pd.read_csv(f'data_lake/raw/{anio_inicial}.csv')

    for elemento in range(anio_inicial + 1, anio_final + 1, 1):
        if elemento == anio_inicial + 1:
            archivo = pd.read_csv(f'data_lake/raw/{elemento}.csv')
            archivo_concat = pd.concat([archivo_inicial, archivo], ignore_index = True)
        else:
            archivo = pd.read_csv(f'data_lake/raw/{elemento}.csv')
            archivo_concat = pd.concat([archivo_concat, archivo], ignore_index = True)

    archivo_concat.columns = ['fecha', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

    archivo_concat_melt = pd.melt(archivo_concat, id_vars = ['fecha'], value_vars = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], var_name = 'hora', value_name = 'precio')
    archivo_concat_melt = archivo_concat_melt.sort_values(by=['fecha', 'hora'])
    archivo_concat_melt = archivo_concat_melt[archivo_concat_melt['fecha'].notnull()]

    archivo_concat_melt.to_csv(f'data_lake/cleansed/precios-horarios.csv', header = True, index = False)

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
