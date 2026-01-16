# Extractor de Metadatos Automatizado - GCP

Solución serverless que utiliza **Cloud Functions (2nd Gen)** y **Eventarc** para extraer metadatos de archivos subidos a **Cloud Storage**.

## Arquitectura del Sistema
1. **Trigger**: Google Cloud Storage (evento `finalized`).
2. **Procesamiento**: Python 3.10+ con Functions Framework.
3. **Seguridad**: Service Account personalizada con roles de `Storage Object Viewer` y `Logs Writer`.

## Pruebas Unitarias
Se implementó un set de pruebas con `unittest` para validar la integridad del código.
**Ejecución:**
`python -m unittest test_main.py`

## Evidencias
<img width="2560" height="1599" alt="image" src="https://github.com/user-attachments/assets/1a7cf3a4-5864-4f7b-9e79-3da61533ea11" />
<img width="2098" height="1186" alt="image" src="https://github.com/user-attachments/assets/67732905-9180-4fe6-a4c1-55be3f80c74c" />
