import pandas as pd
import os
import json
import hashlib
from datetime import datetime

# Pega o caminho da pasta onde este script esta salvo
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Define os caminhos de entrada (ajustado para a pasta que voce ja tem)
# Se os arquivos estiverem em outra pasta, mude apenas o nome entre aspas
PASTA_ORIGEM = os.path.join(PASTA_ATUAL, "Dados intermediarios")
FILE_LEGIT = os.path.join(PASTA_ORIGEM, "02_legit_features.csv")
FILE_PHISH_REAL = os.path.join(PASTA_ORIGEM, "02_phish_features.csv")
FILE_PHISH_SYNC = os.path.join(PASTA_ORIGEM, "02_phish_synthetic_features.csv")

# Define onde vai salvar (Sempre dentro da pasta do script)
OUTPUT_DIR = os.path.join(PASTA_ATUAL, "Dataset_Final_TCC")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "phishing_detection_benchmark.csv")
OUTPUT_CARD = os.path.join(OUTPUT_DIR, "dataset_card.json")
OUTPUT_HASH = os.path.join(OUTPUT_DIR, "dataset_hash.txt")

def carregar_dados(caminho, label_esperado, is_synthetic, source_dataset):
    if not os.path.exists(caminho):
        print(f"[ERRO] Arquivo nao encontrado: {caminho}")
        return pd.DataFrame()
    
    try:
        df = pd.read_csv(caminho)
        df['source_dataset'] = source_dataset
        df['is_synthetic'] = is_synthetic
        df['augmentation_type'] = df.get('augmentation_type', 'original')
        df['label'] = label_esperado
        print(f"[OK] Carregado: {source_dataset} ({len(df)} linhas)")
        return df
    except Exception as e:
        print(f"[ERRO] Falha ao ler {source_dataset}: {e}")
        return pd.DataFrame()

def main():
    print(f"Pasta do Projeto: {PASTA_ATUAL}")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Criando pasta de saida: {OUTPUT_DIR}")

    # 1. Carrega os dados
    df_legit = carregar_dados(FILE_LEGIT, 0, 0, "Tranco_Top_1M")
    df_real_phish = carregar_dados(FILE_PHISH_REAL, 1, 0, "PhishTank_Verified")
    df_sync_phish = carregar_dados(FILE_PHISH_SYNC, 1, 1, "Synthetic_Pipeline")

    datasets = [df for df in [df_legit, df_real_phish, df_sync_phish] if not df.empty]
    
    if not datasets:
        print("\n[!] NENHUM DADO FOI CARREGADO. Verifique se os nomes dos arquivos estao corretos.")
        return

    # 2. Une os dados
    df_final = pd.concat(datasets, ignore_index=True).fillna(0)
    
    # Adiciona categoria
    def classificar(row):
        if row['label'] == 0: return 'legitimate'
        return 'synthetic_adversarial' if row['is_synthetic'] == 1 else 'human_phishing'
    
    df_final['data_category'] = df_final.apply(classificar, axis=1)

    # 3. SALVAMENTO REAL
    print(f"Tentando salvar em: {OUTPUT_CSV}")
    df_final.to_csv(OUTPUT_CSV, index=False)
    
    if os.path.exists(OUTPUT_CSV):
        print(">>> SUCESSO: Arquivo CSV gravado no disco!")
    else:
        print(">>> ERRO: O Windows nao permitiu a gravacao do arquivo.")

    # 4. Metadados e Hash
    hash_val = hashlib.sha256(open(OUTPUT_CSV, 'rb').read()).hexdigest()
    
    card = {
        "metadata": {"version": "v1.0.0", "sha256": hash_val},
        "statistics": {
            "total": len(df_final),
            "categories": df_final['data_category'].value_counts().to_dict()
        }
    }

    with open(OUTPUT_CARD, "w") as f:
        json.dump(card, f, indent=4)
    
    with open(OUTPUT_HASH, "w") as f:
        f.write(f"SHA-256: {hash_val}")

    print("\n" + "="*40)
    print("PROCESSO FINALIZADO")
    print(f"Confira a pasta: {OUTPUT_DIR}")
    print("="*40)

if __name__ == "__main__":
    main()