from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class sign_in(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

        