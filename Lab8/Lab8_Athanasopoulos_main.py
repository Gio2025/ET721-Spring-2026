"""
George Athanasopoulos
Feb 24, 2026
Lab 8, APIs
"""

import pandas as pd

# ----- Example 1: Dataframe using pandas -----
# STEP 1: data collection. dict_ as the static template of our API
dict_ = {
    'a': [11, 21, 31],
    'b': [12, 22, 32]
}

# STEP 2: Create a dataframe using pandas
df = pd.DataFrame(dict_)

# Head method of the dataframe communicates with the API displaying the first few rows of the dataframe

print("\n----- Example 1: Simple API -----")
print(df.head())

# Mean method calculates and returns the mean value of each row of the df
print(f"The mean value is = \n{df.mean()}")


# ----- Example 2: Get NBA team from static.py file -----
# STEP 1: Data collection
from static import get_teams
print("\n----- Example 2: Get NBA team from static file -----")

nba_teams = get_teams()
# testing
print(f"The first 2 teams: {nba_teams[0:2]}")

# STEP 2: Create dataframe
df_teams = pd.DataFrame(nba_teams)
print("\nAll Teams")
print(df_teams.head())

# STEP 3: Working with data in df_teams
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print('\nWarriors')
print(df_warriors)


# ----- Example 3: Working with external APIs -----
# STEP 1: Data collection
# a) Download the pickle file
import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
file_name = "Golden_state.pk1"

print(f"\nDownloading external file!...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download completed!")
else:
    print("Download failed!")

# STEP 2: Create dataframe
# b) Load dataframe from a pickle file
games = pd.read_pickle(file_name)
print(f"\nGames from pickle file")
print(games.head())

# STEP 3: Working with data in df_teams
# c) filter GSW vs Raptors
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains('vs')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]

# testing
print("\nGSW home games")
print(gsw_home_vs_raptors)

# d) Calculate the average of the home and away matches
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()

home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"GSW home average = {home_avg_plus}")
print(f"GSW away average = {away_avg_plus}")

# e) Visualization of data analysis
import matplotlib.pyplot as plt

metrics = ["PLUS_MINUS", "PTS"]
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar([i - bar_width/2 for i in x], home_values, width = bar_width, label = 'Home', color = 'skyblue')
plt.bar([i - bar_width/2 for i in x], away_values, width = bar_width, label = 'Away', color = 'orange')

plt.xticks(x, metrics)
plt.title("GSW vs Raptors")

plt.ylabel("Average Value")
plt.legend()
plt.show(block=True)

input("Press enter to close...")