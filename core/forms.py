from django import forms
from .models import Aluno, Turma

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "sobrenome", "endereco", "dtnasc", "turma"]

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ["nome", "turno"]
