from django.forms import ModelForm, TextInput, NumberInput
from polls.models import Survey

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        # fields = '['user_name', 'user_age']'
        fields = '__all__' # select the all the fields
        labels = {
            "user_name": "User Name",
            "user_age": "User Age",
        }
        widgets = {
            'user_name': TextInput(attrs={'class': 'form-control'}),
            'user_age': NumberInput(attrs={'class': 'form-control'})
        }