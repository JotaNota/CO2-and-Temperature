def filter_data(df, start_year=1980):
    """
    Filtra los datos a partir de un año específico.
    Args:
        df (pd.DataFrame): DataFrame con los datos completos.
        start_year (int): Año de inicio para el filtro.
    Returns:
        pd.DataFrame: DataFrame filtrado a partir del año indicado.
    """
    return df[df['Year'] >= start_year].reset_index(drop=True)

def get_annual_anomalies(df):
    """
    Agrupa los datos por año para calcular el promedio de las anomalías anuales.
    Args:
        df (pd.DataFrame): DataFrame con los datos de temperatura.
    Returns:
        pd.Series: Serie con las anomalías anuales agrupadas por año.
    """
    return df.groupby('Year')['Annual Anomaly'].mean()
