import pandas as pd
import os

manager_files = [
    "DSA dataseti.xlsx - Premier League.csv", 
    "DSA dataseti.xlsx - La Liga.csv",
    "DSA dataseti.xlsx - Bundesliga.csv", 
    "DSA dataseti.xlsx - Serie A.csv",
    "DSA dataseti.xlsx - Ligue 1.csv", 
    "DSA dataseti.xlsx - Eredivisie.csv",
    "DSA dataseti.xlsx - Primeira Liga.csv", 
    "DSA dataseti.xlsx - Pro League.csv",
    "DSA dataseti.xlsx - Süper Lig.csv", 
    "DSA dataseti.xlsx - Czech First League.csv"
]

player_files = [
    "DSA Kariyer dataseti.xlsx - Premier League.csv", 
    "DSA Kariyer dataseti.xlsx - La Liga.csv",
    "DSA Kariyer dataseti.xlsx - Bundesliga.csv", 
    "DSA Kariyer dataseti.xlsx - Serie A.csv",
    "DSA Kariyer dataseti.xlsx - Ligue 1.csv", 
    "DSA Kariyer dataseti.xlsx - Eredevise.csv",
    "DSA Kariyer dataseti.xlsx - Primeria Liga.csv",
    "DSA Kariyer dataseti.xlsx - Pro League.csv",
    "DSA Kariyer dataseti.xlsx - Süper Lig.csv", 
    "DSA Kariyer dataseti.xlsx - Czech First League.csv"
]

def load_and_combine(file_list):
    df_list = []
    for file in file_list:
        if os.path.exists(file):
            temp_df = pd.read_csv(file)
            df_list.append(temp_df)
    
    if df_list:
        return pd.concat(df_list, ignore_index=True)
    return pd.DataFrame()

df_manager = load_and_combine(manager_files)
df_player = load_and_combine(player_files)

df_manager.columns = df_manager.columns.str.strip()
df_player.columns = df_player.columns.str.strip()

df_manager['Name'] = df_manager['Name'].astype(str).str.strip()
df_player['Name'] = df_player['Name'].astype(str).str.strip()

combined_df = pd.merge(df_manager, df_player, on='Name', how='inner', suffixes=('_manager', '_player'))

combined_df.to_csv("dsa210_merged_data.csv", index=False)
print(f"Merged {len(combined_df)} records.")
