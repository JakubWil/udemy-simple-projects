from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
df = pd.read_csv('data.csv')


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(100,100,100)
    pdf.cell(0, 12, txt=row['Topic'], ln=1, align='L')
    pdf.line(10, 20, 200, 20)

    
  


pdf.output('output.pdf')




