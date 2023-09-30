
from .forms import NewRegisterForm, LoginForm
from .models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return HttpResponse("Hola, bienvenido a la tienda.")

def register(request):
    message = 0
    if request.method == 'POST':
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["premium_user"] and form.cleaned_data["admin_user"]:
                form.add_error(None, "No puedes ser tanto un usuario premium como un administrador al mismo tiempo.")
                message = 2  
            else:
                try:
                    registers = User()
                    registers.name = form.cleaned_data["name"]
                    registers.last_name = form.cleaned_data["last_name"]
                    registers.email = form.cleaned_data["email"]
                    registers.phone = form.cleaned_data["phone"]
                    registers.password = make_password(form.cleaned_data["password"])
                    registers.card_number = form.cleaned_data["card_number"]
                    registers.card_name = form.cleaned_data["card_name"]
                    registers.address = form.cleaned_data["address"]
                    registers.billing_address = form.cleaned_data["billing_address"]
                    registers.city = form.cleaned_data["city"]
                    registers.zip_code = form.cleaned_data["zip_code"]
                    registers.premium_user = form.cleaned_data["premium_user"]
                    registers.admin_user = form.cleaned_data["admin_user"]
                    registers.save()
                    message = 1
                    form = NewRegisterForm()
                    return redirect('profile')

                except:
                    message = 3 
        else:
            message = 2 
    else:
        form = NewRegisterForm()

    context = {
        'form': form,
        'message': message,
    }

    return render(request, "register.html", context=context)





# Create your views here.


