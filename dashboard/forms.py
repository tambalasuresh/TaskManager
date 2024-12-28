from django import forms
from user.models import CustomUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'phone_number', 'email', 'password']