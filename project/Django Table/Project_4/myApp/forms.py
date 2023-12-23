from django import forms  # import forms api

class Contact(forms.Form): # inherit forms api's  Form
    # name = forms.CharField(label="user name") # CharField() is for char type or string type
    # email = forms.EmailField(label= "user email")# EmailField  for email type  
    name = forms.CharField(label="User name:")
    email = forms.EmailField(label="User email:")
    age = forms.IntegerField(label="Age:", required=False)
    weight = forms.FloatField(label="Weight:")
    balance = forms.DecimalField(label="Balance:")
    birthday = forms.DateField(label="Birthday:")
    appointment = forms.DateTimeField(label= "Appointment time:")
    hobby = forms.ChoiceField(choices=[('P', "Coding"), ('G', "Gardening"), ("C", "Participating CP")], label="Hobby:")
    food = forms.MultipleChoiceField(choices=[("M", "Mango"),("B","Banana"),("A", "Apple"), ("C","Coconut")],  label="Favoirate Food")
    condition = forms.BooleanField(label="Terms and Condition")
    # choice single value between multiple value

    