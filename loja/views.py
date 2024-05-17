from django.shortcuts import render
from .models import *

# Create your views here.
# Aqui definimos o que que acontece se uma usuario entrar numa pagina, o que que vai aparecer naquela pagina


# No contexto dessa função, request é um objeto que contém informações sobre a solicitação HTTP, como parâmetros GET ou POST, cookies, cabeçalhos, etc. 'homepage.html' é o nome do template que será renderizado e exibido para o usuário.
def homepage(request):
    return render(request, 'homepage.html')

def loja(request):
    # pegando todos os itens(produtos) da minha tabela
    produtos = Produto.objects.all()
    # print(produtos)
    # a chave do dicionario é a variavel que eu vou poder acessar no meu template html, e o valor dessa chave é a minha lista de produtos
    context = {'produtos': produtos}
    return render(request, 'loja.html', context=context)

def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')


def minha_conta(request):
    return render(request, 'usuario/minha_conta.html')

def login(request):
    return render(request, 'usuario/login.html')
