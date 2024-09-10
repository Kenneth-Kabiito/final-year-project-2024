from django.urls import path, include
from django.contrib import admin
from . import views
app_name = 'FileUpload'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_form/', views.upload_form, name='upload_form'),
    path('upload_success/', views.upload_success, name='upload_success'),
    # path('view_upload/<int:uploaded_file_id>/', views.view_upload, name='view_upload'),
    path('upload_file/', views.upload_file, name='upload_file'),
]
