import json
import boto3
from decimal import Decimal

# --- Inicialización de Clientes de AWS ---
textract_client = boto3.client('textract')

# Clase "helper" para manejar la conversión de tipos a JSON
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

# Handler principal
def lambda_handler(event, context):
    print(f"Evento recibido desde API Gateway: {event}")

    try:
        # 1. Parsear el cuerpo de la solicitud que envía API Gateway
        body = json.loads(event.get('body', '{}'))
        
        # 2. Extraer los parámetros del cuerpo de la solicitud
        bucket_name = body.get('bucketName')
        document_name = body.get('documentName')

        # Validar que los parámetros necesarios fueron proporcionados
        if not bucket_name or not document_name:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': "Faltan los parámetros 'bucketName' y 'documentName' en el cuerpo de la solicitud."})
            }

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': "Cuerpo de la solicitud malformado. Se esperaba un JSON válido."})
        }
    
    print(f"Iniciando procesamiento para el documento: {document_name} en el bucket: {bucket_name}")

    try:
        # 3. Llamar a la API de Textract (la lógica principal no cambia)
        response = textract_client.detect_document_text(
            Document={'S3Object': {'Bucket': bucket_name, 'Name': document_name}}
        )

        detected_text = []
        for item in response["Blocks"]:
            if item["BlockType"] == "LINE":
                detected_text.append(item["Text"])
        
        print(f"RESULTADO DE TEXTRACT: {json.dumps(detected_text, indent=2)}")
        
        # 4. Devolver una respuesta exitosa
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'processedDocument': document_name, 'extractedText': detected_text}, cls=DecimalEncoder)
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        # Devolver un error genérico del servidor si algo sale mal con la llamada a Textract
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f"Error al procesar el documento: {str(e)}"}, cls=DecimalEncoder)
        }