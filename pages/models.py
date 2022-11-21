from django.db import models

# Create your models here.


VAIWER_CHOICES = [
    ("Available", ("Available")),
    ("Not Available", ("Not Available")),
    ("No info", ("No info"))

]

EVALUATION_CHOICES = [
    ("Very Difficult; Great", ("Very Difficult; Great")),
    ("Not Difficult; Great", ("Not Difficult; Great")),
    ("Mid Difficult; Great", ("Mid Difficult; Great")),
    ("Easy; Not Good", ("Easy; Not Good")),
    ("Easy; Okay", ("Easy; Okay")),
    ("Difficult; Okay", ("Difficult; Okay")),
    ("Difficult; Great", ("Difficult; Great")),

]


class University(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    qs = models.CharField(max_length=50, blank=True, null=True)
    us = models.CharField(max_length=50, blank=True, null=True)
    public = models.CharField(max_length=50, blank=True, null=True)
    program = models.CharField(max_length=100, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    study_duration = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    other_email = models.EmailField(max_length=254, blank=True, null=True)
    gre = models.CharField(max_length=100, blank=True, null=True)
    gpa = models.CharField(max_length=100, blank=True, null=True)
    ielts = models.CharField(max_length=100, blank=True, null=True)
    toefl = models.CharField(max_length=100, blank=True, null=True)
    gmat = models.CharField(max_length=100, blank=True, null=True)
    fee = models.CharField(max_length=100, blank=True, null=True)
    fee_waiver = models.CharField(
        max_length=100, blank=True, null=True, choices=VAIWER_CHOICES)
    tutaion_fee = models.CharField(max_length=100, blank=True, null=True)
    admission_req = models.CharField(max_length=300, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    acceptance_rate = models.CharField(max_length=100, blank=True, null=True)
    graduation_rate = models.CharField(max_length=100, blank=True, null=True)

    # scholarship = models.CharField(max_length=500, blank=True, null=True)
    # scholarship_size = models.CharField(max_length=500, blank=True, null=True)
    # scholarship_req = models.CharField(max_length=500, blank=True, null=True)
    dedline = models.CharField(max_length=500, blank=True, null=True)
    result = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    evaluation = models.CharField(
        max_length=500, blank=True, null=True, choices=EVALUATION_CHOICES)

    def __str__(self) -> str:
        return self.name


RESEARCH_CHOICES = [
    ("0", ("0")),
    ("1", ("1")),

]

RATING_CHOICES = [
    ("1", ("1")),
    ("2", ("2")),
    ("3", ("3")),
    ("4", ("4")),
    ("5", ("5")),

]


class Admission(models.Model):
    gre = models.IntegerField()
    toefl = models.IntegerField()
    sop = models.FloatField()
    lor = models.FloatField()
    gpa = models.FloatField()
    admit_chance = models.FloatField()
    research = models.CharField(max_length=20, choices=RESEARCH_CHOICES)
    rating = models.CharField(max_length=20, choices=RATING_CHOICES)
