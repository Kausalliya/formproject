from django import forms
from FormApp.models import employee
class employeeforms(forms.ModelForm):  
    class Meta:
        model = employee
        fields = '__all__'
        