from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.get(username='eduardo')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.get(pk=10)
        self.estudante_02 = Estudante.objects.get(pk=11)


    def test_requisicao_get_para_listar_estudantes(self):
        """Teste de requisição GET para a rota de estudantes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(self.url+'11/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante =  Estudante.objects.get(pk=11)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        print(dados_estudante_serializados)
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_um_estudante(self):
        """Teste de requisição POST para um estudante"""
        dados = {
            'nome':'teste',
            'email':'teste@gmail.com',
            'cpf':'58994270000',
            'data_nascimento':'1991-11-11',
            'celular':'51 99999-9999'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE para um estudante"""
        response = self.client.delete(f'{self.url}15/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_estudante(self):
        """Teste de requisição PUT para um estudante"""
        dados = {
            'nome':'teste',
            'email':'testeput@gmail.com',
            'cpf':'73528800038',
            'data_nascimento':'2025-07-22',
            'celular':'21 77777-7777'
        }
        response = self.client.put(f'{self.url}15/', data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


