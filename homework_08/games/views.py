from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  DetailView)
from games.models import Game


def game_view(request):
    model = Game.objects.all()
    return render(request, 'games/game_list.html', {'object_list': model})

class GameListView(ListView):
    model = Game


class GameDetailView(DetailView):
    model = Game
