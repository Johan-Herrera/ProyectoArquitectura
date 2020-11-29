#!/usr/bin/python
from jinja2 import Template
import mysql.connector
from mysql.connector import errorcode
import cgi, cgitb
datos=cgi.FieldStorage()

#Se inicia el html
print('Content-Type: text/html')
print('')
#Se implementa un try que ejecutara la busqueda y en caso que no se pueda imprimira un error
try:
<<<<<<< HEAD
  idc=None
  datos=cgi.FieldStorage()
  cnx = mysql.connector.connect(user='johan', password = 'johan0123', database='ejemplo', host='127.0.0.1')
  cursor=cnx.cursor()
  id = datos.getvalue('ID_Mascota')
  cursor.execute( "SELECT * FROM mascota WHERE ID_Mascota="+id)
=======
  datos=cgi.FieldStorage()  #Se guarda el dato proveniente del textfield del html en esta variable
  cnx = mysql.connector.connect(user='johan', password = 'johan0123', database='ejemplo', host='127.0.0.1')   #Se hace la conexion con el servidor
  cursor=cnx.cursor() #Se crea el objeto que tiene interaccion con la BD
  id = datos.getvalue('ID_Mascota')   #Se le da el valor del textfield a esta variable
  cursor.execute( "SELECT * FROM mascota WHERE ID_Mascota="+id)  #Se define el query que se ejecutara en la BD
  #Se asignaran los valores de la busqueda a las siguientes variables
>>>>>>> 88e4c7e64f11df68f9fe033e13cf0fb02c6044cd
  for ID_Mascota, ID_Cliente, Nombre_Mascota, Edad_Mascota, Raza_Mascota, Patologia_Mascota,Vacuna_Hecha, Fecha_Vacuna in cursor.fetchall() :
    idm= ID_Mascota
    idc= ID_Cliente
    nombre= Nombre_Mascota
    edad= Edad_Mascota
    raza= Raza_Mascota
    pato= Patologia_Mascota
    vh= Vacuna_Hecha
    fv= Fecha_Vacuna
  if(idc!=None):
    #Se implementa el render que mostrara los resultados de la consulta
 	 with open('vistas/minde.html' ,'r') as f:
       		 doc = f.read()
       		 template = Template(doc)
       		 page = template.render(ID_Mascota=idm, ID_Cliente=idc, Nombre_Mascota=nombre, Edad_Mascota=edad, Raza_Mascota=raza, Patologia_Mascota=pato,Vacuna_Hecha=vh, Fecha_Vacuna=fv)
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
    print("Ingreso una Identificacion Invalida")
else:
    cnx.close()

