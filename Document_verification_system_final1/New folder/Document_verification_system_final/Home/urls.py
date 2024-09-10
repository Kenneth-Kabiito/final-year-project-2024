from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('landing/', views.landing, name='landing'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('account/', views.account, name='account'),
    # path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('reset_confirm/<uidb64>/<token>/', views.reset_confirm, name='reset_confirm'),  
]
