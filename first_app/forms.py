from dataclasses import field, fields
import email
from itertools import tee
from django import forms
from django.core.exceptions import ValidationError

from .models import User
from first_app.models import UserProfileInfor

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

# this is for admin
class NewUserForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label= 'Enter Your Email Again')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data.get('verify_email')

        if email != vmail:
            raise forms.ValidationError("Make Sure Emails Match")

    class Meta():
        model = User
        fields = ['name', 'email']

# this is for user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfor
        fields = ('portfolio_site', 'profile_pic')

