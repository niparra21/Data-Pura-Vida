# Este script lee un archivo CSV desde S3 y lo escribe en una tabla con formato Apache Iceberg.

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession

# --- Configuración Inicial Estándar de Glue ---
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# --- Parámetros de la Tabla Iceberg ---
# Define dónde se guardarán los datos de la tabla Iceberg en S3 y cómo se llamará en el catálogo.
S3_BUCKET_NAME = "poc-datalake-datapv-danielo"
GLUE_DB_NAME = "poc_datalake_db"
GLUE_TABLE_NAME = "dataset_transacciones"
# El identificador completo de la tabla para Spark, incluyendo el nombre del catálogo configurado.
TABLE_IDENTIFIER = f"glue_catalog.{GLUE_DB_NAME}.{GLUE_TABLE_NAME}"

# --- Lectura de Datos de Entrada (CSV) ---
# Lee el archivo CSV que subimos a S3.
input_s3_path = f"s3://{S3_BUCKET_NAME}/datos_entrada/datos_v2.csv" # Aqui se selecciona el archivo 
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_s3_path]},
    format="csv",
    format_options={"withHeader": True, "inferSchema": True}, # Le decimos que tiene encabezado e infiera los tipos de datos
)
dataframe = dynamic_frame.toDF() # Convierte el DynamicFrame de Glue a un DataFrame de Spark, que es más estándar.
print(">>> Datos de entrada leídos y convertidos a DataFrame de Spark:")
dataframe.show()

# --- Escritura en la Tabla Iceberg (Creación Inicial) ---
# Esta es la operación principal. Escribe el DataFrame en S3 y crea/actualiza la tabla en el catálogo de Glue en un solo paso.
dataframe.write.format("iceberg") \
    .mode("append") \ # Se selecciona el modo aqui
    .saveAsTable(TABLE_IDENTIFIER)

print(f">>> Tabla Iceberg '{TABLE_IDENTIFIER}' creada o sobreescrita exitosamente.")

job.commit()
