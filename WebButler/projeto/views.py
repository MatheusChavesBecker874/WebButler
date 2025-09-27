from django.shortcuts import render, redirect
from .models import Atividade, Turma, Aluno
from django.shortcuts import render

# ---------- ATIVIDADES ----------
def lista_atividades(request):
    atividades = Atividade.objects.all()
    return render(request, "lista_atividades.html", {"atividades": atividades})

def criar_atividade(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        turma_id = request.POST.get("turma")

        turma = Turma.objects.get(id=turma_id) if turma_id else None
        Atividade.objects.create(titulo=titulo, descricao=descricao, turma=turma)
        return redirect("lista_atividades")

    turmas = Turma.objects.all()
    return render(request, "criar_atividade.html", {"turmas": turmas})


# ---------- TURMAS ----------
def lista_turmas(request):
    turmas = Turma.objects.all()
    return render(request, "lista_turmas.html", {"turmas": turmas})

def criar_turma(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        Turma.objects.create(nome=nome)
        return redirect("lista_turmas")
    return render(request, "criar_turma.html")


# ---------- ALUNOS ----------
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, "lista_alunos.html", {"alunos": alunos})

def criar_aluno(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        turma_id = request.POST.get("turma")

        turma = Turma.objects.get(id=turma_id) if turma_id else None
        Aluno.objects.create(nome=nome, turma=turma)
        return redirect("lista_alunos")

    turmas = Turma.objects.all()
    return render(request, "criar_aluno.html", {"turmas": turmas})

def inicio(request):
    return render(request, 'inicio.html')