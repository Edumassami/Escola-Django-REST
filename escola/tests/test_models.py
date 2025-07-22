from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '64563780014',
            data_nascimento = '2025-07-22',
            celular = '11 99999-9999'
        )

    def test_verifica_atributos_de_estudante(self):
        """Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '64563780014')
        self.assertEqual(self.estudante.data_nascimento, '2025-07-22')
        self.assertEqual(self.estudante.celular, '11 99999-9999')

class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'T01',
            descricao = 'Teste de Modelo de Curso 01',
            nivel = 'B',
        )

    def test_verifica_atributos_de_curso(self):
        """Teste que verifica os atributos do modelo de Curso"""
        self.assertEqual(self.curso.codigo, 'T01')
        self.assertEqual(self.curso.descricao, 'Teste de Modelo de Curso 01')
        self.assertEqual(self.curso.nivel, 'B')

class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '64563780014',
            data_nascimento = '2025-07-22',
            celular = '11 99999-9999'
        )

        self.curso = Curso.objects.create(
            codigo = 'T01',
            descricao = 'Teste de Modelo de Curso 01',
            nivel = 'B',
        )

        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'N',
        )

    def test_verifica_atributos_de_matricula(self):
        """Teste que verifica os atributos do modelo de Matricula"""
        self.assertEqual(self.matricula.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.matricula.curso.codigo, 'T01')
        self.assertEqual(self.matricula.periodo, 'N')