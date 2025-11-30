from django import forms
from .models import Rotina, Aula, Compromisso

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
    
class CompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ["titulo", "data_inicio", "data_fim", "lembrete_minutos"]
        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex: Reunião TCC"
            }),
            "data_inicio": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control"
            }),
            "data_fim": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "class": "form-control"
            }),
            "lembrete_minutos": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
                "placeholder": "30"
            }),
        }