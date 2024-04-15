from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, label='Adresse Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse Email'}))
    username = forms.CharField(max_length=150, label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}))
    password1 = forms.CharField(max_length=150, label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(max_length=150, label="Confirmer le mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'autofocus': True})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})