from django.urls import path, include,re_path
from.import views
from .views import HomeView, GameDetailsView, AddGameView,HypeView,MehView,AddCommentView,RedView,genre,GenreFilter,UpdateGameView
from django.views.generic import TemplateView
urlpatterns = [
    #path('',views.home, name='home'),
    path('',HomeView.as_view(), name="home"),
    path('gamedetails/<int:pk>', GameDetailsView.as_view(), name='gamedetails'),
    path('addgame/', AddGameView.as_view(), name='add'),
    path('hype/<int:pk>', HypeView, name='hype_game'),
    path('meh/<int:pk>', MehView, name='meh_game'),
    path('gamedetails/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('red/<int:pk>', RedView.as_view(), name='red'),
    path('genfilter',genre,name="genrefilter"),
    path('gamedetails/edit/<int:pk>', UpdateGameView.as_view(), name='update_game'),

]
 