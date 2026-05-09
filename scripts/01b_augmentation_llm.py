import pandas as pd
import random
from urllib.parse import urlparse, urlunparse
import re
import os


random.seed(42)

INPUT_FILE = "Dados intermediarios/01_phish_cleaned.csv"
OUTPUT_FILE = "Dados intermediarios/01_phish_synthetic_pipeline.csv"

QTD_SEMENTES = 200

def validar_url(url):
    """Valida se a URL gerada possui uma estrutura real e possível na web."""
    padrao = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(padrao, url) is not None

def aplicar_pipeline_adversarial(url_original):
    """Aplica mutações apenas no domínio, preservando a estrutura original da URL."""
    parsed = urlparse(url_original)
    netloc = parsed.netloc
    
    if not netloc:
        return []

    # Separação rudimentar do domínio para não depender de bibliotecas externas complexas
    partes = netloc.split('.')
    if len(partes) < 2:
        return []
    
    tld = partes[-1]
    sld = partes[-2]
    subdominio = ".".join(partes[:-2]) + "." if len(partes) > 2 else ""

    variacoes = []

    # Helper para montar a URL alterando apenas o netloc (Preserva paths e query)
    def montar_url(novo_netloc):
        return urlunparse((parsed.scheme or 'https', novo_netloc, parsed.path, parsed.params, parsed.query, parsed.fragment))

    # 1. Homóglifos (Substituição visual)
    substituicoes = {'a': '@', 'o': '0', 'i': '1', 'l': '1', 'e': '3', 's': '5', 'm': 'rn'}
    sld_mutado = sld
    for char, sub in substituicoes.items():
        if char in sld_mutado:
            sld_mutado = sld_mutado.replace(char, sub, 1)
            break
    if sld_mutado != sld:
        novo_netloc = f"{subdominio}{sld_mutado}.{tld}"
        variacoes.append((montar_url(novo_netloc), 'homoglyph'))

    # 2. Injeção de Subdomínio de Urgência (Muito realista)
    iscas = ['secure', 'auth', 'login', 'verify']
    isca_escolhida = random.choice(iscas)
    novo_netloc = f"{isca_escolhida}-{subdominio}{sld}.{tld}" if subdominio else f"{isca_escolhida}.{sld}.{tld}"
    variacoes.append((montar_url(novo_netloc), 'subdomain_injection'))

    # 3. Adição de Hífen no SLD (Typosquatting)
    iscas_hifen = ['-secure', '-login', '-support']
    isca_hifen = random.choice(iscas_hifen)
    novo_netloc = f"{subdominio}{sld}{isca_hifen}.{tld}"
    variacoes.append((montar_url(novo_netloc), 'hyphenation'))

    # 4. Omissão de caractere no SLD
    if len(sld) > 4:
        idx = random.randint(1, len(sld) - 2)
        sld_omitido = sld[:idx] + sld[idx+1:]
        novo_netloc = f"{subdominio}{sld_omitido}.{tld}"
        variacoes.append((montar_url(novo_netloc), 'omission'))

    # 5. Manipulação de TLD (Extensões maliciosas comuns)
    tlds_maliciosos = ['xyz', 'site', 'online', 'top']
    tld_mutado = random.choice(tlds_maliciosos)
    if tld != tld_mutado:
        novo_netloc = f"{subdominio}{sld}.{tld_mutado}"
        variacoes.append((montar_url(novo_netloc), 'tld_manipulation'))

    # Ponto 3: Retorna apenas URLs estruturalmente válidas
    return [(url, tipo) for url, tipo in variacoes if validar_url(url)]


def main():
    print(">>> Iniciando Synthetic Adversarial URL Generation Pipeline...")
    
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"Erro: Arquivo {INPUT_FILE} nao encontrado.")
        return

    df_amostra = df.sample(n=QTD_SEMENTES, random_state=42)
    dados_sinteticos = []

    for index, row in df_amostra.iterrows():
        url_original = row['url']
        variacoes = aplicar_pipeline_adversarial(url_original)
        
        for url_gerada, tipo_aumento in variacoes:
            # Ponto 4 e 5: Documentação rigorosa da origem e tipo do dado
            dados_sinteticos.append({
                'url': url_gerada,
                'label': 1,
                'is_synthetic': 1,
                'augmentation_type': tipo_aumento,
                'seed_url': url_original # Rastreabilidade extra para o paper
            })

    df_resultado = pd.DataFrame(dados_sinteticos)
    
    
    qtd_antes = len(df_resultado)
    df_resultado = df_resultado.drop_duplicates(subset=['url'])
    qtd_depois = len(df_resultado)
    
    print(f"    - Duplicatas removidas: {qtd_antes - qtd_depois}")

    df_resultado.to_csv(OUTPUT_FILE, index=False)
    
    print(f"\n>>> PIPELINE CONCLUÍDO COM SUCESSO!")
    print(f">>> {len(df_resultado)} URLs adversariais geradas, validadas e rotuladas.")
    print(f">>> Arquivo salvo em: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()