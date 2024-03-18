# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 09:05:22 2024

@author: georg
"""

from excel_preprocess import excel_preprocess, cuentas_ingreso, cuentas_descuentos
from pdf_generator import generate_payroll_summary


df = excel_preprocess('Nomina feb 2024.xls')

for i in df.Nombre.unique():
    df_temp = df[df['Nombre'] == i]
    generate_payroll_summary(df_temp, cuentas_ingreso, cuentas_descuentos)

