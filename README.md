# Ex02 Django ORM Web Application
## Date: 16-05-2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<WhatsApp Image 2025-05-16 at 19.42.22_fd599bd1.jpg>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
admin.py
```
from django.contrib import admin
from .models import Movie,MovieAdmin

admin.site.register(Movie,MovieAdmin)
```
models.py
```
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
```
## OUTPUT
![alt text](<Screenshot 2025-05-16 193720.png>)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
