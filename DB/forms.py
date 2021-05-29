from .models import User
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, PasswordInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'password', 'age', 'male', 'female']

        widgets = {
            "nickname": TextInput(attrs={
                'class': 'data data_reg',
                'placeholder': 'Логин',
            }),
            "password": PasswordInput(attrs={
                'class': 'data data_reg',
                'placeholder': 'Пароль',
            }),
            "age": NumberInput(attrs={
                'class': 'data data_reg',
                'placeholder': 'Возраст',
            }),
            "male": CheckboxInput(attrs={
                'class': 'data data_reg',
                'placeholder': 'муж',
            }),
            "female": CheckboxInput(attrs={
                'class': 'data data_reg',
                'placeholder': 'жен',
            })
        }