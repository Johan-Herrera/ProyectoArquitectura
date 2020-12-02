#!/usr/bin/python
from jinja2 import Template
import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb
datos=cgi.FieldStorage()

print('Content-Type: text/html')
print('')
try:
  idc=None  #Se le asigna None a la variable que guaradara la Identificacion del cliente
  datos=cgi.FieldStorage()  #Se extraen los datos que se encontraron en el formulario del HTML
  cnx = mysql.connector.connect(user='johan', password = 'johan0123', database='ejemplo', host='127.0.0.1')  #Se hace conexion con la base de datos
  cursor=cnx.cursor()  #Se crea el objeto que mandara los datos a la base de datos
  id = datos.getvalue('id1') 
  clave = datos.getvalue('clave1')
  comillas = "'"
  cursor.execute( "select * from cliente where ID_Cliente="+id+" and clave="+comillas+clave+comillas)  #Se hace la busqueda con codigo SQL en la base de datos
  for ID_Cliente in cursor.fetchall() :    #Se extraen los datos resultantes de l busqueda hecha por la base de datos y se comparan con el ID que halla ingresado el cliente
    idc=ID_Cliente
  if(idc!=None):  #Se hace el render de una pagina con los datos de la ID buscada 
         with open('vistas/interfazCliente.html' ,'r') as f:
                 doc = f.read()
                 template = Template(doc)
                 page = template.render(nombre="Juan", ID_Cliente=19)
                 print(page)
  else:
         print("Has ingresado una Identificacion Inexistente")
  cnx.close()  #Se finaliza la conexion con la base de datos
except mysql.connector.Error as err:  #Se hace el manejo de errores basico
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cnx.close()

