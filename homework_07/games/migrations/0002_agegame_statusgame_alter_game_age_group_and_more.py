# Generated by Django 5.0.6 on 2024-06-11 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='age_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.agegame'),
        ),
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.statusgame'),
        ),
    ]
