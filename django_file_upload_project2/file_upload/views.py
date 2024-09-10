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
from .forms import UploadFileForm
from .models import UploadedFile

def index(request):
    return render(request, 'index.html')

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
    return render(request, 'register.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()  # Save the uploaded file
            return render(request, 'upload_success.html', {'uploaded_file': uploaded_file})
    else:
        form = UploadFileForm()
    return render(request, 'upload_form.html', {'form': form})

def view_upload(request, uploaded_file_id):
    try:
        uploaded_file = UploadedFile.objects.get(pk=uploaded_file_id)
        return render(request, 'view_upload.html', {'uploaded_file': uploaded_file})
    except UploadedFile.DoesNotExist:
        return render(request, 'error.html', {'message': 'File not found'})


def upload_success(request):
    return render(request, 'upload_success.html')  # Adjust template name if needed

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

def upload_success(request):
    return render(request, 'upload_success.html')


def about(request):
    return render(request, 'about.html')

@login_required
def account(request):
    return render(request, 'account.html')

def landing(request):
    return render(request, 'upload_form.html')

