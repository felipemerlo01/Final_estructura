import pandas as pd

def lector_proyectos(archivo):
    try:
        proyectos = pd.read_csv(archivo, delimiter=';', encoding='utf-8')
        
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no se encontró.")
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {archivo} está vacío o no contiene datos.")
    except pd.errors.ParserError:
        print(f"Error: Hubo un problema al analizar el archivo {archivo}. Asegúrate de que esté en formato CSV válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    return proyectos


# habría q hacer lista o tupla o dic para guardar los objetos de los proyectos(?)



""" def leer_Proyectos(path, Hotel):
    proyectos = pd.read_csv(path)
    
    for _, row in habitaciones.iterrows():
        nueva_habitacion = Habitacion(int(row["Numero"]), int(row["Precio por noche"]), int(row["Capacidad"]), row["Tipo"], row["Banio privado"], row["Balcon"])
        Hotel.habitaciones[nueva_habitacion.numero] = nueva_habitacion """