from django.db import models


class Turma(models.Model):
    TURNOS_CHOICES = (
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno')
    )

    nome = models.CharField('Nome', max_length=50)
    turno = models.CharField('Turno', choices=TURNOS_CHOICES, max_length=10)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        return self.nome

    def display_disciplinas(self):
        disciplinas = self.disciplina_set.all()
        return ", ".join(d.nome for d in disciplinas)


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=70)
    endereco = models.CharField('Endereço', max_length=100)
    dtnasc = models.DateField('Data de nascimento')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos_turma')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Boletim(models.Model):
    periodo = models.PositiveIntegerField('Período')
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Boletim'
        verbose_name_plural = 'Boletins'

    def __str__(self):
        return f'Boletim do aluno {self.aluno}'


class Disciplina(models.Model):
    carga_horaria = models.PositiveIntegerField()
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição')
    turma = models.ManyToManyField(Turma)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome
