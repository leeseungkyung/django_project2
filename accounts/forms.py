from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1','password2']