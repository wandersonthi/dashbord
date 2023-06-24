from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfoPlus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info_plus')
    picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='profile_pictures/default.png')
