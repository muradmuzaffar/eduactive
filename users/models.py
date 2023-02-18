from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jgp',blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email =models.EmailField(max_length=250,blank=True,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    