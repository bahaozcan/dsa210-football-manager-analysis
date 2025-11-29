import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dsa210_merged_data.csv')

df['Player_Clubs_Count'] = pd.to_numeric(df['No. of Clubs'], errors='coerce')
df['Manager_PPG'] = pd.to_numeric(df['PPG All Time'], errors='coerce')

h6_data = df.dropna(subset=['Player_Clubs_Count', 'Manager_PPG'])

correlation, p_value = stats.pearsonr(h6_data['Player_Clubs_Count'], h6_data['Manager_PPG'])

print(f"Correlation: {correlation:.4f}")
print(f"P-value: {p_value:.4f}")

plt.figure(figsize=(10, 6))
sns.regplot(x='Player_Clubs_Count', y='Manager_PPG', data=h6_data, 
            scatter_kws={'alpha':0.5, 'color': 'brown'}, 
            line_kws={'color':'blue'})

plt.title(f'Hypothesis 6: Number of Clubs Played For vs Manager PPG\n(r={correlation:.2f}, p={p_value:.4f})')
plt.xlabel('Number of Clubs Played For')
plt.ylabel('Manager Career PPG')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('hypothesis6_visual.png')
plt.show()
