from django.test import TestCase
from games.models import AgeGame, Game, StatusGame, Category
from faker import Faker
from games.management.commands._manual import status_game, category

class TestCategory(TestCase):
    def test_str_categoty(self):
        fake = Faker('ru-Ru')
        test_category = Category.objects.create(
            name=fake.random_element(category)
        )
        self.assertEqual(str(test_category), test_category.name)


class TestGame(TestCase):
    def setUp(self):
        fake = Faker('ru-Ru')
        self.test_category = Category.objects.create(
            name=fake.random_element(category)
        )
        self.status = StatusGame.objects.create(
            name=fake.random_element(status_game)
        )
        self.age = AgeGame.objects.create(
            name=str(fake.random_int(min=1, max=18)) + '+'
        )
        self.game = Game.objects.create(
            name=fake.catch_phrase(),
            description=fake.text(max_nb_chars=200),
            status=self.status,
            category=self.test_category,
            age_group=self.age,
            min_players=fake.random_int(min=1, max=5),
            max_players=fake.random_int(min=5, max=10),
            price=fake.random_int(min=100, max=2000)
        )

    def tearDown(self):
        print(self.game)


    def test_str_game(self):
        self.assertEqual(str(self.game), f'{self.game.name} ({self.age.name}) - {self.game.price} rub')