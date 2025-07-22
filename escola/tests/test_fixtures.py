from django.test import TestCase
from escola.models import Estudante, Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def test_carregamento_da_fixtures(self):
        """Teste que verifica o carregamento da fixtures"""
        estudante = Estudante.objects.get(cpf='37235800097')
        curso = Curso.objects.get(pk=6)
        self.assertEqual(estudante.email,'gustavomartins@uol.com.br')
        self.assertEqual(curso.codigo, 'CDJ01')