import pandas as pd
import os
import csv
from Clases.Proyecto import Proyecto

# Obtiene el path relevante de base de datos
def obtener_path():
    try:
        path_programa = os.path.abspath(__file__)
        directorio_actual = os.path.dirname(path_programa)
        path = os.path.join(directorio_actual, 'Base de datos', 'db_Proyectos.csv')
        path = os.path.abspath(path)

        return path
    except Exception as e:
        print(f'Se presentó el error {e} al intentar buscar el directorio')
        return

def lector_proyectos(path, PROYECTOS):
    try:
        proyectos = pd.read_csv(path, delimiter=';', encoding='utf-8')
        for _, row in proyectos.iterrows():
            nuevo_proyecto = Proyecto(
                int(row["proyecto_id"]),
                row["titulo"],
                row["fecha_inicio"],
                row["fecha_finalizacion"],
                int(row["monto_financiado_solicitado"]),
                int(row["monto_financiado_adjudicado"]),
                row["cantidad_miembros_F"],
                row["cantidad_miembros_M"],
                row["cantidad_miembros_S/D"],
                row["area"],
                row["subarea"],
                row["tipo_proyecto"])
            PROYECTOS.dic_proyectos[nuevo_proyecto.proyecto_id] = nuevo_proyecto        
    except FileNotFoundError:
        print(f"Error: El archivo {path} no se encontró.")
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {path} está vacío o no contiene datos.")
    except pd.errors.ParserError:
        print(f"Error: Hubo un problema al analizar el archivo {path}. Asegúrate de que esté en formato CSV válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def menu_principal():
    print('''
¿Que desea visualizar?
1. Distribución de los proyectos por área de investigación
2. Porcentaje de participación de las mujeres en los diferentes proyectos
3. Tiempo promedio de terminación de los proyectos según el sub área
4. Porcentaje de proyectos que han utilizado tecnologías emergentes
5. Proyectos ordenados por la fecha de inicialización
6. Relación entre el monto de financiamiento solicitado y el monto de financiamiento otorgado
7. Salir
''')

def validar_opcion_menu(opcion, cantidad_opciones):
    while (True):
        try:
            while (not (1 <= int(opcion) <= cantidad_opciones)):
                opcion = input('Opcion invalida. Ingrese una de las opciones del menú: ')
            print()
            return opcion
        except ValueError:
            opcion = input('Opcion invalida. Ingrese una de las opciones del menú: ')

def validar_proyecto_int(id_proyecto):
    while (True):
        try:
            id_proyecto = int(id_proyecto) 
            return id_proyecto
        except ValueError:
            id_proyecto = input('Ingrese un ID de proyecto válido (número entero): ')

def validar_proyecto_existente(id_proyecto, dic_proyectos):
    while (True):
        if id_proyecto in dic_proyectos:
            proyecto_elegido = dic_proyectos[id_proyecto]
            return proyecto_elegido
        else:
            print(f"No se encontró un proyecto con ID {id_proyecto}.")
            return
        
def imprimir_tabla(filas, columnas, cantidad_por_pag):
    # Encontrar el ancho maximo de las columnas
    ancho_col_max = [max(len(str(item)) for item in column) for column in zip(columnas, *filas)]
    
    # Imprimir columnas
    formato_columnas = " ".join("{{:<{}}}".format(ancho) for ancho in ancho_col_max)
    print(formato_columnas.format(*columnas))

    # Imprimir filas
    for i, fila in enumerate(filas, start=1):
        print(formato_columnas.format(*fila))

        # Imprimir hoja de filas y preguntar si desea continuar
        if i % cantidad_por_pag == 0:
            continuar = input("\n¿Desea imprimir más filas? (Si/No): ").capitalize()
            if continuar != 'Si':
                break
            # Imprimir columnas
            print()
            print(formato_columnas.format(*columnas))

def crear_csv(nombre_file, filas, encabezados):
    try:
        with open(nombre_file+'.csv', 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            # Titulos
            writer.writerow(encabezados)
            # Filas
            writer.writerows(filas)
            print(f"Se ha creado el archivo {nombre_file} correctamente\n")
    except Exception as e:
        print(f'Ocurrió el siguiente error al crear el archivo CSV: {e}')