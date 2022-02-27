import email
from itertools import tee
from django import forms
from django.core.exceptions import ValidationError

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label= 'Enter Your Email Again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data.get('verify_email')

        if email != vmail:
            raise forms.ValidationError("Make Sure Emails Match")