# dsa210-football-manager-analysis
An analysis of the correlation between a football manager's playing career and their managerial success for my courseDSA 210.
DSA 210 Project Proposal: Can we figure out a players success as a football manager before even they start? An Analysis of How Football Playing Careers Affect Managerial Outcomes 
Data Frame: Managers that are active during 2025 and managed a club from Europa's top 10 leagues.

Motivation: For people around me, football is more than just a sport; it's a part of our lives and a constant topic of debate. A belief we've always shared is that iconic players we grew up with, like Arda Turan, Atiba Hutchinson, and Alex de Souza, would naturally become great managers to our beloved teams. We assumed their great footballing careers and the impact they had on their clubs would directly translate to success from the start. But is this really the case? This project was born from that simple question. Is there a solid correlation between a successful playing career and a successful managerial one, or is it just an idea fueled by a few exceptions like Zidane? Furthermore, the debate often gets more specific. Many people I know are convinced that a player's position is a key factor, arguing that great midfielders, with their on-field vision, are destined to make better coaches. The purpose of this project is to reject or solidify these opinions. By collecting and analyzing career data, My project aims to figure out whether the data supports these claims and to find an answer to these questions.

Data Sources: The data for this project will be collected manually from publicly available online football statistics databases. The core of this project relies on creating a unified dataset that combines a manager's statistics from both their playing and coaching careers.

Primary Data: Managerial Career Statistics The primary data will focus on the managerial careers of individuals and will be sourced mainly from Sofascore. This platform provides comprehensive and well-structured data on coaching careers. I also will use footystats to make sure. Source: https://www.sofascore.com https://footystats.org

Metrics to Collect: Clubs managed and tenure dates, Career win percentage, Average points-per-game (PPG), Trophies and honors won as a manager, Managerial years Job Stabilty(e.g., How many times did they got sacked) etc.

Enriching Data: Playing Career Statistics To enrich the managerial data, I will collect the some important playing career statistics for each individual in the dataset. This will allow for a direct analysis of the correlation between playing and coaching success. These stats will be sourced from Transfermarkt, Playmakerstats and Fbref. Sources: https://www.transfermarkt.com, https://www.playmakerstats.com https://fbref.com

Metrics to Collect: The player's primary and detailed positions (e.g., Midfielder(Number 6), Defender(Right-back)), Total number of official appearances, Career goal conturbutions, Trophies and honors won as a player, The competitive level of the clubs they played for, The League and Clubs that they played for etc.

By merging these two datasets, I will create a complete profile for each person, enabling the analysis required to answer the project's core questions.

Data Analysis: Analytical methods will be used to investigate the relationship between a manager's playing career and their coaching success. The analysis is divided into two main stages: exploratory analysis with hypothesis testing, followed by the implementation of machine learning models.

Exploratory Data Analysis and Hypothesis: Testing The initial phase will focus on cleaning the data, exploring it visually, and testing core assumptions.

Player-Manager Correlation Analysis: I will create scatter plots and correlation matrices to visualize the relationship between key player metrics (e.g., goals scored, number of appearances, trophies won) and managerial success metrics (e.g., career win percentage, points-per-game). This will provide an initial answer to whether successful players tend to become successful managers.

Positional Impact Comparison: To investigate the common belief that certain positions produce better managers, I will use box plots to compare the distributions of managerial win percentages across different playing positions (Defenders, Midfielders, Forwards).

Hypothesis Testing: I will conduct a formal hypothesis test to determine if observed differences are statistically significant. For example: Null Hypothesis (H₀): There is no significant difference in the mean career win percentage between managers who played as midfielders and managers who played in other positions.

Machine Learning Implementation The primary analytical goal is to predict the possibility of a players chance of being succsesfull as a manager based on their career stats using supervised and unsupervised machine learning methods.

Findings Expected Findings: I expect to find that a midfield with a lot of appearences who did not changed a lot of clubs and played mainly in tactical leagues such as Serie A or La Liga to be a better manager than others. However i dont think career goals and trophies won as a player would affect the managerial sucsess.

Limitations and Future Work

Limitations: There is a lot of other factors that affects such as work ethic. This can outshine the data from their player careers which would result in a data analysis that doesnt tell anything. Also comparing 'sucsess' will be hard for teams that does not share a common goal. For example We can't say that a coach which has 1.8 ppg which coaches a big club is better than a manager with 1.5 ppg that manages a relegetion contender. 
Future Work: The model could be extended to find the coaches that has the highest possibility of sucsess for a given team. This can help the teams which are desprate need of sucsesfull coaches.
