from django.shortcuts import render, redirect
from .models import Team
from .models import PlayerSeasonStats
from .models import Player
# Create your views here.
def index(request):
    context = {}  
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
        print('----------------------')
    
        Bios = Player.objects.all()
        Bios = Bios.filter(first_name=query)
        print(Bios.all)
        print('----------------------')
        AllStats = PlayerSeasonStats.objects.filter(player=Bios[0])
        Stats = AllStats[len(AllStats) - 1]

        print(Bios[0].id)
        context = {
            'Stats': Stats,
            'Bios': Bios,
            'player_id': Bios[0].id,
        }
        return redirect('trading_card', Bios[0].id)
        
    return render(request, 'espn_app/index.html', {'c': context})
        
def nba_player(request):
        # return redirect('trading_card', context['player_id'])
    context = {}  
    durant = 201142;
    giannis = 203507;
    lebron = 2544;
    
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
        print('----------------------')
    
        Bios = Player.objects.all()
        Bios = Bios.filter(first_name=query)
        print(Bios.all)
        print('----------------------')
        AllStats = PlayerSeasonStats.objects.filter(player=Bios[0])
        Stats = AllStats[len(AllStats) - 1]

        print(Bios[0].id)
        context = {
            'Stats': Stats,
            'Bios': Bios,
            'player_id': Bios[0].id,
        }
        return redirect('trading_card', Bios[0].id)
    
    
    
    image_url = 'https://cdn.nba.com/headshots/nba/latest/1040x760/1631262.png'
    return render(request, 'espn_app/nba_player.html', {'image_url': image_url})

def nba_teams(request):
    context = {}  
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
        print('----------------------')
    
        Bios = Player.objects.all()
        Bios = Bios.filter(first_name=query)
        print(Bios.all)
        print('----------------------')
        AllStats = PlayerSeasonStats.objects.filter(player=Bios[0])
        Stats = AllStats[len(AllStats) - 1]

        print(Bios[0].id)
        context = {
            'Stats': Stats,
            'Bios': Bios,
            'player_id': Bios[0].id,
        }
        return redirect('trading_card', Bios[0].id)
    
    Teams = Team.objects.all

        
    context = {
        'Teams' : Teams,
        
    }
    return render(request, 'espn_app/nba_team.html', context)

def nba_team(request, team_id):
    context = {}  
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
        print('----------------------')
    
        Bios = Player.objects.all()
        Bios = Bios.filter(first_name=query)
        print(Bios.all)
        print('----------------------')
        AllStats = PlayerSeasonStats.objects.filter(player=Bios[0])
        Stats = AllStats[len(AllStats) - 1]

        print(Bios[0].id)
        context = {
            'Stats': Stats,
            'Bios': Bios,
            'player_id': Bios[0].id,
        }
        return redirect('trading_card', Bios[0].id)
    
    Target = Team.objects.get(id = team_id)
    AllMember = PlayerSeasonStats.objects.filter(team_id= team_id)
    CurrentMembers = AllMember.filter(season_id = "2022-23")
   
    context ={
        "Target" : Target,
        "CurrentMembers" : CurrentMembers,
    }
    return render(request,'espn_app/team.html', context)

def trading_card(request, card_id):
    context = {}  
    if request.method == 'POST':
        query = request.POST.get('query')
        print(query)
        print('----------------------')
    
        Bios = Player.objects.all()
        Bios = Bios.filter(first_name=query)
        print(Bios.all)
        print('----------------------')
        AllStats = PlayerSeasonStats.objects.filter(player=Bios[0])
        Stats = AllStats[len(AllStats) - 1]

        print(Bios[0].id)
        context = {
            'Stats': Stats,
            'Bios': Bios,
            'player_id': Bios[0].id,
        }
        return redirect('trading_card', Bios[0].id)

    
    AllStats = PlayerSeasonStats.objects.filter(player_id = card_id)
    Stats = AllStats[len(AllStats) - 1]
    Bios = Player.objects.get(id=card_id)
    
    context = {
        'Stats' : Stats,
        'Bios' : Bios,
        'player_id': card_id,
    }

    return render(request, 'espn_app/trading_card.html' , context )

