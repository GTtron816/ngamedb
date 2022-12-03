from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from.models import Game
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Game
    template_name= 'home.html'


class GameDetailsView(DetailView):
    model = Game
    template_name = 'game_details.html'

class AddGameView(CreateView):
    model = Game
    template_name = 'addgame.html'
    fields = '__all__'