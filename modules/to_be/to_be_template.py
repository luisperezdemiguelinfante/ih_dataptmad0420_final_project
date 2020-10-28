import pandas as pd

def to_be_eficiencias(template):

    dedicacion = pd.read_excel(
        '/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/raw/garnica.xlsx')

    dedicacion_clean = dedicacion[
        ['site', 'employee', 'position', 'task description', 'reported fte', 'total', 'field', 'level1', 'level2',
         'level3', 'operative']].dropna()

    eficiencias = pd.read_excel(
        '/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/raw/eficiencias.xlsx')

    dedicacion_csc = dedicacion_clean[dedicacion_clean['operative'].eq('CSC')].pivot_table(
        values=['reported fte'],
        index=['level1'],
        aggfunc='sum').fillna(0).round(2)



    dedicacion_total = dedicacion_clean.pivot_table(values=['reported fte'], index=['level1'], aggfunc='sum').fillna(
        0).round(2)

    porcentaje_dedicacion = pd.merge(dedicacion_csc, dedicacion_total, how='inner', on='level1')
    porcentaje_dedicacion['%'] = (
                (porcentaje_dedicacion['reported fte_x'] / porcentaje_dedicacion['reported fte_y']) * 100).round(2)

    eficiencias_total = pd.merge(eficiencias, porcentaje_dedicacion, how='inner', on='level1')
    eficiencias_total = eficiencias_total[['level1', 'tipo', 'nombre', 'eficiencias', '%']]

    def f(row):
        if row['tipo'] == 'comun':
            val = row['eficiencias'] * row['%']
        else:
            val = row['eficiencias'] * 100
        return val

    eficiencias_total['eficiencias totales'] = eficiencias_total.apply(f, axis=1).round(2)
    eficiencias_totales_summary = eficiencias_total.groupby('level1')['eficiencias totales'].sum().to_frame()

    eficiencias_totales_summary.to_csv(
        '/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/processed/eficiencias_totales.xlsx')

    return eficiencias_totales_summary