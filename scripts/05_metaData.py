import pandas as pd
import hashlib
import json
import os
from datetime import datetime

print("📊 Gerando Hash e Metadados do Projeto...")

def file_hash(path):
    if not os.path.exists(path): return None
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

arquivos_finais = [
    'FINAL_A_train.csv', 'FINAL_A_val.csv', 
    'FINAL_A_test.csv', 'FINAL_B_test_real.csv'
]

hashes = {arq: file_hash(arq) for arq in arquivos_finais}

# Coletando alguns números rápidos para o relatório
train_a_len = len(pd.read_csv('FINAL_A_train.csv'))
test_b = pd.read_csv('FINAL_B_test_real.csv')

metadata = {
    "project": "Detecção de Phishing: ML vs DL",
    "version": "1.0",
    "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "methodology": "Domain-Aware Temporal Split with Tranco Uniform Sampling",
    "scenarios": {
        "Scenario_A": {"description": "Balanced 50/50", "train_size": train_a_len},
        "Scenario_B": {"description": "Imbalanced 10/90", "test_size": len(test_b)}
    },
    "file_integrity_sha256": hashes
}

with open("dataset_metadata.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=4)

print("✅ Etapa 5 Concluída! O arquivo 'dataset_metadata.json' foi gerado com sucesso.")
print("🚀 Pipeline finalizado. Seu dataset está pronto.")