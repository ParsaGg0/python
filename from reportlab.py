from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# Register a Unicode font
pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))

# Create PDF
file_path = '/mnt/data/network_roles_resume.pdf'
c = canvas.Canvas(file_path, pagesize=A4)
width, height = A4

# Set title
c.setFont('DejaVu', 16)
c.drawCentredString(width/2, height - 30, "مهارت‌ها و موضوعات تخصصی شبکه")

# Define sections and items
sections = {
    "🔹 حوزه‌ معماری و طراحی شبکه": [
        "طراحی و استقرار معماری شبکه نرم‌افزارمحور (SDN) با Python و OpenDaylight",
        "تحلیل و پیاده‌سازی توپولوژی‌های محاسبات لبه (Edge Computing) در شبکه‌های IoT",
        "ساخت شبکه مبتنی بر میکروسرویس با Kubernetes و CNI Plugins"
    ],
    "🔹 حوزه‌ اتوماسیون و اسکریپت‌نویسی": [
        "اتوماسیون کانفیگ زیرساخت شبکه با Ansible + Python",
        "توسعه اسکریپت‌های هوشمند SNMP Polling و NetFlow Collection برای مانیتورینگ بلادرنگ",
        "یکپارچه‌سازی APIهای کنترلر شبکه (REST/SOAP) جهت به‌روز‌رسانی خودکار قوانین فایروال"
    ],
    "🔹 حوزه‌ بهره‌وری و بهینه‌سازی": [
        "بهینه‌سازی عملکرد مسیریابی (Routing) با اسکریپت‌های پایتون و BGP Community",
        "تحلیل ترافیک و شناسایی گلوگاه‌های شبکه با ELK Stack و Python",
        "پیاده‌سازی QoS پیشرفته و اولویت‌بندی ترافیک حساس (Voice, Video) در سوئیچ‌های Cisco"
    ],
    "🔹 حوزه‌ امنیت شبکه": [
        "راه‌اندازی محیط Honeypot و کشف تهدیدات پیشرفته با Scapy",
        "اتوماسیون فرایند واکنش به رخداد (Incident Response) با Python & Splunk",
        "پیاده‌سازی سیاست‌های Zero Trust Network برای محیط‌های Hybrid Cloud"
    ],
    "🔹 حوزه‌ Cloud & Virtualization": [
        "طراحی شبکه مجازی (VPC/VNet) امن در AWS و Azure",
        "یکپارچه‌سازی شبکه لایه ۳ با Calico و Cilium در کلاستر‌های Kubernetes",
        "راه‌اندازی و خودکارسازی VPN Site-to-Site و Remote Access با Terraform"
    ]
}

# Starting position
y = height - 50
c.setFont('DejaVu', 12)

for section, items in sections.items():
    c.drawString(20 * mm, y, section)
    y -= 8 * mm
    for item in items:
        c.drawString(30 * mm, y, f"• {item}")
        y -= 6 * mm
        if y < 40 * mm:
            c.showPage()
            y = height - 30
            c.setFont('DejaVu', 12)
    y -= 4 * mm

c.save()
file_path
