from django.shortcuts import render, redirect, get_object_or_404
from .models import Turma2, Aluno2, Atividade2
from django.http import HttpResponse

# ---------- Página inicial ----------
def inicio(request):
    return render(request, "inicio.html")

# ---------- Visualizar Alunos ----------
def lista_alunos(request):
    alunos = Aluno2.objects.all()
    return render(request, "alunos/lista.html", {"alunos": alunos})

def novo_aluno(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")

        if nome and email:
            Aluno2.objects.create(nome=nome, email=email)
            return redirect("lista_alunos")

    return render(request, "alunos/novo.html")

# ---------- Turma ----------
def nova_turma(request):
    if request.method == "POST":
        nome = request.POST.get("nome")

        if nome:
            Turma2.objects.create(nome=nome)
            return redirect("lista_turmas")

    return render(request, "turmas/nova.html")


# ---------- Visualizar/Criar Atividades ----------
def lista_atividades(request):
    atividades = Atividade2.objects.all()
    return render(request, "atividades/lista.html", {"atividades": atividades})

def criar_atividade(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        turma_id = request.POST.get("turma")
        progresso = request.POST.get("progresso", 0)

        turma = Turma2.objects.get(id=turma_id)

        Atividade2.objects.create(
            titulo=titulo,
            descricao=descricao,
            turma=turma,
            progresso=progresso
        )
        return redirect("lista_atividades")

    turmas = Turma2.objects.all()
    return render(request, "criar_atividade.html", {"turmas": turmas})



# ---------- Editar Atividade ----------
def editar_atividade(request, atividade_id):
    atividade = Atividade2.objects.get(id=atividade_id)

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        progresso = request.POST.get("progresso")
        acao = request.POST.get("acao")

        if titulo and descricao:
            atividade.titulo = titulo
            atividade.descricao = descricao

            if acao == "salvar_progresso":
                atividade.progresso = int(progresso) if progresso else 0
            elif acao == "resetar_progresso":
                atividade.progresso = 0

            atividade.save()
            return redirect("lista_atividades")

    return render(request, "atividades/editar.html", {"atividade": atividade})

# ---------- Criar ----------
def criar_aluno(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        turma_id = request.POST.get("turma")
        if nome and turma_id:
            turma = Turma2.objects.get(id=turma_id)
            Aluno2.objects.create(nome=nome, turma=turma)
            return redirect("lista_alunos")
    turmas = Turma2.objects.all()
    return render(request, "criar_aluno.html", {"turmas": turmas})

def criar_turma(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        if nome:  
            Turma2.objects.create(nome=nome)
            return redirect("lista_turmas")
    return render(request, "criar_turma.html")

def lista_turmas(request):
    turmas = Turma2.objects.all()
    return render(request, "lista_turmas.html", {"turmas": turmas})


def lista_alunos(request):
    alunos = Aluno2.objects.all()
    return render(request, "lista_alunos.html", {"alunos": alunos})

# ---------- Horários ----------

def editar_horarios(request, atividade_id):
    atividade = get_object_or_404(Atividade2, id=atividade_id)

    if request.method == "POST":
        horario_inicio = request.POST.get("horario_inicio")
        horario_fim = request.POST.get("horario_fim")

        if horario_inicio:
            atividade.horario_inicio = horario_inicio
        if horario_fim:
            atividade.horario_fim = horario_fim

        atividade.save()

        return redirect("lista_atividades")
    return render(request, "editar_horarios.html", {"atividade": atividade})

def ativar_rotina(request, atividade_id):
    atividade = get_object_or_404(Atividade2, id=atividade_id)
    atividade.ativo = True
    atividade.save()
    return redirect('lista_atividades')

def excluir_rotina(request, atividade_id):
    atividade = get_object_or_404(Atividade2, id=atividade_id)
    atividade.delete()
    return redirect("lista_atividades")


def minha_view(request):
    if request.method == "POST":
        return HttpResponse("Form enviado com sucesso")
    elif request.method == "GET":
        return HttpResponse("Página carregada")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])
