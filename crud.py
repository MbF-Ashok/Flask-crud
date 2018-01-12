from flask import Flask,render_template,request,redirect
from flask import jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/first/<string:par>")
def first(par):
	return "Test "+par

@app.route("/")
def form():
	return render_template("form.html")

@app.route("/editaction",methods=["GET","POST","PUT"])
def editaction():
	if request.method == "POST":
		cnx = mysql.connector.connect(user='root',password='R@shok123',database='flask_crud')
		cursor = cnx.cursor(buffered = True)
		update = ("UPDATE fruits_table SET fruit = %(new_name)s WHERE id=%(id)s")
		cursor.execute(update,{"new_name" : request.form['fruit'],"id" : request.form['id']})
		cnx.commit()
		cnx.close()
		return redirect("/list")
@app.route("/addaction",methods=["GET","POST"])
def addaction():
	if request.method == "POST":
		cnx = mysql.connector.connect(user='root',password='R@shok123',database='flask_crud')
		cursor = cnx.cursor(buffered = True)
		insert = ("INSERT INTO fruits_table (fruit) VALUES (%s)")
		cursor.execute(insert,(request.form['username'],))
		cnx.commit()
		cnx.close()
		return redirect("/list")
@app.route("/list")
def list():
	cnx = mysql.connector.connect(user='root',password='R@shok123',database='flask_crud')
	cursor = cnx.cursor(buffered = True)
	select = ("SELECT * FROM fruits_table")
	cursor.execute(select)
	data = cursor.fetchall()
	cnx.commit()
	cnx.close()
	# return jsonify({'data':data})
	return render_template("list.html",data=data)

@app.route("/delete/<id>")
def delete(id):
	cnx = mysql.connector.connect(user='root',password='R@shok123',database='flask_crud')
	cursor = cnx.cursor(buffered = True)
	delete = ("DELETE FROM fruits_table WHERE id=%(id_num)s")
	cursor.execute(delete,{'id_num':id},)
	cnx.commit()
	cnx.close()
	return redirect("/list")

@app.route("/edit/<id>")
def edit(id):
	cnx = mysql.connector.connect(user='root',password='R@shok123',database='flask_crud')
	cursor = cnx.cursor(buffered = True)
	select = ("SELECT * FROM fruits_table WHERE id =%(id_num)s")
	cursor.execute(select,{'id_num':id},)
	name = cursor.fetchall()
	cnx.commit()
	cnx.close()
	return render_template("editform.html",name=name)
@app.route('/processjson',methods=['POST'])
def processjson():
	return jsonify({'result':'success'})	

if __name__ == "__main__":
	app.run(debug=True,port=8000)


