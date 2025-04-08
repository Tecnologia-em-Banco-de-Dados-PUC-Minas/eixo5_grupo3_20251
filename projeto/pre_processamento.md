# *Pré-Processamento de Dados*
Nesta etapa do projeto, concentramos nossos esforços no pré-processamento dos dados, visando prepará-los para as análises subsequentes e o treinamento de algoritmos de aprendizado de máquina.

### *Camada Bronze para Silver:*
Nesta fase, os dados brutos são armazenados no bucket s3://neonatais/Bronze/ em formato Parquet com todas as colunas no formato de dados "string". Essa camada representa a origem dos dados sem tratamento, mantendo o estado original para posterior processamento.
O job inicia com a leitura dos dados brutos e, em seguida, remove duplicatas para garantir a integridade dos registros, eliminando possíveis redundâncias que comprometeriam a qualidade do dataset. Após isso, uma transformação SQL é aplicada para selecionar apenas as colunas que julgamos pertinentes ao objetivo do trabalho (como sigla_uf, data_nascimento, peso...). Essas transformações padronizam o conjunto de dados e mantém o foco nas informações mais relevantes. Por fim, o resultado é gravado no bucket s3://neonatais/Silver/ em formato .parquet com compressão Snappy, estruturando a camada Silver como um ambiente com dados limpos, porém com o tipo de dado não definido. 
![image alt](https://github.com/Tecnologia-em-Banco-de-Dados-PUC-Minas/eixo5_grupo3_20251/blob/main/Bronze_To_Silver.png?raw=true)

Mais detalhes do script disponível em: 
[Script_Bronze_To_Silver.py](../Script_Bronze_To_Silver.py)

### *Camada Silver para Gold:*

Os dados da camada Silver são lidos para serem refinados. Um mapeamento detalhado é realizado para converter os tipos de dados de acordo com a necessidade da análise. Por exemplo, o campo data_nascimento é convertido de string para data, enquanto campos como peso, apgar1 e apgar5 passam de string para inteiros. Essa transformação garante que os dados estejam no formato ideal para uso em machine learning, evitando problemas de desempenho e inconsistências. Após a aplicação de regras de qualidade similares às utilizadas na etapa anterior, os dados refinados são gravados no bucket s3://neonatais/Gold/ com compressão Snappy. A camada Gold é otimizada para machine learning, contendo somente os campos essenciais e com tipagem adequada, o que facilita a aplicação de algoritmos e melhora o desempenho do treinamento.

![image alt](https://github.com/Tecnologia-em-Banco-de-Dados-PUC-Minas/eixo5_grupo3_20251/blob/main/Silver_To_Gold.png?raw=true)

Mais detalhes do script disponível em: 
[Script_Silver_To_Gold.py](../Script_Silver_To_Gold.py)

