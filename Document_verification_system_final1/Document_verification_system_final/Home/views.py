from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    return render(request, 'registration/index.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Correctly logs in the user
                return redirect('landing')  # Redirect to the landing page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


def password_reset(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Home/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                return redirect("/reset_confirm/")
    password_reset_form = PasswordResetForm()
    return render(request, "Home/password_reset.html", {"password_reset_form": password_reset_form})



def reset_confirm(request, uidb64=None, token=None):
    from django.contrib.auth.tokens import default_token_generator
    from django.contrib.auth.views import PasswordResetConfirmView

    class CustomPasswordResetConfirmView(PasswordResetConfirmView):
        template_name = "Home/reset_confirm.html"

    return CustomPasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token)
    return render(request, 'Home/reset_confirm.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('landing')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def about(request):
    return render(request, 'registration/about.html')

@login_required
def account(request):
    return render(request, 'registration/account.html')

def landing(request):
    return render(request, 'registration/landing.html')
