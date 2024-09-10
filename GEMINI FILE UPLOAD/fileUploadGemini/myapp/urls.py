from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('account/', views.account, name='account'),
    path('logout/', views.logout_user, name='logout'),
    path('upload_form/', views.upload_form, name='upload_form'),
    path('upload/', views.upload_file, name='upload'),
    path('upload_success/', views.upload_success, name='upload_success'),
]
