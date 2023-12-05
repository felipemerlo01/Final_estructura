from Funciones_extra import imprimir_tabla, crear_csv, imprimir_distribucion_por_area, graficar_datos
from datetime import datetime
import os

class Proyectos:
    def __init__(self):
        self.dic_proyectos = {}
                
    def participacion_genero_promedio(self):
        informacion = []
        for proyecto in self.dic_proyectos.values():
            registro = proyecto.porcentaje_participacion_genero()
            if (registro is not None):
                informacion.append(registro)
            
        columnas = ["ID Proyecto", "Masculino (%)", "Femenino (%)", "Sin Datos (%)"]
        
        print('Información porcentual de proyectos por sexo: \n')
            
        imprimir_tabla(informacion, columnas, 10)
    
    def distribucion_por_area(self):
        cant_proyectos_area_subarea = {} # Cantidad de proyectos por area y subarea

        for proyecto in self.dic_proyectos.values():
            area_del_proyecto = proyecto.area
            subarea_del_proyecto = proyecto.subarea
            
            if area_del_proyecto not in cant_proyectos_area_subarea:
                cant_proyectos_area_subarea[area_del_proyecto] = {}
            
            if subarea_del_proyecto not in cant_proyectos_area_subarea[area_del_proyecto]:
                cant_proyectos_area_subarea[area_del_proyecto][subarea_del_proyecto] = 1
            else:
                cant_proyectos_area_subarea[area_del_proyecto][subarea_del_proyecto] += 1
        
        # Imprimimos la informacion
        imprimir_distribucion_por_area(cant_proyectos_area_subarea)
        
        # Graficamos 
        graficar_datos(cant_proyectos_area_subarea)
    
    # Guardar y visualizar una lista de proyectos ordenados por la fecha de inicialización.
    def proyectos_ordenados_por_fecha_inicio(self):
        # Ordenar el diccionario por la fecha de inicialización
        proyectos_ordenados = sorted(self.dic_proyectos.items(), key=lambda x: datetime.strptime(x[1].fecha_inicio, "%d/%m/%y"))
        # Convertir proyectos ordenados a formato de lista de filas
        filas = [(id_proyecto, proyecto.fecha_inicio) for id_proyecto, proyecto in proyectos_ordenados]
        columnas = ["ID", "Fecha de Inicio"]
        
        # Crea un archivo CSV
        nombre_file = 'ProyectosOrdenadosPorFechaInicio'
        if os.path.exists(nombre_file+'.csv'):
            print(f'El archivo {nombre_file} ya existe \n')
        else:
            crear_csv(nombre_file, filas, columnas)       

        # Imprimir usando la función existente
        print('Proyectos ordenados por fecha de inicio en orden ascendente: \n')
        imprimir_tabla(filas, columnas, 20)
        
    def porcentaje_tecnologias_emergentes(self):
        total_proyectos = len(self.dic_proyectos)
        proyectos_tecnologias_emergentes = 0
        if total_proyectos == 0:
            return 0  
        for proyecto in self.dic_proyectos.values():
            if proyecto.tipo_proyecto == "Tecnología e Innovación":
                proyectos_tecnologias_emergentes += 1
        porcentaje = round((proyectos_tecnologias_emergentes / total_proyectos) * 100, 2)
        
        print(f"Porcentaje de proyectos que utilizan tecnologias emergentes: {porcentaje}%")

    def tiempo_terminacion_segun_subarea(self):
        subareas = {}   #Key: subareas - Values: [suma, cantidad]
        
        # Agrego al diccionario la subarea si no esta, y su informacion de suma y cantidad correspondiente
        for proyecto in self.dic_proyectos.values():
            dias = proyecto.tiempo_de_terminacion()
            if (dias != None):
                if proyecto.subarea not in subareas:            
                    subareas[proyecto.subarea] = [dias,1]
                else:
                    subareas[proyecto.subarea][0] += dias
                    subareas[proyecto.subarea][1] += 1
        
        columnas = ['Subarea', 'Promedio de terminacion (dias)']
        informacion = []
        
        # Iteramos por subarea para calcular cada promedio
        for subarea, lista in subareas.items():
            promedio = round(lista[0]/lista[1], 2)
            fila = [subarea, promedio]
            informacion.append(fila)
        
        # Imprime/visualiza la tabla de promedios por subarea
        print('Promedio de tiempo de terminacion de proyectos por subarea en dias: \n')
        imprimir_tabla(informacion, columnas, 10)

    def monto_solicitado_otorgado(self):
        columnas = ['ID Proyecto', 'Monto solicitado', 'Monto otorgado', 'Indice de financiación (%)']
        informacion = []
        for id, proyecto in self.dic_proyectos.items():
            proporcion = proyecto.proporcion_monto()
            fila = (id, proyecto.monto_financiado_solicitado, proyecto.monto_financiado_adjudicado, proporcion)
            informacion.append(fila)
        
        imprimir_tabla(informacion, columnas, 10)
