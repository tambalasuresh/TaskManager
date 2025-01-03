# Generated by Django 5.1.1 on 2024-11-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_type', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TeamCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_type', models.CharField(max_length=400)),
            ],
        ),
    ]
