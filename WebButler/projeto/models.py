from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from datetime import time
from django.utils import timezone

# Turmas ----------------

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="alunos", null=True, blank=True)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True) 



class Turma2(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno2(models.Model):
    nome = models.CharField(max_length=100)
    turma = models.ForeignKey(Turma2, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.turma.nome}"



class Atividade2(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    turma = models.ForeignKey(Turma2, on_delete=models.CASCADE, related_name="atividades")
    progresso = models.IntegerField(default=0)
    
    horario_inicio = models.TimeField(null=True, blank=True)
    horario_fim = models.TimeField(null=True, blank=True)


    def __str__(self):
        return self.titulo

# Rotinas ------------

class Rotina(models.Model):
    nome = models.CharField(max_length=100)
    dias = models.CharField(max_length=100, default='')
    horario_inicio = models.TimeField(default="00:00")
    horario_fim = models.TimeField(default="00:00")
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Aula(models.Model):
    rotina = models.ForeignKey(Rotina, on_delete=models.CASCADE, related_name="aulas")
    disciplina = models.CharField(max_length=200)
    dia = models.CharField(max_length=10, choices=[
        ("seg", "Segunda"), ("ter", "Terça"), ("qua", "Quarta"),
        ("qui", "Quinta"), ("sex", "Sexta"), ("sab", "Sábado"), ("dom", "Domingo")
    ])
    inicio = models.TimeField()
    fim = models.TimeField()
    
    def clean(self):
        if self.inicio >= self.fim:
            raise ValidationError("Hora de início deve ser antes da hora de fim")
        
        conflitos = self.__class__.objects.filter(
            rotina=self.rotina, dia=self.dia
            ).exclude(id=self.id)
        
        for aula in conflitos:
            if self.inicio < aula.fim and self.fim > aula.inicio:
                raise ValidationError(
                    f"Conflito entre {self.disciplina} e {aula.disciplina} no dia {self.dia}"
                    )

    def __str__(self):
        return f"{self.disciplina} - {self.dia} ({self.inicio} às {self.fim})"