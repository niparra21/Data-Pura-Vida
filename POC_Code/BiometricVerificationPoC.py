import json
import boto3

# --- Inicialización de Clientes de AWS ---
rekognition_client = boto3.client('rekognition')

def lambda_handler(event, context):
    """
    Punto de entrada para la función Lambda.
    1. Recibe los nombres del documento y la selfie desde el body.
    2. Llama a la API CompareFaces de Rekognition.
    3. Devuelve un resultado claro sobre la coincidencia.
    """
    print(f"Evento recibido: {event}")

    try:
        body = json.loads(event.get('body', '{}'))
        bucket_name = body.get('bucketName')
        document_name = body.get('documentName') # Imagen de la cédula
        selfie_name = body.get('selfieName')     # Imagen de la selfie

        if not all([bucket_name, document_name, selfie_name]):
            return {'statusCode': 400, 'body': json.dumps({'error': "Faltan 'bucketName', 'documentName' y 'selfieName'."})}
    except Exception as e:
        return {'statusCode': 400, 'body': json.dumps({'error': f"Cuerpo de solicitud inválido: {str(e)}"})}

    try:
        # --- Llamada a la API CompareFaces de Rekognition ---
        response = rekognition_client.compare_faces(
            SourceImage={'S3Object': {'Bucket': bucket_name, 'Name': document_name}},
            TargetImage={'S3Object': {'Bucket': bucket_name, 'Name': selfie_name}},
            SimilarityThreshold=95.0  # Umbral de similitud estricto del 95%
        )

        final_response_body = {}

        # Rekognition devuelve una lista de caras que coinciden. Si está vacía, no hubo coincidencia.
        if response['FaceMatches']:
            match = response['FaceMatches'][0] # Tomamos la primera y mejor coincidencia
            final_response_body = {
                "matchFound": True,
                "similarity": round(match['Similarity'], 2),
                "message": "La verificación biométrica fue exitosa."
            }
        else:
            final_response_body = {
                "matchFound": False,
                "message": "Las caras no coinciden o la similitud está por debajo del umbral."
            }

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(final_response_body)
        }

    except rekognition_client.exceptions.InvalidParameterException as e:
        # Este error ocurre a menudo si Rekognition no puede detectar una cara en una de las imágenes.
        print(f"ERROR de parámetro en Rekognition: {str(e)}")
        return {
            'statusCode': 400, 
            'body': json.dumps({
                "matchFound": False,
                "error": "No se pudo detectar una cara en una o ambas imágenes."
            })
        }
    except Exception as e:
        print(f"ERROR general: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps({'error': f"Error interno del servidor: {str(e)}"}) }