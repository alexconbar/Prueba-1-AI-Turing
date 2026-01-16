import functions_framework
import logging

# Configuración básica de logs
logging.basicConfig(level=logging.INFO)

@functions_framework.cloud_event
def metadata_extractor(cloud_event):
    # Obtener metadatos de la carga útil del evento
    data = cloud_event.data
    
    try:
        # VALIDACIÓN CRÍTICA: Si el evento no tiene nombre de archivo, 
        # lanzamos un error para que el bloque 'except' lo capture.
        if not data or 'name' not in data:
            raise ValueError("El evento no contiene el nombre del archivo (campo 'name' ausente).")

            file_name = data["name"]
            logging.info(f"Procesando archivo: {file_name}")
            
            # Simulación de extracción de otros metadatos
            bucket = data.get("bucket", "desconocido")
            size = data.get("size", "0")
            
            print(f"--- Metadatos del Archivo ---")
            print(f"Nombre: {file_name}")
            print(f"Bucket: {bucket}")
            print(f"Tamaño: {size} bytes")
        
        return "OK", 200

    except Exception as e:
        # Esto capturará el ValueError de arriba y cualquier otro fallo inesperado
        logging.error(f"Error procesando el evento: {str(e)}")
        return "Error", 500
