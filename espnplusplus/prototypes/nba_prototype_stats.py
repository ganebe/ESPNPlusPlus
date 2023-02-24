from nba_api.stats.endpoints import playercareerstats

lebron_james_id = 2544

career = playercareerstats.PlayerCareerStats(player_id=lebron_james_id)

# pandas data frames
print('NBA ID 2544 is LeBron James\n')
print(career.get_data_frames()[0])