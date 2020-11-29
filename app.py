#!/usr/bin/python
from flask import Flask, request
from jinja2 import Template
import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb

# instantiate the app
app = Flask(__name__)

# sanity check route
@app.route('/productos',methods=['GET'])
def producto():
    return 'mostrando productos'

@app.route('/crearProductos',methods=['POST'])
def crearProducto():
    print('Content-Type: text/html')
    print('')

    ID_Mascota = request.form['id_mascota']
    ID_Cliente = request.form['id']
    Nombre_Mascota = request.form['nombre']
    Edad_Mascota = request.form['edad']
    Raza_Mascota = request.form['raza']
    Patologia_Mascota = request.form['patologia']
    Vacuna_Hecha = request.form['fechaH']
    Fecha_Vacuna = request.form['fechaP']
    try:
      datos=cgi.FieldStorage()
      cnx = mysql.connector.connect(user='johan', password = 'johan0123', database='ejemplo', host='127.0.0.1')
      cursor=cnx.cursor()
      add_user = ("INSERT INTO mascota (ID_Mascota, ID_Cliente, Nombre_Mascota, Edad_Mascota, Raza_Mascota, Patologia_Mascota, Vacuna_Hecha, Fecha_Vacuna) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
      data_user = (ID_Mascota,ID_Cliente,Nombre_Mascota,Edad_Mascota,Raza_Mascota,Patologia_Mascota,Vacuna_Hecha,Fecha_Vacuna)
      cursor.execute(add_user, data_user)
      cnx.commit()
      return("Se ha registrado exitosamente la mascota")
      cnx.close()
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        return(str(err))
    else:
        cnx.close()


@app.route('/modificarProductos',methods=['POST'])
def modificarProducto():
    print('Content-Type: text/html')
    print('')
    
    ID_Mascota = request.form['ID_Mascota']
    ID_Cliente = request.form['ID_Cliente']
    Nombre_Mascota = request.form['Nombre_Mascota']
    Edad_Mascota = request.form['Edad_Mascota']
    Raza_Mascota = request.form['Raza_Mascota']
    Patologia_Mascota = request.form['Patologia_Mascota']
    Vacuna_Hecha = request.form['Vacuna_Hecha']
    Fecha_Vacuna = request.form['Fecha_Vacuna']
    try:
      datos=cgi.FieldStorage()
      cnx = mysql.connector.connect(user='johan', password = 'johan0123', database='ejemplo', host='127.0.0.1')
      cursor=cnx.cursor()
      add_user = ("UPDATE mascota set ID_Cliente=%s, Nombre_Mascota=%s, Edad_Mascota=%s, Raza_Mascota=%s, Patologia_Mascota=%s, Vacuna_Hecha=%s, Fecha_Vacuna=%s WHERE ID_Mascota=%s")
      data_user = (ID_Cliente,Nombre_Mascota,Edad_Mascota,Raza_Mascota,Patologia_Mascota,Vacuna_Hecha,Fecha_Vacuna,ID_Mascota)
      cursor.execute(add_user, data_user)
      cnx.commit()
      return("Se ha actualizado exitosamente la informacion")
      cnx.close()
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        return(str(err))
    else:
        cnx.close()


@app.route('/eliminarProductos',methods=['DELETE'])
def eliminarProducto():
    return 'elim productos'


if __name__ == '__main__':
    app.run(host='0.0.0.0')


