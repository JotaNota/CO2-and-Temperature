import pandas as pd

def load_data(file_path):
    """
    Carga el archivo CSV y retorna un DataFrame de Pandas.
    Args:
        file_path (str): Ruta al archivo CSV.
    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print("Error al cargar el archivo:", e)
        return None

def clean_data(df):
    """
    Realiza la limpieza inicial del DataFrame, eliminando columnas irrelevantes o valores nulos si es necesario.
    Args:
        df (pd.DataFrame): DataFrame original.
    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    # Filtrar solo las columnas necesarias o limpiar valores aquí
    # Puedes adaptar esta sección según las necesidades de tu análisis
    return df.dropna()  # Ejemplo: quitar filas con valores nulos
