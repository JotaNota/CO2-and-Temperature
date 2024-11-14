import requests

def download_file(url, local_path):
    """
    Descarga un archivo desde una URL y lo guarda en una ubicación local.
    Args:
        url (str): URL del archivo a descargar.
        local_path (str): Ruta de destino donde se guardará el archivo.
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
        print(f"Archivo descargado y guardado en '{local_path}'")
    else:
        print(f"Error al descargar el archivo. Código de estado: {response.status_code}")
