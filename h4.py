import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dsa210_merged_data.csv')

df['Manager_PPG'] = pd.to_numeric(df['PPG All Time'], errors='coerce')
df = df.dropna(subset=['League Played Most', 'Manager_PPG'])
df['League Name'] = df['League Played Most'].astype(str)

league_counts = df['League Name'].value_counts()
valid_leagues = league_counts[league_counts >= 5].index
df_filtered = df[df['League Name'].isin(valid_leagues)]

groups = [df_filtered[df_filtered['League Name'] == league]['Manager_PPG'] for league in valid_leagues]
f_stat, p_value = stats.f_oneway(*groups)

print(f"ANOVA P-value: {p_value:.4f}")
print("\nAverage PPG by League:")
print(df_filtered.groupby('League Name')['Manager_PPG'].mean().sort_values(ascending=False))

plt.figure(figsize=(12, 8))
order = df_filtered.groupby('League Name')['Manager_PPG'].median().sort_values(ascending=False).index

sns.boxplot(x='League Name', y='Manager_PPG', data=df_filtered, order=order, palette='viridis')

plt.title(f'Manager Success by Player Career League\n(ANOVA p={p_value:.4f})')
plt.ylabel('Average Points Per Game (PPG)')
plt.xlabel('League Played Most')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('hypothesis4_league_by_league.png')
plt.show()
