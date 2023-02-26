import mysql.connector

import nba_api.stats.static.teams as nba_teams
import nba_api.stats.static.players as nba_players

from mysql_handler import MySQLHandler
import nba_schema

def create_teams_table(handler: MySQLHandler):
    table_description = nba_schema.TABLES['teams']
    handler.create_table('teams', table_description)
    teams = nba_teams.get_teams()
    for team in teams:
        handler.insert_data('teams', team, team['full_name'])

def create_players_table(handler: MySQLHandler):
    table_description = nba_schema.TABLES['players']
    handler.create_table('players', table_description)
    active_players = nba_players.get_active_players()
    for player in active_players:
        handler.insert_data('players', player, player['full_name'])

if(__name__ == '__main__'):
    handler = MySQLHandler(
        host = 'localhost',
        user = 'root',
        password = 'password'
    )
    handler.drop_database('nba')
    handler.close()

    handler = MySQLHandler(
        host = 'localhost',
        user = 'root',
        password = 'password',
        autocommit = False
    )
    handler.use_database(nba_schema.DB_NAME)
    create_teams_table(handler)
    create_players_table(handler)
    handler.commit()
    handler.close()
