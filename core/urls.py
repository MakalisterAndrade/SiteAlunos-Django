from django.urls import path

import core.views as views

urlpatterns = [
    path('', views.FaculdadeIndexView.as_view(), name='index'),

    path("turma/", views.TurmaListView.as_view(), name="turma_list"),
    path("aluno/", views.AlunoListView.as_view(), name="aluno_list"),

    path("turma/criar/", views.TurmaCreateView.as_view(), name="turma_create"),
    path("aluno/criar/", views.AlunoCreateView.as_view(), name="aluno_create"),

]