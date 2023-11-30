from datetime import datetime

class Proyecto:
    def __init__(self, proyecto_id, titulo ,fecha_inicio, fecha_finalizacion, monto_financiado_solicitado, monto_financiado_adjudicado, cantidad_miembros_F, cantidad_miembros_M, cantidad_miembros_SD, area, subarea, tipo_proyecto):
        self.proyecto_id = proyecto_id
        self.titulo = titulo
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.monto_financiado_solicitado = monto_financiado_solicitado
        self.monto_financiado_adjudicado = monto_financiado_adjudicado
        self.cantidad_miembros_F = cantidad_miembros_F
        self.cantidad_miembros_M = cantidad_miembros_M
        self.cantidad_miembros_SD = cantidad_miembros_SD
        self.area = area
        self.subarea = subarea
        self.tipo_proyecto = tipo_proyecto
    
    # Visualizar la relación entre el monto de financiamiento solicitado y el monto de financiamiento
    def relacion_monto_financiamiento(self):
        pass

    # Porcentaje de participacion del proyecto por sexo
    def porcentaje_participacion_genero(self):
        if ('SIN DATOS' not in (self.cantidad_miembros_F, self.cantidad_miembros_M, self.cantidad_miembros_SD)):
            total_miembros = int(self.cantidad_miembros_F) + int(self.cantidad_miembros_M) + int(self.cantidad_miembros_SD)
            
            femenino = round((int(self.cantidad_miembros_F)/total_miembros)*100,3)
            masculino = round((int(self.cantidad_miembros_M)/total_miembros)*100,3)
            sin_datos = round((int(self.cantidad_miembros_SD)/total_miembros)*100,3)
            
            resultado = [self.proyecto_id, masculino, femenino, sin_datos]
            return resultado
        else:
            return 
        
    # Calcular tiempo de terminacion: fecha_fin - fecha_inicio
    def tiempo_de_terminacion(self):
        if (isinstance(self.fecha_finalizacion, str)):
            fecha_inicio = datetime.strptime(self.fecha_inicio, "%d/%m/%y")
            fecha_finalizacion = datetime.strptime(self.fecha_finalizacion, '%d/%m/%y')
            tiempo = (fecha_finalizacion - fecha_inicio).days
            return tiempo
        return     # Retorna vacio si se trata de un proyecto sin fecha de finalizacion
        # 

    


    

    