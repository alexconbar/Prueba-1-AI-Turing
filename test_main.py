import unittest
from unittest.mock import MagicMock
from main import metadata_extractor

class TestCloudFunction(unittest.TestCase):

    def test_metadata_extraction_success(self):
        """Prueba un flujo donde el evento trae todos los datos correctamente"""
        # 1. Creamos un 'mock' (simulacro) del evento que enviaría Google Cloud
        mock_event = MagicMock()
        mock_event.data = {
            "name": "foto_prueba.jpg",
            "bucket": "bucket-examen-ti",
            "size": "5000",
            "contentType": "image/jpeg"
        }
        
        # 2. Ejecutamos la función con el evento simulado
        response, status_code = metadata_extractor(mock_event)
        
        # 3. Verificamos que el resultado sea exitoso (200 OK)
        self.assertEqual(status_code, 200)
        self.assertEqual(response, "OK")

    def test_metadata_extraction_error(self):
        """Prueba el manejo de errores cuando el evento viene vacío o malformado"""
        # 1. Simulamos un evento que no tiene la estructura esperada (falta 'data')
        mock_event = MagicMock()
        mock_event.data = {} 
        
        # 2. Ejecutamos la función
        response, status_code = metadata_extractor(mock_event)
        
        # 3. Verificamos que el código maneje el error devolviendo un 500
        self.assertEqual(status_code, 500)
        self.assertEqual(response, "Error")

if __name__ == '__main__':
    unittest.main()
