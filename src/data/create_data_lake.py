"""
Modulo de creación de directorios
----------------------------------------
Este modulo crea el esquema de carpetas que servirán para contener los diferentes datos y resultados

>>> create_data_lake()
assert os.path.isdir("data_lake/business") is True
assert os.path.isdir("data_lake/business/reports/figures") is True
assert os.path.isdir("data_lake/business/features") is True
assert os.path.isdir("data_lake/business/forecasts") is True
assert os.path.isdir("data_lake/cleansed") is True
assert os.path.isdir("data_lake/landing") is True
assert os.path.isdir("data_lake/raw") is True
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

    os.mkdir('data_lake', exist_ok=True)
    os.mkdir('data_lake/landing', exist_ok=True)
    os.mkdir('data_lake/raw', exist_ok=True)
    os.mkdir('data_lake/cleansed', exist_ok=True)
    os.mkdir('data_lake/business', exist_ok=True)
    os.mkdir('data_lake/business/reports', exist_ok=True)
    os.mkdir('data_lake/business/reports/figures', exist_ok=True)
    os.mkdir('data_lake/business/features', exist_ok=True)
    os.mkdir('data_lake/business/forecasts', exist_ok=True)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
