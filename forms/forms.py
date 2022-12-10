from django import forms
from .models import Registeration


class RegisterationForm(forms.ModelForm):

    class Meta:
        model = Registeration
        fields = "__all__"
    
    def clean_terms_confirmed(self):
        terms_confirmed = self.cleaned_data.get('terms_confirmed')
        if not terms_confirmed:
            raise forms.ValidationError('This field is required')
        return terms_confirmed
