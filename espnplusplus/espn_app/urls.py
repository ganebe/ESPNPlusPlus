from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/player', views.player, name='player'),
]