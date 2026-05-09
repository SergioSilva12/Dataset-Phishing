# 🛡️ Pipeline Temporal para Detecção de Phishing

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Machine Learning]
![Deep Learning]
![License]
![Status](https://img.shields.io/badge/Status-Pesquisa%20Ativa-success.svg)

> **Framework Experimental Reproduzível para Pesquisa em Detecção de URLs Maliciosas, Robustez Temporal e IA Adversarial.**

---

# 📌 Visão Geral

Este repositório apresenta uma pipeline completa de Engenharia de Dados desenvolvida para construção de benchmarks científicos voltados à detecção de URLs de phishing.

O projeto foi concebido para sustentar experimentos acadêmicos rigorosos envolvendo:

- Algoritmos clássicos de **Machine Learning**;
- Arquiteturas profundas de **Deep Learning**;
- Estratégias híbridas de **Inferência Adaptativa**;
- Avaliação de robustez contra técnicas modernas de evasão lexical.

A framework foi projetada especificamente para mitigar limitações metodológicas frequentemente observadas na literatura, incluindo:

- *Data Leakage*;
- *Concept Drift* temporal;
- Memorização de domínios;
- Viés de popularidade;
- Protocolos irreais de avaliação experimental;
- Ausência de cenários adversariais.

---

# 🔬 Metodologia Experimental

Para garantir rigor científico, validade estatística e reprodutibilidade, a pipeline implementa um protocolo multicamadas fundamentado em práticas modernas de cibersegurança.

---

## 1️⃣ Prevenção de *Data Leakage* com Separação por Domínio

Estratégias tradicionais de divisão aleatória frequentemente introduzem vazamento de informação entre treino e teste.

Para mitigar esse problema, a pipeline aplica uma estratégia de **Domain-Aware Split**, garantindo isolamento estrito entre domínios nos subconjuntos experimentais.

Isso assegura que os modelos aprendam padrões generalizáveis de phishing, em vez de apenas memorizar URLs previamente observadas.

---

## 2️⃣ Protocolo de Isolamento Temporal

A pipeline adota um particionamento cronológico que simula condições reais de implantação (*Zero-Day Detection*).

Os modelos são treinados utilizando campanhas históricas e avaliados sobre ameaças futuras inéditas, reduzindo vieses otimistas e avaliando a robustez frente ao fenômeno de *Concept Drift*.

---

## 3️⃣ Estratégia de Amostragem de URLs Legítimas

Em vez de utilizar apenas o topo do ranking da Tranco List, aplicou-se uma estratégia de amostragem uniforme distribuída sobre toda a base de domínios legítimos.

Essa abordagem reduz vieses de popularidade e aproxima o benchmark da diversidade estrutural observada na web pública real.

---

# 🧬 Data Augmentation Adversarial

A pipeline incorpora um módulo avançado de geração sintética de URLs maliciosas inspirado em estratégias reais utilizadas por campanhas modernas de phishing.

---

## 🎯 Motivação

Sistemas tradicionais de detecção frequentemente sofrem degradação de desempenho quando confrontados com URLs inéditas ou variantes lexicalmente modificadas.

Esse problema se tornou ainda mais relevante com o crescimento de ferramentas automatizadas baseadas em IA generativa, capazes de produzir milhares de variações maliciosas para evasão de filtros de segurança.

Dessa forma, o módulo de *Data Augmentation Adversarial* foi desenvolvido com três objetivos principais:

- Simular estratégias modernas de evasão lexical;
- Reduzir o viés de estagnação do dataset;
- Avaliar a capacidade de generalização dos modelos diante de mutações sintéticas inéditas.

---

## ⚙️ Estratégias de Geração Sintética

As URLs adversariais são geradas preservando a estrutura semântica original da URL enquanto realizam mutações controladas no domínio.

As técnicas implementadas incluem:

| Técnica | Descrição |
| :--- | :--- |
| **Homoglyph Attacks** | Substituição visual de caracteres (`o → 0`, `l → 1`) |
| **Typosquatting** | Inserção/remoção de caracteres simulando erros humanos |
| **Subdomain Injection** | Inclusão de termos como `login`, `secure`, `verify` |
| **Hyphenation Attacks** | Inserção estratégica de hífens |
| **TLD Manipulation** | Alteração de extensões para `.xyz`, `.site`, `.online` |

Todas as URLs geradas passam por validação estrutural e controle de duplicidade antes de serem incorporadas ao benchmark.

---

## 📊 Proporção Estratégica

As URLs sintéticas representam aproximadamente **0.4%** do conjunto final de teste.

Essa baixa proporção foi intencionalmente adotada para simular o comportamento real da web, onde ataques adversariais sofisticados representam uma pequena fração do tráfego total, funcionando como uma "agulha no palheiro".

Assim, o benchmark avalia:
- Robustez;
- Generalização;
- Sensibilidade a evasão;
- Capacidade de detecção de ataques inéditos.

---

# 📊 Cenários de Avaliação

A framework produz dois cenários experimentais complementares.

| Cenário | Distribuição | Objetivo Principal | Métricas Foco |
| :--- | :--- | :--- | :--- |
| **A (Balanceado)** | 50% Legítimas / 50% Phishing | Comparação justa entre arquiteturas | Precision, Recall, F1-Score, AUC-PR |
| **B (Realista)** | 90% Legítimas / 10% Phishing | Simulação de tráfego real | False Positive Rate (FPR), Robustez |

Os datasets encontram-se organizados em duas versões:
- **Baseline (sem augmentation)**;
- **Advanced (com augmentation adversarial)**.

Isso permite estudos de ablação e análise do impacto do augmentation sobre a generalização dos modelos.

---

# ⚙️ Engenharia de Features

A pipeline extrai atributos lexicais e estatísticos amplamente utilizados na literatura científica.

| Feature | Descrição |
| :--- | :--- |
| `url_length` | Quantidade total de caracteres na URL |
| `entropy` | Entropia de Shannon da string |
| `has_ip` | Detecta uso de endereços IP no domínio |
| `num_subdomains` | Quantidade de subdomínios |
| `domain_extraction` | Normalização do domínio raiz |

---

# 🗂️ Estrutura do Repositório

```text
📦 phishing-dataset-pipeline
 ┣ 📂 Dados Brutos
 ┃ ┗ 📜 Feeds originais (PhishTank / Tranco)

 ┣ 📂 Dados intermediarios
 ┃ ┗ 📜 CSVs processados e checkpoints do pipeline

 ┣ 📂 Dataset Final com aug
 ┃ ┗ 📜 Benchmark final contendo URLs adversariais

 ┣ 📂 Dataset Final sem aug
 ┃ ┗ 📜 Benchmark baseline sem augmentation

 ┣ 📂 scripts
 ┃ ┣ 📜 01_cleaning.py
 ┃ ┣ 📜 01b_augmentation_llm.py
 ┃ ┣ 📜 02_feature.py
 ┃ ┣ 📜 02b_feature_synthetic.py
 ┃ ┣ 📜 03_create_benchmark.py
 ┃ ┣ 📜 03_split.py
 ┃ ┣ 📜 04_scenarios.py
 ┃ ┣ 📜 04_time_split_stratified.py
 ┃ ┗ 📜 05_metaData.py

 ┣ 📜 README.md
 ┣ 📜 .gitignore
 ┗ 📜 teste.py

# 👨‍💻 Autor

<div align="center">

## Sérgio Silva de Oliveira

Estudante de Ciência da Computação — IFCE Campus Iguatu

Pesquisador com foco em:

🔹 Deep Learning  
🔹 Segurança Cibernética  
🔹 Detecção de Phishing  
🔹 Robustez Adversarial  
🔹 Machine Learning Aplicado

</div>

---

# 📚 Citação

Caso este repositório contribua para sua pesquisa ou projeto acadêmico, considere citar este projeto e referenciar o Instituto Federal do Ceará (IFCE).

```bibtex
@misc{silva2026phishingbenchmark,
  author       = {Sérgio Silva de Oliveira},
  title        = {Temporal Phishing Detection Benchmark},
  year         = {2026},
  institution  = {Instituto Federal do Ceará (IFCE)},
  note         = {Framework Experimental para Detecção de URLs Maliciosas e IA Adversarial},
  url          = {https://github.com/SergioSilva12/Dataset-Phishing}
}
