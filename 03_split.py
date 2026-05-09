import pandas as pd

print("🛡️ Aplicando Domain-Aware Temporal Split no Phishing...")
df_phish = pd.read_csv('02_phish_features.csv')

# Converte data de volta
df_phish['submission_time'] = pd.to_datetime(df_phish['submission_time'])

# Estatísticas por domínio
domain_stats = df_phish.groupby('domain').agg(
    first_seen=('submission_time', 'min'),
    url_count=('url', 'count')
).sort_values(by='first_seen')

domain_stats['cumulative_urls'] = domain_stats['url_count'].cumsum()
total_urls = domain_stats['url_count'].sum()

p_70 = int(total_urls * 0.70)
p_85 = int(total_urls * 0.85)

def assign_split(cum_urls):
    if cum_urls <= p_70: return 'train'
    elif cum_urls <= p_85: return 'val'
    else: return 'test'

domain_stats['split'] = domain_stats['cumulative_urls'].apply(assign_split)
df_phish = df_phish.merge(domain_stats[['split']], left_on='domain', right_index=True)

phish_treino = df_phish[df_phish['split'] == 'train'].drop(columns=['split'])
phish_val = df_phish[df_phish['split'] == 'val'].drop(columns=['split'])
phish_teste = df_phish[df_phish['split'] == 'test'].drop(columns=['split'])

phish_treino.to_csv('03_phish_train.csv', index=False)
phish_val.to_csv('03_phish_val.csv', index=False)
phish_teste.to_csv('03_phish_test.csv', index=False)
print("✅ Etapa 3 Concluída! Isolamento temporal garantido.")