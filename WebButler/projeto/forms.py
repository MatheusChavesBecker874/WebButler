from django import forms
from .models import Rotina, Aula

class RotinaForm(forms.ModelForm):
    class Meta:
        model = Rotina
        fields = ["nome", "dias", "horario_inicio", "horario_fim"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "placeholder": "Ex: Rotina 2025.2",
                "class": "form-control"
            }),
            "dias": forms.TextInput(attrs={
                "placeholder": "Ex: seg/qua/sex",
                "class": "form-control"
            }),
            "horario_inicio": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control"
            }),
            "horario_fim": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control"
            }),
        }

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ["disciplina", "dia", "inicio", "fim"]

    def clean(self):
        cleaned_data = super().clean()
        # A lógica de conflito já está no `clean()` do model Aula
        return cleaned_data