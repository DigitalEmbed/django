from django.contrib import admin
from escola.models import Aluno, Curso


class TabelaAlunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'documento', 'tipo_documento', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'documento')
    list_per_page = 20


class TabelaCursos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codigo', 'descricao', 'nivel')
    list_display_links = ('id', 'nome', 'codigo')
    search_fields = ('nome', 'codigo')
    list_per_page = 20


admin.site.register(Aluno, TabelaAlunos)
admin.site.register(Curso, TabelaCursos)