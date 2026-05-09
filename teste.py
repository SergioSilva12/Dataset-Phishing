import pandas as pd
import os

# Caminhos baseados na estrutura que criamos
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_TESTE = os.path.join(PASTA_ATUAL, "Dataset Fianl Splits", "test.csv")

def main():
    if not os.path.exists(CAMINHO_TESTE):
        print(f"Erro: Nao encontrei o arquivo em {CAMINHO_TESTE}")
        return

    # Carrega os dados
    df = pd.read_csv(CAMINHO_TESTE)

    print("\n" + "="*60)
    print("      VISUALIZACAO DO BENCHMARK (CONJUNTO DE TESTE)      ")
    print("="*60)

    # 1. Resumo Quantitativo
    print(f"\nTotal de URLs no Teste: {len(df)}")
    print("\nDistribuicao por Categoria:")
    dist = df['data_category'].value_counts()
    for cat, qtd in dist.items():
        porcentagem = (qtd / len(df)) * 100
        print(f" - {cat:22}: {qtd:6} ({porcentagem:.1f}%)")

    print("\n" + "-"*60)
    print("AMOSTRAS REAIS POR CATEGORIA")
    print("-"*60)

    # 2. Amostras de cada categoria
    categorias = ['legitimate', 'human_phishing', 'synthetic_adversarial']
    
    for cat in categorias:
        print(f"\n>>> CATEGORIA: {cat.upper()}")
        # Pegamos 3 exemplos aleatorios de cada uma
        amostra = df[df['data_category'] == cat].head(3)
        
        if amostra.empty:
            print(" (Nenhuma amostra encontrada)")
            continue

        for i, row in amostra.iterrows():
            print(f"\n URL: {row['url']}")
            print(f" Features -> Comprimento: {row['url_length']} | Entropia: {row['entropy']:.2f} | Subdominios: {row['num_subdomains']}")
            if cat == 'synthetic_adversarial':
                print(f" Metodo de IA: {row['augmentation_type']}")

    print("\n" + "="*60)
    print("Fim da Visualizacao")
    print("="*60)

if __name__ == "__main__":
    main()