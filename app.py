from flask import Flask, render_template, request, redirect, session, send_file
from utils.pdf_generator import gerar_pdf
from datetime import datetime

app = Flask(__name__)
app.secret_key = "boletim_rp_secret"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["nome"] = request.form["nome"]
        session["id"] = request.form["id"]
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "nome" not in session:
        return redirect("/")
    return render_template("dashboard.html", nome=session["nome"])

@app.route("/boletim", methods=["GET", "POST"])
def boletim():
    if "nome" not in session:
        return redirect("/")
    if request.method == "POST":
        dados = request.form.to_dict()
        dados["nome"] = session["nome"]
        dados["id"] = session["id"]
        dados["data"] = datetime.now().strftime("%d/%m/%Y %H:%M")
        pdf_path = gerar_pdf(dados)
        return send_file(pdf_path, as_attachment=True)
    return render_template("boletim.html")

if __name__ == "__main__":
    app.run(debug=True)
