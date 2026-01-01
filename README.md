# DSA 210 Project
## An analysis of the correlation between a football manager's playing career and their managerial success for DSA 210.

DSA 210 Project Proposal: Can we figure out a players success as a football manager before even they start? This project aims to collect data from both managerial and footballing careers of football coaches.

Data Frame: Managers that are active during 2024-25 season and managed a club from Europe's top 10 leagues.

# Motivation
For people around me, football is more than just a sport; it's a part of our lives and a constant topic of debate. A belief we've always shared is that iconic players we grew up with, like Arda Turan, Atiba Hutchinson, and Alex de Souza, would naturally become great managers to our beloved teams. We assumed their great footballing careers and the impact they had on their clubs would directly translate to success from the start. But is this really the case? This project was born from that simple question. Is there a solid correlation between a successful playing career and a successful managerial one, or is it just an idea fueled by a few exceptions like Zidane? 

Furthermore, the debate often gets more specific. Many people I know are convinced that a player's position is a key factor, arguing that great midfielders, with their on-field vision, are destined to make better coaches. The purpose of this project is to reject or solidify opinions like these. By collecting and analyzing career data, My project aims to figure out whether the data supports these claims and to find an answer to these questions.

# Data Sources
The data for this project will be collected from publicly available online football statistics databases. The core of this project relies on creating a unified dataset that combines a manager's statistics from both their playing and coaching careers.

## Primary Data

Managerial Career Statistics The primary data will focus on the managerial careers of individuals and will be sourced from Sofascore. This platform provides comprehensive and well-structured data on coaching careers. 

Source: https://www.sofascore.com 

Metrics to Collect: Clubs managed, Career win percentage, Average points-per-game (PPG), Number of trophies and honors won as a manager, Managerial years.

## Enriching Data

Player Career Statistics To enrich the managerial data, I will collect the some important playing career statistics for each individual in the dataset. This will allow for a direct analysis of the correlation between playing and coaching success. These stats will be sourced from Transfermarkt 

Source: https://www.transfermarkt.com

## Metrics to Collect 

The player's positions, Total number of official appearances, Career goals, Number of trophies and honors won as a player, The League that they played for the most.

By merging these two datasets, I will create a complete profile for each person, enabling the analysis required to answer the project's core questions.

# Hypothesis and Results

## Hypothesis 1: Managers who won trophies as players are more successful managers.

Null Hypothesis: There is no correlation between number of throphies won as player and PPG as managers.

Result: Rejected H0 (p = 0.006, Correlation = +0.20).

Analysis: The data reveals a statistically significant positive link between a player's trophies and their managerial success. This suggests that "winning" is a important skill; players exposed to championship environments internalize the standards required to replicate that success on the sideline. 

## Hypothesis 2: Players who won trophies will continue to win trophies as managers.

Null Hypothesis: There is no correlation between number of tropies won as player and as manager.

Result: Rejected H0 (p < 0.01, Strong Positive Correlation).

Analysis: This indicates elite clubs hire former winners (Probably former superstars of their history like Zidane for Real Madrid), placing them in a better position to win managerial titles immediately.

## Hypothesis 3: Midfielders perform better as managers than other positions.

Null Hypothesis: There is no correlation between position and managerial success.

Result: Rejected H0 (p = 0.003).

Analysis: Former Midfielders achieved a significantly higher average PPG (1.63) compared to Goalkeepers (1.42), Defenders (1.53) and Forwards (1.52). This supports the theory that the midfield role—which requires highest tactical capacity is the best preparation for coaching.

## Hypothesis 4: Playing in top-tier leagues provides a better managerial foundation.

Null Hypothesis: There is no correlation with the players most played league and their managerial success.

Result:  Rejected H0 (p = 0.05).

Analysis: Managers who spent their playing careers mostly in the Top 5 Leagues (England, Spain, Italy, Germany, France) significantly outperformed those from smaller leagues. This implies that exposure to elite tactical systems and high-pressure environments helps a lot when developing coaching skills.

## Hypothesis 5: More games played as a player leads to a longer, more stable managerial career.

Null Hypothesis: There is no correlation between player appearances and their job stability as managers.

Result : Failed to reject H0 (p = 0.40)

Analysis: Career longevity as a player does not predict job stabilty as a manager. A player with 500 appearances is just as likely to be fired quickly as a player with less appearances, proving that management requires a completely different skillset than playing durability.

## Hypothesis 6: Players who adopted to more clubs makes better managers.

Null Hypothesis: There is no correlation between the number of clubs a player played for and their managerial success.

Result: Failed to Reject H0 (p = 0.27).

Analysis: Adaptability as a player does not predict managerial success. The data shows that players who changed clubs more often does not perform better than the players with less. This suggests that the ability to adapt to new clubs as a player is a different skill set than being successful as a manager.

# Machine Learning

To move beyond simple correlations, I implemented three distinct machine learning approaches to categorize managers based on their playing history, classify them into "Elite" vs. "Average" tiers, and attempt to predict their exact Points Per Game (PPG).

## Part 1: Unsupervised Learning (Finding the Archetypes)
Goal: To identify if there are natural "groupings" or profiles of managers based on their playing careers, without strictly labeling them as successful or not. Method: K-Means Clustering.Features Used: Player Appearances, Trophies Won, Number of Clubs Played For.Result: The algorithm identified 4 distinct clusters:

Cluster 0 (Average Players): ~427 Apps, ~3 Trophies. Primarily Midfielders. They are the largest group (53 managers) with a solid average PPG of 1.59.

Cluster 1 (The Legends): ~544 Apps, ~16 Trophies. These are the superstars. This group had the highest managerial PPG (1.70), supporting the idea that great players can become great managers. 

Cluster 2 (The Journeymen): ~304 Apps, ~1.5 Trophies. Often Forwards. This group had the lowest average managerial success (PPG 1.48).

Cluster 3 (The Low-Profile Players): ~176 Apps, <1 Trophy. Despite the lack of playing fame, they performed surprisingly well (PPG 1.56), outperforming the Journeymen.

## Part 2: Supervised Learning (Classification)
Goal: To build a model that can predict whether a current player will become an "Elite" manager (defined as having a PPG above the median). Method: Decision Tree Classifier. Input Features: Player Apps, Trophies Won, Number of Clubs, and Playing Position. Result: The model achieved a accuracy of 72%.  The alltough the accuracy seems promosing, It does not show us the full picture. The model relies heavily on "Experience" (Apps), but as the Live Demo showed, this creates a major blind spot. 

## Part 3: Regression Challenge (Predicting Exact PPG)
Goal: To see if we could predict a manager's exact PPG using a Random Forest Regressor.Result: The model achieved an R^2 Score of -0.19. Analysis: A negative score confirms that predicting exact managerial PPG based solely on playing stats is impossible. The variance is too high, suggesting that coaching success depends on factors outside the pitch (leadership, tactical study, club resources).

## Part 4: Testing
Goal: To validate the model against real-world examples and active players. I tested 24 specific names. Result: The model achieved 62.5% Accuracy. What we learned from the failures: The model displayed two distinct biases: The "Legend Bias" (False Positives): It incorrectly predicted Wayne Rooney, Steven Gerrard, Andrea Pirlo, and Diego Maradona as ELITE. Why? Because they had massive playing stats (High Apps + High Trophies). The model assumed their playing greatness would translate to management, but in reality, it did not.The "Underdog Blind Spot" (False Negatives): It incorrectly predicted managers like Jorge Jesus as AVERAGE. Why? Because these managers had average or short playing careers (Low Apps). The model penalized them for not being "famous" players, completely missing their tactical genius. Conclusion: The machine learning analysis proves that while "Legendary Players" (Cluster 1) have a slightly higher ceiling, mainly because they have usually manage elite teams. The model cannot identify the "Student of the Game"—the low-profile player who becomes a world-class tactician.

# Limitations and Future Work

The primary metric for success, Points Per Game (PPG), is mostly dependent on the strength of the club. A manager achieving 1.4 PPG with a relegation-threatened team, might be "Elite," while a manager achieving 1.8 PPG with a top team might be underperforming. Our model treats raw PPG as the absolute truth, which penalizes overachieving managers at smaller clubs.
##

Football management relies heavily on leadership, tactical innovation, and crisis management—qualities that do not appear in a spreadsheet. The model failed to predict "Tactical Geniuses"  because their genius lies in their brains, not in their playing stats.
##

The dataset consists of managers currently active in top leagues. It excludes thousands of failed managers, which may skew the results to make it look like "Great Players" succeed more often than they actually do. Because usually most of the elite managers give a chance at coaching, but few stays after some time.
##

Instead of raw PPG, we should calculate "Performance vs. Expected"—comparing a manager's results against their club's wage bill or squad market value. This would correctly identify managers who outperform their budget.
##

Including data from the last 30 years (rather than just current managers) would increase the sample size and help the machine learning model find more stable patterns.
