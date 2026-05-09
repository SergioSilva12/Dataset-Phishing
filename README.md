🛡️ Pipeline Temporal para Detecção de Phishing
Framework Experimental de Engenharia de Dados para Pesquisa em Detecção de URLs Maliciosas
📌 Visão Geral

Este repositório contém uma pipeline reproduzível de Engenharia de Dados desenvolvida para a construção de datasets de alta qualidade voltados à pesquisa em detecção de URLs de phishing.

O projeto foi concebido para sustentar experimentos acadêmicos rigorosos envolvendo a comparação entre:

algoritmos clássicos de Machine Learning;
arquiteturas profundas de Deep Learning;
estratégias híbridas de inferência adaptativa para sistemas de cibersegurança.

A pipeline foi projetada especificamente para mitigar limitações metodológicas frequentemente observadas na literatura de detecção de phishing, incluindo:

Data Leakage;
Concept Drift temporal;
memorização de domínios;
viés de popularidade em URLs legítimas;
protocolos irreais de avaliação experimental.

Os datasets gerados são adequados para pesquisas em:

Machine Learning;
Deep Learning;
Edge AI;
Inferência Adaptativa;
Sistemas Inteligentes de Cibersegurança.
🔬 Metodologia Experimental

Para garantir rigor científico, validade estatística e reprodutibilidade experimental, a pipeline implementa um protocolo multicamadas fundamentado em práticas modernas de avaliação em cibersegurança.

1️⃣ Prevenção de Data Leakage com Separação por Domínio

Estratégias tradicionais de divisão aleatória frequentemente introduzem vazamento de informação ao permitir que URLs pertencentes ao mesmo domínio apareçam simultaneamente nos conjuntos de treino e teste.

Para mitigar esse problema, a pipeline aplica uma estratégia de Domain-Aware Split, garantindo isolamento estrito entre domínios presentes em diferentes subconjuntos experimentais.

Essa abordagem assegura que os modelos aprendam características generalizáveis de phishing, em vez de memorizar padrões específicos de determinados domínios.

2️⃣ Protocolo de Isolamento Temporal

A pipeline adota uma estratégia cronológica de particionamento que simula condições reais de implantação operacional.

Os modelos são treinados utilizando campanhas históricas de phishing e avaliados sobre ameaças futuras inéditas, reproduzindo o comportamento de sistemas reais como:

Firewalls;
Secure Web Gateways;
Sistemas Anti-Phishing;
Motores de detecção Zero-Day.

O protocolo temporal reduz vieses otimistas causados por sobreposição cronológica e permite avaliar robustez frente ao fenômeno de Concept Drift.

3️⃣ Estratégia de Amostragem de URLs Legítimas

Em vez de utilizar apenas os domínios mais populares do ranking da Tranco List
, a pipeline aplica amostragem aleatória uniforme sobre toda a distribuição de URLs legítimas.

Essa abordagem reduz:

viés de popularidade;
viés lexical;
simplificações artificiais decorrentes de domínios excessivamente conhecidos.

Consequentemente, os datasets gerados aproximam-se de forma mais realista da diversidade estrutural da web pública.

4️⃣ Cenários Realistas de Avaliação

A framework produz dois cenários experimentais complementares.

🔹 Cenário A — Avaliação Balanceada
50% URLs legítimas
50% URLs de phishing

Esse cenário é destinado à:

comparação justa entre arquiteturas;
extração controlada de métricas;
análise da capacidade discriminativa dos modelos.

Principais métricas avaliadas:

Precisão (Precision);
Revocação (Recall);
F1-Score;
AUC-PR.
🔹 Cenário B — Avaliação em Cenário Real
90% URLs legítimas
10% URLs de phishing

Esse cenário reproduz distribuições observadas em ambientes reais de tráfego web e prioriza a análise de:

Taxa de Falsos Positivos (False Positive Rate);
Robustez operacional;
Viabilidade prática de implantação.
⚙️ Engenharia de Features

A pipeline extrai atributos lexicais e estatísticos amplamente utilizados na literatura de detecção de phishing.

Feature	Descrição
Comprimento da URL	Quantidade total de caracteres
Entropia de Shannon	Mede aleatoriedade textual
Presença de IP	Detecta uso de endereços IP brutos
Número de Subdomínios	Quantidade de níveis hierárquicos
Extração de Domínio	Normalização de domínio raiz
Metadados Temporais	Informações cronológicas das campanhas
🧪 Protocolo de Reprodutibilidade

Para garantir experimentação determinística e reproduzível, a framework incorpora:

controle global de sementes aleatórias (random seeds);
geração determinística de datasets;
hashes SHA-256 para integridade;
arquitetura ETL modular;
versionamento de metadados;
rastreabilidade temporal completa.

Todos os datasets gerados são acompanhados de arquivos estruturados de metadados contendo:

janelas temporais de coleta;
distribuições de classes;
estatísticas de pré-processamento;
taxas de remoção de duplicatas;
distribuições das features extraídas.
🗂️ Estrutura do Repositório
📦 phishing-dataset-pipeline
 ┣ 📂 1_scripts
 ┃ ┣ 📜 01_cleaning.py
 ┃ ┃ ┗━ Normalização, remoção de duplicatas e pré-processamento
 ┃ ┣ 📜 02_feature_engineering.py
 ┃ ┃ ┗━ Extração de atributos lexicais e estatísticos
 ┃ ┣ 📜 03_temporal_split.py
 ┃ ┃ ┗━ Particionamento cronológico com isolamento por domínio
 ┃ ┣ 📜 04_scenarios.py
 ┃ ┃ ┗━ Construção dos cenários balanceado e realista
 ┃ ┗ 📜 05_metadata.py
 ┃   ┗━ Geração de metadados e hashes SHA-256
 ┃
 ┣ 📂 2_dados_brutos
 ┃ ┗━ Bases originais (PhishTank / Tranco)
 ┃
 ┣ 📂 3_dados_intermediarios
 ┃ ┗━ Checkpoints e artefatos processados
 ┃
 ┣ 📂 4_dataset_final
 ┃ ┗━ Datasets finais prontos para treinamento e avaliação
 ┃
 ┗ 📜 README.md
📊 Fontes dos Dados
URLs de Phishing
PhishTank
URLs Legítimas
Tranco List
⚠️ Ameaças à Validade

Apesar dos mecanismos rigorosos de controle experimental, algumas limitações permanecem:

dependência de feeds públicos de phishing;
obsolescência temporal das campanhas;
representatividade parcial do tráfego legítimo da web;
possíveis mudanças distribucionais ao longo do tempo.

Essas limitações são explicitamente documentadas visando transparência metodológica e integridade científica.

🚀 Aplicações de Pesquisa

Os datasets gerados são adequados para pesquisas envolvendo:

Machine Learning clássico;
Deep Learning;
Generalização temporal;
Detecção de phishing Zero-Day;
Sistemas de Edge AI;
Inferência Adaptativa;
Classificação Seletiva;
Benchmarking computacional de modelos leves.
📖 Citação

Caso este repositório contribua para sua pesquisa, considere citá-lo adequadamente em publicações acadêmicas.

📜 Licença

Este projeto é destinado exclusivamente para fins acadêmicos e de pesquisa.
