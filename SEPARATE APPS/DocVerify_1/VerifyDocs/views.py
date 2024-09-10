from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Correctly logs in the user
                return redirect('Authenticate:upload_form')  # Redirect to the landing page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'Authenticate:registration/login.html', {'form': form})

@login_required
def process_file(request):
    return render(request, 'process_file.html')  # Adjust template name if needed

@login_required
def verify_success(request):
    return render(request, 'verify_success.html')

def logout_view(request):
    logout(request)
    return redirect('Authenticate:index')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_file = form.save()  # Save the uploaded file
#             return render(request, 'FileUpload:upload_success.html', {'uploaded_file': uploaded_file})  # Pass uploaded file to template
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload_form.html', {'form': form})

# def view_upload(request, uploaded_file_id):
#     try:
#         uploaded_file = UploadedFile.objects.get(pk=uploaded_file_id)
#         return render(request, 'view_upload.html', {'uploaded_file': uploaded_file})
#     except UploadedFile.DoesNotExist:
#         return render(request, 'error.html', {'message': 'File not found'})  # Handle missing file (optional)
