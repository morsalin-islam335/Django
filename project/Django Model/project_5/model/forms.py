from django import forms


from model.models import modelTeacher



class Teacher(forms.ModelForm):
    class Meta:
        model = modelTeacher
        fields = '__all__'
        labels = {
            "id":"teacher's id",
            "name": "teacher's name",
            "subject": "subject"
        }
        # exclude = ['id']  # it will be show all fields without id fields
        widget = {
            'name': forms.TextInput(attrs = {'class': 'btn-primary'})
        }

        help_texts = {
            'id':"input id here",
            'subject': 'input subject here'
        }

        error_message = {
            "id":{'required': "id is required"} # nested dictionary
        }
