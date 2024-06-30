from django.db.models import QuerySet
from django.test import TestCase
from games.models import AgeGame, Game, StatusGame, Category
from games.management.commands._manual import status_game, category
from faker import Faker
from django.urls import reverse


class TestGameListView(TestCase):
    def setUp(self):
        fake = Faker('ru-Ru')

        self.url = '/list/'
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



    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context_data(self):
        response = self.client.get(self.url)
        self.assertIn('game_list', response.context)
        object_list = response.context['game_list']
        self.assertTrue(isinstance(object_list, QuerySet))
        self.assertEqual(len(object_list),1)


class TestGameDetailView(TestCase):
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

        self.url = reverse('games:detail', kwargs={'pk': self.game.pk})

    def test_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)


