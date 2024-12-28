from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.
class TeamCategory(models.Model):
    team_type = models.CharField(max_length=400)

    def __str__(self):
        return self.team_type


class Player(models.Model):
    marriage_status = [('married',"Married"),("unmarried","Unmarried")]
    bat_type =[('right_hand','Right Hand'),('left_hand','Left Hand')]
    bowl_type = [('spinner','Spinner'),('all_rounder','All-Rounder'),('fast_bowler','Fast-Bowler'),('medium_fast_bowler','Medium Fast Bowler')]
    name = models.CharField(max_length=400)
    nationality = models.CharField(max_length=400)
    Date_of_birth = models.CharField(max_length=300)
    team_type = models.ForeignKey(TeamCategory,related_name='team', on_delete=models.CASCADE)
    player_type = models.CharField(max_length=50,default="right_hand",choices=bat_type)
    bowl_type = models.CharField(max_length=50,default="spinner",choices=bowl_type)
    player_img = models.ImageField(upload_to='player', null=True, blank=True)
    marriage_status = models.CharField(max_length=50,default="unmarried",choices=marriage_status)
    phone_number = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class UserTeam(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_teams',null=True, blank=True)
    team_name = models.CharField(max_length=255)
    match_date = models.DateField()
    players = models.ManyToManyField(Player, related_name='user_teams')

    def __str__(self):
        return f"{self.team_name} by {self.user.email}"  # Use `email` if it's available on `CustomUser`
