from django.forms import ModelForm
from .models import Appointment
from django import forms

class AppointmentForm(ModelForm):
    
    class Meta:
        model = Appointment
        fields = '__all__'