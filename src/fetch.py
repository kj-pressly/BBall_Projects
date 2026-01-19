#this code fetches a specific players shot data from the nba api and returns it as a pandas dataframe 
import pandas as pd
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players

def get_playerID(playerName: str) -> int:
    
    player_dict = players.find_players_by_full_name(playerName)
    if player_dict:
        return player_dict[0]['id']
    else:
        raise ValueError(f"Player '{playerName}' not found.")
    
def get_playerShots(playerID: int, season: str = '2022-23', seasonType: str = 'Regular Season', teamID: int = 0) -> pd.DataFrame:
    
    shotchart = shotchartdetail.ShotChartDetail(
        team_id=teamID,
        player_id=playerID,
        season_type_all_star=seasonType,
        season_nullable=season
    )
    
    shots = shotchart.get_data_frames()[0]
    return shots

print(get_playerID("LeBron James"))
print(get_playerShots(2544))  # LeBron James' player ID is 2544
