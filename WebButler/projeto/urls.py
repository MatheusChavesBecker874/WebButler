from django.urls import path
from . import views 

urlpatterns = [
    # Autenticação
    path("", views.login_view, name="login"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Página inicial
    path("inicio/", views.inicio, name="inicio"),

    # Alunos
    path("alunos/", views.lista_alunos, name="lista_alunos"),
    path("alunos/novo/", views.novo_aluno, name="novo_aluno"),
    path("alunos/nova/", views.criar_aluno, name="criar_aluno"),

    # Turmas
    path("turmas/", views.lista_turmas, name="lista_turmas"),
    path("turmas/nova/", views.nova_turma, name="nova_turma"),

    # Atividades
    path("atividades/", views.lista_atividades, name="lista_atividades"),
    path("atividades/nova/", views.criar_atividade, name="criar_atividade"),
    path("atividades/<int:atividade_id>/editar/", views.editar_atividade, name="editar_atividade"),
    path("atividades/<int:atividade_id>/editar-horarios/", views.editar_horarios, name="editar_horarios"),
    path("atividades/<int:atividade_id>/ativar/", views.ativar_rotina, name="ativar_rotina"),
    path("atividades/<int:atividade_id>/excluir/", views.excluir_rotina, name="excluir_rotina"),

    # Rotinas
    path("listar/", views.listar_rotinas, name="listar_rotinas"),
    path("nova/", views.criar_rotina, name="criar_rotina"),

    # Compromissos
    path("compromissos/", views.lista_compromissos, name="lista_compromissos"),
    path("compromissos/novo/", views.novo_compromisso, name="novo_compromisso"),
    path("compromissos/sobrescrever/", views.sobrescrever_compromisso, name="sobrescrever_compromisso"),
    path("compromissos/<int:id>/remover/", views.remover_compromisso, name="remover_compromisso"),
]