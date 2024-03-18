from fpdf import FPDF
from tempfile import NamedTemporaryFile

def generate_payroll_summary(df, cuentas_ingreso, cuentas_descuentos, zip_archive):
    employee_name = df['Nombre'].iloc[0]
    sueldo_bruto = df[df['Cuenta'] == 'Mensual']['Valor'].iloc[0]
    total_ingresos = sueldo_bruto = df[df['Cuenta'] == 'Ingresos']['Valor'].iloc[0]
    df_ingresos = df[df['Cuenta'].isin(cuentas_ingreso)]
    df_deducciones = df[df['Cuenta'].isin(cuentas_descuentos)]
    total_deducciones = df[df['Cuenta'] == 'Descuentos']['Valor'].iloc[0]
    total_pago = df[df['Cuenta'] == 'Pagar']['Valor'].iloc[0]
    # Create instance of FPDF class
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add a page
    pdf.add_page()

    # Set font for the entire document
    pdf.set_font("Arial", size=12)
    pdf.image("logo.png", x=10, y=10, w=30)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Volante de Pago", ln=True, align="C")
    pdf.ln(20)

    # Employee details
    pdf.set_font("Arial", style="", size=12)
    pdf.cell(0, 10, f"Nombre del Empleado: {employee_name}", ln=True)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Ingresos:", ln=True)
    pdf.set_font("Arial", style="", size=10)
    pdf.cell(0, 10, f"Sueldo Bruto: RD${'{:,.1f}'.format(sueldo_bruto)}", ln=True)
    for index, row in df_ingresos.iterrows():
        pdf.cell(0, 10, f"{row['Cuenta']}: RD${'{:,.1f}'.format(row['Valor'])}", ln=True)
    pdf.cell(0, 10, f"Total de Ingresos: RD${'{:,.1f}'.format(total_ingresos)}", ln=True)    
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Deducciones:", ln=True)
    pdf.set_font("Arial", style="", size=10)
    for index, row in df_deducciones.iterrows():
        pdf.cell(0, 10, f"{row['Cuenta']}: RD${'{:,.1f}'.format(row['Valor'])}", ln=True)
    pdf.cell(0, 10, f"Total de Deducciones: RD${'{:,.1f}'.format(total_deducciones)}", ln=True)  
    pdf.ln(10)

    # Total payment
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, f"Pago total: RD${'{:,.1f}'.format(total_pago)}", ln=True)
    pdf.ln(10)

    # Footer
    pdf.set_font("Arial", style="", size=10)
    pdf.cell(0, 10, "Colegio Jaime Molina Mota", ln=True, align="C")

    # Save the PDF to the specified output path
    with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        pdf.output(temp_pdf.name)  # Generate PDF and save to temporary file
    
    zip_archive.write(temp_pdf.name, f"volante_{employee_name}.pdf")