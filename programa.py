# Importaciones
from Funciones_extra import obtener_path, lector_proyectos, menu_principal, validar_opcion_menu
from Clases.Proyectos import Proyectos

#que te copie el path 
path = obtener_path()

# Menu
if (path):
    continuar = True
    cargado = False

    while (continuar):
        if (not cargado):
            PROYECTOS = Proyectos()
            lector_proyectos(path, PROYECTOS)
            cargado = True
        
        menu_principal()
        opcion = validar_opcion_menu(input('Ingrese una opción: '), 7)
        if (opcion == '1'):
            PROYECTOS.distribucion_por_area()
        elif (opcion =='2'):
            PROYECTOS.participacion_genero_promedio()
        elif (opcion == '3'):
            PROYECTOS.tiempo_terminacion_segun_subarea()
        elif (opcion == '4'):
            PROYECTOS.porcentaje_tecnologias_emergentes()
        elif (opcion == '5'):
            PROYECTOS.proyectos_ordenados_por_fecha_inicio()
        elif (opcion == '6'):
            PROYECTOS.monto_solicitado_otorgado()
        else:
            continuar = False

