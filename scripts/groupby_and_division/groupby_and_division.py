import pandas as pd
import numpy as np

df = pd.DataFrame({
    'state': ['AA', 'BB', 'CC', 'DD'] * 3,
    'bene_1_count': [np.random.randint(10000, 99999) for _ in range(12)],
    'bene_2_count': [np.random.randint(10000, 99999) for _ in range(12)]})

teste_1 = df.groupby(['state']).agg(auxilio_total = ('bene_1_count', sum))              
teste_2 = df.groupby(['state']).apply(lambda x: x['bene_1_count'].sum() / x['bene_2_count'].sum())
teste_1['proporcao_beneficiada'] = teste_2.values

print(teste_1)