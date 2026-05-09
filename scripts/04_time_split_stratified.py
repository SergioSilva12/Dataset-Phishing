import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Caminhos
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV = os.path.join(PASTA_ATUAL, "Dataset Final com aug", "phishing_detection_benchmark.csv")
OUTPUT_DIR = os.path.join(PASTA_ATUAL, "Dataset Fianl Splits")

def main():
    if not os.path.exists(INPUT_CSV):
        print("[ERRO] Arquivo benchmark nao encontrado.")
        return

    df = pd.read_csv(INPUT_CSV)
    print(f"Dataset carregado com {len(df)} amostras.")

    # ==========================================================
    # DIVISAO ESTRATIFICADA (Garante categorias em todos os sets)
    # ==========================================================
    
    # 1. Separa 70% para Treino e 30% para o resto (Val + Teste)
    # O parametro 'stratify' e o segredo: ele olha a coluna data_category
    df_train, df_temp = train_test_split(
        df, 
        test_size=0.30, 
        random_state=42, 
        stratify=df['data_category'] 
    )

    # 2. Divide os 30% restantes ao meio (15% Val / 15% Teste)
    df_val, df_test = train_test_split(
        df_temp, 
        test_size=0.50, 
        random_state=42, 
        stratify=df_temp['data_category']
    )

    # Criar pasta de saida
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Salvar arquivos
    df_train.to_csv(os.path.join(OUTPUT_DIR, "train.csv"), index=False)
    df_val.to_csv(os.path.join(OUTPUT_DIR, "validation.csv"), index=False)
    df_test.to_csv(os.path.join(OUTPUT_DIR, "test.csv"), index=False)

    print("\n" + "="*40)
    print("DIVISAO ESTRATIFICADA CONCLUIDA")
    print("="*40)
    print(f"Treino:     {len(df_train)} amostras")
    print(f"Validacao:  {len(df_val)} amostras")
    print(f"Teste:      {len(df_test)} amostras")
    
    print("\nValidacao de Categoria no TREINO:")
    print(df_train['data_category'].value_counts(normalize=True).map(lambda n: f'{n:.2%}'))

if __name__ == "__main__":
    main()