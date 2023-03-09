from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import GENDER_CHOICES
from pages.models import DEGREE_CHOICES


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control cs-input',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control cs-input passborder',
        'placeholder': 'Password',
        'aria-describedby': 'showHidePass'
    }))


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control cs-input',
        'placeholder': 'First Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control cs-input',
        'placeholder': 'Last Name'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control cs-input',
        'placeholder': 'Username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control cs-input',
        'placeholder': 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control cs-input',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control cs-input',
        'placeholder': 'Re-Type Password'
    }))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


class UpdateUserForm(forms.ModelForm):
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


    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']




class ProfileForm(forms.ModelForm):
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

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+994 (00) 000 00 00',
        'class':'cs-input mt-2',
        'name':'phoneNumber',
        'id':'phoneNumber',
        'type':'number',
        'pattern':""

    }))
    gender = forms.ChoiceField(widget=forms.Select(attrs={
        'placeholder': 'select Gender',
        'class':"d-block cs-input mt-2",
    }), choices=GENDER_CHOICES)

    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'placeholder': 'select Gender',
        'class':"cs-input mt-2",
        'type':'date',
        
    }))

    #Background

    gpa = forms.FloatField(widget=forms.NumberInput(attrs={
        'placeholder': '/4',
        'class':"d-block cs-input mt-2"
    }))

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

    university = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter University',
        'class':'cs-input mt-2',
        'type':'text'

    }))

    speciality = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Speciality',
        'class':'cs-input mt-2',
        'type':'text'
    }))

    class Meta:
        model = Profile
        fields = ['first_name','last_name','email','phone_number','birthday','gender',
                  'gpa','gre','ielts','toefl','gmat','university','speciality','degree']
        
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['gmat'].required = False
        self.fields['gpa'].required = False
        self.fields['gre'].required = False
        self.fields['ielts'].required = False
        self.fields['toefl'].required = False
        self.fields['university'].required = False
        self.fields['speciality'].required = False
        self.fields['degree'].required = False


        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['email'].required = False
        self.fields['phone_number'].required = False
        self.fields['birthday'].required = False
        self.fields['gender'].required = False

