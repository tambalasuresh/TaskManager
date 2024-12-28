from django.contrib import admin
from .models import *

class TeamCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','team_type']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id','name','player_img','nationality','team_type','player_type','bowl_type','marriage_status']
    list_filter = ['team_type','bowl_type']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','team_name','user','match_date']

admin.site.register(TeamCategory,TeamCategoryAdmin)
admin.site.register(UserTeam,TeamAdmin)
admin.site.register(Player,PlayerAdmin)
