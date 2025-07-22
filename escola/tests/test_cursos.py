from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursosTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='eduardo')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso_01 = Curso.objects.get(pk=5)
        self.curso_02 = Curso.objects.get(pk=6)
    
    def test_requisicao_get_para_listar_cursos(self):
        """Teste de requisição GET para a rota de cursos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_get_para_listar_um_curso(self):
        """Teste de requisição GET para um curso"""
        response = self.client.get(self.url+'7/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso =  Curso.objects.get(pk=7)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados)

    def test_requisicao_post_para_criar_um_curso(self):
        """Teste de requisição POST para um curso"""
        dados = {
            'codigo':'T00',
            'descricao':'Teste de Curso',
            'nivel':'B',
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_curso(self):
        """Teste de requisição DELETE para um curso"""
        response = self.client.delete(f'{self.url}7/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_curso(self):
        """Teste de requisição PUT para um curso"""
        dados = {
            'codigo':'T05',
            'descricao':'Teste PUT na rota de Cursos',
            'nivel':'A'
        }
        response = self.client.put(f'{self.url}7/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)