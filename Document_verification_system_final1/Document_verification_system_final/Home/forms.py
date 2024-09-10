from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
    middle_name = forms.CharField(max_length=30, required=False, help_text='Middle Name')
    last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')
    email = forms.EmailField(max_length=254, required=True, help_text='Email Address')
    username = forms.CharField(max_length=30, required=True, help_text='Last Name')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.username = self.cleaned_data['username']
        
        if commit:
            user.save()
        return user

# class UpdateProfileForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=30, required=True, help_text='First Name')
#     last_name = forms.CharField(max_length=30, required=True, help_text='Last Name')
#     email = forms.EmailField(max_length=254, required=True, help_text='Email Address')
#     username = forms.CharField(max_length=30, required=True, help_text='Last Name')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')

#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.username = self.cleaned_data['username']
        
#         if commit:
#             user.save()
#         return user