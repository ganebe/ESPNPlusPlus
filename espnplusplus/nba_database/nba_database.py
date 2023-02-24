import mysql.connector

import nba_api.stats.static.teams as nba_teams
import nba_api.stats.static.players as nba_players

import mysql_utils as utils
import nba_schema

# FOR TESTING
from time import sleep

def create_teams_table(cursor):
    table_description = nba_schema.TABLES['teams']
    utils.create_table(cursor, 'teams', table_description)
    teams = nba_teams.get_teams()
    for team in teams:
        utils.insert_data(cursor, 'teams', team, team['full_name'])

def create_players_table(cursor):
    table_description = nba_schema.TABLES['players']
    utils.create_table(cursor, 'players', table_description)
    active_players = nba_players.get_active_players()
    for player in active_players:
        utils.insert_data(cursor, 'players', player, player['full_name'])

if(__name__ == '__main__'):
    cnx = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'password'
    )
    cursor = cnx.cursor()
    print('\nSTART\n')
    input()
    utils.use_database(cursor, nba_schema.DB_NAME)
    cnx.commit()
    print('\nNEXT: CREATING TEAMS TABLE\n')
    input()
    create_teams_table(cursor)
    cnx.commit()
    print('\nNEXT: CREATING PLAYERS TABLE\n')
    input()
    create_players_table(cursor)
    cnx.commit()
    cnx.close()