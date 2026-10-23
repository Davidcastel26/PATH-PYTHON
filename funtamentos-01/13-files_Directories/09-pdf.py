from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Hola mundo en PDF", ln=True, align='C')
pdf.cell(200, 10, txt="linea dos estimados", ln=True, align='C')

pdf.output("file.dpf")