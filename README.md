# 🛡️ Pipeline de Dados para Detecção de Phishing: ML vs Deep Learning

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Academic Project](https://img.shields.io/badge/Status-Pesquisa%20Ativa-success?style=for-the-badge)

## 📌 Sobre o Projeto
Este repositório contém a pipeline de Engenharia de Dados desenvolvida para estruturar um dataset robusto de URLs legítimas e maliciosas (Phishing). O objetivo primário dos dados gerados é alimentar experimentos acadêmicos que comparam a eficácia de algoritmos clássicos de **Machine Learning** (Random Forest, SVM) frente a arquiteturas de **Deep Learning** (CNNs, LSTMs).

A metodologia empregada foca em resolver falhas comuns na literatura de cibersegurança, como o viés de popularidade, o vazamento de dados (*Data Leakage*) e a degradação de conceito temporal (*Concept Drift*).

## 🔬 Metodologia Científica Aplicada

Para garantir validade estatística e rigor de nível de publicação (*Qualis A*), o pipeline implementa:

1. **Prevenção de *Data Leakage* (Domain-Aware Split):** O particionamento entre conjuntos de Treino, Validação e Teste é feito isolando os domínios-raiz. Isso garante que o modelo aprenda características de phishing de fato, e não memorize domínios específicos.
2. **Isolamento Temporal:** A divisão cronológica simula o comportamento real de um *firewall* ou antivírus, treinando com dados do passado para detectar ameaças (Zero-Day) no futuro.
3. **Amostragem Legítima Uniforme:** Em vez de utilizar apenas o topo do ranking da *Tranco List* (o que criaria um viés de domínios curtos e famosos), aplicou-se amostragem aleatória uniforme sobre toda a base de domínios seguros.
4. **Cenários de Validação Realistas:**
   - **Cenário A (Balanceado):** Distribuição 50/50 para extração de métricas justas de base matemática (Precisão, Recall).
   - **Cenário B (Desbalanceado):** Distribuição 10/90 no conjunto de teste, simulando o tráfego do mundo real e focando na análise da Taxa de Falsos Positivos.

## 🗂️ Estrutura do Repositório

O projeto adota uma arquitetura modular ETL (Extract, Transform, Load) organizada da seguinte forma:

```text
📦 phishing-dataset-pipeline
 ┣ 📂 1_scripts                  # Módulos Python do pipeline
 ┃ ┣ 📜 01_cleaning.py           # Normalização, remoção de duplicatas e amostragem
 ┃ ┣ 📜 02_feature.py            # Extração de features matemáticas (Entropia, IPs, etc.)
 ┃ ┣ 📜 03_split.py              # Domain-Aware Temporal Split
 ┃ ┣ 📜 04_scenarios.py          # Construção dos Cenários A e B
 ┃ ┗ 📜 05_metaData.py           # Geração de Hashes SHA-256 e Metadados
 ┣ 📂 2_dados_brutos             # Arquivos originais (PhishTank / Tranco JSON/CSV)
 ┣ 📂 3_dados_intermediarios     # Checkpoints das etapas do pipeline
 ┗ 📂 4_dataset_final            # ✅ Arquivos finais prontos para o Treinamento de IA
