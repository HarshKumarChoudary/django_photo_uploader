from django import forms 
from .models import imageTable

class imgform(forms.ModelForm):
    class Meta:
        model = imageTable
        fields = '__all__'
        labels = {'image':''}