import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame
from pyspark.sql import functions as SqlFuncs

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
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

# Script generated for node Bronze
Bronze_node1744048860746 = glueContext.create_dynamic_frame.from_options(format_options={}, connection_type="s3", format="parquet", connection_options={"paths": ["s3://neonatais/Bronze/"], "recurse": True}, transformation_ctx="Bronze_node1744048860746")

# Script generated for node Exclusão de Linhas Duplicadas
ExclusodeLinhasDuplicadas_node1744048898074 =  DynamicFrame.fromDF(Bronze_node1744048860746.toDF().dropDuplicates(), glueContext, "ExclusodeLinhasDuplicadas_node1744048898074")

# Script generated for node Selecionando Colunas
SqlQuery0 = '''
select 
escolaridade_mae,
raca_cor_mae,
idade_mae,
sigla_uf,
id_municipio_nascimento_nome,
local_nascimento,
data_nascimento,
hora_nascimento,
sexo,
peso,
raca_cor,
apgar1,
apgar5,
id_anomalia,
semana_gestacao_estimada,
gestacao_agr,
tipo_gravidez,
tipo_parto,
pre_natal_agr,
quantidade_filhos_vivos,
quantidade_filhos_mortos
from  myDataSource
where data_nascimento IS NOT NULL
    and apgar1 < 11
    and apgar5 < 11
    and idade_mae > 7 and idade_mae < 66
    and sigla_uf IS NOT NULL
    and peso > 340 and peso < 7000
'''
SelecionandoColunas_node1744049807297 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"myDataSource":ExclusodeLinhasDuplicadas_node1744048898074}, transformation_ctx = "SelecionandoColunas_node1744049807297")

# Script generated for node Silver
EvaluateDataQuality().process_rows(frame=SelecionandoColunas_node1744049807297, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1744048833890", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Silver_node1744048979797 = glueContext.write_dynamic_frame.from_options(frame=SelecionandoColunas_node1744049807297, connection_type="s3", format="glueparquet", connection_options={"path": "s3://neonatais/Silver/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Silver_node1744048979797")

job.commit()
