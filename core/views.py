from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView
from django.contrib import messages

from .forms import AlunoForm
from .models import Turma, Aluno

class BaseView(SuccessMessageMixin):
    success_message = None

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message % form.cleaned_data)
        return response

class FaculdadeIndexView(TemplateView):
    template_name = 'base.html'

class TurmaListView(ListView):
    model = Turma
    context_object_name = 'turmas'
    template_name = 'turma/list.html'
    ordering = ['-id']

class TurmaCreateView(BaseView, CreateView):
    model = Turma
    fields = ["nome", "turno"]
    template_name = 'turma/form.html'
    success_url = reverse_lazy("turma_list")
    success_message = "%(nome)s criado com sucesso!"

class TurmaUpdateView(BaseView, UpdateView):
    model = Turma
    fields = ["nome", "turno"]
    template_name = 'turma/form.html'
    success_url = reverse_lazy("turma_list")
    success_message = "%(nome)s atualizado com sucesso!"

class TurmaDeleteView(BaseView, DeleteView):
    model = Turma
    template_name = 'turma/delete.html'
    success_url = reverse_lazy("turma_list")
    success_message = "Excluído com sucesso!"

class AlunoListView(ListView):
    model = Aluno
    context_object_name = 'alunos'
    template_name = 'aluno/list.html'
    ordering = ['-id']

class AlunoCreateView(BaseView, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/form.html'
    success_url = reverse_lazy("aluno_list")
    success_message = "%(nome)s criado com sucesso!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['turmas'] = Turma.objects.all()  # Passa a lista de turmas para o contexto
        return context

class AlunoUpdateView(BaseView, UpdateView):
    model = Aluno
    fields = ["nome", "sobrenome", "endereco", "dtnasc", "turma"]
    template_name = 'aluno/form.html'
    success_url = reverse_lazy("aluno_list")
    success_message = "%(nome)s atualizado com sucesso!"

class AlunoDeleteView(BaseView, DeleteView):
    model = Aluno
    template_name = 'aluno/delete.html'
    success_url = reverse_lazy("aluno_list")
    success_message = "Excluído com sucesso!"
