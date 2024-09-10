from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
app_name = 'VerifyDocs'

urlpatterns = [
    path('', views.process_file, name='process_file'),
    path('verify_success/', views.verify_success, name='verify_success'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
