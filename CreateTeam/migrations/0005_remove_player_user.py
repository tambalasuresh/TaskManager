# Generated by Django 5.1.1 on 2024-11-06 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CreateTeam', '0004_player_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='user',
        ),
    ]