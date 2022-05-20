from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
cnn = mysql.connector.connect(host="localhost", user="root",
passwd="72781951",database="pagina")


@app.route("/") 
def inicio():
  return render_template("inicio.html")

@app.route("/register", methods=["POST","GET"]) 
def register():
  email=request.form.get("email")
  contrasena=request.form.get("contrasena")
  contrasena2=request.form.get("contrasena2")

  if contrasena == contrasena2:
    cur = cnn.cursor()
    sql = "INSERT INTO usuarios (Username, Password) VALUE('{}','{}') ".format(email,contrasena)
    cur.execute(sql)
    cnn.commit()
    cur.close()
    if request.method == "POST":
      return redirect(url_for('login')) 
    else:
      return render_template("Register.html")
  return render_template("Register.html")

@app.route('/login', methods=['POST','GET'])
def login():
  email=request.args.get("email")
  contrasena=request.form.get("contrasena")
  
  if request.method == "GET":
    cur = cnn.cursor()
    sql = "SELECT Password FROM usuarios WHERE Username = '{}'" .format(email)
    print(email)
    cur.execute(sql)
    datos = cur.fetchall()
    for d in datos:
      print(d)
    cur.close()
    cnn.commit()  
  return render_template("Login.html")


@app.route("/productos") 
def productos():
  return render_template("productos.html")


@app.route("/cart") 
def cart():
  return render_template("Cart.html")
  
@app.route("/register_product", methods=['POST','GET']) 
def register_product():
  namepro=request.form.get("namepro")
  precio=request.form.get("precio")
  nombreimg=request.form.get("nombreimg")
  Def=request.form.get("Def")
  curs = cnn.cursor()
  sql = "INSERT INTO productos (Nombre,Precio,Url,Descrip) VALUE('{}','{}','{}','{}') ".format(namepro,precio,nombreimg,Def)
  curs.execute(sql)
  cnn.commit()
  curs.close()
  if request.method == "POST":
    return redirect(url_for('productos')) 
  else:
    return render_template("Register_Pro.html")

@app.route("/redes") 
def redes():
  return render_template("redes.html")
  

@app.route("/pago") 
def pago():
  return render_template("pago.html")

if __name__ == '__main__':
    app.run(debug=True  )