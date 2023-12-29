from django import forms  # import forms api

from django.core import validators

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

    

# class StudentData(forms.Form):
#     name = forms.CharField(widget = forms.TextInput)
#     email = forms.CharField(widget = forms.EmailInput)

#     # def clean_name(self):
#     #     valName = self.cleaned_data['name']
#     #     if len  (valName) <10:
#     #         raise forms.ValidationError("name will be min 10 char")
        

#     # def clean_email(self):
#         # valName = self.cleaned_data['email']
#         # if '.com' not in valName:
#         #     raise forms.ValidationError("your forms must be contain .com")

#         # check all validation 
        

#     def clean(self):
#         cleaned_data = super().clean() # it will be give all data
#         print("printing cleand data",cleaned_data) # it also give same output
#         print("printing validate data", self.cleaned_data)
#         valemail = self.cleaned_data['email']
#         if '.com' not in valemail:
#             raise forms.ValidationError("your email must be contain .com")
    

def commentValidator(value):
    if len(value) >= 100:
        raise forms.ValidationError("Char limit is 100")
    
class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter your name"}), validators = [validators.MaxLengthValidator(20, message = "Max length will be 20"), validators.MinLengthValidator(5, message="min chars will be 5")])

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder":"Enter your valid email"}), 
        validators=[validators.EmailValidator(message="input email is not a valid email")])

    age = forms.IntegerField(
    validators=[
        validators.MaxValueValidator(32, message="Your age won't be over 31"),
        validators.MinValueValidator(19, message="Your age won't be less than 19")
    ]
)

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['png','pdf'],message="allowed extension are .jpg and .pdf")])

    comment = forms.CharField(label="Comment", validators= [commentValidator])

    numeric_field = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'Enter a number'}))

    




