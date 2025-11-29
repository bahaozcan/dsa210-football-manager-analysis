# DSA 210 Project
# An analysis of the correlation between a football manager's playing career and their managerial success for DSA 210.

DSA 210 Project Proposal: Can we figure out a players success as a football manager before even they start? This project aims to collect data from both managerial and footballing careers of football coaches.

Data Frame: Managers that are active during 2024-25 season and managed a club from Europe's top 10 leagues.

# Motivation
For people around me, football is more than just a sport; it's a part of our lives and a constant topic of debate. A belief we've always shared is that iconic players we grew up with, like Arda Turan, Atiba Hutchinson, and Alex de Souza, would naturally become great managers to our beloved teams. We assumed their great footballing careers and the impact they had on their clubs would directly translate to success from the start. But is this really the case? This project was born from that simple question. Is there a solid correlation between a successful playing career and a successful managerial one, or is it just an idea fueled by a few exceptions like Zidane? 

Furthermore, the debate often gets more specific. Many people I know are convinced that a player's position is a key factor, arguing that great midfielders, with their on-field vision, are destined to make better coaches. The purpose of this project is to reject or solidify opinions like these. By collecting and analyzing career data, My project aims to figure out whether the data supports these claims and to find an answer to these questions.

# Data Sources
The data for this project will be collected from publicly available online football statistics databases. The core of this project relies on creating a unified dataset that combines a manager's statistics from both their playing and coaching careers.

Primary Data

Managerial Career Statistics The primary data will focus on the managerial careers of individuals and will be sourced from Sofascore. This platform provides comprehensive and well-structured data on coaching careers. 

Source: https://www.sofascore.com 

Metrics to Collect: Clubs managed, Career win percentage, Average points-per-game (PPG), Number of trophies and honors won as a manager, Managerial years.

Enriching Data

Player Career Statistics To enrich the managerial data, I will collect the some important playing career statistics for each individual in the dataset. This will allow for a direct analysis of the correlation between playing and coaching success. These stats will be sourced from Transfermarkt 

Source: https://www.transfermarkt.com

Metrics to Collect: The player's positions, Total number of official appearances, Career goals, Number of trophies and honors won as a player, The League that they played for the most.

By merging these two datasets, I will create a complete profile for each person, enabling the analysis required to answer the project's core questions.

# Hypothesis and Results

# Hypothesis 1: Managers who won trophies as players are more successful managers.

Null Hypothesis: There is no correlation between number of throphies won as player and PPG as managers.

Result: Rejected H0 (p = 0.007, Correlation = +0.20).

Analysis: The data reveals a statistically significant positive link between a player's trophies and their managerial success. This suggests that "winning" is a important skill; players exposed to championship environments internalize the standards required to replicate that success in the sideline. 

# Hypothesis 2: Players who won trophies will continue to win trophies as managers.

Null Hypothesis: There is no correlation between number of thropies won as player and as manager.

Result: Rejected H0 (p < 0.01, Strong Positive Correlation).

Analysis: This indicates elite clubs hire former winners (Probably former superstars of their history like Zidane for Real Madrid), placing them in a better position to win managerial titles immediately.

# Hypothesis 3: Midfielders perform better as managers than other positions.

Null Hypothesis: There is no correlation between position and managerial success.

Result: Rejected H0 (p = 0.006).

Analysis: Former Midfielders achieved a significantly higher average PPG (1.63) compared to Goalkeepers (1.42), Defenders (1.53) and Forwards (1.52). This supports the theory that the midfield role—which requires highest tactical capacity is the best preparation for coaching.

# Hypothesis 4: Playing in top-tier leagues provides a better managerial foundation.

Null Hypothesis: There is no correlation with the players most played league and their managerial success.

Result:  Rejected H0 (p = 0.011).

Analysis: Managers who spent their playing careers mostly in the Top 5 Leagues (England, Spain, Italy, Germany, France) significantly outperformed those from smaller leagues. This implies that exposure to elite tactical systems and high-pressure environments helps a lot when developing coaching skills.

# Hypothesis 5: More games played as a player leads to a longer, more stable managerial career.

Null Hypothesis: There is no correlation between player appearances and their job stability as managers.

Result : Failed to reject H0 (p = 0.69)

Analysis: Career longevity as a player does not predict job stabilty as a manager. A player with 500 appearances is just as likely to be fired quickly as a player with less appearances, proving that management requires a completely different skillset than playing durability.

# Hypothesis 6: Players who adopted to more clubs makes better managers.

Null Hypothesis: There is no correlation between the number of clubs a player played for and their managerial success

Result: Failed to Reject H0 (p = 0.21).

Analysis: Adaptability as a player does not predict managerial success. The data shows that players who changed clubs more often does not perform better than the players with less. This suggests that the ability to adapt to new clubs as a player is a different skill set than being successfull as a manager.

# Limitations

PPG and Thropies won is not enough for a analysis to figure out if a manager is successfull or not. There are lot of factors within the football that makes it harder to frame a manager as succsessfull or not.
