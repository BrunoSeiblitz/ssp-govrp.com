from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from datetime import datetime

LOGOS = {
    "PM": "static/logos/pm.png",
    "PC": "static/logos/pc.png",
    "BOMBEIROS": "static/logos/bombeiros.png",
    "PRF": "static/logos/prf.png",
    "PF": "static/logos/pf.png"
}

def gerar_pdf(d):
    os.makedirs("temp", exist_ok=True)
    nome_arquivo = f"temp/boletim_{datetime.now().timestamp()}.pdf"
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    logo = LOGOS.get(d["corporacao"])
    if logo and os.path.exists(logo):
        c.drawImage(logo, 50, altura - 130, width=80, height=80, preserveAspectRatio=True)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(150, altura - 60, "BOLETIM DE OCORRÊNCIA")
    c.drawString(150, altura - 80, d["corporacao"])

    c.setFont("Helvetica", 10)
    y = altura - 160

    campos = [
        ("Agente", d["nome"]),
        ("ID In-Game", d["id"]),
        ("Unidade", d["unidade"]),
        ("Tipo de Ocorrência", d["tipo"]),
        ("Local", d["local"]),
        ("Descrição", d["descricao"]),
        ("Data/Hora", d["data"])
    ]

    for titulo, valor in campos:
        c.drawString(50, y, f"{titulo}:")
        c.drawString(180, y, str(valor))
        y -= 20

    c.setFont("Helvetica-Oblique", 8)
    c.drawString(50, 40, "Documento fictício – Uso exclusivo para Roleplay (FiveM)")
    c.save()
    return nome_arquivo
