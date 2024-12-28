# Generated by Django 5.1.1 on 2024-11-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateTeam', '0008_alter_player_bowl_type_alter_player_player_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bowl_type',
            field=models.CharField(choices=[('all rounder', 'All-Rounder'), ('spinner', 'Spinner'), ('fast bowler', 'Fast-Bowler'), ('medium fast bowler', 'Medium Fast Bowler')], default='spinner', max_length=50),
        ),
    ]