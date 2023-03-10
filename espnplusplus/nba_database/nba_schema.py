# The following reference was heavily used to create this file:
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html

from nba_api.stats.library.data import teams
from nba_api.stats.library.data import team_index_abbreviation, \
    team_index_nickname, team_index_city, team_index_state, team_index_full_name, team_index_id
from nba_api.stats.library.data import players
from nba_api.stats.library.data import player_index_first_name, \
    player_index_last_name, player_index_full_name, player_index_id

def get_max_len(iterable, index):
    return max(map(len, map(str, (element[index] for element in iterable))))

team_lengths = {
    'abbreviation' : get_max_len(teams, team_index_abbreviation),
    'nickname'     : get_max_len(teams, team_index_nickname),
    'city'         : get_max_len(teams, team_index_city),
    'state'        : get_max_len(teams, team_index_state),
    'full_name'    : get_max_len(teams, team_index_full_name),
    'logo'         : len('https://cdn.nba.com/logos/nba//primary/L/logo.svg') + get_max_len(teams, team_index_id)
}

player_lengths = {
    'first_name' : get_max_len(players, player_index_first_name),
    'last_name'  : get_max_len(players, player_index_last_name),
    'full_name'  : get_max_len(players, player_index_full_name),
    'headshot'   : len('https://cdn.nba.com/headshots/nba/latest/1040x760/.png') + get_max_len(players, player_index_id)
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
   f"  `logo`         varchar({team_lengths['logo']})         NOT NULL,"
    "  `year_founded` int(11)                                 NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['players'] = (
    "CREATE TABLE `players` ("
    "  `id`         int(11)                                 NOT NULL,"
   f"  `first_name` varchar({player_lengths['first_name']}) NOT NULL,"
   f"  `last_name`  varchar({player_lengths['last_name']})  NOT NULL,"
   f"  `full_name`  varchar({player_lengths['full_name']})  NOT NULL,"
   f"  `headshot`   varchar({player_lengths['headshot']})   NOT NULL,"
    "  `is_active`  bool                                    NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['team_stats'] = (
    "CREATE TABLE `team_stats` ("
    "  `team_id`                  int(11)       NOT NULL,"
    "  `year`                     varchar(7)    NOT NULL,"
    "  `games_played`             int(11)       NOT NULL,"
    "  `wins`                     int(11)       NOT NULL,"
    "  `losses`                   int(11)       NOT NULL,"
    "  `winning_percentage`       decimal(4, 3) NOT NULL,"
    "  `field_goals_made`         int(11)       NOT NULL,"
    "  `field_goals_attempted`    int(11)       NOT NULL,"
    "  `field_goal_percentage`    decimal(4, 3) NOT NULL,"
    "  `three_pointers_made`      int(11)       NOT NULL,"
    "  `three_pointers_attempted` int(11)       NOT NULL,"
    "  `three_pointer_percentage` decimal(4, 3) NOT NULL,"
    "  `free_throws_made`         int(11)       NOT NULL,"
    "  `free_throws_attempted`    int(11)       NOT NULL,"
    "  `free_throw_percentage`    decimal(4, 3) NOT NULL,"
    "  `offensive_rebounds`       int(11)       NOT NULL,"
    "  `defensive_rebounds`       int(11)       NOT NULL,"
    "  `rebounds`                 int(11)       NOT NULL,"
    "  `assists`                  int(11)       NOT NULL,"
    "  `steals`                   int(11)       NOT NULL,"
    "  `blocks`                   int(11)       NOT NULL,"
    "  `turnovers`                int(11)       NOT NULL,"
    "  `personal_fouls`           int(11)       NOT NULL,"
    "  `points`                   int(11)       NOT NULL,"
    "  PRIMARY KEY (`team_id`, `year`),"
    "  CONSTRAINT `fk_team_id` FOREIGN KEY (`team_id`) "
    "     REFERENCES `teams` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['player_stats'] = (
    "CREATE TABLE `player_stats` ("
    "  `player_id`                int(11)       NOT NULL,"
    "  `year`                     varchar(7)    NOT NULL,"
    "  `team_id`                  int(11)       NOT NULL,"
    "  `player_age`               int(11)       NOT NULL,"
    "  `games_played`             int(11)       NOT NULL,"
    "  `games_started`            int(11)       NOT NULL,"
    "  `minutes_played`           int(11)       NOT NULL,"
    "  `field_goals_made`         int(11)       NOT NULL,"
    "  `field_goals_attempted`    int(11)       NOT NULL,"
    "  `field_goal_percentage`    decimal(4, 3) NOT NULL,"
    "  `three_pointers_made`      int(11)       NOT NULL,"
    "  `three_pointers_attempted` int(11)       NOT NULL,"
    "  `three_pointer_percentage` decimal(4, 3) NOT NULL,"
    "  `free_throws_made`         int(11)       NOT NULL,"
    "  `free_throws_attempted`    int(11)       NOT NULL,"
    "  `free_throw_percentage`    decimal(4, 3) NOT NULL,"
    "  `offensive_rebounds`       int(11)       NOT NULL,"
    "  `defensive_rebounds`       int(11)       NOT NULL,"
    "  `rebounds`                 int(11)       NOT NULL,"
    "  `assists`                  int(11)       NOT NULL,"
    "  `steals`                   int(11)       NOT NULL,"
    "  `blocks`                   int(11)       NOT NULL,"
    "  `turnovers`                int(11)       NOT NULL,"
    "  `personal_fouls`           int(11)       NOT NULL,"
    "  `points`                   int(11)       NOT NULL,"
    "  PRIMARY KEY (`player_id`, `year`, `team_id`),"
    "  CONSTRAINT `fk_player_id` FOREIGN KEY (`player_id`) "
    "     REFERENCES `players` (`id`) ON DELETE CASCADE,"
    "  CONSTRAINT `fk_team_id` FOREIGN KEY (`team_id`) "
    "     REFERENCES `teams` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['rosters'] = (
    "CREATE TABLE `rosters` ("
    "  `player_id`  int(11)       NOT NULL,"
    "  `team_id`    int(11)       NOT NULL,"
    "  `number`     int(11)       NOT NULL,"
    "  `position`   varchar(3)    NOT NULL,"
    "  `height`     int(11)       NOT NULL,"
    "  `weight`     int(11)       NOT NULL,"
    "  `birth_date` date          NOT NULL,"
    "  `age`        int(11)       NOT NULL,"
    "  `experience` varchar(2)    NOT NULL,"
    "  `school`     varchar(100)  NOT NULL,"
    "  `acquisition` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`player_id`),"
    "  CONSTRAINT `fk_player_id` FOREIGN KEY (`player_id`) "
    "     REFERENCES `players` (`id`) ON DELETE CASCADE,"
    "  CONSTRAINT `fk_team_id` FOREIGN KEY (`team_id`) "
    "     REFERENCES `teams` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['standings'] = (
    "CREATE TABLE `standings` ("
    "  `team_id`                int(11)    NOT NULL,"
    "  `wins`                   int(11)    NOT NULL,"
    "  `losses`                 int(11)    NOT NULL,"
    "  `conference`             char(4)    NOT NULL,"
    "  `conference_wins`        int(11)    NOT NULL,"
    "  `conference_losses`      int(11)    NOT NULL,"
    "  `conference_rank`        int(11)    NOT NULL,"
    "  `division`               varchar(9) NOT NULL,"
    "  `division_wins`          int(11)    NOT NULL,"
    "  `division_losses`        int(11)    NOT NULL,"
    "  `division_rank`          int(11)    NOT NULL,"
    "  `home_wins`              int(11)    NOT NULL,"
    "  `home_losses`            int(11)    NOT NULL,"
    "  `road_wins`              int(11)    NOT NULL,"
    "  `road_losses`            int(11)    NOT NULL,"
    "  `last_10_wins`           int(11)    NOT NULL,"
    "  `last_10_losses`         int(11)    NOT NULL,"
    "  `last_10_home_wins`      int(11)    NOT NULL,"
    "  `last_10_home_losses`    int(11)    NOT NULL,"
    "  `last_10_road_wins`      int(11)    NOT NULL,"
    "  `last_10_road_losses`    int(11)    NOT NULL,"
    "  `overtime_wins`          int(11)    NOT NULL,"
    "  `overtime_losses`        int(11)    NOT NULL,"
    "  `current_streak`         int(11)    NOT NULL,"
    "  `vs_east_wins`           int(11)    NOT NULL,"
    "  `vs_east_losses`         int(11)    NOT NULL,"
    "  `vs_atlantic_wins`       int(11)    NOT NULL,"
    "  `vs_atlantic_losses`     int(11)    NOT NULL,"
    "  `vs_central_wins`        int(11)    NOT NULL,"
    "  `vs_central_losses`      int(11)    NOT NULL,"
    "  `vs_southeast_wins`      int(11)    NOT NULL,"
    "  `vs_southeast_losses`    int(11)    NOT NULL,"
    "  `vs_west_wins`           int(11)    NOT NULL,"
    "  `vs_west_losses`         int(11)    NOT NULL,"
    "  `vs_northwest_wins`      int(11)    NOT NULL,"
    "  `vs_northwest_losses`    int(11)    NOT NULL,"
    "  `vs_pacific_wins`        int(11)    NOT NULL,"
    "  `vs_pacific_losses`      int(11)    NOT NULL,"
    "  `vs_southwest_wins`      int(11)    NOT NULL,"
    "  `vs_southwest_losses`    int(11)    NOT NULL,"
    "  `jan_wins`               int(11)    NOT NULL,"
    "  `jan_losses`             int(11)    NOT NULL,"
    "  `feb_wins`               int(11)    NOT NULL,"
    "  `feb_losses`             int(11)    NOT NULL,"
    "  `mar_wins`               int(11)    NOT NULL,"
    "  `mar_losses`             int(11)    NOT NULL,"
    "  `apr_wins`               int(11)    NOT NULL,"
    "  `apr_losses`             int(11)    NOT NULL,"
    "  `may_wins`               int(11)    NOT NULL,"
    "  `may_losses`             int(11)    NOT NULL,"
    "  `jun_wins`               int(11)    NOT NULL,"
    "  `jun_losses`             int(11)    NOT NULL,"
    "  `jul_wins`               int(11)    NOT NULL,"
    "  `jul_losses`             int(11)    NOT NULL,"
    "  `aug_wins`               int(11)    NOT NULL,"
    "  `aug_losses`             int(11)    NOT NULL,"
    "  `sep_wins`               int(11)    NOT NULL,"
    "  `sep_losses`             int(11)    NOT NULL,"
    "  `oct_wins`               int(11)    NOT NULL,"
    "  `oct_losses`             int(11)    NOT NULL,"
    "  `nov_wins`               int(11)    NOT NULL,"
    "  `nov_losses`             int(11)    NOT NULL,"
    "  `dec_wins`               int(11)    NOT NULL,"
    "  `dec_losses`             int(11)    NOT NULL,"
    "  `total_points`           int(11)    NOT NULL,"
    "  `opponent_totals_points` int(11)    NOT NULL,"
    "  PRIMARY KEY (`team_id`),"
    "  CONSTRAINT `fk_team_id` FOREIGN KEY (`team_id`) "
    "     REFERENCES `teams` (`id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")
