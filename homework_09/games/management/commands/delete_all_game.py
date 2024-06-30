from django.core.management.base import BaseCommand
from games.models import (Category,
                                     Game,
                                     RentGame,
                                     StatusGame,
                                     AgeGame,)

class Command(BaseCommand):
    def handle(self, *args, **options):
        Game.objects.all().delete()
        Category.objects.all().delete()
        RentGame.objects.all().delete()
        StatusGame.objects.all().delete()
        AgeGame.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all games'))


