from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    full_name   = models.CharField(default="", max_length=50)
    image       = models.ImageField(upload_to='profile/%Y/%m/%d/', default='/static/images/profile.png')
    address     = models.TextField(default="")
    country     = models.CharField(default="",max_length=50)
    city        = models.CharField(default="",max_length=50)
    phone       = models.CharField(default="",max_length=15)
    zipcode     = models.CharField(default="",max_length=10)
    email       = models.EmailField(default="", max_length=254)
    
    
    
