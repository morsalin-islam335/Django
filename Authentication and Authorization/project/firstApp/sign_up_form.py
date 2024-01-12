from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms

class sign_up(UserCreationForm):
    first_name = forms.CharField(max_length= 60, widget=forms.TextInput(attrs={'id': "required"}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

        