import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dsa210_merged_data.csv')

df['Manager_PPG'] = pd.to_numeric(df['PPG All Time'], errors='coerce')
h3_data = df[df['General Position'].isin(['Midfielder', 'Defender', 'Forward', 'Goalkeeper'])].dropna(subset=['Manager_PPG'])

groups = [h3_data[h3_data['General Position'] == pos]['Manager_PPG'] for pos in h3_data['General Position'].unique()]
f_stat, p_value = stats.f_oneway(*groups)

print(f"ANOVA F-statistic: {f_stat:.4f}")
print(f"ANOVA P-value: {p_value:.4f}")

midfielders = h3_data[h3_data['General Position'] == 'Midfielder']['Manager_PPG']
others = h3_data[h3_data['General Position'] != 'Midfielder']['Manager_PPG']
t_stat, p_val_ttest = stats.ttest_ind(midfielders, others)

print(f"Midfielders vs Others P-value: {p_val_ttest:.4f}")
print(f"Midfielder Avg PPG: {midfielders.mean():.2f}")
print(f"Others Avg PPG: {others.mean():.2f}")

plt.figure(figsize=(10, 6))
order = h3_data.groupby('General Position')['Manager_PPG'].median().sort_values(ascending=False).index

sns.boxplot(x='General Position', y='Manager_PPG', data=h3_data, order=order, palette='viridis')

plt.title(f'Hypothesis 3: Manager Performance by Player Position\n(Midfielders vs Others p={p_val_ttest:.4f})')
plt.ylabel('Average Points Per Game (PPG)')
plt.xlabel('Playing Position')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig('hypothesis3_clean_boxplot.png')
plt.show()
