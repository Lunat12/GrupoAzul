from django import forms
from django.contrib.auth.forms import AuthenticationForm


class NewRegisterForm(forms.Form):
    name = forms.CharField(label='name',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'name'}))
    last_name = forms.CharField(label='last_name',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'last_name'}))
    email = forms.CharField(label='email',max_length=250,
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'email'}))
    phone = forms.IntegerField(label='phone',
                        widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'phone'}))
    password = forms.CharField(label='password',
                        widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'password'}))
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
    
class LoginForm(AuthenticationForm):
    email = forms.CharField(label='Email', max_length=250, 
                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', 
                        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
