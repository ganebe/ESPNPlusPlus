from django.shortcuts import render
from .models import Team
from .models import PlayerSeasonStats
from .models import Player
# Create your views here.
def index(request):
    context = {
        'name' : 'erik'
    }
    return render(request, 'espn_app/index.html', {'c':context})
        
def nba_player(request):
    image_url = 'https://cdn.nba.com/headshots/nba/latest/1040x760/1631262.png'
    return render(request, 'espn_app/nba_player.html', {'image_url': image_url})

def nba_teams(request):
    Teams = Team.objects.all
    context = {
        'Teams' : Teams
    }
    return render(request, 'espn_app/nba_team.html', context)

def nba_team(request, team_id):
    Target = Team.objects.get(id = team_id)
    return render(request,'espn_app/team.html'      , {"Target" : Target})

def trading_card(request, card_id):
    Stats = PlayerSeasonStats.objects.filter(player_id = card_id)
    Bios = Player.objects.get(id = card_id)
    context = {
        'Stats' : Stats,
        'Bios' : Bios,
        'player_id': card_id,
    }
    return render(request, 'espn_app/trading_card.html' , context )