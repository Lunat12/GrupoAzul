
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewRegisterForm
from .models import Registers

def index(request):
    return HttpResponse("Hola, bienvenido a la tienda.")

def register(request):
    message = 0
    registers = None
    if request.method == 'POST':
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()

                registers=Registers.objects.create(
                    id_user=user,
                    phone=form.cleaned_data['phone'],
                    card_number=form.cleaned_data['card_number'],
                    card_name=form.cleaned_data['card_name'],
                    address=form.cleaned_data['address'],
                    billing_address=form.cleaned_data['billing_address'],
                    city=form.cleaned_data['city'],
                    zip_code=form.cleaned_data['zip_code'],
                    premium_user=form.cleaned_data['premium_user'],
                    admin_user=form.cleaned_data['admin_user']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.save()


                message = 1
                form = NewRegisterForm()
            
            except:
                    message = 3
        else:
            message = 2
    else:
        form = NewRegisterForm()

    context = {
        'form': form,
        'message': message,
        'registers':registers,
    }

    return render(request, "register.html", context=context)


def login(request):
    if request.method=='POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('profile')
    else:
        form=AuthenticationForm()

    context={
        'form':form,
    }

    return render(request,'login.html',context=context)



def profile(request):
    if request.user.is_authenticated:
        user=request.user
        registers=Registers.objects.get(id_user=user)

    context={
        'user':user,
        'registers':registers,
    }

    return render(request,'profile.html',context=context)
# Create your views here.


