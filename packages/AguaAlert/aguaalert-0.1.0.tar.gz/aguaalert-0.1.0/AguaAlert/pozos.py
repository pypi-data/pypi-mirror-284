import pandas as pd

def registrar_ubicacion(nombre, coordenadas, niveles):
    """
    Registra una nueva ubicación y sus niveles de agua.

    :param nombre: str - Nombre de la ubicación.
    :param coordenadas: str - Coordenadas de la ubicación (latitud, longitud).
    :param niveles: list - Lista de niveles históricos de agua (3 valores).
    :return: str - Mensaje de éxito.
    """
    new_data = pd.DataFrame([[nombre, coordenadas] + niveles], columns=["nombre", "coordenadas", "nivel1", "nivel2", "nivel3"])
    new_data.to_csv('data/ubicaciones.csv', mode='a', header=False, index=False)
    return f"Ubicación '{nombre}' registrada exitosamente."

def registrar_precipitacion(nombre, precipitaciones):
    """
    Registra datos históricos de precipitación para una ubicación.

    :param nombre: str - Nombre de la ubicación.
    :param precipitaciones: list - Lista de datos históricos de precipitación (3 valores).
    :return: str - Mensaje de éxito.
    """
    new_data = pd.DataFrame([[nombre] + precipitaciones], columns=["nombre", "precip1", "precip2", "precip3"])
    new_data.to_csv('data/precipitacion.csv', mode='a', header=False, index=False)
    return f"Datos de precipitación para '{nombre}' registrados."
