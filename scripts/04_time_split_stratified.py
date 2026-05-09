import pandas as pd
import os

# Pega o caminho da pasta onde este script esta salvo
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Define o caminho do dataset mestre gerado no passo 03
INPUT_CSV = os.path.join(PASTA_ATUAL, "Dataset_Final_TCC", "phishing_detection_benchmark.csv")

# Define a pasta de destino para os splits
OUTPUT_DIR = os.path.join(PASTA_ATUAL, "Dataset_Splits_TCC")

def main():
    print(f"Lendo benchmark em: {INPUT_CSV}")
    
    if not os.path.exists(INPUT_CSV):
        print("[ERRO] O arquivo benchmark nao foi encontrado. Rode o script 03 primeiro.")
        return

    # Carrega o dataset mantendo a ordem original (importante para o time split)
    df = pd.read_csv(INPUT_CSV)
    total_linhas = len(df)
    
    print(f"[OK] Dataset carregado: {total_linhas} amostras.")

    # 1. Definição dos pontos de corte (70% | 15% | 15%)
    indice_treino = int(total_linhas * 0.70)
    indice_val = int(total_linhas * 0.85) # 70% + 15%

    # 2. Divisao Temporal (Sem shuffle global antes do corte)
    df_train = df.iloc[:indice_treino].copy()
    df_val = df.iloc[indice_treino:indice_val].copy()
    df_test = df.iloc[indice_val:].copy()

    # 3. Embaralhamento (Shuffle) apenas dentro do conjunto de TREINO
    # Isso ajuda o modelo a convergir sem vazar informacao do futuro (val/teste)
    df_train = df_train.sample(frac=1, random_state=42).reset_index(drop=True)

    # Cria a pasta de saida
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 4. Salvamento dos arquivos
    df_train.to_csv(os.path.join(OUTPUT_DIR, "train.csv"), index=False)
    df_val.to_csv(os.path.join(OUTPUT_DIR, "validation.csv"), index=False)
    df_test.to_csv(os.path.join(OUTPUT_DIR, "test.csv"), index=False)

    # 5. Relatorio de Integridade para o Artigo
    print("\n" + "="*40)
    print("DIVISAO TEMPORAL CONCLUIDA")
    print("="*40)
    print(f"Treino (70%):     {len(df_train)} amostras")
    print(f"Validacao (15%):  {len(df_val)} amostras")
    print(f"Teste (15%):      {len(df_test)} amostras")
    print("-" * 40)
    print(f"Arquivos salvos em: {OUTPUT_DIR}")
    
    # Verifica se a coluna de classificacao esta correta no teste (Sua ideia!)
    print("\nDistribuicao de categorias no conjunto de TESTE:")
    print(df_test['data_category'].value_counts())

if __name__ == "__main__":
    main()