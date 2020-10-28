import pandas as pd

def alcance_analisis(template):

    employees_site = template.groupby('site')['employee'].nunique().to_frame().sort_values(by='employee', ascending=False).reset_index()

    #def division_tareas(empresa):
    split_task_all = template.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_all['% dedication'] = ((split_task_all['reported fte'] / split_task_all['reported fte'].sum()) * 100).round(2)
    split_task_all = split_task_all.append(split_task_all.sum(numeric_only=True), ignore_index=True)
    split_task_all.replace('', 'total')

    #def division_tareas_site(empresa):
    as_is_plantas = template[template['site'] != 'hq']
    split_task_site = as_is_plantas.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_site['% dedication'] = ((split_task_site['reported fte'] / split_task_site['reported fte'].sum()) * 100).round(2)
    split_task_site = split_task_site.append(split_task_site.sum(numeric_only=True), ignore_index=True)

    #def division_tareas_hq(empresa):
    as_is_hq = template[template['site']=='hq']
    split_task_hq = as_is_hq.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_hq['% dedication'] = ((split_task_hq['reported fte'] / split_task_hq['reported fte'].sum()) * 100).round(2)
    split_task_hq = split_task_hq.append(split_task_hq.sum(numeric_only=True), ignore_index=True)


    #def fte_proceso(empresa):
    split_field = template.groupby('field')['reported fte'].sum().to_frame().round(2).sort_values(by='reported fte', ascending=False).reset_index()


    with pd.ExcelWriter('/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/results/as_is/tables/as_is_1_alcance.xlsx') as writer:
        employees_site.to_excel(writer, sheet_name='1_alcance_employee_site')
        split_task_all.to_excel(writer, sheet_name='1_alcance_as_is_split_task_all')
        split_task_site.to_excel(writer, sheet_name='1_alcance_split_task_site')
        split_task_hq.to_excel(writer, sheet_name='1_alcance_split_task_hq')
        split_field.to_excel(writer, sheet_name='1_alcance_split_field')

    #dictionary_alcance_analisis= {employees_site: '1_alcance_employee_site',
            #split_task_all: '1_alcance_as_is_split_task_all',
            #split_task_site: '1_alcance_split_task_site',
            #split_task_hq: '1_alcance_split_task_hq'}
            #split_field: '1_alcance_split_field'}

    #return dictionary_alcance_analisis



    return employees_site, split_task_all, split_task_site, split_task_hq, split_field
