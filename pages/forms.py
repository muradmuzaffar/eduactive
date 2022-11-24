from django import forms
from .models import Admission

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