from fpdf import FPDF
from PIL import Image

def create_shirtificate(name):
    # --- PDF Setup ---
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    page_width = 210
    page_height = 297

    # --- Title at the top ---
    pdf.set_font("Arial", "B", 36)
    pdf.set_text_color(0, 0, 0)  # black text
    title = "CS50 Shirtificate"
    pdf.set_y(20)  # 20mm from top
    pdf.cell(0, 10, title, 0, 1, "C")  # centered horizontally

    # --- Shirt Image ---
    shirt_path = "shirtificate.png"
    img = Image.open(shirt_path)
    
    # Resize shirt to max 150mm width while keeping aspect ratio
    max_width = 150
    width, height = img.size
    ratio = max_width / width
    shirt_width = max_width
    shirt_height = height * ratio
    shirt_x = (page_width - shirt_width) / 2
    shirt_y = 80  # vertical position from top
    pdf.image(shirt_path, x=shirt_x, y=shirt_y, w=shirt_width, h=shirt_height)

    # --- User Name on Shirt ---
    pdf.set_font("Arial", "B", 30)
    pdf.set_text_color(255, 255, 255)  # white text

    user_text = name
    text_width = pdf.get_string_width(user_text)
    text_x = (page_width - text_width) / 2
    text_y = shirt_y + shirt_height / 2 - 10  # middle of shirt
    pdf.set_xy(text_x, text_y)
    pdf.cell(text_width, 10, user_text)

    # --- Subtext under Name ---
    subtext = "took CS50"
    pdf.set_font("Arial", "", 20)
    subtext_width = pdf.get_string_width(subtext)
    subtext_x = (page_width - subtext_width) / 2
    subtext_y = text_y + 15  # slightly below the name
    pdf.set_xy(subtext_x, subtext_y)
    pdf.cell(subtext_width, 10, subtext)

    # --- Save PDF ---
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    name = input("First and Last Name: ")
    create_shirtificate(name)
