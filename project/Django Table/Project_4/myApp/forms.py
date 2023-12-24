from django import forms  # import forms api

class Contact(forms.Form): # inherit forms api's  Form
    user = forms.CharField(label="user name", initial="Morsalin", help_text="input your full name")
    profile_pic = forms.FileField()
    name = forms.CharField(label="User name:")
    email = forms.EmailField(label="User email:")
    age = forms.IntegerField(label="Age:", required=False)
    weight = forms.FloatField(label="Weight:")
    balance = forms.DecimalField(label="Balance:")
    # birthday = forms.DateField(label="Birthday:")  #that is a valid process
    birthday = forms.CharField(label="Birthday:", widget=forms.DateInput(attrs={"type": 'date'}))
    # appointment = forms.DateTimeField(label= "Appointment time:")
    appointment = forms.CharField(label= "Appointment time:", widget=forms.DateInput(attrs={"type":"datetime-local"}))
    hobby = forms.ChoiceField(choices=[('P', "Coding"), ('G', "Gardening"), ("C", "Participating CP")], label="Hobby:", widget=forms.RadioSelect)
    food = forms.MultipleChoiceField(choices=[("M", "Mango"),("B","Banana"),("A", "Apple"), ("C","Coconut")],  label="Favoirate Food", widget = forms.CheckboxSelectMultiple)
    comment = forms.CharField(label="comment", widget = forms.Textarea(attrs = {"class":'class1',"id":'text-area-id',"placeholder":'Comments here'})) 
    condition = forms.BooleanField(label="Terms and Condition")  #choice single value between multiple value

    