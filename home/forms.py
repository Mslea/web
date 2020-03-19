from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label='tai khoan',max_length=255)
    email = forms.EmailField(label='email',max_length=255)
    password1 = forms.CharField(label='mat khau',widget=forms.PasswordInput())
    password2 = forms.CharField(label='nhap lai pass',widget=forms.PasswordInput())
        
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password2:
                return password2
        raise forms.ValidationError('mat khau khong hop le')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('username khong hop le')
        try: 
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('username ton tai')

    def save(self):
        User.objects.create_user(username = self.cleaned_data['username'],email=self.cleaned_data['email'], password=self.cleaned_data['password1'])