from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey('Topic', on_delete = models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccesRecord(models.Model):
    name = models.ForeignKey('Webpage', on_delete = models.CASCADE)
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date

# For admin sign up
class NewAdmin(models.Model):
    name = models.CharField(max_length=264, unique=True)
    email = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name

# For user registration
class UserProfileInfor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user