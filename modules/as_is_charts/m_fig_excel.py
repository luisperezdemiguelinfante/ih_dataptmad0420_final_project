
import xlsxwriter
from os import listdir
from os.path import isfile, join
import os
import glob
import re

def excel_chart(template):
    #workbook = xlsxwriter.Workbook('image.xlsx')
    #worksheet = workbook.add_worksheet()

    # Original image.
    #worksheet.insert_image('B2', 'plantas_process_finanzas.png')



    #had to change the path, i do not know why is not reading the correct one
    # i dont know how to give order of each sheet to capture one of them
    #howerver i dont know how to include in sheets independently


    path = ('/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/results/as_is/charts')
    lista = []

    for file in os.listdir(path):
        if file.endswith('.png'):
            lista.append(file)



    #this is to include them all in the same sheet, i dont know how to separate them

    list_name = ["first sheet", "second sheet", "third sheet"]

    #create a function to go over the list and no matter the lenght
    #worksheet.insert_image('B2', 'lista[0].png')
    #i = 0
    #while i < len(lista):
        #print(lista[i])
        #i = i + 1

    with xlsxwriter.Workbook('/Users/luisdemiguel/Desktop/Ironhack/ih_dataptmad0420_final_project/data/results/as_is/charts/excel_charts.xlsx') as workbook:

        for sheet_name in list_name:
            worksheet = workbook.add_worksheet(sheet_name)
            worksheet.write('B2', 'field_fte_split')
            worksheet.insert_image('B5', 'field_fte_split.png')
            worksheet.write('L2', 'split_task_all')
            worksheet.insert_image('L5', 'split_task_all.png')
            worksheet.write('T2', 'split_task_hq')
            worksheet.insert_image('T5', 'split_task_hq.png')
            worksheet.write('AB2', 'split_task_plantas')
            worksheet.insert_image('AB5', 'split_task_plantas.png')
            worksheet.write('B33', 'hq_process_finanzas')
            worksheet.insert_image('B35', 'hq_process_finanzas.png')
            worksheet.write('L33', 'hq_process_supply')
            worksheet.insert_image('L35', 'hq_process_supply.png')
            worksheet.write('Z33', 'hq_process_industrial')
            worksheet.insert_image('Z35', 'hq_process_industrial.png')
            worksheet.write('B68', 'plantas_process_finanzas')
            worksheet.insert_image('B70', 'plantas_process_finanzas.png')
            worksheet.write('P68', 'plantas_process_supply')
            worksheet.insert_image('P70', 'plantas_process_supply.png')
            worksheet.write('AD68', 'hq_process_industrial')
            worksheet.insert_image('AD70', 'plantas_process_industrial.png')


    return