from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'), 
    path('atividades/', views.lista_atividades, name='lista_atividades'),
    path('atividades/novo/', views.criar_atividade, name='criar_atividade'),
    path('turmas/', views.lista_turmas, name='lista_turmas'),
    path('turmas/novo/', views.criar_turma, name='criar_turma'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('alunos/novo/', views.criar_aluno, name='criar_aluno'),
]
