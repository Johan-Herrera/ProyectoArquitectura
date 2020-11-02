#!/usr/bin/python3
from jinja2 import Template
import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb
datos=cgi.FieldStorage()

print('Content-Type: text/html')
print('')


try:
  datos=cgi.FieldStorage()
  cnx = mysql.connector.connect(user='johan', password = 'johan0123', database='ejemplo', host='127.0.0.1')
  cursor=cnx.cursor()
  id = datos.getvalue('id')
  nombre = datos.getvalue('nombre')
  apellido = datos.getvalue('apellido')
  email = datos.getvalue('email')
  tel = datos.getvalue('tel')
  clave = datos.getvalue('clave')
  add_user = ("INSERT INTO cliente (ID_Cliente, Nombre_Cliente, Apellido_Cliente, Email_Cliente, Telefono_Cliente, clave) VALUES (%s,%s,%s,%s,%s,%s)")
  data_user = (id,nombre,apellido,email,tel,clave)
  cursor.execute(add_user, data_user)
  cnx.commit()
  with open('vistas/consulta.html' ,'r') as f:
        doc = f.read()
        template = Template(doc)
        page = template.render(nombre="Juan", ID_Cliente=19)
        print(page)
  cnx.close()
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cnx.close()



