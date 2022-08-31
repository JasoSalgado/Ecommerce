# accounts/views.py
# Django modules
from email.message import EmailMessage
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

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
            
            # Creates a username from a user´s email
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                username=username,
                                                password=password)
            user.phone_number = phone_number
            user.save()                                    

            # Activating user sending an email
            current_site = get_current_site(request)
            mail_subject = "Por favor activa tu cuenta en E-commerce"
            body = render_to_string("accounts/account_verification_email.html", {
                "user": user, 
                "domain": current_site,
                # It is not recommended to send public uid´s, that is we have to encode it
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            })

            # Process of sending emails
            to_email = email
            send_email = EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()


            #messages.success(request, "Se registró el usuario exitosamente")

            return redirect("/accounts/login/?command=verification&email="+email)

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
            messages.success(request, "Has iniciado sesión exitosamente.")
            return redirect("dashboard")
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


def activate(request, uidb64, token):
    """
    Activate account
    """
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Felicidades tu cuenta está activada.")
        return redirect("login")
    else:
        messages.error(request, "La activación es inválida.")
        return redirect("register")


@login_required(login_url="login")
def dashboard(request):
    """
    Dashboard path.
    Users logged only
    """
    return render(request, "accounts/dashboard.html")