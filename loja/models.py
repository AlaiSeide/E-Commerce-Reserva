from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Users
# Cliente 
    #- nome
    #- email
    #- telefone
    #- usuario
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    # Quando um usuário visita um site, um id_sessao é gerado e armazenado tanto no servidor quanto no navegador do usuário (geralmente em um cookie). Este id_sessao permite que o servidor rastreie e lembre o estado do usuário à medida que ele navega pelo site. Por exemplo, em um site de comércio eletrônico, o id_sessao pode ser usado para rastrear os itens que um usuário adicionou ao carrinho de compras.
    id_sessao =  models.CharField(max_length=100, null=True, blank=True)
    # OneToOneField(User): Isso significa que para cada Cliente, há um único User correspondente. E para cada User, há um único Cliente correspondente. É como um casamento entre o Cliente e o User - cada um só pode ter um parceiro.

    # on_delete=models.CASCADE: Isso significa que se o User correspondente for excluído, então o Cliente também será excluído. É como dizer “se o User desaparecer, o Cliente também desaparecerá”.
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nome)
    
# Categoria (Masculino, Feminino, Infantil)
class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.nome)

# Tipo (Camisa, Calca)
class Tipo(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.nome)
# Produto
    #- imagem
    #- nome
    #- preco
    #- ativo
    #- categoria
    #- tipo
class Produto(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    # ex: 10.000.000,00
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    # ForeignKey(Categoria): Isso significa que cada Produto pode estar associado a uma única Categoria. No entanto, uma Categoria pode estar associada a muitos Produtos. É como dizer que cada produto pertence a uma categoria, mas uma categoria pode ter muitos produtos.

    # null=True, blank=True: Isso permite que o campo categoria seja deixado em branco em um formulário (blank=True) e também permite que o campo categoria seja NULL no banco de dados (null=True). Isso é útil se você quiser permitir produtos que não estão associados a nenhuma categoria.

    # on_delete=models.SET_NULL: Isso significa que se a Categoria associada for excluída, então o campo categoria do Produto será definido como NULL. É como dizer “se a categoria desaparecer, o produto ainda existirá, mas não estará mais associado a nenhuma categoria”.
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}, Tipo: {self.tipo}, Preco: {self.preco}'

# Itemestoque
    # produto (ex: camisa) 
    # cor (ex: azul, amarelo, laranja, verde)
    # tamanho (ex: P M G)
    # quantidade
class ItemEstoque(models.Model):
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)
    cor = models.CharField(max_length=200, null=True, blank=True)
    tamanho = models.CharField(max_length=200, null=True, blank=True)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return str(self.produto)


# Endereco
    # rua
    # numero
    # complemento
    # cep
    # cidade
    # estado
    # cliente
class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado =models.CharField(max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.rua)
# Pedido
    #- cliente
    #- data_finalizacao
    #- finalizacao
    #- id_transacao
    #- endereco
    #- codigo_pedido
    #- preco

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transacao =  models.CharField(max_length=200, null=True, blank=True)
    data_finalizacao = models.DateTimeField(null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.cliente)

# ItensPedido
    # itemestoque (ex: camisa, laranja, M)
    # quantidade (e: 10 itens)
class ItensPedido(models.Model):
    itemestoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.itemestoque)


class Banner(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    link_destino =  models.CharField(max_length=400, null=True, blank=True)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.link_destino} - Ativo: {self.ativo}'