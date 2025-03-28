from django import forms
from .models import CVEntry

class CVEntryForm(forms.ModelForm):
    class Meta:
        model = CVEntry
        exclude = ['cv']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'order': forms.NumberInput(attrs={'min': 0})
        }
