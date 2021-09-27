from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to="profile/")
    city  = models.ForeignKey("City",related_name="uer_city",on_delete=CASCADE)
    
    
    
class City(models.Model):
    name =models.CharField(max_length = 30)
    