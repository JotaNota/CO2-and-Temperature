from data_downloader import download_file
from data_loader import load_data, set_headers
from data_processing import filter_data, get_annual_anomalies
from visualization import plot_annual_anomalies

def main():
    # Parámetros de configuración
    url = 'https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Land_and_Ocean_complete.txt'
    local_path = r'C:\Users\JUAN DIAZ\Desktop\Projects\DataNoob\data\Weather_data\Land_and_Ocean_complete.txt'
    
    # Descargar el archivo
    download_file(url, local_path)
    
    # Cargar los datos
    df = load_data(local_path)
    
    # Definir cabeceras
    headers = [
        'Year', 'Month', 'Monthly Anomaly', 'Monthly Unc', 
        'Annual Anomaly', 'Annual Unc', 'Five-year Anomaly', 'Five-year Unc', 
        'Ten-year Anomaly', 'Ten-year Unc', 'Twenty-year Anomaly', 'Twenty-year Unc'
    ]
    
    # Configurar las cabeceras y mostrar los primeros datos
    df = set_headers(df, headers)
    
    # Filtrar y procesar los datos
    df_filtered = filter_data(df, start_year=1980)
    annual_anomalies = get_annual_anomalies(df_filtered)
    
    # Visualizar las anomalías anuales
    plot_annual_anomalies(annual_anomalies)

if __name__ == "__main__":
    main()
