import nba_api.stats.library.data as nba_data
import nba_api.stats.static.teams as nba_api_teams
import nba_api.stats.static.players as nba_api_players

import random
import re
import time
import webbrowser


class Team:
    def __init__(self, nba_id, abbreviation, nickname, year_founded, city, full_name, state, championship_year):
        self.nba_id = nba_id
        self.abbreviation = abbreviation
        self.nickname = nickname
        self.year_founded = year_founded
        self.city = city
        self.full_name = full_name
        self.state = state
        self.championship_year = championship_year

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return f'Team({self.nba_id}, {self.abbreviation}, {self.nickname}, {self.year_founded}, {self.city}, {self.full_name}, {self.state}, {self.championship_year})'


class Player:
    def __init__(self, nba_id, first_name, last_name, full_name, active):
        self.nba_id = nba_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.active = active
        self.headshot = f'https://cdn.nba.com/headshots/nba/latest/1040x760/{nba_id}.png'

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return f'Player({self.nba_id}, {self.first_name}, {self.last_name}, {self.full_name}, {self.active})'


def get_teams():
    teams = {}
    for team_data in nba_data.teams:
        team = Team(
            team_data[nba_data.team_index_id],
            team_data[nba_data.team_index_abbreviation],
            team_data[nba_data.team_index_nickname],
            team_data[nba_data.team_index_year_founded],
            team_data[nba_data.team_index_city],
            team_data[nba_data.team_index_full_name],
            team_data[nba_data.team_index_state],
            team_data[nba_data.team_index_championship_year]
        )
        teams[team.full_name] = team
    return teams


def get_players():
    players = {}
    for player_data in nba_data.players:
        player = Player(
            player_data[nba_data.player_index_id],
            player_data[nba_data.player_index_first_name],
            player_data[nba_data.player_index_last_name],
            player_data[nba_data.player_index_full_name],
            player_data[nba_data.player_index_is_active]
        )
        players[player.full_name] = player
    return players


def search(iterable, name):
    pattern = re.compile(name.lower())
    results = []
    for obj in iterable:
        if(pattern.search(str(obj).lower())):
            results.append(obj)
    if(len(results) == 0):
        return None
    return results


def showcase_headshots(headshots, wait):
    active_players = nba_api_players.get_active_players()
    for i in range(headshots):
        player = random.choice(active_players)
        print(player['full_name'])
        open_player_headshot(player)
        time.sleep(wait)


def showcase_team_logos(logos, wait):
    teams = nba_api_teams.get_teams()
    for i in range(logos):
        team = random.choice(teams)
        print(team['full_name'])
        open_team_logo(team['nickname'])
        time.sleep(wait)


def open_player_headshot(player):
    webbrowser.open(f'https://cdn.nba.com/headshots/nba/latest/1040x760/{player["id"]}.png')


def open_team_logo(team):
    for t in nba_data.teams:
        if(t[nba_data.team_index_nickname].lower() == team.lower()):
            webbrowser.open(f'https://cdn.nba.com/logos/nba/{t[nba_data.team_index_id]}/primary/L/logo.svg')
            break


if(__name__ == '__main__'):
    teams = get_teams()
    players = get_players()
    giannis = search(players.values(), 'giannis')[0]