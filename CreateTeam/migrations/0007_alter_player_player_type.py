# Generated by Django 5.1.1 on 2024-11-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateTeam', '0006_player_marriage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_type',
            field=models.CharField(choices=[('righthand', 'Right Hand'), ('lefthand', 'Left Hand')], default='righthand', max_length=50),
        ),
    ]
