import pandas as pd


def plantilla(empresa):  # pestana='dedicaciones'):
    dedicacion = pd.read_excel(
        '/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/raw/garnica.xlsx')

    dedicacion_clean = dedicacion[
        ['site', 'employee', 'position', 'task description', 'reported fte', 'total', 'field', 'level1', 'level2',
         'level3', 'operative']].dropna()

    with pd.ExcelWriter(
            '/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/processed/template.xlsx') as writer:
        dedicacion_clean.to_excel(writer, sheet_name='template')


    return dedicacion_clean


def plantilla_hq(template):
    dedicacion_clean_hq = template[template['site'] == 'hq']

    return dedicacion_clean_hq


def plantilla_plantas(template):
    dedicacion_clean_plantas = template[template['site'] != 'hq']

    return dedicacion_clean_plantas
