# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:54:01 2024

@author: gbournigal
"""

import pandas as pd


cuentas_ingreso = ['Extras']

cuentas_descuentos = [    
    'AFP',
    'SFS',
    'COOP',
    'Prestamos',
    'Coleg',
    'Comunic',
    'Escolares',
    'Dieta',
    'Uniforme',
    'Retenciones'
    ]
    

def excel_preprocess(file):
    df = pd.read_excel(file, sheet_name='Nómina fija')
    row_number = df.index[df.iloc[:, 0] == 'Carnet'].tolist()[0]
    df = df.iloc[row_number:]
    df.columns = df.iloc[0]
    df.columns = df.columns.str.strip()
    df = df.drop(df.index[:2])
    df.reset_index(drop=True, inplace=True)
    df['Mensual'] = df['Mensual'].fillna(0)
    mensual_index = df.columns.get_loc("Mensual")
    df.iloc[:, mensual_index + 1] = df.iloc[:, mensual_index + 1].fillna(0)
    
    df = df[pd.to_numeric(df['Mensual'], errors='coerce').notnull()]
    df = df[pd.to_numeric(df.iloc[:, mensual_index + 1], errors='coerce').notnull()]
    df['Mensual'] = df['Mensual'].fillna(0) + df.iloc[:, mensual_index + 1].fillna(0)
    df = df[df['Nombre'].notnull()]
    df = df[df['Carnet'] != 'Nivel:']
    
    columns_to_keep = [
        'Nombre',
        'Mensual',
        'Extras',
        'Ingresos',
        'AFP',
        'SFS',
        'COOP',
        'Prestamos',
        'Coleg',
        'Comunic',
        'Escolares',
        'Dieta',
        'Uniforme',
        'Retenciones',
        'Descuentos',
        'Pagar'
        ]
    
    
    df = df[columns_to_keep]
    long_df = pd.melt(df, id_vars=['Nombre'], var_name='Cuenta', value_name='Valor')
    long_df = long_df.dropna()
    return long_df[(long_df['Cuenta'].isin(['Mensual', 'Descuentos', 'Pagar'])) | (long_df['Valor'] != 0)]
