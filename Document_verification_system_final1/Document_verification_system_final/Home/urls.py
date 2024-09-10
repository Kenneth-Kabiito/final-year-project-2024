from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('upload_form/', views.upload_form, name='upload_form'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('account/', views.account, name='account'),
    # path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('password_reset/', views.password_reset, name='password_reset'),
    # path('reset_confirm/<uidb64>/<token>/', views.reset_confirm, name='reset_confirm'),
    path('upload_success/', views.upload_success, name='upload_success'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('process_document/', views.process_document, name='process_document'),
    # path('view_upload/<int:uploaded_file_id>/', views.view_upload, name='view_upload'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)