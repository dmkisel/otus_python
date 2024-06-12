from django.contrib import admin
from .models import (Category,
                     Game,
                     RentGame,
                     StatusGame,
                     AgeGame,)
# Register your models here.

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(RentGame)
admin.site.register(StatusGame)
admin.site.register(AgeGame)