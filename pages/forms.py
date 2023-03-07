from django import forms
from .models import Contact,University,Apply
from .models import DEGREE_CHOICES
from django.core.validators import MaxValueValidator,MinValueValidator


options = University.objects.values_list('program', flat=True)


class AdmissionForm(forms.Form):
    gpa = forms.FloatField(widget=forms.NumberInput(attrs={
        'placeholder': '/4',
        'class':"d-block cs-input mt-2"
    }), validators=[MinValueValidator(0), MaxValueValidator(4)])

    gre = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': '/340',
        'class':"d-block cs-input mt-2"
    }))

    ielts = forms.FloatField(widget=forms.NumberInput(attrs={
        'placeholder': '/9',
        'class':"d-block cs-input mt-2"
    }))

    gmat = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': '/800',
        'class':"d-block cs-input mt-2"
    }))

    toefl = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': '/120',
        'class':"d-block cs-input mt-2"
    }))

    degree = forms.ChoiceField(widget=forms.Select(attrs={
        'placeholder': 'select Degree',
        'class':"d-block cs-input mt-2",
    }), choices=DEGREE_CHOICES)

    # program = forms.ChoiceField(widget=forms.Select(attrs={
    #     'placeholder': 'select Degree',
    #     'class':"d-block cs-input mt-2",
    # }), choices=options[0:5])


    def __init__(self, *args, **kwargs):
        super(AdmissionForm, self).__init__(*args, **kwargs)
        self.fields['gmat'].required = False
        self.fields['gre'].required = False
        self.fields['ielts'].required = False
        self.fields['toefl'].required = False
        





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



class ApplyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
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
    class Meta:
        model = Apply
        fields = ['name','email']