import folium

def create_map(data, output_file='mapa_interactivo.html'):
    """
    Crea un mapa interactivo utilizando los datos de emisiones de CO2.
    Args:
        data (dict): Diccionario con los datos para visualizar.
        output_file (str): Nombre del archivo HTML donde se guardará el mapa.
    """
    # Inicializar el mapa en una ubicación central (ejemplo: coordenadas globales)
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Añadir datos al mapa
    for country, co2 in data.items():
        # Crear marcadores o círculos en el mapa (Ejemplo de círculo)
        folium.CircleMarker(
            location=[country['latitude'], country['longitude']],  # Debes tener latitud y longitud para cada país
            radius=5,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6,
            popup=f"{country['name']}: {co2}M toneladas"
        ).add_to(m)

    # Guardar el mapa en un archivo HTML
    m.save(output_file)
    print(f"Mapa guardado en {output_file}")
