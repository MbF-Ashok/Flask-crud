from flask import Flask, render_template, redirect, url_for
import pdfkit

app = Flask(__name__)
@app.route('/')
def pdf_template():
	# pdfkit.from_file('/home/user/Flask-crud/template.html', 'out.pdf')
	body = """
    <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
      </head>
      Hello World!
      </html>
    """
	value = pdfkit.from_string(body, 'out.pdf')
	return value

if __name__ == '__main__':
	app.run(debug=True,port=8081)
