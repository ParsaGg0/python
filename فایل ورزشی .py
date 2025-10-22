from fpdf import FPDF

# Create a simplified Persian PDF using English-compatible fonts (without reshaping)
class SimplePersianPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "برنامه تمرینی بدنسازی - مخصوص آقا", 0, 1, "C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

# Initialize PDF
pdf = SimplePersianPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Workout plan (Persian text, without reshaping)
workout_texts = [
    "شنبه: اسکوات هالتر – ۳ ست × ۸-۱۰ تکرار (عضلات چهارسر و کمر)؛ پرس سینه هالتر – ۳×۱۰ (سینه/سرشانه)؛ زیر بغل هالتر خم – ۳×۱۰ (پشت)؛ کرانچ شکم – ۳×۱۲-۱۵.",
    "دوشنبه: ددلیفت – ۳×۸-۱۰ (پشت و ران)؛ پرس سرشانه – ۳×۸-۱۰ (سرشانه)؛ بارفیکس یا لت‌پول‌داون – ۳×۶-۱۰ (پشت و بازو)؛ پلانک – ۳ ست از ۳۰-۶۰ ثانیه.",
    "پنج‌شنبه: لانگز یا اسکوات جلو – ۳×۱۰-۱۲ (پایین‌تنه)؛ دیپ (پاراالل) یا پرس سینه دمبل – ۳×۱۰؛ زیر بغل دمبل خم – ۳×۱۰؛ پلانک پهلو – ۲-۳ ست × ۲۰ ثانیه برای هر سمت.",
    "وزنه‌ها طوری انتخاب شوند که ۸ تا ۱۲ تکرار قابل انجام باشد. بین ست‌ها حدود ۱-۲ دقیقه استراحت کنید."
]

# Add text to PDF
for line in workout_texts:
    pdf.multi_cell(0, 10, line)

# Save PDF
pdf_path = "/mnt/data/برنامه_تمرینی_هفتگی.pdf"
pdf.output(pdf_path)

pdf_path
