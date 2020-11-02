#!/usr/bin/python3
from jinja2 import Template
import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb
datos=cgi.FieldStorage()
#Se inicializa el html que se mostrara
print('Content-Type: text/html')
print('')

#Se implementa un try que ejecutara el registro de un veterinario/cliente
try:
  datos=cgi.FieldStorage() #Se extraen los valores de los textfields del html en esta variable
  cnx = mysql.connector.connect(user='johan', password = 'johan0123', database='ejemplo', host='127.0.0.1') #Se hace la conexion con la base de datos
  cursor=cnx.cursor() #Se crea la variable que se comunica con la BD
  #Se asignan los valores de los textfield a cada una de las siguientes variable
  id = datos.getvalue('id')
  nombre = datos.getvalue('nombre')
  apellido = datos.getvalue('apellido')
  email = datos.getvalue('email')
  tel = datos.getvalue('tel')
  clave = datos.getvalue('clave')
  #Se define el comando de insercion en la BD
  add_user = ("INSERT INTO cliente (ID_Cliente, Nombre_Cliente, Apellido_Cliente, Email_Cliente, Telefono_Cliente, clave) VALUES (%s,%s,%s,%s,%s,%s)")
  data_user = (id,nombre,apellido,email,tel,clave)
  #Se ejecuta el comando de insercion en la BD
  cursor.execute(add_user, data_user)
  cnx.commit()
  with open('vistas/consulta.html' ,'r') as f:
        doc = f.read()
        template = Template(doc)
        page = template.render(nombre="Juan", ID_Cliente=19)
        print(page)
  cnx.close()    #Se cierra la conxion con la BD
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cnx.close()



