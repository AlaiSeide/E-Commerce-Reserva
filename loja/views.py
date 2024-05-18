from django.shortcuts import render
from .models import *

# Create your views here.
# Aqui definimos o que que acontece se uma usuario entrar numa pagina, o que que vai aparecer naquela pagina


# No contexto dessa função, request é um objeto que contém informações sobre a solicitação HTTP, como parâmetros GET ou POST, cookies, cabeçalhos, etc. 'homepage.html' é o nome do template que será renderizado e exibido para o usuário.
# Esta é a função 'homepage'. Ela recebe um parâmetro: 'request'.
# 'request' é a solicitação HTTP que foi enviada para o servidor.
def homepage(request):

    # Aqui, estamos pegando todos os banners que estão ativos na nossa página inicial.
    # 'Banner.objects.filter(ativo=True)' retorna todos os objetos Banner que têm 'ativo' definido como True.
    banners = Banner.objects.filter(ativo=True)

    # Aqui, estamos criando um dicionário chamado 'context'.
    # Este dicionário será usado para enviar dados para o nosso template HTML.
    # A chave 'banners' no dicionário 'context' contém a nossa lista de banners.
    context = {'banners': banners}

    # Finalmente, esta linha renderiza o template 'homepage.html', passando o dicionário 'context' como contexto.
    # Isso significa que, dentro do template 'homepage.html', podemos acessar a lista de banners usando a chave 'banners'.
    return render(request, 'homepage.html', context=context)



# Esta é a função 'loja'. Ela recebe dois parâmetros: 'request' e 'nome_categoria'.
# 'request' é a solicitação HTTP que foi enviada para o servidor.
# 'nome_categoria' é o nome de uma categoria de produtos. Se não for fornecido, seu valor será None.
def loja(request, nome_categoria=None):

    # Esta linha imprime o valor de 'nome_categoria' no console.
    print(nome_categoria)

    # Aqui, estamos pegando todos os produtos que estão ativos na nossa loja.
    # 'Produto.objects.filter(ativo=True)' retorna todos os objetos Produto que têm 'ativo' definido como True.
    produtos = Produto.objects.filter(ativo=True)

    # Esta parte do código verifica se 'nome_categoria' foi fornecido.
    # Se foi, então filtramos a lista de produtos para incluir apenas os produtos dessa categoria.
    if nome_categoria:
    # Na linha categoria__nome, você está acessando o campo nome do modelo relacionado Categoria através do modelo Produto. Isso é chamado de lookup de campo relacionado no Django.

    # Por exemplo, se você tem um modelo Produto que tem uma relação com o modelo Categoria, você pode acessar os campos do modelo Categoria a partir do modelo Produto usando a sintaxe categoria__nome.

    # Isso é útil quando você quer filtrar ou ordenar os objetos Produto com base em algum campo do modelo Categoria. Por exemplo, você pode querer obter todos os produtos que pertencem a uma determinada categoria. Você pode fazer isso assim:
        produtos = produtos.filter(categoria__nome=nome_categoria)

    # Aqui, estamos criando um dicionário chamado 'context'.
    # Este dicionário será usado para enviar dados para o nosso template HTML.
    # A chave 'produtos' no dicionário 'context' contém a nossa lista de produtos.
    context = {'produtos': produtos}

    # Finalmente, esta linha renderiza o template 'loja.html', passando o dicionário 'context' como contexto.
    # Isso significa que, dentro do template 'loja.html', podemos acessar a lista de produtos usando a chave 'produtos'.
    return render(request, 'loja.html', context=context)


def ver_produto(request, id_produto, id_cor=None):
    tem_estoque = False
    cores = {}
    tamanhos = {}

    # Busca um objeto Produto no banco de dados com base no id fornecido
    produto = Produto.objects.get(id=id_produto)

    # Filtra os itens de estoque que correspondem ao produto e que têm quantidade maior que 0
    itensestoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)
    if len(itensestoque) > 0:
        tem_estoque = True
        cores = {item.cor for item in itensestoque}

        if id_cor:
            itensestoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0, cor__id=id_cor)
            tamanhos = {item.tamanho for item in itensestoque}
    # Cria um dicionário de contexto com o produto para ser passado para o template
    context = {'produto': produto, 'itens_estoque': itensestoque, 'tem_estoque': tem_estoque, 'cores': cores, 'tamanhos': tamanhos}

    # Renderiza a página 'ver_produto.html' passando o contexto
    return render(request, 'ver_produto.html', context=context)


def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')


def minha_conta(request):
    return render(request, 'usuario/minha_conta.html')

def login(request):
    return render(request, 'usuario/login.html')
