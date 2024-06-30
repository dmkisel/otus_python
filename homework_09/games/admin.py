from django.contrib import admin
from .models import (Category,
                     Game,
                     StatusGame,
                     RentGame,
                     AgeGame,)
# Register your models here.

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(StatusGame)
admin.site.register(RentGame)
admin.site.register(AgeGame)