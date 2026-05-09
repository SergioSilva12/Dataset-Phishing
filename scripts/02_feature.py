import pandas as pd
import math
from collections import Counter
from urllib.parse import urlparse

def shannon_entropy(data):
    """Calcula a complexidade/aleatoriedade da URL."""
    if not data: return 0
    entropy = 0
    for x in Counter(data).values():
        p_x = float(x) / len(data)
        entropy -= p_x * math.log(p_x, 2)
    return entropy

def extract_features(df):
    print("Engenharia de features em andamento...")
    df['domain'] = df['url'].apply(lambda x: urlparse(str(x)).netloc)
    df['url_length'] = df['url'].apply(lambda x: len(str(x)))
    df['entropy'] = df['url'].apply(shannon_entropy)
    df['has_ip'] = df['domain'].apply(lambda d: 1 if str(d).replace('.','').isnumeric() else 0)
    df['num_subdomains'] = df['domain'].apply(lambda d: str(d).count('.'))
    return df

print("⚙️ Carregando dados limpos...")
df_phish = pd.read_csv('01_phish_cleaned.csv')
df_legit = pd.read_csv('01_legit_cleaned.csv')

df_phish = extract_features(df_phish)
df_legit = extract_features(df_legit)

df_phish.to_csv('02_phish_features.csv', index=False)
df_legit.to_csv('02_legit_features.csv', index=False)
print("✅ Etapa 2 Concluída! Features matemáticas adicionadas.")