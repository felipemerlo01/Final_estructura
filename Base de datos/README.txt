Se unificaron los archivos:
proyectos_2015, proyectos_2016, proyectos_2017, proyectos_2018

Asi como sus referencias (relevantes al análisis):
ref_disciplina, ref_estado_projecto, ref_tipo_proyecto, proyecto_disciplina

Y solo se mantuvieron las columnas necesarias.

ACLARACIONES sobre depuración de la base de datos:
    - Al hacer BUSCARV habia proyecto_id que no existian en el archivo proyecto_disciplina --> se le puso que su id_disciplina es -1 (que quiere decir SIN DATOS en ref_disciplina)
		- Aquellos que devuelven id_diciplina = 0 también se los reemplaza por -1 ya que no existe tal disciplina
						
    - Al hacer BUSCARV para obtener "tipo_proyecto_cyt_desc" de ref_tipo_proyecto, hay celdas vacias en "tipo_proyecto_id" en db_Proyectos por lo tanto en vez de tirar error reemplazzamos con "SIN DATOS"		
                                                      
    - Como existian disrectores con sexo "S/D" que no conformaban parte ni de cantidad_miembros_M ni cantidad_miembros_F, se recalcularon tanto cantidad_miembros_M y cantidad_miembros_F para incluir al director, asi como una columna de  cantidad_miembros_S/D ya que esos participantes sin informacion siguen formando parte del calculo de la proporcion de participantes por sexo.														
															