from fpdf import FPDF

def generate_bo_pdf(transcribed_text: str) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, transcribed_text)
    
    pdf_path = "boletim_ocorrencia.pdf"
    pdf.output(pdf_path)
    
    return pdf_path
