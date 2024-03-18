# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 09:05:22 2024

@author: georg
"""

import streamlit as st
import io
import zipfile

from excel_preprocess import excel_preprocess, cuentas_ingreso, cuentas_descuentos
from pdf_generator import generate_payroll_summary


st.set_page_config(
    page_title="JMM: Nómina",
    page_icon="",
    layout="wide",
)

st.title('Volantes nómina JMM')

file = st.file_uploader("Seleccione el xls de nómina", type='xls')

if file is not None:
    df = excel_preprocess(file)
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, mode="w") as zip_archive:
        for employee_name in df.Nombre.unique():
            df_temp = df[df['Nombre'] == employee_name]
            generate_payroll_summary(df_temp, cuentas_ingreso, cuentas_descuentos, zip_archive)
    
    zip_buffer.seek(0)

    st.download_button(label="Descargar Volantes en ZIP",
                       data=zip_buffer,
                       file_name="volantes_nomina.zip",
                       mime="application/zip")