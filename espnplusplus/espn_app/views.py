from django.shortcuts import render
# Create your views here.
def index(request):
    context = {
        'name' : 'erik'
    }
    return render(request, 'espn_app/index.html', {'c':context})
        
def nba_player(request):
    image_url = 'https://cdn.nba.com/headshots/nba/latest/1040x760/1631262.png'
    return render(request, 'espn_app/nba_player.html', {'image_url': image_url})

def nba_team(request):
    return render(request, 'espn_app/nba_team.html', {})