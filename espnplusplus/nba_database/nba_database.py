from collections import deque

import nba_api.stats.static.teams as nba_teams
import nba_api.stats.static.players as nba_players
from nba_api.stats.endpoints import CommonTeamRoster, TeamYearByYearStats, \
    PlayerCareerStats, LeagueStandingsV3

import mysql.connector
from mysql.connector.cursor import MySQLCursor

import mysql_utils as utils
import nba_schema
import api_to_db_headers as api_to_db

def update_teams_table(cursor: MySQLCursor) -> None:
    table_name = 'teams'
    # Create the table if it doesn't already exist.
    operation = f"SHOW tables FROM {cursor._cnx.database} LIKE '{table_name}'"
    cursor.execute(operation)
    if(cursor.rowcount == 0):
        table_description = nba_schema.TABLES[table_name]
        utils.create_table(cursor, table_name, table_description)
    # Add teams to the table.
    teams = deque(nba_teams.get_teams())
    while(teams):
        team = teams.popleft()
        team['logo'] = nba_schema.TEAM_LOGO_URL_FORMAT.format(team['id'])
        api_to_db.change_dict_keys(team, api_to_db.HEADERS.get('teams'))
        utils.insert_or_update_dict(cursor, table_name, team)
    # Commit just in case autocommit is disabled.
    cursor._cnx.commit()

# TODO: Add enum for whether you want to update all, active, or inactive players
def update_players_table(cursor: MySQLCursor) -> None:
    table_name = 'players'
    # Create the table if it doesn't already exist.
    operation = f"SHOW tables FROM {cursor._cnx.database} LIKE '{table_name}'"
    cursor.execute(operation)
    if(cursor.rowcount == 0):
        table_description = nba_schema.TABLES[table_name]
        utils.create_table(cursor, table_name, table_description)
    # Add players to the table.
    players = deque(nba_players.get_players())
    while(players):
        player = players.popleft()
        player['headshot'] = (nba_schema.PLAYER_HEADSHOT_URL_FORMAT
                              .format(player['id']))
        api_to_db.change_dict_keys(player, api_to_db.HEADERS.get('players'))
        utils.insert_or_update_dict(cursor, table_name, player)
    # Commit just in case autocommit is disabled.
    cursor._cnx.commit()

"""
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
"""

if(__name__ == '__main__'):
    cnx = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'password'
    )
    cursor = cnx.cursor(buffered = True)

    #utils.delete_database(cursor, nba_schema.DB_NAME + '2')

    utils.use_database(cursor, nba_schema.DB_NAME + '2')

    update_teams_table(cursor)
    update_players_table(cursor)

    #create_teams_table(handler)
    #create_players_table(handler)
    #create_player_season_stats_table(handler)

    cnx.close()
