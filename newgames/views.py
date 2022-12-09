from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from.models import Game
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Game
    template_name= 'home.html'


class GameDetailsView(DetailView):
    model = Game
    template_name = 'game_details.html'

    def get_context_data(self, *args,**kwargs):
        context = super(GameDetailsView, self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(Game, id=self.kwargs['pk'])
        total_hyped=stuff.total_hype()
        total_meh=stuff.total_mehs()
        setmeh = False
        sethyped = False
        if stuff.hype.filter(id=self.request.user.id).exists():
            sethyped = True
        if stuff.meh.filter(id=self.request.user.id).exists():
            setmeh = True

        context["total_hyped"] = total_hyped
        context["total_meh"] = total_meh
        context["sethyped"]=  sethyped
        context["setmeh"]=  setmeh
        return context
 
class AddGameView(CreateView):
    model = Game
    template_name = 'addgame.html'
    fields = '__all__'

def HypeView(request, pk):
    game = get_object_or_404(Game, id=request.POST.get('game_id'))
    sethyped = False
    if game.hype.filter(id=request.user.id).exists():
        game.hype.remove(request.user)
        sethyped = False
    else:
        game.hype.add(request.user)
        sethyped = True
    return HttpResponseRedirect(reverse('gamedetails', args=[str(pk)]))


def MehView(request, pk):
    game = get_object_or_404(Game, id=request.POST.get('game_meh'))
    setmeh = False
    if game.meh.filter(id=request.user.id).exists():
        game.meh.remove(request.user)
        setmeh = False
    else:
        game.meh.add(request.user)
        setmeh = False
    return HttpResponseRedirect(reverse('gamedetails', args=[str(pk)]))

