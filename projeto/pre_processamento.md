# *Pré-Processamento de Dados*
Nesta etapa do projeto, concentramos nossos esforços no pré-processamento dos dados, visando prepará-los para as análises subsequentes e o treinamento de algoritmos de aprendizado de máquina.

## Escolha de Colunas

A base de dados utilizada neste estudo contém 70 colunas, com informações sobre a mãe, a gestação, o parto o recém-nascido além de dados sobre o local e o tempo do nascimento Cada linha da base representa um registro individual de nascimento ou seja, a unidade de análise é o próprio nascimento.

O objetivo deste trabalho é investigar possíveis correlações entre a condição socioeconômica da mãe e a saúde do neonato. Embora a base contenha uma ampla variedade de informações, nem todas serão consideradas na análise. O foco será direcionado às variáveis que dizem respeito à condição materna à saúde do recém-nascido e ao contexto temporal e geográfico do nascimento.

## Indicadores de Condição Socioeconômica Materna

Para compor um indicador representativo da condição socioeconômica da mãe, foram selecionadas variáveis que refletem aspectos *educacionais, sociais, raciais* e relacionados à *saúde reprodutiva*. Abaixo, descrevem-se os atributos mais diretamente associados a esse constructo:

- **`escolaridade_mae`**: indicador direto do nível socioeconômico, relacionado ao acesso à educação formal.
- **`idade_mae`**: idades muito precoces ou avançadas podem sinalizar contextos de maior vulnerabilidade social.
- **`raca_cor_mae`**: frequentemente utilizada em estudos de desigualdade social e racial, sendo um componente relevante no contexto brasileiro.
- **`quantidade_filhos_vivos`**: pode refletir acesso ao planejamento familiar e a métodos contraceptivos.
- **`quantidade_filhos_mortos`**: óbitos infantis anteriores podem indicar falhas no acesso a serviços de saúde, apontando para vulnerabilidades sociais.
- **`pre_natal_agr`**: reflete o nível de acompanhamento médico durante a gestação, geralmente relacionado ao acesso e qualidade dos serviços de saúde.
- **`tipo_parto`**: pode indicar o tipo de assistência recebida (pública ou privada), sendo utilizado como *proxy* indireto de condição socioeconômica.
- **`gestacao_agr`** e **`semana_gestacao_estimada`**: embora sejam variáveis clínicas, podem refletir desigualdades no acompanhamento pré-natal e nas condições de saúde da mãe.

Essas variáveis, utilizadas isoladamente ou de forma combinada, possibilitam a criação de indicadores ou categorias de condição socioeconômica ajustados aos objetivos analíticos do estudo.

## Indicadores de Saúde Neonatal

Para avaliar o estado de saúde do recém-nascido, foram selecionadas variáveis diretamente relacionadas às **condições clínicas do bebê no momento do nascimento**. Os principais atributos considerados são:

- **`peso`**: variável fundamental na saúde neonatal, com baixo peso associado a maior risco de complicações e óbitos.
- **`apgar1`** e **`apgar5`**: avaliam a vitalidade do bebê com base em sinais como batimentos cardíacos, respiração, tônus muscular, resposta a estímulos e coloração da pele.
- **`id_anomalia`**: a presença de anomalias congênitas afeta diretamente o prognóstico e a saúde geral do recém-nascido.
- **`semana_gestacao_estimada`**: a prematuridade (nascimento antes de 37 semanas) é um fator de risco importante para a saúde neonatal.
- **`gestacao_agr`**: versão categorizada da variável anterior, usada para facilitar análises comparativas.
- **`tipo_gravidez`**: gestações múltiplas aumentam o risco de complicações tanto para a mãe quanto para os bebês.
- **`tipo_parto`**: pode influenciar o estado clínico do bebê, especialmente em casos de cesáreas de emergência ou partos com intercorrências.


Essas variáveis oferecem uma base sólida para a construção de **indicadores de saúde neonatal**, bem como para a identificação de padrões de risco que poderão ser correlacionados com os fatores socioeconômicos maternos.


## Indicadores de Contexto Temporal e Geográfico do Nascimento

Além das variáveis socioeconômicas maternas e dos indicadores de saúde neonatal, também foram consideradas variáveis relacionadas ao contexto em que o nascimento ocorreu tanto no aspecto geográfico quanto temporal Essas informações são úteis para análises regionais ou sazonais.

###  Contexto Geográfico

- **`sigla_uf`**: sigla da Unidade Federativa onde ocorreu o nascimento.
- **`id_municipio_nascimento_nome`**: nome do município de nascimento.
- **`local_nascimento`**: tipo de estabelecimento onde ocorreu o parto (por exemplo, hospital, domicílio, outro).

### Contexto Temporal

- **`data_nascimento`**: data exata em que o nascimento ocorreu.
- **`hora_nascimento`**: horário em que o parto foi realizado.

Essas variáveis auxiliam na estratificação de análises por região e período além de contribuírem para a compreensão das condições em que os nascimentos se deram em diferentes localidades e horários.
Foi realizada uma etapa de verificação da integridade dos dados com o intuito de identificar valores duplicados, campos nulos e possíveis incongruências**. Essas verificações foram feitas por meio do BigQuery (Google Cloud) que oferece suporte a comandos SQL e proporciona uma visualização eficiente dos dados em grande volume. Por se tratarem de diversas queries de exploração, elas não serão listadas neste trabalho.

---


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

