from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 50)
        self.cell(0, 10, "CS50 Shirtificate", align="C", ln=True)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def chapter_title(self, name):
        self.set_font("Arial", "B", 30)
        self.set_text_color(255, 255, 255)
        self.set_xy(0, 100)
        self.cell(0, 10, f"{name} took CS50", 0, 1, "C")

def create_shirtificate(name):
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=70, w=190, h=200)
    pdf.chapter_title(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    name = input("First and Last Name: ")
    create_shirtificate(name)
