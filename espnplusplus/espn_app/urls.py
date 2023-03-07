from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('nba/player', views.nba_player, name='nba_player'),
    path('nba/team', views.nba_team, name ='nba_team'),
]