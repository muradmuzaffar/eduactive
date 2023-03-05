from django import forms
from .models import Admission,Contact
from .models import DEGREE_CHOICES

class AdmissionForm(forms.ModelForm):
    gpa = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '/100',
        'class':"d-block cs-input mt-2"
    }))

    gre = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '/340',
        'class':"d-block cs-input mt-2"
    }))

    ielts = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '/9',
        'class':"d-block cs-input mt-2"
    }))

    degree = forms.ChoiceField(widget=forms.Select(attrs={
        'placeholder': 'select Degree',
        'class':"d-block cs-input mt-2",
    }), choices=DEGREE_CHOICES)
    class Meta:
        model = Admission
        fields = ['gre','gpa','ielts','degree']
        labels = {
            'gre':'GRE Scores ( out of 340 )',
            'toefl':'TOEFL Scores ( out of 120 )',
            'sop':'Statement of Purpose -(SOP) Strength ( out of 5 )',
            'lor':'Letter of Recommendation-(LOR) Strength ( out of 5 )',
            'gpa':'Undergraduate GPA-CGPA ( out of 10 )',
            'research':'Research Experience ( either 0 or 1 )',
            'rating':'University Rating ( out of 5 )',
        }




class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Name',
        'class':'cs-input mt-2',
        'name':'firstName',
        'id':'firstName',
        'type':'text'

    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Last Name',
        'class':'cs-input mt-2',
        'name':'lastName',
        'id':'lastName',
        'type':'text'
    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'sendme@mail.com',
        'class':'cs-input mt-2',
        'name':'email',
        'id':'email',
        'type':'email'
    }))

    number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+994 (00) 000 00 00',
        'class':'cs-input mt-2',
        'name':'phoneNumber',
        'id':'phoneNumber',
        'type':'number',
        'pattern':""

    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'I am reaching you for',
        'class':'cs-input mt-2',
        'name':'message',
        'id':'message',

    }))

    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','number','message']

        