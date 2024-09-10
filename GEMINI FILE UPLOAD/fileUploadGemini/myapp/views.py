from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UploadForm
from .models import Document


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload_form')
        else:
            # Handle invalid login
            pass
    else:
        form = UserRegistrationForm()  # Reuse the form for login page messages (optional)
    return render(request, 'login.html', {'form': form})


@login_required
def account(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'account.html', {'documents': documents})


@login_required
def upload_form(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            document.user = request.user
            document.save()
            return redirect('upload_success')
    else:
        form = UploadForm()
    return render(request, 'upload_form.html', {'form': form})


@login_required
def upload_success(request):
    return render(request, 'upload_success.html')

def logout_user(request):
    logout(request)  # Call the built-in logout function
    return redirect('login')  # Redirect to login page after logout

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            document.user = request.user
            document.save()
            return redirect('upload_success')
    else:
        form = UploadForm()
    return render(request, 'upload_form.html', {'form': form})