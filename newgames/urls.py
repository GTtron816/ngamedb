from django.urls import path, include
#from.import views
from .views import HomeView, GameDetailsView, AddGameView,HypeView,MehView

urlpatterns = [
    #path('',views.home, name='home'),
    path('',HomeView.as_view(), name="home"),
    path('gamedetails/<int:pk>', GameDetailsView.as_view(), name='gamedetails'),
    path('addgame/', AddGameView.as_view(), name='add'),
    path('hype/<int:pk>', HypeView, name='hype_game'),
    path('meh/<int:pk>', MehView, name='meh_game'),
]
 