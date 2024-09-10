from django.shortcuts import render, redirect
from .forms import DocumentForm

def home(request):
    return render(request, 'home/upload_document.html')

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
        	form.save()
        	return redirect('document_list')
    else:
    	form = DocumentForm()
    	return render(request, 'upload_document.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents', documents})
        