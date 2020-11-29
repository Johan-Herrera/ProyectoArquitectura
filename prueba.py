<div id="inicio">
<input type="button" class="btn btn-primary" value="Registrar Mascota" id="btn_registrar" name="btn_registrar">
<input type="button" value="Consultar Informacion De Una Mascota" class="btn btn-primary" id="btn_consultar">
<input type="button" value="Modificar Informacion De Una Mascota" class="btn btn-primary" id="btn_modificar">
</div>

<div id="consulta" style="display: none;">
<form action="controladorConsulta.py" method="GET">
Identificacion de la mascota
<p><input type="text" name="ID_Mascota" id="ID_Mascota"/>
<input type="submit" value="Buscar" id="buscar">
</form>
</div>


<div id="registro" style="display: none;">
<form action="cgi-bin/registroMascota.py" method="GET">
<p>Ingrese la Identificacion de la mascota:
<input type="text" name="id_mascota" id="id_mascota"/> </p>
<p>Ingrese la Identificacion del dueño:
<input type="text" name="id" id="id"/> </p>
<p>Ingrese el Nombre de la mascota:
<input type="text" name="nombre" id="nombre"/></p>
<p>Ingrese la edad de la mascota:
<input type="text" name="edad" id="edad"/></p>
<p>Ingrese la raza de la mascota:
<input type="text" name="raza" id="raza"/></p>
<p>Ingrese las patologias de la mascota(si presenta alguna):
<input type="text" name="patologia" id="patologia"/></p>
<p>Ingrese la ultima fecha de vacunacion de la mascota(dd-mm-aaaa):
<input type="text" name="fechaH" id="fechaH"/></p>
<p>Ingrese la proxima fecha de vacunacion de la mascota(dd-mm-aaaa):
<input type="text" name="fechaP" id="fechaP"/></p>
<p></p>
<input type="submit" value="enviar" onclick="f()" />
</form>
</div>


<div id="actualizarMascota" style="display: none;">
<form action="cgi-bin/actualizarMascota.py" method="GET">
<p>Ingrese la Identificacion de la mascota:
<input type="text" name="id_mascota1" id="id_mascota1"/> </p>
<p>Ingrese la Identificacion del dueño:
<input type="text" name="id1" id="id1"/> </p>
<p>Ingrese el Nombre de la mascota:
<input type="text" name="nombre1" id="nombre1"/></p>
<p>Ingrese la edad de la mascota:
<input type="text" name="edad1" id="edad1"/></p>
<p>Ingrese la raza de la mascota:
<input type="text" name="raza1" id="raza1"/></p>
<p>Ingrese las patologias de la mascota(si presenta alguna):
<input type="text" name="patologia1" id="patologia1"/></p>
<p>Ingrese la ultima fecha de vacunacion de la mascota(dd-mm-aaaa):
<input type="text" name="fechaH1" id="fechaH1"/></p>
<p>Ingrese la proxima fecha de vacunacion de la mascota(dd-mm-aaaa):
<input type="text" name="fechaP1" id="fechaP1"/></p>
<p></p>
<input type="submit" value="enviar" onclick="h()" />
</form>
</div>


<script>
$( "#btn_registrar" ).click(function() {
  $("#inicio").hide(0);
  $("#registro").show(0);
});
$( "#btn_consultar" ).click(function() {
  $("#inicio").hide(0);
  $("#consulta").show(0);
});
$( "#btn_modificar" ).click(function() {
  $("#inicio").hide(0);
  $("#actualizarMascota").show(0);
});
</scrip>

