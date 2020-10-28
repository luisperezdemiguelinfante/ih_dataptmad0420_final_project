from modules import m_acquisition
import pandas as pd

def tareas_proceso(template):
    filter_hq = template['site'] == 'hq'
    data_hq = template[filter_hq]
    data_sites = template[~filter_hq]


    pivot_process_site_all = template.reset_index().pivot_table(values=['reported fte'],index=['field', 'level1'], columns=['site'],aggfunc='sum').fillna(0).round(2)
    pivot_process_site_hq = data_hq.reset_index().pivot_table(values=['reported fte'],index=['field', 'level1'], columns=['site'],aggfunc='sum').fillna(0).round(2)
    pivot_process_site_plantas = data_sites.reset_index().pivot_table(values=['reported fte'],
                                                                                    index=['field', 'level1'],
                                                                                    columns=['site'],
                                                                                    aggfunc='sum').fillna(0).round(2)

    # HQ
    pivot_process_site_hq_finanzas = pivot_process_site_hq.loc["finanzas", ('reported fte', slice(None))]
    pivot_process_site_hq_supply_chain = pivot_process_site_hq.loc["supply chain", ('reported fte', slice(None))]
    pivot_process_site_hq_industrial = pivot_process_site_hq.loc["industrial", ('reported fte', slice(None))]

    #plantas
    pivot_process_site_plantas_finanzas = pivot_process_site_plantas.loc["finanzas", ('reported fte', slice(None))]
    pivot_process_site_plantas_supply_chain = pivot_process_site_plantas.loc[
        "supply chain", ('reported fte', slice(None))]
    pivot_process_site_plantas_industrial = pivot_process_site_plantas.loc["industrial", ('reported fte', slice(None))]

    with pd.ExcelWriter('/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/results/as_is/tables/as_is_3_1_process_site.xlsx') as writer:
        pivot_process_site_all.to_excel(writer, sheet_name='3_1_process_site_all')
        pivot_process_site_hq.to_excel(writer, sheet_name='3_1_process_site_hq')
        pivot_process_site_plantas.to_excel(writer, sheet_name='3_1_process_site_plantas')

        # HQ
        pivot_process_site_hq_finanzas.to_excel(writer, sheet_name='3_1_site_hq_finanzas')
        pivot_process_site_hq_supply_chain.to_excel(writer, sheet_name='3_1_site_hq_supply_chain')
        pivot_process_site_hq_industrial.to_excel(writer, sheet_name='3_1_site_hq_industrial')

        # Plantas
        pivot_process_site_plantas_finanzas.to_excel(writer, sheet_name='3_1_site_plantas_finanzas')
        pivot_process_site_plantas_supply_chain.to_excel(writer, sheet_name='3_1_site_plantas_supply_chain')
        pivot_process_site_plantas_industrial.to_excel(writer, sheet_name='3_1_site_plantas_industrial')


    return pivot_process_site_all, pivot_process_site_hq, pivot_process_site_plantas, pivot_process_site_hq_finanzas, pivot_process_site_hq_supply_chain, pivot_process_site_hq_industrial, pivot_process_site_plantas_finanzas, pivot_process_site_plantas_supply_chain, pivot_process_site_plantas_industrial
