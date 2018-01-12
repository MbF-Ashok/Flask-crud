from flask import Flask,render_template,request,redirect
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
app = Flask(__name__)
@app.route("/")
pdf_ = canvas.Canvas('ex.pdf')
# c.drawImage('ar.jpg', 0, 0, 10*cm, 10*cm)
c.showPage()
c.save()
if __name__ == "__main__":
	app.run(debug=True)
