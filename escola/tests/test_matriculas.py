from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante, Curso, Matricula

class MatriculasTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='eduardo')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.get(pk=10)
        self.estudante_02 = Estudante.objects.get(pk=11)
        self.curso_01 = Curso.objects.get(pk=6)
        self.curso_02 = Curso.objects.get(pk=7)
        self.matricula_02 = Matricula.objects.create(
            estudante = self.estudante_01,
            curso = self.curso_02,
            periodo = 'V'
        )
        self.matricula_03 = Matricula.objects.create(
            estudante = self.estudante_02,
            curso = self.curso_01,
            periodo = 'N'
        )

    def test_requisicao_get_para_listar_matriculas(self):
        """Teste de requisição GET para a rota de matriculas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_uma_matricula(self):
        """Teste de requisição POST para uma matricula"""
        dados = {
            'estudante':self.estudante_02.pk,
            'curso':self.curso_02.pk,
            'periodo':'M',
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_uma_matricula(self):
        """Teste de requisição DELETE para uma matricula"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_requisicao_put_para_atualizar_uma_matricula(self):
        """Teste de requisição PUT para uma matricula"""
        dados = {
            'estudante':self.estudante_02.pk,
            'curso':self.curso_02.pk,
            'periodo':'V'
        }
        response = self.client.put(f'{self.url}1/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)