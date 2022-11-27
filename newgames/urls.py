from django.urls import path, include
#from.import views
from .views import HomeView, GameDetailsView

urlpatterns = [
    #path('',views.home, name='home'),
    path('',HomeView.as_view(), name="home"),
    path('gamedetails/<int:pk>', GameDetailsView.as_view(), name='gamedetails'),
]
