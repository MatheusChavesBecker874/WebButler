from django.shortcuts import render, redirect, get_object_or_404
from .models import Turma2, Aluno2, Atividade2, Rotina, Aula, Compromisso
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RotinaForm, AulaForm, CompromissoForm
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

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
    return render(request, "nova")

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

# -------- Login --------

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

# ------- Rotinas ---------

def criar_rotina(request):
    if request.method == "POST":
        form = RotinaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rotina criada com sucesso!")
            return redirect("listar_rotinas")
        else:
            messages.error(request, "Erro ao criar rotina")
    else:
        form = RotinaForm()
    return render(request, "nova_rotina.html", {"form": form})

def listar_rotinas(request):
    rotinas = Rotina.objects.all()
    return render(request, "listar_rotinas.html", {"rotinas": rotinas})

@login_required
def lista_compromissos(request):
    compromissos = Compromisso.objects.order_by("data_inicio")
    return render(request, "compromissos/lista.html", {"compromissos": compromissos})


@login_required
def novo_compromisso(request):
    if request.method == "POST":
        form = CompromissoForm(request.POST)

        if form.is_valid():
            compromisso = form.save(commit=False)

            try:
                compromisso.clean()  # C2 + C3
                compromisso.save()

                messages.success(request, "Compromisso criado com sucesso!")
                return redirect("lista_compromissos")

            except ValidationError as e:
                erro = list(e.messages)[0]

                # Ativa popup de sobrescrever se der conflito
                if "Deseja sobrescrever" in erro:
                    request.session["novo_compromisso"] = {
                        "titulo": form.cleaned_data["titulo"],
                        "data_inicio": form.cleaned_data["data_inicio"].isoformat(),
                        "data_fim": form.cleaned_data["data_fim"].isoformat(),
                        "lembrete": form.cleaned_data["lembrete_minutos"],
                    }
                    request.session["confirmar_sobrescrita"] = True

                messages.error(request, erro)

    else:
        form = CompromissoForm()

    return render(request, "compromissos/novo.html", {"form": form})

@login_required
def sobrescrever_compromisso(request):
    dados = request.session.get("novo_compromisso")

    if not dados:
        messages.error(request, "Nenhum compromisso para sobrescrever.")
        return redirect("novo_compromisso")

    data_inicio = datetime.fromisoformat(dados["data_inicio"])
    data_fim = datetime.fromisoformat(dados["data_fim"])

    # Apaga os conflitos
    Compromisso.objects.filter(
        data_inicio__lt=data_fim,
        data_fim__gt=data_inicio
    ).delete()

    # Cria o novo
    Compromisso.objects.create(
        titulo=dados["titulo"],
        data_inicio=data_inicio,
        data_fim=data_fim,
        lembrete_minutos=dados["lembrete"]
    )

    # Limpa sessão
    del request.session["novo_compromisso"]
    del request.session["confirmar_sobrescrita"]

    messages.success(request, "Compromisso substituído com sucesso!")
    return redirect("lista_compromissos")

@login_required
def remover_compromisso(request, id):
    compromisso = get_object_or_404(Compromisso, id=id)

    if compromisso.recorrente:
        return redirect("remover_recorrente", id=id)

    if request.method == "POST":
        compromisso.delete()
        messages.success(request, "Compromisso removido com sucesso!")
        return redirect("lista_compromissos")

    return render(request, "compromissos/confirmar_remocao.html", {"compromisso": compromisso})

@login_required
def remover_recorrente(request, id):
    compromisso = get_object_or_404(Compromisso, id=id)

    if request.method == "POST":
        acao = request.POST.get("acao")

        if acao == "ocorrencia":
            CompromissoRecorrenciaExcecao.objects.create(
                compromisso=compromisso,
                data=compromisso.data_inicio.date()
            )
            messages.success(request, "Ocorrência removida com sucesso!")
            return redirect("lista_compromissos")

        elif acao == "todos":
            compromisso.delete()
            messages.success(request, "Todas as ocorrências foram removidas.")
            return redirect("lista_compromissos")

    return render(request, "compromissos/remover_recorrente.html", {
        "compromisso": compromisso
    })