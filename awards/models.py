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
    
    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name


class Project(models.Model):
    webimage= models.ImageField(upload_to='webimage/',null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=70)
    description= models.TextField()
    link= models.CharField(max_length=200)


    def save_project(self):
        self.save()

    @classmethod
    def search_by_name(cls,serach_term):

        projects= cls.objects.filter(name__icontains=serach_term)\

        return projects

    def no_of_ratings(self):
        ratings=Rating.objects.filter(project=self)
        return len(ratings)

    def __str__(self):
        return self.name            

          
