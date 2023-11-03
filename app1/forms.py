from django import forms
from .models import Donor, BloodRequest

class MyForm(forms.Form):
    user_input = forms.CharField(label='Enter some text')

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = '__all__'
