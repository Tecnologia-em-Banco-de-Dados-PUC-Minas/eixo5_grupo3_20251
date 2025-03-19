# **Governança de dados**
A base de dados utilizada neste projeto é de domínio público e foi obtida por meio do site basedosdados.org, que disponibiliza informações oriundas do Sistema de Informações sobre Nascidos Vivos (SINASC), elaborado pelo Departamento de Informática do SUS (DATASUS). Esses dados são fornecidos em formato CSV, organizados em arquivos de até 1 GB, totalizando 16,51 GB, e abrangem o período de 1979 a 2023. Por já estarem anonimizados e em conformidade com as diretrizes da Lei Geral de Proteção de Dados (LGPD), não demandam tratamento adicional para garantir a proteção de informações pessoais, o que simplifica o processo inicial de manipulação.

## Ciclo de vida dos Dados
A extração dos dados será realizada manualmente a partir da plataforma basedosdados.org, que utiliza o BigQuery como ferramenta de suporte, facilitando o acesso às informações. Após o download, os dados serão armazenados localmente e submetidos a um processo de transformação e modelagem utilizando o PySpark, executado no ambiente do Visual Studio Code. Esse processo seguirá o modelo medalhão, estruturado em etapas bem definidas: na Landing Stage, os dados brutos serão recebidos; na camada Bronze, passarão por limpezas iniciais; na Silver, serão enriquecidos com transformações mais elaboradas; e, finalmente, na Gold, serão consolidados em tabelas otimizadas, organizadas no formato de modelo estrela. O resultado dessas etapas será salvo em arquivos Parquet, um formato eficiente e compacto. Em seguida, os dados tratados serão carregados para uma instância do Amazon S3 na AWS, onde servirão como base para a aplicação de técnicas de Machine Learning por meio do SageMaker, possibilitando análises avançadas relacionadas aos objetivos do projeto.

## Tecnologias Utilizadas

### Armazenamento Local
![Armazenamento Local](local.png)

### AWS
![AWS](aws.png)

### PySpark
![PySpark](pyspark.png)

### S3
![S3](s3.png)

### SageMaker
![SageMaker](sagemaker.png)

