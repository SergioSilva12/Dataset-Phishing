import pandas as pd

print("⚖️ Construindo Cenários Finais A e B...")
phish_train = pd.read_csv('03_phish_train.csv')
phish_val = pd.read_csv('03_phish_val.csv')
phish_test = pd.read_csv('03_phish_test.csv')
df_legit = pd.read_csv('02_legit_features.csv')

legit_idx = 0
def get_legit_slice(count):
    global legit_idx
    slice_df = df_legit.iloc[legit_idx : legit_idx + count].copy()
    legit_idx += count
    return slice_df

def build_scenario(phish_df, ratio_legit=1.0):
    count_phish = len(phish_df)
    count_legit = int(count_phish * ratio_legit)
    
    legit_df = get_legit_slice(count_legit)
    colunas = ['url', 'url_length', 'entropy', 'has_ip', 'num_subdomains', 'label']
    
    combined = pd.concat([phish_df[colunas], legit_df[colunas]])
    return combined.sample(frac=1, random_state=42).reset_index(drop=True)

# Cenário A (50% / 50%)
train_A = build_scenario(phish_train, 1.0)
val_A = build_scenario(phish_val, 1.0)
test_A = build_scenario(phish_test, 1.0)

# Cenário B (10% Phishing / 90% Legítimo) -> Só para Teste
test_B = build_scenario(phish_test, 9.0)

train_A.to_csv('FINAL_A_train.csv', index=False)
val_A.to_csv('FINAL_A_val.csv', index=False)
test_A.to_csv('FINAL_A_test.csv', index=False)
test_B.to_csv('FINAL_B_test_real.csv', index=False)
print("✅ Etapa 4 Concluída! Datasets prontos para treinamento.")