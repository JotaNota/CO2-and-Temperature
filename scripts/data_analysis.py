def select_relevant_columns(df, year='2021'):
    """
    Selecciona las columnas 'Country Name' y el año más reciente.
    Args:
        df (pd.DataFrame): DataFrame de datos.
        year (str): Año a seleccionar.
    Returns:
        pd.DataFrame: DataFrame con columnas relevantes.
    """
    return df[['Country Name', year]]

def format_co2_values(df):
    """
    Formatea los valores de emisiones de CO2 para que sean más legibles.
    Args:
        df (pd.DataFrame): DataFrame de emisiones de CO2.
    Returns:
        pd.DataFrame: DataFrame con la columna 'CO2 Emissions' formateada.
    """
    df['CO2 Emissions'] = df['CO2 Emissions'].apply(lambda x: f"{x / 1e6:.2f}M")
    return df
