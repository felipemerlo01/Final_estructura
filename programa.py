# Importaciones
from Funciones_extra import obtener_path, lector_proyectos, menu_principal, validar_opcion_menu, validar_proyecto_existente
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
            pass
        elif (opcion =='2'):
            PROYECTOS.participacion_genero_promedio()
        elif (opcion == '3'):
            pass
        elif (opcion == '4'):
            porcentaje_tecnologias_emergentes = PROYECTOS.porcentaje_tecnologias_emergentes()
            print(f"Porcentaje de proyectos de que utilizan tecnologias emergentes: {porcentaje_tecnologias_emergentes}%")
        elif (opcion == '5'):
            PROYECTOS.proyectos_ordenados_por_fecha_inicio()
        elif (opcion == '6'):
            pass
        else:
            continuar = False

