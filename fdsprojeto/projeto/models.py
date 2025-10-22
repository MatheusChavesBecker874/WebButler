from django.db import models

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
