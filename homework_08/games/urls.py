from django.urls import path
from games import views

app_name = 'games'

urlpatterns = [
    path('', views.game_view, name='index'),
    path('games/', views.GameListView.as_view(), name='list'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='detail'),
]