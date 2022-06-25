"""
Modulo de creación de directorios
----------------------------------------
Este modulo crea el esquema de carpetas que servirán para contener los diferentes datos y resultados

>>> create_data_lake()

"""

def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    #raise NotImplementedError("Implementar esta función")

    import os

    #os.mkdir('data_lake', exist_ok=True)
    #os.mkdir('data_lake/landing', exist_ok=True)
    #os.mkdir('data_lake/raw', exist_ok=True)
    #os.mkdir('data_lake/cleansed', exist_ok=True)
    #os.mkdir('data_lake/business', exist_ok=True)
    #os.mkdir('data_lake/business/reports', exist_ok=True)
    #os.mkdir('data_lake/business/reports/figures', exist_ok=True)
    #os.mkdir('data_lake/business/features', exist_ok=True)
    #os.mkdir('data_lake/business/forecasts', exist_ok=True)

    os.mkdir('data_lake')
    os.mkdir('data_lake/landing')
    os.mkdir('data_lake/raw')
    os.mkdir('data_lake/cleansed')
    os.mkdir('data_lake/business')
    os.mkdir('data_lake/business/reports')
    os.mkdir('data_lake/business/reports/figures')
    os.mkdir('data_lake/business/features')
    os.mkdir('data_lake/business/forecasts')

if __name__ == "__main__":
    import doctest

    doctest.testmod()
