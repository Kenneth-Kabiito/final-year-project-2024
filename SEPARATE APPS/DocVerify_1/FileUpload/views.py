from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
from django.contrib.auth import logout

def upload_success(request):
    return render(request, 'FileUpload:upload_success.html')  # Adjust template name if needed

def results(request):
    return render(request, 'results.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def logout(request):
    return render(request, 'Authenticate:index')

def upload_form(request):
    return render(request, 'FileUpload:upload_form.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()  # Save the uploaded file
            return render(request, 'FileUpload:upload_success.html', {'uploaded_file': uploaded_file})  # Pass uploaded file to template
    else:
        form = UploadFileForm()
    return render(request, 'upload_form.html', {'form': form})

# def view_upload(request, uploaded_file_id):
#     try:
#         uploaded_file = UploadedFile.objects.get(pk=uploaded_file_id)
#         return render(request, 'view_upload.html', {'uploaded_file': uploaded_file})
#     except UploadedFile.DoesNotExist:
#         return render(request, 'error.html', {'message': 'File not found'})  # Handle missing file (optional)
