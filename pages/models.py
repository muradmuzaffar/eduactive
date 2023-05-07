from django.db import models

# Create your models here.


VAIWER_CHOICES = [
    ("Available", ("Available")),
    ("Not Available", ("Not Available")),
    ("No info", ("No info"))

]


DEGREE_CHOICES = [
    ("Bachelor", ("Bachelor")),
    ("Master", ("Master")),
    ("Ph.D.", ("Ph.D.")),
    ("Exchange programme", ("Exchange programme")),
    ("Training programme", ("Training programme"))

]






REGION_CHOICES = [
    ("EU", ("EU")),
    ("US", ("US")),
    ("non-EU", ("non-EU")),

]

FIELD_CHOICES = [
    ("Business Management", ("Business Management")),
    ("Economics", ("Economics")),
    ("Social Sciences", ("Social Sciences")),
    ("Finance & Accounting", ("Finance & Accounting")),
    ("Physics", ("Physics")),
    ("Engineering", ("Engineering")),
    ("Analytics", ("Analytics")),
    ("Archaeology", ("Archaeology")),
    ("Chemistry", ("Chemistry")),
    ("Science", ("Science")),
    ("Computer Sciences", ("Computer Sciences")),
    ("Biology", ("Biology")),
    ("Astronomy", ("Astronomy")),
    ("Medicine", ("Medicine")),
    ("Informatics", ("Informatics")),
    ("Health", ("Health")),
    ("Biotechnology", ("Biotechnology")),
    ("Management", ("Management")),
    ("Nutrition", ("Nutrition")),
    ("Architecture", ("Architecture")),
    ("Technologies", ("Technologies")),
    ("Mechatronics", ("Mechatronics")),
    ("Technology", ("Technology")),
    ("Nanotechnologies", ("Nanotechnologies")),
    ("Bioengineering", ("Bioengineering")),
    ("Biomechanics", ("Biomechanics")),
    ("Design", ("Design")),
    ("Robotics", ("Robotics")),
    ("Systems", ("Systems")),
    ("Logistics", ("Logistics")),
    ("Nanobiotechnology", ("Nanobiotechnology")),
    ("Diagnostics", ("Diagnostics")),
    ("Cryptography", ("Cryptography")),
    ("Manufacturing", ("Manufacturing")),
    ("Nursing", ("Nursing")),
    ("Education", ("Education")),
    ("Arts", ("Arts")),
    ("Geography", ("Geography")),
    ("Mathematics", ("Mathematics")),
    ("Agriculture", ("Agriculture")),
    ("Geoinformatics", ("Geoinformatics")),
    ("Analysis", ("Analysis")),
    ("Economy", ("Economy")),
    ("Transport", ("Transport")),
    ("Industry", ("Industry")),
    ("Archeology", ("Archeology")),
    ("Studies", ("Studies")),
    ("Dietetics", ("Dietetics")),
    ("Sciences", ("Sciences")),
    ("Midwifery", ("Midwifery")),
    ("Training", ("Training")),
    ("Physiotherapy", ("Physiotherapy")),
    ("Telecommunication", ("Telecommunication")),
]




class Scholarship(models.Model):
    region = models.CharField(max_length=50, blank=True, null=True,choices=REGION_CHOICES)
    country = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    description = models.TextField()
    eligibity = models.TextField()
    benefits = models.TextField()
    link = models.CharField(max_length=300)
    dedline = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name



class University(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    qs_rank = models.CharField(max_length=50, blank=True, null=True)
    qs_id= models.CharField(max_length=50, blank=True, null=True)


    program = models.CharField(max_length=100, blank=True, null=True)
    study_field = models.CharField(max_length=100, blank=True, null=True,choices=FIELD_CHOICES)
    degree = models.CharField(max_length=100, blank=True, null=True,choices=DEGREE_CHOICES)

    study_duration = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    # other_email = models.EmailField(max_length=254, blank=True, null=True)

    gre = models.CharField(max_length=100, blank=True, null=True)
    gpa = models.CharField(max_length=100, blank=True, null=True)
    ielts = models.CharField(max_length=100, blank=True, null=True)
    toefl = models.CharField(max_length=100, blank=True, null=True)
    gmat = models.CharField(max_length=100, blank=True, null=True)

    fee = models.CharField(max_length=100, blank=True, null=True)
    # fee_waiver = models.CharField(max_length=100, blank=True, null=True, choices=VAIWER_CHOICES)
    tution_fee = models.CharField(max_length=100, blank=True, null=True)
    deadline = models.CharField(max_length=500, blank=True, null=True)

    country = models.CharField(max_length=100, blank=True, null=True,choices=REGION_CHOICES)
    state_city = models.CharField(max_length=100, blank=True, null=True)
    # city = models.CharField(max_length=100, blank=True, null=True)
    city_living_cost = models.CharField(max_length=100, blank=True, null=True)
    # acceptance_rate = models.CharField(max_length=100, blank=True, null=True)
    
    
    # graduation_rate = models.CharField(max_length=100, blank=True, null=True)  
    # result = models.CharField(max_length=500, blank=True, null=True)
    # link = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=3000, blank=True, null=True)



    

    # def __str__(self):
    #     return self.name


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






class Contact(models.Model):

    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    number = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.first_name





CATEGORY_CHOICES = [
    ("Sport", ("Sport")),
    ("Movie", ("Movie")),
    ("News", ("News")),
    ("Climate", ("Climate")),

]
class Blogs(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    quote = models.CharField(max_length=300,blank=True,null=True)
    image = models.ImageField()
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True,choices=CATEGORY_CHOICES)



    def __str__(self):
        return self.title
    
class Apply(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    university_name = models.CharField(max_length=250,blank=True,null=True)
    program = models.CharField(max_length=250,blank=True,null=True)
    gre = models.CharField(max_length=100, blank=True, null=True)
    gpa = models.CharField(max_length=100, blank=True, null=True)
    ielts = models.CharField(max_length=100, blank=True, null=True)
    toefl = models.CharField(max_length=100, blank=True, null=True)
    gmat = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    number = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.first_name

