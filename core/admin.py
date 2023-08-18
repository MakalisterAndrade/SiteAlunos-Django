from django.contrib import admin

from core.models import Aluno, Boletim, Turma, Disciplina


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turno', 'display_disciplinas')

    def display_disciplinas(self, turma):
        """
        Exibe as disciplinas da turma separadas por vírgula.
        """
        disciplinas = turma.disciplina_set.all()[:2]
        return ', '.join(d.nome for d in disciplinas)

    display_disciplinas.short_description = 'Disciplinas'


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'dtnasc', 'endereco', 'turma')
    search_fields = ['nome', 'sobrenome']

    def nome_completo(self, aluno):
        """
        Retorna o nome completo do aluno.
        """
        return f'{aluno.nome} {aluno.sobrenome}'

    nome_completo.short_description = 'Nome Completo'


@admin.register(Boletim)
class BoletimAdmin(admin.ModelAdmin):
    list_display = ('periodo', 'aluno')


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')
