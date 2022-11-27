from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Game
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Game
    template_name= 'home.html'


class GameDetailsView(DetailView):
    model = Game
    template_name = 'game_details.html'

