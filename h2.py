import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dsa210_merged_data.csv')

df['Manager_Trophies'] = pd.to_numeric(df['Trophies'], errors='coerce').fillna(0)
df['Player_Trophies'] = pd.to_numeric(df['Trophies Won'], errors='coerce').fillna(0)

h2_data = df[['Player_Trophies', 'Manager_Trophies']].dropna()

correlation, p_value = stats.pearsonr(h2_data['Player_Trophies'], h2_data['Manager_Trophies'])

print(f"Correlation: {correlation:.4f}")
print(f"P-value: {p_value:.4f}")

plt.figure(figsize=(10, 6))
sns.regplot(x='Player_Trophies', y='Manager_Trophies', data=h2_data, 
            scatter_kws={'alpha':0.5, 'color': 'green'}, 
            line_kws={'color':'blue'})

plt.title(f'Hypothesis 2: Player Trophies vs Manager Trophies\n(r={correlation:.2f}, p={p_value:.4f})')
plt.xlabel('Number of Trophies Won as Player')
plt.ylabel('Number of Trophies Won as Manager')
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('hypothesis2_visual.png')
plt.show()
