from django.db import models
from django.contrib.auth.models import User
from pages.models import DEGREE_CHOICES

GENDER_CHOICES = [
    ("Male", ("Male")),
    ("Female", ("Female")),
]

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=100,blank=True,null=True,choices=GENDER_CHOICES)
    email =models.EmailField(max_length=250,blank=True,null=True)
    phone_number = models.CharField(max_length=100,blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)

    #background
    gre = models.IntegerField( blank=True, null=True)
    gpa = models.FloatField( blank=True, null=True)
    ielts = models.FloatField(blank=True, null=True)
    toefl = models.IntegerField( blank=True, null=True)
    gmat = models.IntegerField( blank=True, null=True)
    university = models.CharField(max_length=300,blank=True,null=True)
    speciality = models.CharField(max_length=300,blank=True,null=True)
    degree = models.CharField(max_length=100,blank=True,null=True,choices=DEGREE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    