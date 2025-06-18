# *Otimização e Propostas Futuras*

Esta etapa foca em **comparar o planejamento da governança de dados com as ações já realizadas** no projeto, ajustando-as aos princípios de governança (prestação de contas, transparência, LGPD, administração e qualidade de dados).

O projeto seguiu o **ciclo de vida dos dados**, extraindo-os do BigQuery, armazenando-os no AWS S3 (camadas Bronze, Silver, Gold via AWS Glue) e utilizando o Amazon SageMaker para Machine Learning.


## Avaliação e Ajustes da Governança:

* **Prestação de Contas:** O fluxo de dados é claro. Para aprimorar, sugere-se criar uma matriz RACI e documentar responsabilidades e permissões de acesso em cada camada do S3.
* **Transparência:** A documentação do pré-processamento e das métricas é boa. Recomenda-se facilitar o acesso e versionamento dos scripts de ETL e modelos, além de disponibilizar um dicionário de dados da tabela Gold.
* **Conformidade com a LGPD:** O uso de dados anonimizados do SINASC (domínio público) é um ponto forte. Para maior robustez, é importante referenciar a documentação oficial da anonimização.
* **Administração de Dados:** O fluxo e uso de tecnologias (BigQuery, S3, Glue) são bem definidos. Propostas incluem monitoramento de qualidade em cada camada, políticas de retenção e uso de um catálogo de dados (AWS Glue Data Catalog).
* **Padrões de Qualidade de Dados:** A remoção de duplicatas e o mapeamento de tipos de dados contribuem para a qualidade. É crucial formalizar as regras de qualidade aplicadas e implementar métricas para monitoramento contínuo.


## Otimizações Realizadas no Projeto:

O projeto já incorporou diversas otimizações:

1.  **Pré-processamento detalhado:** Inclusão de preenchimento de nulos, One-Hot Encoding e Normalização.
2.  **Divisão reprodutível dos dados:** Uso de `random_state=42` para garantir a consistência dos resultados.
3.  **Avaliação de múltiplos modelos e hiperparâmetros:** Testes com XGBoost, Ridge Regression e Random Forest, com diferentes configurações.
4.  **Expansão das métricas de avaliação:** Adição de MSLE, RMSLE e MaxError para uma análise mais completa do desempenho do modelo.
5.  **Análise detalhada e visualizações:** Interpretação das métricas e criação de gráficos para entender tendências nos dados da base Gold.
6.  **Identificação do melhor modelo:** O **XGBoost** foi eleito o mais eficiente, apesar da baixa capacidade de explicar a variância dos dados.


## Propostas Futuras e Oportunidades de Mercado:

Para continuar evoluindo, o projeto pode focar em:

* **Otimização avançada de hiperparâmetros** (Grid Search, Bayesian Optimization) e exploração de **novos algoritmos** (LightGBM, CatBoost, Redes Neurais).
* **Engenharia de atributos** para criar variáveis mais robustas e aprimorar a capacidade explicativa dos modelos.
* **Validação e monitoramento mais robustos** da qualidade dos dados.
* Implementação de **técnicas de ensemble learning** para melhorar a precisão.
* **Upgrade da infraestrutura** na AWS para lidar com mais dados e variáveis.
* Desenvolvimento de **dashboards interativos** para facilitar a comunicação e operacionalização dos insights.

Essas melhorias abrem caminho para diversas **oportunidades de mercado** na área de saúde materno-infantil, como:

* Desenvolvimento de **sistemas de apoio à decisão clínica** para identificação de riscos.
* Criação de **plataformas de monitoramento de saúde pública** para órgãos governamentais.
* Oferta de **soluções de saúde preventiva e personalizada** para gestantes.
* Parcerias para **pesquisa e desenvolvimento** em saúde.
* Análise de riscos para **seguradoras** no setor.