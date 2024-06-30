from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView, CreateView, UpdateView, DeleteView)
from games.models import Game,RentGame
from games.forms import GameForm



def game_view(request):
    model = Game.objects.all()
    return render(request, 'games/game_list.html', {'object_list': model})

class GameListView(ListView):
    model = Game


class GameDetailView(DetailView):
    model = Game

class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    success_url = reverse_lazy('games:list')

class GameUpdateView(UpdateView):
    model = Game
    fields = '__all__'
    success_url = reverse_lazy('games:list')

class GameDeleteView(DeleteView):
    model = Game
    success_url = reverse_lazy('games:list')
    permission_required = 'games.delete_game'

class RentListView(ListView):
    model = RentGame


class RentDetailView(DetailView):
    model = RentGame