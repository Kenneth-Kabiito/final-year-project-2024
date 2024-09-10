from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

@login_required
def about(request):
    return render(request, 'registration/about.html')

@login_required
def account(request):
    return render(request, 'registration/account.html')

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
                return redirect('FileUpload:upload_form')  # Redirect to the landing page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'Authenticate:registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('FileUpload:upload_form')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
