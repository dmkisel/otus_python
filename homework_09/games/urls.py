from django.urls import path
from games import views

app_name = 'games'

urlpatterns = [
    path('', views.game_view, name='index'),
    path('list/', views.GameListView.as_view(), name='list'),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='detail'),
    path('create/', views.GameCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.GameUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.GameDeleteView.as_view(), name='delete'),

    path('rent_list/', views.RentListView.as_view(), name='rent'),
]