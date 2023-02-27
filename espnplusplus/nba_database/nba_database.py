from multiprocessing.dummy import active_children
import nba_api.stats.static.teams as nba_teams
import nba_api.stats.static.players as nba_players
from nba_api.stats.endpoints import playercareerstats

from mysql_handler import MySQLHandler
import nba_schema

player_season_stats_columns = {
    'PLAYER_ID'  : 'player_id',
    'SEASON_ID'  : 'season_id',
    'TEAM_ID'    : 'team_id',
    'PLAYER_AGE' : 'player_age',
    'GP'         : 'games_played',
    'GS'         : 'games_started',
    'MIN'        : 'minutes_played',
    'FGM'        : 'field_goals_made',
    'FGA'        : 'field_goals_attempted',
    'FG_PCT'     : 'field_goal_percentage',
    'FG3M'       : 'three_pointers_made',
    'FG3A'       : 'three_pointers_attempted',
    'FG3_PCT'    : 'three_pointer_percentage',
    'FTM'        : 'free_throws_made',
    'FTA'        : 'free_throws_attempted',
    'FT_PCT'     : 'free_throw_percentage',
    'OREB'       : 'offensive_rebounds',
    'DREB'       : 'defensive_rebounds',
    'REB'        : 'rebounds',
    'AST'        : 'assists',
    'STL'        : 'steals',
    'BLK'        : 'blocks',
    'TOV'        : 'turnovers',
    'PF'         : 'personal_fouls',
    'PTS'        : 'points'
}

def create_teams_table(handler: MySQLHandler) -> None:
    table_name = 'teams'
    table_description = nba_schema.TABLES[table_name]
    handler.create_table(table_name, table_description)
    teams = nba_teams.get_teams()
    for team in teams:
        handler.insert_data(table_name, team, team['full_name'])
    handler.commit()

def create_players_table(handler: MySQLHandler) -> None:
    table_name = 'players'
    table_description = nba_schema.TABLES[table_name]
    handler.create_table(table_name, table_description)
    active_players = nba_players.get_active_players()
    for player in active_players:
        handler.insert_data(table_name, player, player['full_name'])
    handler.commit()

def create_player_season_stats_table(hander: MySQLHandler) -> None:
    table_name = 'player_season_stats'
    table_description = nba_schema.TABLES[table_name]
    handler.create_table(table_name, table_description)
    active_players = nba_players.get_active_players()
    for player in active_players:
        player_career_stats = playercareerstats.PlayerCareerStats(player_id = player['id'])
        player_career_stats_dict = player_career_stats.get_normalized_dict()['SeasonTotalsRegularSeason']
        for player_season_stats_dict in player_career_stats_dict:
            player_season_stats_row = change_dict_keys(player_season_stats_dict, player_season_stats_columns)
            handler.insert_data(table_name, player_season_stats_row, f"{player['full_name']}, {player_season_stats_dict['SEASON_ID']}, {player_season_stats_dict['TEAM_ABBREVIATION']}")
    handler.commit()

def change_dict_keys(dictionary: dict, old_to_new_keys: dict) -> dict:
    return dict((old_to_new_keys[key], value) for (key, value) in dictionary.items() if key in old_to_new_keys)

if(__name__ == '__main__'):
    handler = MySQLHandler(
        host = 'localhost',
        user = 'root',
        password = '1234'
    )
    handler.drop_database('nba')
    handler.close()

    handler = MySQLHandler(
        host = 'localhost',
        user = 'root',
        password = '1234',
        autocommit = False
    )

    handler.use_database(nba_schema.DB_NAME)

    create_teams_table(handler)
    create_players_table(handler)
    create_player_season_stats_table(handler)

    handler.close()
