from django.db import models

# Create your models here.
class MenueItem(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()

class Reservation(models.Model):
    firstName=models.CharField(max_length=255)
    lastName=models.CharField(max_length=255)
    guestcnt=models.IntegerField()
    
