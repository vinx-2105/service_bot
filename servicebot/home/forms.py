from django import forms
from home.models import Locations

class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ['name', 'path']
