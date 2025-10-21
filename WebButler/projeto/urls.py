from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_view, name="login"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("inicio/", views.inicio, name="inicio"),
    path("alunos/", views.lista_alunos, name="lista_alunos"),
    path("alunos/novo/", views.novo_aluno, name="novo_aluno"),
    path("alunos/nova/", views.criar_aluno, name="criar_aluno"),
    path("turmas/", views.lista_turmas, name="lista_turmas"),
    path("turmas/nova/", views.nova_turma, name="nova"),
    path("turmas/nova/", views.criar_turma, name="nova"),
    path("atividades/", views.lista_atividades, name="lista_atividades"),
    path("atividades/nova/", views.criar_atividade, name="criar_atividade"),
    path("atividades/<int:atividade_id>/editar/", views.editar_atividade, name="editar_atividade"),
    path("atividades/<int:atividade_id>/editar-horarios/", views.editar_horarios, name="editar_horarios"),
    path("atividades/<int:atividade_id>/ativar/", views.ativar_rotina, name="ativar_rotina"),
    path("atividades/<int:atividade_id>/excluir/", views.excluir_rotina, name="excluir_rotina"),
]
