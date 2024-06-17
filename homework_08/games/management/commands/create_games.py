from django.core.management.base import BaseCommand
from games.models import (Category,
                          Game,
                          StatusGame,
                          AgeGame, )
from ._manual import (category,
                      age_group,
                      status_game,
                      games)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for item in category:
            new_category = Category(name=item)
            new_category.save()
        self.stdout.write(self.style.SUCCESS('Successfully add category'))
        for item in status_game:
            new_status_game = StatusGame(name=item)
            new_status_game.save()
        self.stdout.write(self.style.SUCCESS('Successfully add status'))
        for item in age_group:
            new_age_group = AgeGame(name=item)
            new_age_group.save()
        self.stdout.write(self.style.SUCCESS('Successfully add age limit'))
        for game in games:
            new_game = Game(name=game["name"],
                            description=game["description"],
                            status=StatusGame.objects.get(name=status_game[game["status"]]),
                            category=Category.objects.get(name=category[game["category"]]),
                            min_players=game["min_players"],
                            max_players=game["max_players"],
                            age_group=AgeGame.objects.get(name=age_group[game["age_group"]]),
                            price=game["price"],
                            )
            new_game.save()
        self.stdout.write(self.style.SUCCESS('Successfully create games'))