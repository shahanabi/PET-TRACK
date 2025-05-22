from django import forms
from .models import GroomingBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = GroomingBooking
        fields = ['pet_name', 'owner_name', 'date', 'time', 'address']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
