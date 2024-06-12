from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StatusGame(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AgeGame(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(StatusGame, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    age_group = models.ForeignKey(AgeGame, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.age_group}) - {self.price} rub'


class RentGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.game} - {self.date_start} - {self.date_end}'

