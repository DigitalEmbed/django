from django.db import models


class Aluno(models.Model):
    class Documento(models.IntegerChoices):
        RG = 0
        CPF = 1
    nome = models.CharField(max_length=30, blank=False, null=False)
    documento = models.CharField(max_length=11, blank=False, null=False, unique=True)
    tipo_documento = models.IntegerField(choices=Documento.choices, blank=False, null=False)
    data_nascimento = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    Nivel = (
        ('B', 'Baixo'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    nome = models.CharField(max_length=15, blank=False, null=False)
    codigo = models.CharField(max_length=10, blank=False, null=False, unique=True)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=Nivel, blank=False, null=False, default='B')

    def __str__(self):
        return "[" + self.codigo + "]" + self.nome

