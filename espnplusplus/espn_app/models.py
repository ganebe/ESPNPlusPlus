from django.db import models

# Create your models here.

class PlayerSeasonStats(models.Model):
    player = models.OneToOneField('Player', models.DO_NOTHING, primary_key=True)
    season_id = models.CharField(max_length=7)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    player_age = models.IntegerField()
    games_played = models.IntegerField()
    games_started = models.IntegerField()
    minutes_played = models.IntegerField()
    field_goals_made = models.IntegerField()
    field_goals_attempted = models.IntegerField()
    field_goal_percentage = models.DecimalField(max_digits=4, decimal_places=3)
    three_pointers_made = models.IntegerField()
    three_pointers_attempted = models.IntegerField()
    three_pointer_percentage = models.DecimalField(max_digits=4, decimal_places=3)
    free_throws_made = models.IntegerField()
    free_throws_attempted = models.IntegerField()
    free_throw_percentage = models.DecimalField(max_digits=4, decimal_places=3)
    offensive_rebounds = models.IntegerField()
    defensive_rebounds = models.IntegerField()
    rebounds = models.IntegerField()
    assists = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()
    personal_fouls = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_season_stats'
        unique_together = (('player', 'season_id', 'team'),)


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=18)
    full_name = models.CharField(max_length=24)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'players'


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    abbreviation = models.CharField(max_length=3)
    nickname = models.CharField(max_length=13)
    city = models.CharField(max_length=13)
    state = models.CharField(max_length=20)
    full_name = models.CharField(max_length=22)
    year_founded = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'teams'