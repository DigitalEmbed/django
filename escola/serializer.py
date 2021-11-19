from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'documento', 'tipo_documento', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.nome')
    periodo = serializers.SerializerMethodField()
    nivel = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo', 'nivel']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

    def get_nivel(self, obj):
        return obj.curso.get_nivel_display()


class ListaAlunosMatriculaSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    tipo_documento = serializers.SerializerMethodField()
    documento = serializers.ReadOnlyField(source='aluno.documento')

    class Meta:
        model = Matricula
        fields = ['aluno', 'tipo_documento', 'documento']

    def get_tipo_documento(self, obj):
        return obj.aluno.get_tipo_documento_display()
