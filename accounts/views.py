# accounts/views.py
# Django modules
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# My modules
from accounts.forms import RegistrationForm
from accounts.models import Account

def register(request):
    """
    Register new user
    """
    # An instance of forms.py RegistrationForm
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Capture data from client
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # Creates a username from user´s email
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                username=username,
                                                password=password)
            user.phone_number = phone_number
            user.save()                                    

            messages.success(request, "Se registró el usuario exitosamente")
            return redirect("register")

    context = {
        "form": form,
    }

    return render(request, "accounts/register.html", context)


def login(request):
    """
    Login user
    """
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Las credenciales son incorrectas.")
            return redirect("login")


    return render(request, "accounts/login.html")


@login_required(login_url="login")
def logout(request):
    """
    Logout
    """
    auth.logout(request)
    messages.success(request, "Has cerrado tu sesión")
    
    return redirect("login")