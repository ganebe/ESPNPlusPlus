from nba_api.stats.endpoints import playercareerstats, playerprofilev2

print('A')

lebron_james_id = 2544

print('B')

import time

print('C')

start = time.time()

#print('D')

#career = playercareerstats.PlayerCareerStats(player_id = lebron_james_id)

c = playercareerstats.PlayerCareerStats(1631262)

"""
c1 = playercareerstats.PlayerCareerStats(2544)
c2 = playercareerstats.PlayerCareerStats(2617)
c3 = playercareerstats.PlayerCareerStats(2738)
c4 = playercareerstats.PlayerCareerStats(101108)
c5 = playercareerstats.PlayerCareerStats(200752)
c6 = playercareerstats.PlayerCareerStats(200768)
c7 = playercareerstats.PlayerCareerStats(200782)
c8 = playercareerstats.PlayerCareerStats(201142)
c9 = playercareerstats.PlayerCareerStats(201143)
c10 = playercareerstats.PlayerCareerStats(201144)
"""

for k, v in c.get_normalized_dict().items():
    print(k, '\n')
    print(v, '\n\n\n')

d = c.get_normalized_dict()

for i in d['SeasonTotalsRegularSeason']:
    print(i)
    print('\n\n\n')

#print(c1.get_dict())

#print('E')

end = time.time()

print(end - start)

#profile = playerprofilev2.PlayerProfileV2(player_id = lebron_james_id)
# pandas data frames
#print('NBA ID 2544 is LeBron James\n')
#print(career.get_data_frames()[0])