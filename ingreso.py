#!/usr/bin/python
from jinja2 import Template
import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb
datos=cgi.FieldStorage()

print('Content-Type: text/html')
print('')
try:
  idc=None
  datos=cgi.FieldStorage()
  cnx = mysql.connector.connect(user='johan', password = 'johan0123', database='ejemplo', host='127.0.0.1')
  cursor=cnx.cursor()
  id = datos.getvalue('id1')
  clave = datos.getvalue('clave1')
  comillas = "'"
  cursor.execute( "select * from cliente where ID_Cliente="+id+" and clave="+comillas+clave+comillas)
  for ID_Cliente in cursor.fetchall() :
    idc=ID_Cliente
  if(idc!=None):
         with open('vistas/interfazCliente.html' ,'r') as f:
                 doc = f.read()
                 template = Template(doc)
                 page = template.render(nombre="Juan", ID_Cliente=19)
                 print(page)
  else:
         print("Has ingresado una Identificacion Inexistente")
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

