from django import forms
from django.contrib.auth.forms import UserCreationForm

class NewRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First name', max_length=250, 
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'first name'}))
    last_name = forms.CharField(label='last name', max_length=250, 
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'last name'}))
    email = forms.EmailField(label='email', max_length=250, 
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'email'}))
    phone = forms.CharField(label='phone', max_length=15,
                    widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'phone'}))
    password1 = forms.CharField(label='password',
                    widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'password'}))
    password2 = forms.CharField(label='repeat password', 
                    widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'repeat password'}))
    card_number = forms.CharField(label='card_number',max_length=350,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'card_number'}))
    card_name = forms.CharField(label='card_name',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'card_name'}))
    address= forms.CharField(label='address',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'address'}))
    billing_address = forms.CharField(label='billing_address',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'billing_address'}))
    city = forms.CharField(label='city',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'city'}))
    zip_code = forms.IntegerField(label='zip_code',
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'zip_code'}))
    premium_user = forms.BooleanField(label='premium_user',required=False,
                        widget=forms.CheckboxInput(attrs={'class':"form-control",'placeholder':'name'}))
    admin_user = forms.BooleanField(label='admin_user',required=False,
                        widget=forms.CheckboxInput(attrs={'class':"form-control",'placeholder':'name'}))

    

