import pandas as pd
import numpy as np
import random
import requests
import io
import zipfile
from urllib.parse import urlparse
import os

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

def normalize_url(url):
    """Remove parâmetros inúteis e padroniza a URL."""
    url = str(url).lower().strip()
    try:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    except:
        return url

print("📥 [1/2] Lendo e normalizando PhishTank...")
df_phish = pd.read_json('online-valid-organizado.json')
df_phish['submission_time'] = pd.to_datetime(df_phish['submission_time'])
df_phish['url'] = df_phish['url'].apply(normalize_url)
df_phish = df_phish.drop_duplicates(subset=['url'], keep='first')
df_phish['label'] = 1

print("📥 [2/2] Baixando e normalizando Tranco List (Legítimas)...")
url_tranco = "https://tranco-list.eu/top-1m.csv.zip"
r = requests.get(url_tranco)
z = zipfile.ZipFile(io.BytesIO(r.content))
df_legit = pd.read_csv(z.open('top-1m.csv'), names=['rank', 'url'])

df_legit['url'] = 'https://' + df_legit['url']
df_legit['url'] = df_legit['url'].apply(normalize_url)
df_legit = df_legit.drop_duplicates(subset=['url'], keep='first')

# Amostragem sem viés (Pegamos 3x o tamanho do phishing para ter margem nos cenários)
sample_size = len(df_phish) * 3
df_legit = df_legit.sample(n=sample_size, random_state=SEED)
df_legit['label'] = 0

# Salvando etapa 1
df_phish.to_csv('01_phish_cleaned.csv', index=False)
df_legit.to_csv('01_legit_cleaned.csv', index=False)
print("✅ Etapa 1 Concluída! Arquivos base salvos.")