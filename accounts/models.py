from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to="profile/")
    city  = models.ForeignKey("City",related_name="uer_city",on_delete=CASCADE , blank=True , null=True)
    def __str__(self):
        return str(self.user)
    # Create New User  --> create new Profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
class City(models.Model):
    name =models.CharField(max_length = 30)
    def __str__(self):
        return str(self.name)
    