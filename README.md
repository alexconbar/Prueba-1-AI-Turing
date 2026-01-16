# Extractor de Metadatos Automatizado - GCP

Solución serverless que utiliza **Cloud Functions (2nd Gen)** y **Eventarc** para extraer metadatos de archivos subidos a **Cloud Storage**.

## Arquitectura del Sistema
1. **Trigger**: Google Cloud Storage (evento `finalized`).
2. **Procesamiento**: Python 3.10+ con Functions Framework.
3. **Seguridad**: Service Account personalizada con roles de `Storage Object Viewer` y `Logs Writer`.

## Diagrama de Arquitectura
**Flujo de Datos:** `Google Cloud Storage` ➔ `Eventarc Trigger` ➔ `Cloud Function` (Python) ➔ `Cloud Logging`

##Explicación del Proceso
**Trigger:** La carga de un archivo (como el tuyo S14.jpg) en el bucket `bucket_prueba_gcp` genera un evento de tipo `google.cloud.storage.object.v1.finalized`.

**Procesamiento:** La Cloud Function recibe este evento de forma asíncrona. El código extrae el nombre, tamaño y tipo de contenido directamente del `objeto cloud_event.data`.

**Validación:** Se incluyó un bloque `try-except` para asegurar que, si el evento viene malformado o sin nombre, la función responda con un error controlado (HTTP 500) en lugar de fallar silenciosamente.

**Salida:** Los metadatos se envían a Cloud Logging, permitiendo la trazabilidad del proceso.

## Pruebas Unitarias
Se implementó un set de pruebas con `unittest` para validar la integridad del código.
**Ejecución:**
`python -m unittest test_main.py`

## Evidencias
<img width="2560" height="1599" alt="image" src="https://github.com/user-attachments/assets/1a7cf3a4-5864-4f7b-9e79-3da61533ea11" />
<img width="2098" height="1186" alt="image" src="https://github.com/user-attachments/assets/67732905-9180-4fe6-a4c1-55be3f80c74c" />
