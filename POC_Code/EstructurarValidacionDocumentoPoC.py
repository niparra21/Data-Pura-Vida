import json
import boto3
import uuid
import re
from datetime import datetime

# --- Inicialización de Clientes de AWS ---
textract_client = boto3.client('textract')
dynamodb = boto3.resource('dynamodb')

# --- Nombre de la tabla de DynamoDB ---
DYNAMODB_TABLE_NAME = 'ResultadosValidacionDocumentos'

def parse_textract_data(blocks):
    """
    Función helper para parsear la salida de DetectDocumentText y encontrar nuestros campos.
    """
    extracted_data = {}
    
    # Extraemos todas las líneas de texto detectadas
    lines = [item["Text"] for item in blocks if item["BlockType"] == "LINE"]
    
    # Buscamos cada campo usando expresiones regulares o búsqueda de texto simple
    for line in lines:
        # Buscar Nombre
        if "Nombre:" in line:
            # Tomar el texto después de "Nombre:" y limpiar espacios
            extracted_data['nombre'] = line.split("Nombre:")[1].strip()
        
        # Buscar 1er Apellido
        if "1°Apellido:" in line or "1° Apellido:" in line:
            extracted_data['primerApellido'] = line.split(":")[1].strip()
            
        # Buscar 2do Apellido
        if "2° Apellido:" in line or "2° Apellido:" in line:
            extracted_data['segundoApellido'] = line.split(":")[1].strip()

        # Buscar Cédula de Identidad (Buscamos un patrón como X XXXX XXXX)
        cedula_match = re.search(r'\d\s\d{4}\s\d{4}', line)
        if cedula_match:
            # Limpiamos los espacios para la validación
            extracted_data['numeroCedula'] = cedula_match.group(0).replace(' ', '')
            
    return extracted_data


def lambda_handler(event, context):
    """
    Punto de entrada para la función Lambda.
    1. Llama a la API DetectDocumentText de Textract.
    2. Parsea y estructura los datos extraídos con lógica personalizada.
    3. Aplica una validación simple.
    4. Guarda el resultado en DynamoDB.
    """
    print(f"Evento recibido: {event}")

    try:
        body = json.loads(event.get('body', '{}'))
        bucket_name = body.get('bucketName')
        document_name = body.get('documentName')

        if not bucket_name or not document_name:
            return {'statusCode': 400, 'body': json.dumps({'error': "Faltan 'bucketName' y 'documentName'."})}
    except Exception as e:
        return {'statusCode': 400, 'body': json.dumps({'error': f"Cuerpo de solicitud inválido: {str(e)}"})}

    try:
        # --- 1. Llamada a la API DetectDocumentText de Textract ---
        response = textract_client.detect_document_text(
            Document={'S3Object': {'Bucket': bucket_name, 'Name': document_name}}
        )

        # --- 2. Parseo y Estructuración de los Datos con Lógica Personalizada ---
        extracted_data = parse_textract_data(response.get("Blocks", []))
        
        print(f"Datos estructurados extraídos: {extracted_data}")

        # --- 3. Aplicación de Validación Lógica (VERSIÓN CORREGIDA) ---
        validation_errors = []
        required_fields = ['nombre', 'primerApellido', 'segundoApellido', 'numeroCedula']

        # Primero, verificar que todos los campos requeridos fueron extraídos
        for field in required_fields:
            if field not in extracted_data or not extracted_data.get(field):
                validation_errors.append(f"Campo requerido faltante: '{field}'")

        # Luego, si el campo existe, podemos hacer validaciones de formato adicionales
        if 'numeroCedula' in extracted_data and extracted_data.get('numeroCedula'):
            if not re.match(r'^\d{9}$', extracted_data['numeroCedula']):
                validation_errors.append(f"Formato de número de cédula inválido: {extracted_data['numeroCedula']}")
        
        # --- 4. Persistencia en DynamoDB ---
        validation_id = str(uuid.uuid4())
        
        tabla_resultados = dynamodb.Table(DYNAMODB_TABLE_NAME)
        item_to_save = {
            'idValidacion': validation_id,
            'nombreArchivo': document_name,
            'datosExtraidos': extracted_data,
            'erroresValidacion': validation_errors,
            'estado': 'COMPLETADO_CON_ERRORES' if validation_errors else 'COMPLETADO_OK',
            'timestamp': datetime.utcnow().isoformat()
        }
        
        tabla_resultados.put_item(Item=item_to_save)
        
        print(f"Resultado guardado en DynamoDB con ID: {validation_id}")
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(item_to_save)
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': f"Error interno del servidor: {str(e)}"}) }