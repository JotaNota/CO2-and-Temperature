import pandas as pd

def load_data(file_path):
    """
    Carga los datos desde el archivo especificado y retorna un DataFrame.
    Args:
        file_path (str): Ruta del archivo de datos.
    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    df = pd.read_csv(file_path, delimiter=r'\s+', comment='%', header=None, skiprows=41)
    return df

def set_headers(df, headers):
    """
    Establece las cabeceras para el DataFrame.
    Args:
        df (pd.DataFrame): DataFrame cargado.
        headers (list): Lista de nombres de columnas.
    Returns:
        pd.DataFrame: DataFrame con cabeceras establecidas.
    """
    if len(headers) == len(df.columns):
        df.columns = headers
        print("Cabeceras establecidas correctamente.")
    else:
        print("Error: la cantidad de cabeceras no coincide con el número de columnas.")
    return df
