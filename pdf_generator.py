from fpdf import FPDF
import pandas as pd

def generate_payroll_summary(df):
    # Create instance of FPDF class
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add a page
    pdf.add_page()

    # Set font for the entire document
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, txt="Payroll Summary", ln=True, align="C")
    pdf.ln(10)

    # Employee details
    pdf.set_font("Arial", style="", size=12)
    pdf.cell(0, 10, f"Employee Name: {employee_name}", ln=True)
    pdf.cell(0, 10, f"Salary: ${salary}", ln=True)
    pdf.cell(0, 10, f"Incentives: ${incentives}", ln=True)
    pdf.cell(0, 10, f"Discounts: ${discounts}", ln=True)
    pdf.ln(10)

    # Total payment
    total_payment = salary + incentives - discounts
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(0, 10, f"Total Payment: ${total_payment}", ln=True)
    pdf.ln(10)

    # Footer
    pdf.set_font("Arial", style="", size=10)
    pdf.cell(0, 10, "Thank you for your hard work!", ln=True, align="C")

    # Save the PDF to the specified output path
    pdf.output(output_path)

# Example usage:
employee_name = "John Doe"
salary = 3000
incentives = 500
discounts = 200
output_path = "payroll_summary.pdf"
generate_payroll_summary(employee_name, salary, incentives, discounts, output_path)
print("Payroll summary generated:", output_path)
