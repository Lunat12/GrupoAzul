
from Bicify.tienda.forms import NewRegisterForm
from .models import User
from django.shortcuts import render

def register(request):
    message = 0
    if request.method == 'POST':
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            try:
                registers=User()
                registers.name = form.cleaned_data["name"]
                registers.last_name = form.cleaned_data["last_name"]
                registers.email = form.cleaned_data["email"]
                registers.phone = form.cleaned_data["phone"]
                registers.password = form.cleaned_data["password"]
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
                form=NewRegisterForm()
            except:
                message = 3
        else:
            message = 2
    else:
        form = NewRegisterForm()
    
    context={
        'form':form,
        'message':message,
    }

    return render(request,"register.html",context=context)



# Create your views here.
