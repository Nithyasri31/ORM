from django.db import models
from django.contrib import admin
class Movie (models.Model):
    user_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    moviename=models.CharField(max_length=100)
    mobile_no=models.IntegerField()
    no_of_tickets=models.IntegerField()
    Date=models.DateField()
 
class MovieAdmin(admin.ModelAdmin):
    list_display=('user_id','name','moviename','mobile_no','no_of_tickets','Date')
