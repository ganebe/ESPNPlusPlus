from nba_api.stats.static import teams, players

from nba_api.stats.endpoints import TeamYearByYearStats, PlayerCareerStats, \
    CommonTeamRoster, LeagueStandingsV3

team_id = teams.find_teams_by_nickname('Bucks')[0]['id']
player_id = players.find_players_by_full_name('LeBron James')[0]['id']

"""
team_stats = TeamYearByYearStats(team_id)
nd = team_stats.get_normalized_dict()
for i in nd['TeamStats']:
    print(i)
    print('\n\n')
"""

"""
player_stats = PlayerCareerStats(player_id)
nd = player_stats.get_normalized_dict()
for i in nd['SeasonTotalsRegularSeason']:
    print(i)
    print('\n\n')
"""

"""
team_roster = CommonTeamRoster(team_id)
nd = team_roster.get_normalized_dict()
for i in nd['CommonTeamRoster']:
    print(i)
    print('\n\n')
"""

standings = LeagueStandingsV3()
nd = standings.get_normalized_dict()
for i in nd['Standings']:
    print(i)
    print('\n\n')

"""
from datetime import datetime

non_numbers = set()
positions = set()
non_heights = set()
non_weights = set()
non_birth_dates = set()
non_whole_ages = set()
non_experiences = set()
schools = []
acquisitions = []

for team in teams.get_teams():
    print(team['full_name'] + ':', end = '')
    roster_dict = {}
    try:
        roster = CommonTeamRoster(team['id'], timeout = 2)
        roster_dict = roster.get_normalized_dict()
        print('OK')
    except:
        roster_dict = {'CommonTeamRoster': []}
        print('Failed')
    for player in roster_dict['CommonTeamRoster']:
        # NUM
        try:
            if(not player['NUM'].isdigit()):
                non_numbers.add(player['NUM'])
        except:
            non_numbers.add(player['NUM'])
        # POSITION
        positions.add(player['POSITION'])
        # HEIGHT
        try:
            inches = int(player['HEIGHT'].split('-')[0]) * 12 + int(player['HEIGHT'].split('-')[1])
        except:
            non_heights.add(player['HEIGHT'])
        # WEIGHT
        if(not player['WEIGHT'].isdigit()):
            non_numbers.add(player['WEIGHT'])
        # BIRTH_DATE
        try:
            datetime.strptime(player['BIRTH_DATE'], '%b %d, %Y')
        except:
            non_birth_dates.add(player['BIRTH_DATE'])
        # AGE
        if(player['AGE'] != int(player['AGE'])):
            non_whole_ages.add(player['AGE'])
        # EXP
        if(not player['EXP'].isdigit()):
            non_experiences.add(player['EXP'])
        # SCHOOL
        schools.append(player['SCHOOL'])
        # HOW_ACQUIRED
        acquisitions.append(player['HOW_ACQUIRED'])
print('NUM:', non_numbers, '\n')
print('POS:', positions, '\n')
print('HEIGHT:', non_heights, '\n')
print('WEIGHT:', non_weights, '\n')
print('BIRTH:', non_birth_dates, '\n')
print('AGES:', non_whole_ages, '\n')
print('EXP:', non_experiences, '\n')
print('SCHOOL:', max(map(len, schools)), '\n')
print('ACQ:', max(map(len, acquisitions)), '\n')
"""
