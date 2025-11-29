import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dsa210_merged_data.csv')

df['Player_Trophies'] = pd.to_numeric(df['Trophies Won'], errors='coerce').fillna(0)
df['Manager_PPG'] = pd.to_numeric(df['PPG All Time'], errors='coerce')

h1_data = df.dropna(subset=['Player_Trophies', 'Manager_PPG'])

correlation, p_value = stats.pearsonr(h1_data['Player_Trophies'], h1_data['Manager_PPG'])

print(f"Correlation: {correlation:.4f}")
print(f"P-value: {p_value:.4f}")

plt.figure(figsize=(10, 6))
sns.regplot(x='Player_Trophies', y='Manager_PPG', data=h1_data, 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title(f'Hypothesis 1: Player Trophies vs Manager PPG\n(r={correlation:.2f}, p={p_value:.4f})')
plt.xlabel('Number of Trophies Won as Player')
plt.ylabel('Manager Career PPG')
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('hypothesis1_visual.png')
plt.show()
