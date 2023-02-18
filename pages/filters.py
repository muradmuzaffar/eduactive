import django_filters
from django import forms

from .models import University,Scholarship, DEGREE_CHOICES


class ListingFiLters(django_filters.FilterSet):
    class Meta:
        model = University
        fields = {
            'fee_waiver': ['exact'],
            'region':  ['exact'],
            'degree':  ['exact'],
        }



# DEGREE_CHOICES = [
#     ("Bachelor", ("Bachelor")),
#     ("Master", ("Master")),
#     ("PHD", ("PHD")),

# ]


class ListingFiLtersScholarship(django_filters.FilterSet):
    degree = django_filters.MultipleChoiceFilter(
    choices = DEGREE_CHOICES,
    widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'id':'degree'} ,))


    class Meta:
        model = Scholarship
        fields = ['degree']

