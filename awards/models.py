from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'profilepic/', default = 'default.jpeg')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length= 300)
    email = models.EmailField()
    
