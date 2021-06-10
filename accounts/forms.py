from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, PasswordInput


# forms.py
class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'class': 'data data_reg',
                'placeholder': 'Логин',
            }),
            "password": PasswordInput(attrs={
                'class': 'data data_reg',
                'placeholder': 'Пароль',
            })
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user