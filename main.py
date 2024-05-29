import utils
import read_csv
import charts
import pandas as pd
import matplotlib.pyplot as plt

def run():
    df= pd.read_csv('mremh_presupuestoejecutadomisionesecuadorexterior_2024marzo.csv')
    df=df[df['Región']=='América del Norte']
    countries=df['Región'].values
    presupuesto=df['PRESUPUESTO'].values
    charts.generate_pie_chart(countries,presupuesto)

    data=read_csv.read_csv('mremh_presupuestoejecutadomisionesecuadorexterior_2024marzo.csv')
    region=input('Type Region => ')
    print(region)

    result=utils.presupuesto_by_region(data,region)

    if len(result)>0:
        region=result[0]
        print(region)
        labels,values=utils.get_presupuesto(region)
        charts.generate_bar_chart(region['Country'],labels,values)

    if __name__=='__main__':
        run()
    