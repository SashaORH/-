from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['phone', 'email', 'message']
        widgets = {
            'phone': forms.TextInput(attrs={
                'placeholder': '+7 (999) 123-45-67',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@mail.ru',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Ваше обращение...',
                'class': 'form-control',
                'rows': 4
            }),
        }
        labels = {
            'phone': 'Телефон',
            'email': 'Email',
            'message': 'Сообщение'
        }