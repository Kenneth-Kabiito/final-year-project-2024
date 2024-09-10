from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
import cv2
import tensorflow as tf
from django.http import HttpResponseRedirect
from .models import UploadedFile
from .forms import FileUploadForm


@login_required
def upload_success(request):
    return render(request, 'registration/upload_success.html')

@login_required
def about(request):
    return render(request, 'registration/about.html')

@login_required
def account(request):
    return render(request, 'registration/account.html')

@login_required
def upload_form(request):
    return render(request, 'registration/upload_form.html')

@login_required
def results(request):
    return render(request, 'results.html')

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
                return redirect('upload_form')  # Redirect to the landing page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('upload_form')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()  # Save the uploaded file
            return redirect(request, 'registration/upload_success.html', {'uploaded_file': uploaded_file})
    else:
        form = FileUploadForm()
    return render(request, 'upload_form.html', {'form': form})


def process_document(file_path):
    # Load the image
    image = cv2.imread(file_path)
    # Preprocess the image
    image = cv2.resize(image, (224, 224))  # Example resize, adjust based on your model
    image = image / 255.0  # Normalize if required
    image = image.reshape(1, 224, 224, 3)  # Adjust shape based on your model

    # Load the model
    model = tf.keras.models.load_model(settings.MODEL_PATH)

    # Make predictions
    predictions = model.predict(image)

    # Process predictions as needed
    print(predictions)
