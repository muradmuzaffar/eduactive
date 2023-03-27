import django_filters
from django import forms

from .models import University,Scholarship, DEGREE_CHOICES, REGION_CHOICES,VAIWER_CHOICES,FIELD_CHOICES


class ListingFiLtersUniversity(django_filters.FilterSet):
    degree = django_filters.MultipleChoiceFilter(
        choices = DEGREE_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'id':'degree'} ,))
    
    region = django_filters.MultipleChoiceFilter(
        choices = REGION_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'id':'degree'} ,))
    
    fee_waiver = django_filters.MultipleChoiceFilter(
        choices = VAIWER_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'id':'degree'} ,))
    
    study_field = django_filters.MultipleChoiceFilter(
        choices = FIELD_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'id':'degree'} ,))
    class Meta:
        model = University
        fields = {
            'fee_waiver': ['exact'],
            'region':  ['exact'],
            'degree':  ['exact'],
            'study_field':  ['exact'],
        }






class ListingFiLtersScholarship(django_filters.FilterSet):
    degree = django_filters.MultipleChoiceFilter(
        choices = DEGREE_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'id':'degree'} ,))
    
    region = django_filters.MultipleChoiceFilter(
        choices = REGION_CHOICES,
        widget = forms.CheckboxSelectMultiple(attrs={'class':'form-check-input', 'id':'degree'} ,))


    class Meta:
        model = Scholarship
        fields = ['degree','region']

