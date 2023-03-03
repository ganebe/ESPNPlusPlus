from django.shortcuts import render

# Create your views here.
def index(request):
    
    
    context = {
        'name' : 'erik'
    }
    return render(request, 'espn_app/index.html', {'c':context})
        
def player(request):
    return render(request, 'espn_app/player.html')
    