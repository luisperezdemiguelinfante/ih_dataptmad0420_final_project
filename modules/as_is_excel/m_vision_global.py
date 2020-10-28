
import pandas as pd



def empleado_dedicacion(template):
    employees_site = template.groupby('site')['employee'].nunique().to_frame().sort_values(by='site', ascending=False).reset_index()
    employee_dedicacion = template.groupby('site')['reported fte'].sum().to_frame().sort_values(by='site', ascending=False).reset_index().round(2)
    site_employee_dedicacion = pd.merge(employees_site, employee_dedicacion, how='inner', on='site')
    site_employee_dedicacion['% dedicacion'] = ((site_employee_dedicacion['reported fte'] / site_employee_dedicacion['employee']) * 100).round(2)


    filter_hq = template['site'] == 'hq'

    data_hq = template[filter_hq]
    data_sites = template[~filter_hq]

    #3.1 vision global - tipo actividad
    split_task_all = template.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_all['% dedication'] = (
            (split_task_all['reported fte'] / split_task_all['reported fte'].sum()) * 100).round(2)
    split_task_all = split_task_all.append(split_task_all.sum(numeric_only=True), ignore_index=True)
    split_task_all_drop = split_task_all.dropna()
    split_task_all_fig = split_task_all_drop.plot.pie(y='% dedication', figsize=(5, 5),
                                                      autopct='%1.1f%%').figure.savefig('split_task',
                                                                                        bbox_inches='tight')

    split_task_hq = data_hq.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_hq['% dedication'] = (
            (split_task_hq['reported fte'] / split_task_hq['reported fte'].sum()) * 100).round(2)
    split_task_hq = split_task_hq.append(split_task_all.sum(numeric_only=True), ignore_index=True)
    split_task_hq_drop = split_task_hq.dropna()
    split_task_hq_fig = split_task_hq_drop.plot.pie(y='% dedication', figsize=(5, 5),
                                                      autopct='%1.1f%%').figure.savefig('split_task_hq',
                                                                                        bbox_inches='tight')

    split_task_plantas = data_sites.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_plantas['% dedication'] = (
            (split_task_plantas['reported fte'] / split_task_plantas['reported fte'].sum()) * 100).round(2)
    split_task_plantas = split_task_hq.append(split_task_all.sum(numeric_only=True), ignore_index=True)
    split_task_plantas_drop = split_task_plantas.dropna()
    split_task_plantas_fig = split_task_plantas_drop.plot.pie(y='% dedication', figsize=(5, 5),
                                                    autopct='%1.1f%%').figure.savefig('split_task_plantas',
                                                                                      bbox_inches='tight')


    # process - sites

    distribucion_field_hq_fte = data_hq.pivot_table(values=['reported fte'], index=['field'],columns=['site'], aggfunc='sum').fillna(0).round(2)
    distribucion_field_all_plantas_fte = data_sites.pivot_table(values=['reported fte'], index=['field'],columns=['site'], aggfunc='sum').fillna(0).round(2)
    distribucion_field_all_plantas_fte['plantas'] = distribucion_field_all_plantas_fte.sum(axis=1)
    distribucion_field_plantas_fte=distribucion_field_all_plantas_fte['plantas'].to_frame()
    distribucion_field_fte_split = pd.merge(distribucion_field_hq_fte, distribucion_field_plantas_fte, how='inner',on='field')
    distribucion_field_fte_split['total'] = distribucion_field_fte_split.sum(axis=1)
    distribucion_field_fte_split['%'] = (
                (distribucion_field_fte_split['total'] / distribucion_field_fte_split['total'].sum()) * 100).round(2)



    with pd.ExcelWriter('/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/results/as_is/tables/as_is_3_1_vision_global_empleado.xlsx') as writer:
        site_employee_dedicacion.to_excel(writer, sheet_name='3_1_site_employee_dedicacion')
        distribucion_field_fte_split.to_excel(writer, sheet_name='3_1_field_fte')
        split_task_all.to_excel(writer, sheet_name='3_1_task_all')
        split_task_hq.to_excel(writer, sheet_name='3_1_task_hq')
        split_task_plantas.to_excel(writer, sheet_name='3_1_task_plantas')

    #dictionary_vision_global= {site_employee_dedicacion: '3_1_site_employee_dedicacion',
                               #distribucion_field_fte_split: '3_1_field_fte',
                               #split_task_all: '3_1_task_all',
                               #split_task_hq: '3_1_task_hq',
                               #split_task_plantas: '3_1_task_plantas'}


    #return dictionary_vision_global





    return site_employee_dedicacion, distribucion_field_fte_split, split_task_all, split_task_hq, split_task_plantas

'''
return dict(site_employee_dedication: 'sheet_name', distribution_field_fte_split: 'sheet_tanem')
'''

