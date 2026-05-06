from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Projeto
from .models import Tecnologia
from .models import Competencia
from .models import Formacao

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__' 

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'

class RegistoForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='Nome', required=True)
    last_name = forms.CharField(label='Apelido', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']





