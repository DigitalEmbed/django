from rest_framework import viewsets, generics
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculaSerializer
from escola.models import Aluno, Curso, Matricula


class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos."""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos."""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas."""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAlunoView(generics.ListAPIView):
    """Exibindo as matrículas de um determinado aluno."""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculaView(generics.ListAPIView):
    """Exibindo os alunos de um determinado curso."""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculaSerializer
