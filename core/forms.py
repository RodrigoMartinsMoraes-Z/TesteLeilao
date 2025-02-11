from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Leiloeiro, Matricula, Estado

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class MatriculaForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), empty_label="Selecione um estado")

    class Meta:
        model = Matricula
        fields = ['numero', 'estado']

class LeiloeiroCreationForm(forms.ModelForm):
    class Meta:
        model = Leiloeiro
        fields = ['nome', 'cpf', 'email', 'telefone', 'site']