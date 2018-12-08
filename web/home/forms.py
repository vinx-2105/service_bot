from django import forms
from home.models import Location, Order

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'path']

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['source', 'destination']
        widgets = {
            'source':forms.Select,
            'destination':forms.Select,
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
