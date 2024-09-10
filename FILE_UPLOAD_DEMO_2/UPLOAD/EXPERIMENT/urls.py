from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='upload_document'),
    path('upload/', views.upload_document, name="upload_document"),
    path('documents/', views.document_list, name='document_list'),
]