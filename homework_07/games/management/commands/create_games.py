from django.core.management.base import BaseCommand
from games.models import (Category,
                                     Game,
                                     RentGame,
                                     StatusGame,
                                     AgeGame,)
from ._manual import (category,
                      age_group,
                      status_game)

class Command(BaseCommand):
    def handle(self, *args, **options):



        self.stdout.write(self.style.SUCCESS('Successfully create games'))



 # 2. Создание
     #   bear = Category.objects.create(
     #       name='Медведь Неправильный',
     #   )
#
        # 3. Изменение
   #     bear.name = 'Медведь'
   #     bear.save()