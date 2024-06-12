# Generated by Django 5.0.6 on 2024-06-11 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('min_players', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('age_group', models.CharField(max_length=5)),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.category')),
            ],
        ),
        migrations.CreateModel(
            name='RentGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('cost', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
        ),
    ]
