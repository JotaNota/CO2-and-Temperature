from data_loader import load_data, clean_data
from data_analysis import select_relevant_columns, format_co2_values
from visualization import create_map

def main():
    # Ruta al archivo CSV
    file_path = 'API_NY.ADJ.DCO2.CD_DS2_en_csv_v2_5661993.csv'  # Cambia este nombre al de tu archivo

    # 1. Cargar y limpiar los datos
    df = load_data(file_path)
    if df is None:
        print("No se pudo cargar el archivo.")
        return

    df = clean_data(df)

    # 2. Seleccionar columnas relevantes y formatear los valores
    co2_data = select_relevant_columns(df)
    co2_data = format_co2_values(co2_data)

    # 3. Convertir los datos a un diccionario para la visualización
    data_dict = co2_data.set_index('Country Name')['CO2 Emissions'].to_dict()

    # 4. Crear el mapa interactivo
    create_map(data_dict)

if __name__ == "__main__":
    main()
