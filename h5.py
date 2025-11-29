import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dsa210_merged_data.csv')

df['Player_Apps'] = pd.to_numeric(df['Apps'], errors='coerce')
df['Manager_Years'] = pd.to_numeric(df['Total Years'], errors='coerce')

h5_data = df.dropna(subset=['Player_Apps', 'Manager_Years'])

correlation, p_value = stats.pearsonr(h5_data['Player_Apps'], h5_data['Manager_Years'])

print(f"Correlation: {correlation:.4f}")
print(f"P-value: {p_value:.4f}")

plt.figure(figsize=(10, 6))
sns.regplot(x='Player_Apps', y='Manager_Years', data=h5_data, 
            scatter_kws={'alpha':0.5, 'color': 'purple'}, 
            line_kws={'color':'orange'})

plt.title(f'Hypothesis 5: Player Appearances vs Manager Career Stability\n(r={correlation:.2f}, p={p_value:.4f})')
plt.xlabel('Total Matches Played as Player')
plt.ylabel('Total Years as Manager')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('hypothesis5_visual.png')
plt.show()
