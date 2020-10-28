from modules import m_clean
from modules.as_is_excel import m_procesos

#2.1 Alcance del analisis
#para obtener la distribucion en funcion de la naturaleza de actividad por site

all_sites_split_df = m_clean.dedicacion_clean.groupby(['site','operative model'])['reported fte'].sum().to_frame().reset_index()
#tambien por site especifica
site_split_df = all_sites_split_df.groupby('site')
specific_site_split = site_split_df.get_group('valencia')

#tambien por proceso especifico

# 2.2 Procesos
#para obtener un site o proceso especifico
process_site_split = m_procesos.procesos_split_level1.get_group('fuenmayor')
site_process_split = m_procesos.procesos_split_site.get_group('contabilidad general')