"""
Módulo de pipeline.
-------------------------------------------------------------------------------
En este módulo se elabora un Pipeline con luigi, con la finalidad de correr varios scripts en uno solo.
Con este script se importan, transforman, limpian y calculan los promedios diarios y mensuales
de los valores de la electricidad en la bolsa.

>>> pipeline()

"""

"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi
from luigi import Task, LocalTarget
import ingest_data
import transform_data
import clean_data
import compute_daily_prices
import compute_monthly_prices

class IngestTransformCleanData(Task):
    def output(self):
        return LocalTarget(f'data_lake/cleansed/precios-horarios.csv')
    def run(self):
        ingest_data.ingest_data()
        transform_data.transform_data()
        clean_data.clean_data()

class ComputeDailyMonthly(Task):
    def requires(self):
        return IngestTransformCleanData()
    def output(self):
        return LocalTarget([f'data_lake/business/precios-diarios.csv', f'data_lake/business/precios-mensuales.csv'])
    def run(self):
        compute_daily_prices.compute_daily_prices()
        compute_monthly_prices.compute_monthly_prices()

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    luigi.run(['ComputeDailyMonthly', "--local-scheduler"])
