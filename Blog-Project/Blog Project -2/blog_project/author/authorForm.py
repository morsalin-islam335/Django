from django import forms


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# class ProfileForm(forms.ModelForm):
#     class Meta():
#         model = Author
#         fields = "__all__"



class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs= {"id": 'required'}))
    last_name = forms.CharField(max_length = 50, widget = forms.TextInput())

    class Meta:
        model = User
        fields  = ['username','first_name','email']
        
