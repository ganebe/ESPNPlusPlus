from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('nba/player', views.nba_player, name='nba_player'),
    path('nba/teams', views.nba_teams, name ='nba_teams'),
    path('nba/team/<team_id>', views.nba_team, name = 'nba_team'),
    path('nba/card/<card_id>', views.trading_card, name= 'trading_card'),

]