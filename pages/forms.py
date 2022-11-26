from django import forms
from .models import Admission,Contact

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['gre','toefl','sop','lor','gpa','research','rating']
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
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'id':'name'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Surname',
        'id':'subject'

    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'id':'email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Message',
        'id':'message'

    }))

    class Meta:
        model = Contact
        fields = ['name', 'subject',
                  'email', 'message']