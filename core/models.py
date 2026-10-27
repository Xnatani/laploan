from django.db import models
from datetime import date


class Locatario(models.Model):
    TIPO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('funcionario', 'Funcionário'),
    ]
    nome = models.CharField(max_length=120)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='aluno')
    turma = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Locatário'
        verbose_name_plural = 'Locatários'


class Equipamento(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
        ('manutencao', 'Em manutenção'),
    ]
    CONDICAO_CHOICES = [
        ('novo', 'Novo'),
        ('bom', 'Bom'),
        ('regular', 'Regular'),
        ('ruim', 'Ruim'),
    ]
    codigo = models.CharField(max_length=30, unique=True)
    equipamento = models.CharField(max_length=80, default='Notebook')
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    versao = models.CharField(max_length=60, blank=True)
    numero_serie = models.CharField(max_length=80, unique=True)
    processador = models.CharField(max_length=80, blank=True)
    gpu = models.CharField(max_length=80, blank=True)
    ram = models.CharField(max_length=40, blank=True)
    armazenamento = models.CharField(max_length=60, blank=True)
    sistema_operacional = models.CharField(max_length=60, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    condicao = models.CharField(max_length=20, choices=CONDICAO_CHOICES, default='bom')

    def __str__(self):
        return f"{self.codigo} - {self.marca} {self.modelo}"

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'


class Emprestimo(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    locatario = models.ForeignKey(Locatario, on_delete=models.PROTECT)
    data_saida = models.DateField()
    data_prevista = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    observacoes = models.TextField(blank=True)

    @property
    def esta_atrasado(self):
        if self.data_devolucao:
            return self.data_devolucao > self.data_prevista
        return date.today() > self.data_prevista
    esta_atrasado.fget.short_description = 'Atrasado?'

    def __str__(self):
        return f"{self.equipamento} → {self.locatario} ({self.data_saida})"

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'