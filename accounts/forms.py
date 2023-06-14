from typing import Any, Dict
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password2 = forms.CharField(max_length = 50, widget = forms.PasswordInput(attrs={
            'placeholder': 'confirm password',
            'class' : 'form-control'
        }))
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password']

        widgets = { 
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'username'
            }),
             'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'First name'
            }),
             'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Last name'
            }),
             'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder' : 'email'
            }),
             'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder' : 'password'
            })
        }

    def clean(self) -> Dict[str, Any]:
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Password not same')
        return super().clean()

    def save(self, commit: bool = ...) -> Any:
        self.instance.set_password(self.instance.password)
        self.instance.save()
        return super().save(commit)