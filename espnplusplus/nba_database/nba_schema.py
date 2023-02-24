# The following reference was heavily used to create this file:
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

from nba_api.stats.library.data import teams
from nba_api.stats.library.data import team_index_abbreviation, \
    team_index_nickname, team_index_city, team_index_state, team_index_full_name
from nba_api.stats.library.data import players
from nba_api.stats.library.data import player_index_first_name, \
    player_index_last_name, player_index_full_name

def get_max_len(iterable, index):
    return max(map(len, (element[index] for element in iterable)))

team_lengths = {
    'abbreviation' : get_max_len(teams, team_index_abbreviation),
    'nickname'     : get_max_len(teams, team_index_nickname),
    'city'         : get_max_len(teams, team_index_city),
    'state'        : get_max_len(teams, team_index_state),
    'full_name'    : get_max_len(teams, team_index_full_name)
}

player_lengths = {
    'first_name' : get_max_len(players, player_index_first_name),
    'last_name'  : get_max_len(players, player_index_last_name),
    'full_name'  : get_max_len(players, player_index_full_name)
}

DB_NAME = 'nba'

TABLES = {}

TABLES['teams'] = (
    "CREATE TABLE `teams` ("
    "  `id`           int(11)                                 NOT NULL,"
   f"  `abbreviation` varchar({team_lengths['abbreviation']}) NOT NULL,"
   f"  `nickname`     varchar({team_lengths['nickname']})     NOT NULL,"
   f"  `city`         varchar({team_lengths['city']})         NOT NULL,"
   f"  `state`        varchar({team_lengths['state']})        NOT NULL,"
   f"  `full_name`    varchar({team_lengths['full_name']})    NOT NULL,"
    "  `year_founded` int(11)                                 NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['players'] = (
    "CREATE TABLE `players` ("
    "  `id`         int(11)                                 NOT NULL,"
   f"  `first_name` varchar({player_lengths['first_name']}) NOT NULL,"
   f"  `last_name`  varchar({player_lengths['last_name']})  NOT NULL,"
   f"  `full_name`  varchar({player_lengths['full_name']})  NOT NULL,"
   f"  `is_active`  bool                                    NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")