from django.contrib import admin
from .models import *

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','question','correct_answer','user']

admin.site.register(Question,QuestionAdmin)
