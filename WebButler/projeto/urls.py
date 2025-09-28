from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("alunos/", views.lista_alunos, name="lista_alunos"),
    path("alunos/novo/", views.novo_aluno, name="novo_aluno"),
    path("turmas/", views.lista_turmas, name="lista_turmas"),
    path("turmas/nova/", views.nova_turma, name="nova_turma"),
    path("turmas/", views.lista_turmas, name="lista_turmas"),
    path("turmas/nova/", views.nova_turma, name="nova_turma"),
    path("atividades/", views.lista_atividades, name="lista_atividades"),
    path("atividades/nova/", views.criar_atividade, name="criar_atividade"),
    path("atividades/<int:atividade_id>/editar/", views.editar_atividade, name="editar_atividade"),
    path("turmas/nova/", views.criar_turma, name="criar_turma"),
    path("alunos/nova/", views.criar_aluno, name="criar_aluno"),
    path("turmas/", views.lista_turmas, name="lista_turmas"),
    path("alunos/", views.lista_alunos, name="lista_alunos"),
    path("atividades/<int:atividade_id>/editar-horarios/", views.editar_horarios, name="editar_horarios"),
    path("atividades/<int:atividade_id>/ativar/", views.ativar_rotina, name="ativar_rotina"),
    path("atividades/<int:atividade_id>/excluir/", views.excluir_rotina, name="excluir_rotina"),
]
