Silver_To_Gold:
" import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Silver
Silver_node1744044168188 = glueContext.create_dynamic_frame.from_options(format_options={}, connection_type="s3", format="parquet", connection_options={"paths": ["s3://neonatais/Silver/"], "recurse": True}, transformation_ctx="Silver_node1744044168188")

# Script generated for node Change Schema
ChangeSchema_node1744050145999 = ApplyMapping.apply(frame=Silver_node1744044168188, mappings=[("sigla_uf", "string", "sigla_uf", "string"), ("id_municipio_nascimento_nome", "string", "id_municipio_nascimento_nome", "string"), ("local_nascimento", "string", "local_nascimento", "string"), ("data_nascimento", "string", "data_nascimento", "date"), ("hora_nascimento", "string", "hora_nascimento", "varchar"), ("sexo", "string", "sexo", "string"), ("peso", "string", "peso", "int"), ("raca_cor", "string", "raca_cor", "string"), ("apgar1", "string", "apgar1", "int"), ("apgar5", "string", "apgar5", "int"), ("id_anomalia", "string", "id_anomalia", "varchar"), ("semana_gestacao_estimada", "null", "semana_gestacao_estimada", "null"), ("gestacao_agr", "string", "gestacao_agr", "varchar"), ("tipo_gravidez", "string", "tipo_gravidez", "string"), ("tipo_parto", "string", "tipo_parto", "string"), ("pre_natal_agr", "string", "pre_natal_agr", "varchar"), ("quantidade_filhos_vivos", "string", "quantidade_filhos_vivos", "int"), ("quantidade_filhos_mortos", "string", "quantidade_filhos_mortos", "int")], transformation_ctx="ChangeSchema_node1744050145999")

# Script generated for node Gold
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1744050145999, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1744050045588", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Gold_node1744050159095 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1744050145999, connection_type="s3", format="glueparquet", connection_options={"path": "s3://neonatais/Gold/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Gold_node1744050159095")

job.commit()"

