from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('data.csv')


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(100,100,100)
    pdf.cell(0, 12, txt=row['Topic'], ln=1, align='L')
    pdf.line(10, 20, 200, 20)

    for line in range(20,280, 10):
       
         pdf.line(10, line, 200, line)

    
    pdf.ln(265)
    

    #Set footer for main page
    pdf.set_font('Times', 'I', 8)
    pdf.set_text_color(180,180,180)
    pdf.cell(0, 10, txt=row['Topic'], ln=1, align='R')


    for n in range(int(row['Pages']) - 1):
        


        pdf.add_page()
        pdf.ln(277)

        for line in range(20,280, 10):
           
            pdf.line(10, line, 200, line)
        

         #Set footer for other pages
        pdf.set_font('Times', 'I', 8)
        pdf.set_text_color(180,180,180)
        pdf.cell(0, 10, txt=row['Topic'], ln=1, align='R')
       


  


pdf.output('output.pdf')




