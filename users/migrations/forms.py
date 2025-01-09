from .models import registrationmodel
from django import forms

class registrationform(forms.ModelForm):

    class Meta:
        model = registrationmodel
        fields = '__all__'