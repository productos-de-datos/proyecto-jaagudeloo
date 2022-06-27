"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
En este módulo se descargan los datos externos y se almacenan en la carpeta landing del data lake

>>> ingest_data()

"""

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    #raise NotImplementedError("Implementar esta función")

    import os
    import urllib.request

    anio_inicial = 1995
    anio_final = 2021
    rango_anios = list(range(anio_inicial, anio_final + 1, 1))

    for anio in rango_anios:
        try:
            archivo = open(f'data_lake/landing/{anio}.xlsx', 'wb')
            ruta = urllib.request.urlopen(f'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{anio}.xlsx?raw=true')
            archivo.write(ruta.read())
            archivo.close()
        except:
            archivo.close()
            os.remove(f'data_lake/landing/{anio}.xlsx')

            archivo = open(f'data_lake/landing/{anio}.xls', 'wb')
            ruta = urllib.request.urlopen(f'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{anio}.xls?raw=true')
            archivo.write(ruta.read())
            archivo.close()

if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
