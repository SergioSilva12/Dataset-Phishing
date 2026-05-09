import pandas as pd
import math
import re
from urllib.parse import urlparse
import os

INPUT_FILE = "Dados intermediarios/01_phish_synthetic_pipeline.csv"
OUTPUT_FILE = "Dados intermediarios/02_phish_synthetic_features.csv"

def shannon_entropy(string):
    """Calcula a entropia da string"""
    if not string:
        return 0
    entropy = 0
    for x in set(string):
        p_x = float(string.count(x)) / len(string)
        entropy += - p_x * math.log(p_x, 2)
    return entropy

def tem_ip_no_dominio(netloc):
    """Verifica se o domínio é um endereço IP (ex: 192.168.1.1)"""
    padrao_ip = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    return 1 if padrao_ip.search(netloc) else 0

def contar_subdominios(netloc):
    """Estima o número de subdomínios (contando os pontos no domínio)"""
    # Ex: www.login.banco.com.br tem 4 pontos. 
    return netloc.count('.')

def extract_selected_features(row):
    """Extrai estritamente as features solicitadas"""
    url = str(row['url'])
    parsed = urlparse(url)
    dominio = parsed.netloc
    
    features = {
        # Dados de Rastreabilidade (Para controle, você pode dropar antes de treinar)
        'url': url,
        'domain': dominio,
        'label': row['label'],
        'is_synthetic': row['is_synthetic'],
        'augmentation_type': row['augmentation_type'],
        'seed_url': row.get('seed_url', ''), 
        
        # Features Matemáticas para o Machine Learning
        'url_length': len(url),
        'entropy': shannon_entropy(url),
        'has_ip': tem_ip_no_dominio(dominio),
        'num_subdomains': contar_subdominios(dominio)
    }
    
    return pd.Series(features)

def main():
    print(">>> Iniciando a Extração das Features Selecionadas...")
    
    try:
        df_synthetic = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"[!] Erro: Arquivo {INPUT_FILE} não encontrado.")
        return
        
    df_features = df_synthetic.apply(extract_selected_features, axis=1)
    df_features.to_csv(OUTPUT_FILE, index=False)
    
    print(">>> EXTRAÇÃO CONCLUÍDA!")
    print(f">>> Arquivo salvo em: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()