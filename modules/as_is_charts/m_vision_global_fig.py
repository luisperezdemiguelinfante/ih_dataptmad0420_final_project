
import pandas as pd
from pptx import Presentation



def vision_global_fig(template):
    filter_hq = template['site'] == 'hq'

    dedicacion_clean_hq = template[filter_hq]
    dedicacion_clean_plantas = template[~filter_hq]

    #3.1 vision global

    distribucion_field_hq_fte = dedicacion_clean_hq.pivot_table(values=['reported fte'], index=['field'], columns=['site'],
                                                    aggfunc='sum').fillna(0).round(2)
    distribucion_field_all_plantas_fte = dedicacion_clean_plantas.pivot_table(values=['reported fte'], index=['field'],
                                                                columns=['site'], aggfunc='sum').fillna(0).round(2)
    distribucion_field_all_plantas_fte['plantas'] = distribucion_field_all_plantas_fte.sum(axis=1)
    distribucion_field_plantas_fte = distribucion_field_all_plantas_fte['plantas'].to_frame()
    distribucion_field_fte_split = pd.merge(distribucion_field_hq_fte, distribucion_field_plantas_fte, how='inner',
                                            on='field')
    distribucion_field_fte_split['total'] = distribucion_field_fte_split.sum(axis=1)
    distribucion_field_fte_split['%'] = (
            (distribucion_field_fte_split['total'] / distribucion_field_fte_split['total'].sum()) * 100).round(2)

    distribucion_field_fte_split_fig=distribucion_field_fte_split.plot.pie(y='%', figsize=(5, 5), autopct='%1.1f%%').legend(bbox_to_anchor=(1,1.025), loc="upper left").figure.savefig('field_fte_split', bbox_inches='tight')


    #split_task

    split_task_all = template.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_all['% dedication'] = (
                (split_task_all['reported fte'] / split_task_all['reported fte'].sum()) * 100).round(2)
    split_task_all = split_task_all.append(split_task_all.sum(numeric_only=True), ignore_index=True)
    split_task_all_drop = split_task_all.dropna()
    split_task_all_fig = split_task_all_drop.plot.pie(y='% dedication', figsize=(5, 5), autopct='%1.1f%%').figure.savefig('split_task_all', bbox_inches='tight')


    split_task_hq = dedicacion_clean_hq.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_hq['% dedication'] = (
            (split_task_hq['reported fte'] / split_task_hq['reported fte'].sum()) * 100).round(2)
    split_task_hq = split_task_hq.append(split_task_all.sum(numeric_only=True), ignore_index=True)
    split_task_hq_drop = split_task_hq.dropna()
    split_task_hq_fig = split_task_hq_drop.plot.pie(y='% dedication', figsize=(5, 5),
                                                    autopct='%1.1f%%').figure.savefig('split_task_hq',
                                                                                      bbox_inches='tight')

    split_task_plantas = dedicacion_clean_plantas.groupby('operative')['reported fte'].sum().to_frame().reset_index()
    split_task_plantas['% dedication'] = (
            (split_task_plantas['reported fte'] / split_task_plantas['reported fte'].sum()) * 100).round(2)
    split_task_plantas = split_task_plantas.append(split_task_all.sum(numeric_only=True), ignore_index=True)
    split_task_plantas_drop = split_task_plantas.dropna()
    split_task_plantas_fig = split_task_plantas_drop.plot.pie(y='% dedication', figsize=(5, 5),
                                                              autopct='%1.1f%%').figure.savefig('split_task_plantas',
                                                                                                bbox_inches='tight')


    #finanzas plantas
    plantas_process_finanzas = dedicacion_clean_plantas[dedicacion_clean_plantas.field.eq('finanzas')].pivot_table(
        values=['reported fte'],
        index=['field', 'level1'],
        columns=['site'],
        aggfunc='sum').fillna(0).round(2)
    plantas_process_finanzas_fig = (plantas_process_finanzas / plantas_process_finanzas.sum() * 100).T.plot(kind='bar',
                                                                                                            stacked=True,
                                                                                                            figsize=(7,
                                                                                                                     5)).legend(
        bbox_to_anchor=(1, 1.025), loc="upper left").figure.savefig('plantas_process_finanzas', bbox_inches='tight')
    #hq
    hq_process_finanzas = dedicacion_clean_hq[dedicacion_clean_hq.field.eq('finanzas')].pivot_table(
        values=['reported fte'],
        index=['field', 'level1'],
        columns=['site'],
        aggfunc='sum').fillna(0).round(2)
    hq_process_finanzas_fig = (hq_process_finanzas / hq_process_finanzas.sum() * 100).T.plot(kind='bar', stacked=True,
                                                                                             figsize=(4, 5)).legend(
        bbox_to_anchor=(1, 1.025), loc="upper left").figure.savefig('hq_process_finanzas', bbox_inches='tight')

    #supply plantas
    plantas_process_supply = dedicacion_clean_plantas[dedicacion_clean_plantas.field.eq('supply chain')].pivot_table(
        values=['reported fte'],
        index=['field', 'level1'],
        columns=['site'],
        aggfunc='sum').fillna(0).round(2)
    plantas_process_supply_fig = (plantas_process_supply / plantas_process_supply.sum() * 100).T.plot(kind='bar',
                                                                                                      stacked=True,
                                                                                                      figsize=(
                                                                                                      7, 6)).legend(
        bbox_to_anchor=(1, 1.025), loc="upper left").figure.savefig('plantas_process_supply', bbox_inches='tight')

    #hq

    hq_process_supply = dedicacion_clean_hq[dedicacion_clean_hq.field.eq('supply chain')].pivot_table(
        values=['reported fte'],
        index=['field', 'level1'],
        columns=['site'],
        aggfunc='sum').fillna(0).round(2)
    hq_process_supply_fig = (hq_process_supply / hq_process_supply.sum() * 100).T.plot(kind='bar', stacked=True,
                                                                                       figsize=(4, 6)).legend(
        bbox_to_anchor=(1, 1.025), loc="upper left").figure.savefig('hq_process_supply', bbox_inches='tight')

    #industrial plantas
    plantas_process_industrial = dedicacion_clean_plantas[dedicacion_clean_plantas.field.eq('industrial')].pivot_table(
        values=['reported fte'],
        index=['field', 'level1'],
        columns=['site'],
        aggfunc='sum').fillna(0).round(2)
    plantas_process_industrial_fig = (plantas_process_industrial / plantas_process_industrial.sum() * 100).T.plot(
        kind='bar', stacked=True, figsize=(7, 6)).legend(bbox_to_anchor=(1, 1.025), loc="upper left").figure.savefig(
        'plantas_process_industrial', bbox_inches='tight')

    #hq
    hq_process_industrial = dedicacion_clean_hq[dedicacion_clean_hq.field.eq('industrial')].pivot_table(
        values=['reported fte'],
        index=['field', 'level1'],
        columns=['site'],
        aggfunc='sum').fillna(0).round(2)

    hq_process_industrial_fig = (hq_process_industrial / hq_process_industrial.sum() * 100).T.plot(kind='bar',
                                                                                                   stacked=True,
                                                                                                   figsize=(
                                                                                                   5, 6)).legend(
        bbox_to_anchor=(1, 1.025), loc="upper left").figure.savefig('hq_process_industrial', bbox_inches='tight')

    return plantas_process_finanzas_fig, hq_process_finanzas_fig, plantas_process_supply_fig, hq_process_supply_fig, plantas_process_industrial_fig, hq_process_industrial_fig, distribucion_field_fte_split_fig, split_task_all_fig, split_task_hq_fig, split_task_plantas_fig