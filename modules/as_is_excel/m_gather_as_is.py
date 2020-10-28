import pandas as pd
#from modules.as_is_excel import m_alcance_analisis,m_procesos, m_vision_global




#def gather_as_is(template):
    #with pd.ExcelWriter('as_is_excel.xlsx') as writer:
        #m_alcance_analisis.employees_site.to_excel(writer, sheet_name='1_alcance_employee_site')
        #m_alcance_analisis.split_task_all.to_excel(writer, sheet_name='1_alcance_as_is_split_task_all')
        #m_alcance_analisis.split_task_site.to_excel(writer, sheet_name='1_alcance_split_task_site')
        #m_alcance_analisis.split_task_hq.to_excel(writer, sheet_name='1_alcance_split_task_hq')
        #m_alcance_analisis.split_field.to_excel(writer, sheet_name='1_alcance_split_field')

    #return m_alcance_analisis.employees_site, \
           #m_alcance_analisis.split_task_all, \
           #m_alcance_analisis.split_task_site, \
           #m_alcance_analisis.split_task_hq, \
           #m_alcance_analisis.split_field


#def to_excel(df_dict: dict, excel_name: str) -> None:
    #with pd.ExcelWriter(excel_name) as writer:
        #for df, sheet in df_dict.items():
            #df.to_excel(writer, sheet_name=sheet)
