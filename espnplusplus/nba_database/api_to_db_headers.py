def change_dict_keys(dictionary: dict, old_to_new_keys: dict,
                     keep_old_pairs: bool = True) -> dict:
    new_dictionary = {}
    for key, value in dictionary.items():
        if(old_to_new_keys and key in old_to_new_keys):
            new_dictionary[old_to_new_keys[key]] = value
        elif(keep_old_pairs):
            new_dictionary[key] = value
    return new_dictionary

HEADERS = {}

HEADERS['teams'] = {
    'id'           : 'id',
    'abbreviation' : 'abbreviation',
    'nickname'     : 'nickname',
    'city'         : 'city',
    'state'        : 'state',
    'full_name'    : 'full_name',
    'logo'         : 'logo',
    'year_founded' : 'year_founded'
}

"""
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
"""
