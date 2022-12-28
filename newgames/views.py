from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from.models import Game,Comment
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from.forms import CommentForm,AddGameForm
from django.contrib.auth.models import User 
from django.template.response import TemplateResponse
#from .filters import GameFilter
#def home(request):
#   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Game
    template_name= 'home.html'
    

    def get_context_data(self, *args,**kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["games"]=Game.objects.values('gen').distinct()
        return context

class RedView(ListView):
    model = Game
    template_name= 'redirect.html'
    

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
        tot=total_hyped+total_meh
        try:
          inter=(total_hyped/tot)*100
        except:
          inter=0
        try:
          ninter=(total_meh/tot)*100
        except:
          ninter=0
        context["comments"]=Comment.objects.order_by('-date_added')
        context["games"]= Game.objects.values('gen').distinct()
        context["total_hyped"] = total_hyped
        context["total_meh"] = total_meh
        context["sethyped"]=  sethyped
        context["setmeh"]=  setmeh
        context["inter"]= inter
        context["ninter"]= ninter
        return context

 
class AddGameView(CreateView):
    model = Game
    template_name = 'addgame.html'
    form_class=AddGameForm
    def getid(self):
        id=self.kwargs['pk']
    success_url= "/gamedetails/{id}"

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

class AddCommentView(CreateView):
    model = Comment
    form_class= CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.game_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url= "/red/{game_id}"

class GenreFilter(ListView):
    model = Game
    template_name= 'genre.html'
    
def genre(request): 
  select_value = request.GET.get('gen')
  game_filter= Game.objects.filter(gen=select_value)
  games=Game.objects.values('gen').distinct()
  context={
      'game_filter': game_filter,
      'games':games,
      
  }
  return render(request,'genre.html',context)

class UpdateGameView(UpdateView):
    model= Game
    template_name = 'update_game.html'
    form_class=AddGameForm
    def getid(self):
        id=self.kwargs['pk']
    success_url= "/gamedetails/{id}"


    
    


    