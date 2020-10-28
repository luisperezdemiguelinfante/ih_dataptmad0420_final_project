import pandas as pd
from openpyxl import load_workbook

#path = r"./Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/ih_dataptmad0420_final_project/template/as_is_excel.xlsx"

#book = load_workbook(path)
#writer = pd.ExcelWriter(path, engine = 'openpyxl')
#writer.book = book



def process_site_split(template):
    process_site = template.groupby(['level1', 'site'])['reported fte'].sum().to_frame().reset_index()
    site_process = template.groupby(['site', 'level1'])['reported fte'].sum().to_frame().reset_index()


    with pd.ExcelWriter('/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/results/as_is/tables/as_is_2_2_process.xlsx') as writer:
        process_site.to_excel(writer, sheet_name='2_2_process_site')
        site_process.to_excel(writer, sheet_name='2_2_site_process')

    return process_site, site_process